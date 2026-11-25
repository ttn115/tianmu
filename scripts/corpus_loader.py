# -*- coding: utf-8 -*-
"""tianmu 共用語料載入器 —— 只讀被標記為正文的那一段，並自我對帳。

為什麼需要這個檔
----------------
本 repo 的語料 .md 同時裝著三種文字：
  (a) 本庫自己的研究評註，以及寫在檔首的 `>` 來源註記；
  (b) 本庫加的 `###` 分節標題；
  (c) 真正的原典正文。
在這個檔出現之前，每次做詞頻都要重新用手找邊界，而**手找錯過兩次**：
  2026-11-04 「女功 33 次」是在本庫自己的註解上數的（原典只有 4 次）；
  2026-11-17 載入器把本庫寫在檔首的 `>` 註記算進了四份語料的分母
            （譚處端 +116／劉處玄 +99／王處一 +58／郝大通 +122 漢字）。

所以正文邊界現在寫在語料檔裡，machine-readable，而且**標記自帶預期字數**：

    <!-- NUWA-CORPUS BEGIN id=tan-chuduan layer=L1 expect=14711 -->
    ...原典正文...
    <!-- NUWA-CORPUS END id=tan-chuduan -->

`keep_quoted=1` 只給孫不二那一檔：**她的原詩本身是用 `>` 引的**，
所以一個會丟掉 `>` 行的載入器會把她的語料刪光。其餘各檔的 `>` 行都是本庫自述。

用法
----
    from corpus_loader import load, load_all
    text = load("tan-chuduan")          # 一個人的正文（已剝去本庫的字）
    for aid, text in load_all(): ...

自我檢查（會比對標記裡的 expect，以及下面 REGISTERED 的登錄值）：
    python scripts/corpus_loader.py
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HAN = re.compile(r'[一-鿿]')
#: 标记的键值对不限顺序——只要求有 id 与 expect。
#: ⚠️ 原本的正规式写死了 id→layer→expect→flags 的顺序，
#:    于是把 `id=… layer=… select=… expect=…` 全部解析失败（2026-11-18）。
BEGIN = re.compile(r'<!--\s*NUWA-CORPUS\s+BEGIN\s+(?P<kv>[^>]*?)\s*-->')
END = re.compile(r'<!--\s*NUWA-CORPUS\s+END(?:\s+id=(?P<id>[\w-]+))?\s*-->')


def _kv(s):
    """把标记里的 key=value 串解析成 dict。"""
    out = {}
    for tok in s.split():
        if "=" in tok:
            k, v = tok.split("=", 1)
            out[k] = v
    return out

#: 各角色的登錄字數。⚠️ 這些是「本庫對外宣稱」的數字，載入器會與實測對帳。
#: 不符者下面 NOTE 說明原因——**不要為了讓它過而改登錄值**。
REGISTERED = {
    "wang-chongyang": 55912,
    "mayu":           66872,
    "tan-chuduan":    14711,
    "liu-chuxuan":    22116,
    "qiu-chuji":      26023,
    "wang-chuyi":     30537,
    "hao-datong":      8420,
    "sun-buer":          814,
    "li-daochun":     35995,
    "li-daochun-ddhy": 17602,
    #: 《六祖壇經》2026-11-24 分說話人（24 層）。
    #: 2 2 huineng 19,904 -> 13,986，此前壇經字頻偏低約 30%。
    #: 行由品是慧能自述，弘忍／神秀的話在他的引號內，留慧能層但另計轉述。
    #: tanjing-zhong（眾）與 tanjing-kongzhongsheng（空中聲）不是個人。
    "huineng":                 13986,
    "tanjing-recorder":        4195,
    "fahai":                   195,
    "zhichang":                193,
    "zhidao":                  193,
    "xuance":                  183,
    "fada":                    144,
    "xuejian":                 126,
    "weiqu":                   121,
    "zhicheng":                111,
    "xingchang":               108,
    "shenxiu":                 78,
    "xuanjue":                 72,
    "tanjing-zhong":           53,
    "shenhui":                 41,
    "zhihuang":                25,
    "huairang":                19,
    "xingsi":                  15,
    "lizhong-qide":            10,
    "wujinzang-ni":            8,
    "zhitong":                 8,
    "fangbian":                8,
    "tanjing-kongzhongsheng":  7,
    "tanjing-seng":            5,
    #: 《楞嚴經》2026-11-24 分說話人（32 層）。
    #: lengyan 69,940 -> lengyan-fo 40,570（只有 58.0% 是佛在說）。
    #: 二十五圓通實得 24 位；lengyan-dazhong 與 lengyan-cbeta-note 不是個人。
    "lengyan-fo":                40570,
    "lengyan-recorder":          16296,
    "ananda":                    5077,
    "guanshiyin":                2149,
    "lengyan-dazhong":           1398,
    "prasenajit":                453,
    "purna-maitrayaniputra":     352,
    "yueguang-tongzi":           320,
    "chidi":                     280,
    "dashizhi":                  217,
    "purna":                     215,
    "liuliguang":                200,
    "kaundinya":                 186,
    "maitreya":                  171,
    "xukongzang":                148,
    "mahakasyapa":               140,
    "yaowang-yaoshang":          132,
    "puxian":                    126,
    "sundarananda":              124,
    "ucchusma":                  123,
    "upali":                     120,
    "pilindavatsa":              116,
    "manjusri":                  114,
    "maudgalyayana":             112,
    "gavampati":                 108,
    "ksudrapanthaka":            104,
    "subhuti":                   104,
    "xiangyan-tongzi":           100,
    "sariputra":                 100,
    "bhadrapala":                84,
    "aniruddha":                 84,
    "upanisad":                  76,
    "lengyan-cbeta-note":        41,
    "lengyan-xu":       1045,
    #: 《金剛經》2026-11-24 分說話人（3 層）。
    #: jingang 5,183 -> jingang-fo 3,630（70.0%）+ subhuti 1,138 + 記錄者 415。
    #: 招牌句式「即非…是名」佛 22／須菩提 21，而密度須菩提是佛的 3.0 倍
    #: （p=0.00041）——那不是佛獨有的句式。
    #: 《論語》2026-11-24 收入並分說話人（42 層、15,827 漢字、506 章）。
    #: confucius 8,338（52.7%）——本庫 confucius 角色終於有一手語料。
    #: 已剔除：章號行 2,057（11.2%，編者編號）、序說 1,274（朱熹）、
    #: 知道第二十二 27（非通行篇）、維基有聲文獻樣板。
    #: lunyu-undetermined 302 是機械判不出的（不硬塞給孔子）。
    #: 《孟子》2026-11-25 收入並分說話人（39 層、35,383 漢字、778 段）。
    #: mencius 25,977（73.4%）——本庫 mencius 角色的一手語料。
    #: ✅ 與論語不同，本書無章號行。⚠️ 交替占 35%（對話逐段交替而只寫「曰」），
    #: partner 須在卷內跨段保持（逐段重算會讓 28.5% 落到未定）。
    #: ✅ 內部檢驗：寡人 孟子 0.8/萬 vs 諸王 118.2/萬（分離 148 倍）。
    "mencius":               25927,
    "mengzi-recorder":       3226,
    "qi-xuanwang":           1450,
    "wanzhang":              803,
    "gongsun-chou":          755,
    "gongduzi":              664,
    "chenxiang":             362,
    "mengzi-undetermined":   242,
    "gaozi":                 159,
    "teng-wengong":          158,
    "gaozi-mz":              158,
    "chunyu-kun":            140,
    "liang-huiwang":         139,
    "chenzhen":              118,
    "xianqiu-meng":          114,
    "yuezhengzi":            92,
    "lu-pinggong":           80,
    "wuluzi":                74,
    "kuangzhang":            66,
    "mengzi-huo":            64,
    "xuxing":                61,
    "penggeng":              57,
    "zisi":                  57,
    "chongyu":               53,
    "caojiao":               51,
    "zhouxiao":              50,
    "songkeng":              43,
    "zengzi-mz":             34,
    "yizi":                  28,
    "taoying":               28,
    "jingchun":              24,
    "baigui":                24,
    "dai-yingzhi":           23,
    "xuzi":                  19,
    "chenjia":               15,
    "shenzi":                8,
    "song-goujian":          8,
    "gongming-yi":           5,
    "shentong":              4,
    "confucius":             8338,
    "lunyu-recorder":        4000,
    "zigong":                671,
    "zilu":                  424,
    "zixia":                 381,
    "lunyu-undetermined":    302,
    "zizhang":               283,
    "zengzi":                227,
    "ziyou":                 124,
    "yanyuan":               120,
    "youzi":                 70,
    "ranyou":                67,
    "lunyu-huo":             66,
    "jikangzi":              59,
    "zaiwo":                 57,
    "lu-aigong":             55,
    "meng-jingzi":           55,
    "fanchi":                47,
    "zhonggong":             47,
    "shegong":               42,
    "gongxihua":             39,
    "qi-jinggong":           31,
    "yanghuo":               30,
    "ziqin":                 29,
    "simaniu":               29,
    "min-ziqian":            27,
    "lu-dinggong":           25,
    "lunyu-yimin":           24,
    "nangong-kuo":           20,
    "meng-wubo":             19,
    "zifu-jingbo":           18,
    "linfang":               17,
    "guanzhong":             17,
    "yi-fengren":            13,
    "weisheng-mu":           13,
    "ji-zicheng":            10,
    "qu-boyu":               10,
    "lunyu-季氏":              9,
    "zixi":                  4,
    "yuansi":                3,
    "jieni":                 3,
    "meng-yizi":             2,
    "jingang-fo":          3630,
    "subhuti-jingang":     1138,
    "jingang-recorder":    415,
    "taiyi":             6368,
    "wumingshi":       102249,
    "chen-xubai":        5477,
    "wu-shouyang-zhenglun": 10227,
    "wu-shouyang-zizhu":   28259,
    #: 《仙佛合宗語錄》2026-11-22 收入。⚠️ 這本書推翻了本庫據《直論增註》
    #:    寫下的三處結論（天心／任督／玉枕「伍守陽 0 次」）——那是
    #:    **只有他一本書**造成的假缺口。問答體，提問者三人各自一層。
    "wu-shouyang-hezong":  48656,
    "zhu-taihe":            3291,
    "wu-taiyi":             3292,
    "wu-taichu":             169,
    "liu-huayang":      63857,
    "huang-yuanji":    126574,
    "heshanggong":      15197,
    "laozi-jing-heshang": 5284,
    "wangbi":           11797,
    "laozi-jing-wangbi":  5297,
    "guo-xiang":        56558,
    "cheng-xuanying":  160399,
    #: ⚠️ 2026-11-24：34 行卷末題署（「南華真經註疏卷之二」一類）一直
    #: 算在經文層裡，345 漢字（0.52%）。已另立 nanhua-colophon。
    #: ✅ 題署裡「性」0 次「道」0 次，故「內七篇性 0 次」結論不受影響。
    "zhuangzi":          65586,
    "nanhua-colophon":     345,
    #: ---- 《傳習錄》（2026-11-25 收，65,032 漢字／342 條／56 層）----
    #: ⚠️ wang-yangming 是〔先生〕＋〔先生書〕的聯集；
    #:    -yulu（門人筆錄）與 -shu（他自己執筆）分開登錄才能對讀。
    "wang-yangming":             48113,
    "wang-yangming-yulu":        28062,
    "wang-yangming-shu":         20051,
    "wang-yangming-zhuanshu":    2297,
    "cxl-wenzhe":                1800,
    "lu-yuanjing":               1601,
    "xu-ai":                     1228,
    "cxl-rec-huangshengzeng":    1048,
    "cxl-rec-huangyifang":       947,
    "qian-dehong":               940,
    "gu-dongqiao":               842,
    "zhou-daotong":              783,
    "cxl-rec-chenjiuchuan":      768,
    "ouyang-chongyi":            555,
    "cxl-陳九川":                   520,
    "cxl-rec-xuekan":            481,
    "cxl-rec-luchen":            440,
    "cxl-youren":                342,
    "cxl-王嘉秀":                   255,
    "cxl-薛侃":                    229,
    "cxl-陸澄":                    209,
    "cxl-rec-xuai":              201,
    "cxl-黃以方":                   182,
    "cxl-汝中":                    135,
    "cxl-梁日孚":                   127,
    "cxl-rec-huangxiuyi":        98,
    "cxl-蕭惠":                    92,
    "cxl-士德":                    87,
    "cxl-鄒謙之":                   76,
    "cxl-蔡希淵":                   74,
    "cxl-馬子莘":                   52,
    "cxl-鄭朝朔":                   49,
    "cxl-德章":                    46,
    "cxl-正之":                    45,
    "cxl-守衡":                    44,
    "cxl-敷英":                    28,
    "cxl-于中":                    26,
    "cxl-黃誠甫":                   22,
    "cxl-子仁":                    22,
    "cxl-朱本思":                   20,
    "cxl-黃勉叔":                   20,
    "cxl-伯生":                    19,
    "cxl-洪":                     18,
    "cxl-黃勉之":                   16,
    "cxl-范兆期":                   16,
    "cxl-志道":                    15,
    "cxl-國英":                    15,
    "cxl-唐詡":                    14,
    "cxl-侯璧":                    13,
    "cxl-甘泉":                    13,
    "cxl-尚謙":                    12,
    "cxl-柴鳴治":                   10,
    "cxl-孟源":                    10,
    "cxl-惟乾":                    8,
    "cxl-劉觀時":                   7,
    "cxl-黃省曾":                   2,
}
NOTE = {
    "qiu-chuji": "對外曾記 24,344；差 1,679 ＝ 他的 293 行粗體篇名（本載入器保留篇名）",
    "sun-buer":  "對外曾記 756；差 58 ＝ 詩題行（本載入器保留篇名）",
    "mayu":      "對外曾記 68,046；差 1,174（1.7%）⚠️ 未解",
    "zhuangzi":  "本庫此前記 65,954；差 23 ⚠️ 未解（疑為篇題行的計法）",
}


def han(s):
    """漢字數（不含標點與拉丁字）。"""
    return len(HAN.findall(s))


def _strip(lines, keep_quoted=False, drop_bracketed=False, select=None,
           exclude=None):
    r"""剥掉本库自己的字，留下原典。

    `select` 用于「经＋注」体的语料：那种底本把两（三）层写在同一段里，
    靠行的样式区分，所以一个 span 要能只取其中一层。
      select="bold"            只取 `**…**` 行（＝被注的经文层）
      select="quoted:郭象注"    只取 `> 〔郭象注〕…` 行（＝该注者那一层）
    本库有四份这种语料：河上公・王弼・南华（郭象＋成玄英两层）。
    ⚠️ 《道德會元》不同——它的经文夹在注文「之内」用【】标，所以用 drop_bracketed。

    `drop_bracketed=1`：被注的经文夹在注文之间、用 `【】` 标出（例《道德會元》：
    「【道可道，非常道】開口即錯。」）。那段经文不是注者的字，但也不能搬走
    （搬走注文就失去被注的对象），故以旗标处理。
    """
    if select == "bold" or (select or "").startswith("bold:"):
        # ⚠️ bold 行可以帶說話人標籤 `**〔X〕…**`（莊子那一層用）。
        #    `bold` 取全部並剝標籤（規模不變）；`bold:X` 只取 X 的。
        want = select.split(":", 1)[1] if ":" in (select or "") else None
        keep = []
        for l in lines:
            t = l.strip()
            if not re.fullmatch(r'\*\*.+\*\*', t):
                continue
            t = t.strip("*")
            m = re.match(r'〔([^〕]*)〕', t)
            if want is not None:
                if not m or m.group(1) != want:
                    continue
            # ⚠️ exclude：`select=bold` 時排除帶該標籤的行
            #    （《南華》的 34 行卷末題署一直算在經文層裡，345 漢字）
            elif exclude and m and m.group(1) == exclude:
                continue
            if m:
                t = t[m.end():]
            keep.append(t)
        return "\n".join(keep)
    if select and select.startswith("quoted:"):
        #: ⚠️ `quoted:A|B` 取**多個標籤的聯集**。
        #:    《傳習錄》需要它：王陽明在卷上下是〔先生〕（門人筆錄）、
        #:    在卷中是〔先生書〕（他自己執筆），而 `wang-yangming` 要兩者都算。
        #:    兩個標籤分開登錄（`-yulu`／`-shu`）才能對讀，聯集才是他的全部。
        tags = [t for t in select.split(":", 1)[1].split("|") if t]
        pre = tuple("〔" + t + "〕" for t in tags)
        keep = []
        for l in lines:
            t = l.strip()
            if t.lstrip(">").strip().startswith(pre):
                keep.append(re.sub(r'^>*\s*〔[^〕]*〕', '', t))
        return "\n".join(keep)

    keep = []
    for line in lines:
        t = line.lstrip()
        if t.startswith("<!--"):
            continue
        if t.startswith("#") or t.rstrip() == "---":
            continue
        if t.startswith(">"):
            # 其余各档的 `>` 行是本库自述；孙不二那一档的 `>` 行是她的诗。
            if not keep_quoted:
                continue
            t = t.lstrip(">").strip()
            if t:
                keep.append(t)
            continue
        if re.match(r'^\*[^*].*\*$', t):
            continue            # 本库自己的斜体注记行
        keep.append(line)
    out = "\n".join(keep)
    if drop_bracketed:
        out = re.sub(r'【[^】]*】', '', out)
    return out

def _spans(path):
    r"""回传这个档里的 (id, expect, keep_quoted, 正文) 清单。

    ⚠️ 允许**嵌套**：「经＋注」体的语料里，经文与注文占同一批行
    （经文是 `**…**` 行，注是 `> 〔X注〕` 行），所以同一段要能同时属于两层：

        <!-- NUWA-CORPUS BEGIN id=heshanggong   select=quoted:河上公注 expect=… -->
        <!-- NUWA-CORPUS BEGIN id=laozi-heshang select=bold           expect=… -->
        …正文…
        <!-- NUWA-CORPUS END id=laozi-heshang -->
        <!-- NUWA-CORPUS END id=heshanggong -->

    外层的内容会含内层的标记行，而 `_strip` 会丢掉 `<!--` 行，所以无妨。
    END 关最近的未关 BEGIN（后进先出）；带 id 的 END 必须与之相符。
    ⚠️ 键值对不限顺序（只要求 id 与 expect）。
    """
    lines = io.open(path, encoding='utf-8').read().split("\n")
    out, stack = [], []
    for k, line in enumerate(lines):
        m = BEGIN.search(line)
        if m:
            f = _kv(m.group("kv"))
            if "id" not in f or "expect" not in f:
                raise SystemExit("BEGIN 缺 id 或 expect：%s 第 %d 行" % (path, k + 1))
            stack.append((k, f))
            continue
        m = END.search(line)
        if m:
            if not stack:
                raise SystemExit("多餘的 END：%s 第 %d 行" % (path, k + 1))
            i, f = stack.pop()
            if m.group("id") and m.group("id") != f["id"]:
                raise SystemExit("END 的 id 與 BEGIN 不符：%s 第 %d 行（%s ≠ %s）"
                                 % (path, k + 1, m.group("id"), f["id"]))
            out.append((f["id"], int(f["expect"]),
                        f.get("keep_quoted") == "1",
                        _strip(lines[i + 1:k],
                               f.get("keep_quoted") == "1",
                               f.get("drop_bracketed") == "1",
                               f.get("select"),
                               f.get("exclude"))))
    if stack:
        raise SystemExit("BEGIN 沒有收尾：%s 第 %d 行" % (path, stack[-1][0] + 1))
    return out

def _walk():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames
                       if d not in (".git", "sentinel", "scripts", "人格庫")]
        for fn in sorted(filenames):
            if fn.endswith(".md"):
                yield os.path.join(dirpath, fn)


def load_all(check=True):
    """{id: 正文} —— 同一個 id 的多個片段會依檔名順序接起來。"""
    parts, bad = {}, []
    for path in _walk():
        head = io.open(path, encoding='utf-8').read(4096)
        if "NUWA-CORPUS BEGIN" not in head and "NUWA-CORPUS BEGIN" not in \
                io.open(path, encoding='utf-8').read():
            continue
        for aid, expect, _kq, text in _spans(path):
            got = han(text)
            if got != expect:
                bad.append((os.path.relpath(path, ROOT), aid, expect, got))
            parts.setdefault(aid, []).append(text)
    if check and bad:
        for rel, aid, expect, got in bad:
            print("❌ 標記對不上：%s [%s] expect=%d got=%d (%+d)"
                  % (rel, aid, expect, got, got - expect), file=sys.stderr)
        raise SystemExit("語料邊界漂移了——先查分層，不要改 expect。")
    return {aid: "\n".join(v) for aid, v in parts.items()}


def load(author_id, check=True):
    d = load_all(check=check)
    if author_id not in d:
        raise SystemExit("找不到 id=%s；現有：%s" % (author_id, sorted(d)))
    return d[author_id]


def main():
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    print("tianmu 語料載入器 · 自我對帳")
    print("=" * 62)
    corp = load_all(check=False)
    ok = True
    for aid in sorted(corp, key=lambda a: -han(corp[a])):
        got = han(corp[aid])
        reg = REGISTERED.get(aid)
        if reg is None:
            verdict = "（未登錄）"
        elif got == reg:
            verdict = "✅ 與登錄值相符"
        else:
            verdict = "⚠️ 差 %+d" % (got - reg)
            if aid not in NOTE:
                ok = False
        print("  %-16s %8d  %s" % (aid, got, verdict))
        if aid in NOTE:
            print("  %-16s          ↳ %s" % ("", NOTE[aid]))
    print("=" * 62)
    tot = sum(han(t) for t in corp.values())
    print("  合計 %d 漢字，%d 個角色" % (tot, len(corp)))
    print("  全部相符（或已附說明）" if ok else "  ⚠️⚠️ 有未說明的不符，請查分層")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
