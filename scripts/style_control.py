# -*- coding: utf-8 -*-
r"""跨文本比詞頻之前先跑這個：量虛詞占比，並找實測的不變量當對照組。

為什麼需要
----------
本庫跨文本比詞頻一直用「每萬漢字」當分母。那在文體相近的文本之間沒問題，
**但文體一變就有系統性偏差**：虛詞占比高的文本，每個實詞的密度會被機械地壓低。

2026-11-18 的實例（三家《老子》註）：虛詞占比 河上公 24.3%／王弼 35.3%／
李道純 19.8%（極差比 1.787）。用總字分母時王弼 257.7 與李道純 255.3 的「無」
看起來一樣（p=0.908），本庫因此寫了「兩人同在高無那一側」；
**換實詞分母後三對全部顯著（王李 p=0.003），正確的是三階梯度。**

而「對照組」本身也錯過一次：2026-11-10 用「也」證明河上公與王弼無文體假影
（p=0.49），**兩家時成立，加第三家就破了**（李道純 140.5 vs 506／525）。

所以：**不要假設某個字是中性的。對每個候選做所有成對檢定，全部不顯著才合格。**

用法
----
    python scripts/style_control.py            # 跑內建的三家《老子》註示例
    # 或在自己的腳本裡：
    from style_control import report
    report([("甲", text_a), ("乙", text_b), ("丙", text_c)],
           words=["治身", "無", "有", "心"])
"""
import io
import os
import re
import sys
from math import exp, lgamma

HAN = re.compile(r'[一-鿿]')

#: 純語法虛詞：代詞・介詞・連詞・副詞・句末語氣詞。
#: ⚠️ 刻意不含 無/有/為/能/可/得/言/謂/自/相/復——那些在《老子》註一類的文本裡
#:    帶內容，放進分母會把要測的東西一起扣掉。換領域時要重新審這張表。
XU = ["之", "而", "以", "其", "不", "者", "則", "故", "所", "於", "是", "此",
      "乃", "若", "如", "與", "亦", "又", "必", "皆", "常", "夫",
      "矣", "焉", "乎", "哉", "也", "曰"]

#: 等價字集：轉錄用字不同時必須合算，否則會得到假零。
EQ = {"為": ["為", "爲"], "真": ["真", "眞"], "氣": ["氣", "气", "炁"],
      "無": ["無", "无"], "即": ["即", "卽"], "雖": ["雖", "𨿽"]}

#: 對照組候選（找三家都齊平的那些）
CAND = XU + ["有", "無", "為", "能", "可", "得", "言", "謂", "自", "相", "復"]


def han(s):
    return len(HAN.findall(s))


def cnt(text, w):
    return sum(len(re.findall(f, text)) for f in EQ.get(w, [w]))


def fisher(a, b, c, d):
    """2×2 Fisher 精確檢定（雙尾）。⚠️ n 上萬時不要用 comb 版，會爆開。"""
    def lc(n, k):
        return lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1)
    n = a + b + c + d
    r1, c1 = a + b, a + c
    def p(x):
        return exp(lc(c1, x) + lc(n - c1, r1 - x) - lc(n, r1))
    obs = p(a)
    tot = 0.0
    for x in range(max(0, r1 - (n - c1)), min(r1, c1) + 1):
        q = p(x)
        if q <= obs * (1 + 1e-9):
            tot += q
    return min(tot, 1.0)


def denominators(texts):
    """回傳 {名: (總字數, 虛詞次數, 實詞分母)}，並回報極差比。"""
    out = {}
    for k, t in texts:
        tot = han(t)
        xu = sum(cnt(t, w) for w in XU)
        out[k] = (tot, xu, tot - xu)
    ratios = [out[k][1] / out[k][0] for k, _ in texts]
    return out, (max(ratios) / min(ratios) if min(ratios) else float('inf'))


def controls(texts, alpha=0.05, min_count=20):
    """回傳合格的對照組候選：所有成對檢定在 Bonferroni 校正後全不顯著。

    ⚠️ `min_count` 是檢定力門檻——低次數的「不顯著」是檢定力不足，
       不是真的齊平（2026-11-18 的「哉」只有 2/3/8 次）。
    """
    names = [k for k, _ in texts]
    D, _ = denominators(texts)
    pairs = [(i, j) for i in range(len(texts)) for j in range(i + 1, len(texts))]
    alpha_c = alpha / max(1, len(pairs))
    good = []
    for w in CAND:
        c = [cnt(t, w) for _, t in texts]
        if min(c) < min_count:
            continue
        ps = [fisher(c[i], D[names[i]][0] - c[i],
                     c[j], D[names[j]][0] - c[j]) for i, j in pairs]
        if all(p > alpha_c for p in ps):
            d = [10000.0 * c[i] / D[names[i]][0] for i in range(len(texts))]
            good.append((max(d) / min(d), w, c, d, min(ps)))
    good.sort()
    return good, alpha_c


def report(texts, words=(), alpha=0.05):
    """跨文本比較前的完整檢查報告。"""
    names = [k for k, _ in texts]
    D, spread = denominators(texts)
    print("=== 分母 ===")
    print("%-8s %9s %9s %9s %9s" % ("", "總字數", "虛詞", "實詞分母", "虛詞占比"))
    for k in names:
        tot, xu, shi = D[k]
        print("%-8s %9d %9d %9d %8.1f%%" % (k, tot, xu, shi, 100.0 * xu / tot))
    print("   虛詞占比極差比 **%.3f**  → %s" % (
        spread,
        "⚠️⚠️ > 1.2，**不要用每萬總字下跨文本結論，改用實詞分母**"
        if spread > 1.2 else "✅ ≤ 1.2，每萬總字可用"))

    good, alpha_c = controls(texts, alpha=alpha)
    print()
    print("=== 實測的不變量（可當對照組；Bonferroni α=%.4f，次數門檻 20）===" % alpha_c)
    if not good:
        print("   ⚠️⚠️ 找不到合格的對照組——跨文本的密度差異無法排除文體成分。")
    for sp, w, c, d, mp in good:
        print("   %-3s 極差比 %.2f   %s   最小 p=%.3g" % (
            w, sp, " / ".join("%.1f(%d)" % (d[i], c[i]) for i in range(len(texts))), mp))
    print("   ⚠️ 用它當對照組時不能同時拿它下結論——那會循環。")

    if words:
        pairs = [(i, j) for i in range(len(texts))
                 for j in range(i + 1, len(texts))]
        ac = alpha / max(1, len(pairs))
        print()
        print("=== 要測的詞：兩種分母並列 ＋ 實詞分母下的成對檢定 ===")
        for w in words:
            c = [cnt(t, w) for _, t in texts]
            print("  【%s】" % w)
            print("     每萬總字  " + " / ".join(
                "%s %.1f" % (names[i], 10000.0 * c[i] / D[names[i]][0])
                for i in range(len(texts))))
            print("     每萬實詞  " + " / ".join(
                "%s %.1f" % (names[i], 10000.0 * c[i] / D[names[i]][2])
                for i in range(len(texts))))
            for i, j in pairs:
                p = fisher(c[i], D[names[i]][2] - c[i],
                           c[j], D[names[j]][2] - c[j])
                print("       %s vs %s  p=%-11.3g %s" % (
                    names[i], names[j], p, "顯著" if p < ac else "不顯著"))


def _demo():
    """內建示例：三家《老子》註。"""
    T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def marked(path, tag):
        s = io.open(os.path.join(T, path), encoding='utf-8').read()
        i = s.index("道可道")
        i = s.rindex("\n", 0, i)
        end = len(s)
        for mark in ("題記", "音義", "附錄"):   # ⚠️ 不切會多算 466 字題記
            k = s.find(mark, i)
            if k > 0:
                end = min(end, k)
        return "\n".join(re.sub(r'^>\s*〔[^〕]*〕', '', l.strip())
                         for l in s[i:end].split("\n")
                         if l.strip().startswith(">") and tag in l)

    def ddhy():
        s = io.open(os.path.join(T, "道德會元-李道純",
                                 "01-李道純-道德會元.md"), encoding='utf-8').read()
        b = s[s.index("## 註腳・章論・頌"):]
        b = re.sub(r'【[^】]*】', '', b)
        return "\n".join(l for l in b.split("\n") if not l.lstrip().startswith("#"))

    report([("河上公", marked("老子河上公章句-河上公.md", "河上公注")),
            ("王弼", marked("道德經王弼註-王弼.md", "王弼注")),
            ("李道純", ddhy())],
           words=["治身", "無", "有", "心", "道", "氣"])


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    _demo()
