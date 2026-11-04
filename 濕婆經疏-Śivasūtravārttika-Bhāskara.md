# 《濕婆經疏》Śivasūtravārttika — Bhāskara

**梵文書名**：Śivasūtravārttika（शिवसूत्रवार्त्तिक）
**註者**：**Bhāskara**（Bhāskarabhaṭṭa，約 11 世紀，克什米爾），**Divākarabhaṭṭa 之子**
**所註本文**：**Vasugupta 傳出的《[濕婆經](濕婆經-Śivasūtra.md)》——本檔傳本作 75 條（20／10／45）**
**規模**：**經 75 條（180 詞）＋註偈 757 首（3,218 詞）**

> ## 📌 這一檔補上了本資料夾一個長期的方法論缺口
>
> **本資料夾反覆指認「註釋者把框架讀進一個沒有該框架的文本」**（見《[認出之心要](認出之心要-Pratyabhijñāhṛdaya-Kṣemarāja.md)》、《[至上義精要註](至上義精要註-Paramārthasāravivṛti-Yogarāja.md)》）。
> **但只有一家註的時候，有兩個解釋分不開**：
> **(a) 是這個註者自己讀進去的；(b) 那套框架本來就屬於活的傳統，只是根本經文極簡。**
>
> `人格庫/sun-buer-perspective` 的 04 檔就寫著這個限制：**「我沒有陳攖寧以外的註本」。**
>
> **《濕婆經》有兩家獨立的註**——**本檔的 Bhāskara《Vārttika》（75 條，20／10／45）**與 **Kṣemarāja《Vimarśinī》（77 條，22／10／45）**。
> **所以這一次可以分開。結果見下節：(a) 被排除。**

---

## 文本來源與授權

| 項目 | 內容 |
|---|---|
| **來源** | **GRETIL**（哥廷根大學圖書館） |
| **原始檔** | `sa_zivasUtra-with-vArttika.txt` |
| **輸入者** | Oliver Hellwig（2001/02 輸入，2020-07-31 TEI 版） |
| **底本** | **Madhusudan Kaul Shastri, Srinagar: Kashmir Pratap Steam Press, 1925** |
| **授權** | 原文為 11 世紀作品，早已進入公有領域；GRETIL 電子文本採 **CC BY-NC-SA 4.0** |
| **抓取** | 2026-10-14 取得（當時只抽出經文）；**2026-11-04 補收註偈** |

> **本檔依原始檔的 `sivs_`（經）與 `sivsv_`（註偈）標記分層呈現，未改動任何字母。**
>
> ⚠️ **GRETIL 的 header 沒有標註者名**，只寫「Sivasutra (with Vartika)」。
> **歸於 Bhāskara 是依外部文獻**（2026-11-04 查：Bhāskarabhaṭṭa，11 世紀，Divākarabhaṭṭa 之子；現代校譯本為 Mark Dyczkowski，*The Aphorisms of Śiva: The Śivasūtra with Bhāskara's Commentary, the Vārttika*, SUNY Press）。**本檔未查 1925 年底本本身的署名。**
> ⚠️ **另有 J.C. Chatterji 的 1916 年 KSTS 本（Vols. IV & V）**——**與本檔底本是兩個版本，本檔未對校。**

---

## 四項實測（可複驗）

**方法**：依 `sivs_` / `sivsv_` 標記逐一分層（**單一次序掃描，不用跨行正規式**），剝除 `<...>` 標籤、`[ ] * | /` 與章名後切詞。
⚠️ **已先普查編碼變體**：本檔 `@` 僅 1 處、無 `.ṅd`，故不需正規化（這是前一次在 Abhinavagupta 上學到的步驟）。

### 一、十八倍展開——而他的註比經文「更不密」

| | 條數 | 詞數 | **平均詞長** |
|---|--:|--:|--:|
| **經**（Vasugupta） | 75 | 180 | **9.93** |
| **註偈**（Bhāskara） | **757** | **3,218** | **9.42** |
| 倍數 | **10.1×** | **17.9×** | — |

⚠️⚠️ **這是本資料夾第一個「註者沒有寫得更密」的案例。**
**對照**：Yogarāja 註 Abhinavagupta 的 105 頌——**11.26 對 8.20，密 37%**。
**而 Bhāskara 是 9.42 對 9.93——反而低。**
✅ **而這個比較是可靠的**：經與註同在一檔、同一輸入者，**不存在跨檔轉寫慣例的問題**（那個問題見《[怛特羅無上](怛特羅無上-Tantrāloka-Abhinavagupta.md)》檔的更正節）。

### 二、⚠️ 十三個術語在經文裡 0 次——而這一次附了顯著性檢定

| 術語 | 經（180 詞） | **Bhāskara 註**（／萬詞） | **Kṣemarāja 另兩部**（／萬詞） |
|---|:-:|--:|--:|
| **svātantrya** | **0** | 24.9 | 19.5 |
| **vimarśa** | **0** | 24.9 | 22.7 |
| **prakāśa** | **0** | 40.4 | 94.2 |
| **spanda** | **0** | 24.9 | 16.2 |
| **pratyabhijñ** | **0** | 18.6 | 61.7 |
| **camatkār** | **0** | 9.3 | 13.0 |
| **mala** | **0** | 21.8 | 9.7 |
| **āṇava** | **0** | 18.6 | 9.7 |
| **māyīya** | **0** | 3.1 | 13.0 |
| **kārma** | **0** | 6.2 | 6.5 |
| **turya** | **0** | 28.0 | 6.5 |
| **anuttara** | **0** | 6.2 | 6.5 |
| **samāveśa** | **0** | 3.1 | 19.5 |

**合計 74 次（230.0／萬詞）。若經與註同分布，180 詞的經文中期望出現 4.14 次，實際 0 次——Poisson p ≈ 0.016。**

> ⚠️ **單一術語的「0 次」不足為奇**：經文只有 180 詞，每個術語的期望值都在 0.06–0.73 之間。
> **要有意義，必須合計檢定。** 本檔是這個資料夾第一次為詞頻宣稱附上顯著性檢定。

### 三、✅ 三角比對的結論：那套術語屬於傳統，不屬於任何一家註者

**上表第三欄是 Kṣemarāja 在《[認出之心要](認出之心要-Pratyabhijñāhṛdaya-Kṣemarāja.md)》＋《[振動抉擇](振動抉擇-Spandanirṇaya-Kṣemarāja註.md)》裡的密度（共 3,077 詞）。**

**十三個詞，兩家註者全部都用——13／13。**

> **📌 所以「是這個註者自己讀進去的」這個解釋被排除。**
> **成立的是：克什米爾濕婆派的整套技術語彙，在那 180 詞的根本經文裡一個都沒有，而兩家互不相干的註者各自供應它。**
> **這不是某一個人的毛病，是這個註釋傳統的工作方式。**

⚠️ **但這個比對有一個不對等**：Kṣemarāja 那一欄取自他的**另外兩部**著作，**不是他的《濕婆經疏》（Vimarśinī）**——那一部 GRETIL 沒有。
**所以這是「Bhāskara 註濕婆經」對「Kṣemarāja 註別的書」，不是同一本書的兩家註對讀。**
**但 13／13 這個結論不受影響**，因為要問的是那些詞在傳統裡存不存在。

### 四、兩家的偏重可以分開——而這才是各自的指紋

| 詞 | **Bhāskara**（／萬詞） | **Kṣemarāja**（／萬詞） | 誰更重 |
|---|--:|--:|---|
| **turya**（第四位） | **28.0** | 6.5 | **Bhāskara 4.3×** |
| **mala**（垢） | **21.8** | 9.7 | **Bhāskara 2.2×** |
| **āṇava**（個我垢） | **18.6** | 9.7 | **Bhāskara 1.9×** |
| **svātantrya**（至上自由） | **24.9** | 13.0 | **Bhāskara 1.9×** |
| — | | | |
| **cit**（覺） | 43.5 | **169.0** | Kṣemarāja 3.9× |
| **pratyabhijñā**（認出） | 6.2 | **39.0** | Kṣemarāja 6.3× |
| **prakāśa**（顯照） | 18.6 | **71.5** | Kṣemarāja 3.8× |
| **samāveśa**（入定） | 3.1 | **19.5** | Kṣemarāja 6.3× |

**同一套借來的詞，兩種配重**：
**Bhāskara 是「垢與第四位」的註者；Kṣemarāja 是「光與認出」的註者。**

---

## 五、他自己的方法論原則，寫在第一條的末尾

**〔1.1:14〕**：
> **praśleṣāśleṣapāṭhābhyāṃ sūtram āha maheśvaraḥ**
> 「**大自在天是以『連讀』（praśleṣa）與『不連讀』（āśleṣa）兩種讀法說出此經的。**」

> **📌 這一句解釋了一件本資料夾已經記錄、但沒有原因的事。**
> 《[濕婆經](濕婆經-Śivasūtra.md)》檔記著：**本檔傳本第一章 20 條、Kṣemarāja 本 22 條，第二三章完全相同，「原因是兩家對第一章若干條的斷句不同」。**
> **而 Bhāskara 的立場是：經文被說出來時就容許兩種連音斷讀，因而兩種意思。**
> **所以那個條數分歧不是傳抄失誤，是解經原則的直接後果。**

⚠️ **而這個詞用得極省**：`praśleṣa`／`āśleṣa`／`pāṭhābhyāṃ` 全書各 **1 次**，`athavā`（或者說）**1 次**，`vikalpa` **5 次**。
**他宣告了這個原則，卻幾乎沒有再使用它。**

---

## 六、註量分布：他認為哪裡需要說

**有註 73／75 條，註偈共 757 首。**

| 經條 | 原文 | 註偈數 |
|---|---|--:|
| **2.7** | `mātṛkācakrasaṃbodhaḥ`（母字輪之徹悟） | **45** |
| 1.9 | `aviveko māyā sauṣuptam`（無分別即幻，即深眠） | 21 |
| 3.6 | `mohāvaraṇāt siddhiḥ` | 21 |
| 1.6 | `śakticakrasaṃdhāne viśvasaṃhāraḥ` | 20 |
| 1.20 | `mahāhradānusaṃdhānān mantravīryānubhavaḥ` | 20 |
| 3.43 | `naisargikaḥ prāṇasambandhaḥ` | 20 |
| — | | |
| **1.7** | `jñānaṃ jāgrat`（知即醒） | **0** |
| **1.8** | `svapno vikalpāḥ`（夢即分別） | **0** |

> ⚠️⚠️ **三境之中他只註深眠。**
> **醒（1.7）0 首、夢（1.8）0 首、深眠（1.9）21 首。**
> **而全書註偈最多的一條是「母字輪」（2.7，45 首）——那是音聲學的技術核心。**
> **所以他的力氣花在技術與形而上，不花在對境的描述。**

---

## 正文（經與註分層）

## 第一章 prathama unmeṣa

### 〔1.1〕 caitanyam ātmā

*註偈 14 首*

```
caitanyaṃ citkriyārūpaṃ śivasya paramasya yat  // 1.1:1
svātantryam etad evātmā tato 'sau paramaḥ śivaḥ  // 1.1:2
athavā ko 'yam ātmeti praṣṭ bodhayituṃ śiśūn  // 1.1:3
nātmā deho na ca prāṇo na manaḥ khaṃ na śūnyabhūḥ  // 1.1:4
kiṃtu caitanyam evātmety ādiṣṭaṃ parameṣṭhinā  // 1.1:5
atha caitanyam evaitad ātmā svābhāvikaṃ vapuḥ  // 1.1:6
viśeṣācodanād asya jagataś cety arūpiṇaḥ  // 1.1:7
acetyamānaṃ kasyāpi vapuḥ kim api no bhavet  // 1.1:8
cetyamānaṃ tu cidrūpatādātmyāc cinmayaṃ bhavet  // 1.1:9
evaṃ śivoktayā nītyā jaṅgamasthāvarātmanaḥ  // 1.1:10
caitanyam eva viśvasya svarūpaṃ pāramārthikam  // 1.1:11
nanv evaṃvidhaviśvasya caitanyaṃ ced vapus tadā  // 1.1:12
kathaṃ bandhasya sambandha iti śaṅkāṃ vyapohitum  // 1.1:13
praśleṣāśleṣapāṭhābhyāṃ sūtram āha maheśvaraḥ  // 1.1:14
```

### 〔1.2〕 jñānaṃ bandhaḥ

*註偈 5 首*

```
ajñānam iti tatrādyaṃ caitanyasphārarūpiṇi  // 1.2:1
ātmany anātmatājñānaṃ jñānaṃ punar anātmani  // 1.2:2
dehādāv ātmamānitvaṃ dvayam apy etad āṇavam  // 1.2:3
malaṃ svakalpitaṃ svasmin bandhaḥ svecchāvibhāvitaḥ  // 1.2:4
kim āṇavamalātmaiva bandho 'yaṃ nety udīryate  // 1.2:5
```

### 〔1.3〕 yonivargaḥ kalāśarīram

*註偈 12 首*

```
yonir bhedaprathāhetur māyā vargas tadutthitaḥ  // 1.3:1
kalādikṣitiparyantatattvarāśis tadātmakaḥ  // 1.3:2
māyīyākhyaṃ malaṃ tattadbhinnavedyaprathāmayam  // 1.3:3
kaleti kāyam āviśya paricchedakarī nṛṇām  // 1.3:4
vyāpṛtiḥ puṇyapāpātmā śarīraṃ yasya tat punaḥ  // 1.3:5
kārmaṃ ca malam etasmin dvaye bandho 'nuvartate  // 1.3:6
īśvarapratyabhijñāyām uktam etan malatrayam  // 1.3:7
svātantryahānir bodhasya svātantryasyāpy abodhatā  // 1.3:8
dvidhāṇavaṃ malam idaṃ svasvarūpāpahārataḥ  // 1.3:9
bhinnavedyaprathātraiva māyīyaṃ janmabhogadam  // 1.3:10
kartary abodhe kārmaṃ tu māyāśaktyaiva tat trayam  // 1.3:11
ity athaiṣāṃ malānāṃ tu bandhakatvaṃ nirūpyate  // 1.3:12
```

### 〔1.4〕 jñānādhiṣṭhānaṃ mātṛkā

*註偈 19 首*

```
apūrṇam anyatārūpaṃ bhinnavedyaprathātmakam  // 1.4:1
śubhāśubhātmakāśeṣakarmasaṃskāravigraham  // 1.4:2
trividhaṃ malam uktaṃ yat tad eva jñānam ucyate  // 1.4:3
na so 'sti pratyayo loke yaḥ śabdānugamād ṛte  // 1.4:4
anuviddham iva jñānaṃ sarvaṃ śabdena gamyate  // 1.4:5
ity uktanītyā jñānasya vividhasyāsya mātṛkā  // 1.4:6
akārādikṣakārāntapañcāśadvarṇavigrahā  // 1.4:7
śivādikṣitiparyantatattvagrāmaprasūtibhūḥ  // 1.4:8
karandhracitimadhyasthā brahmapāśāvalambikāḥ  // 1.4:9
pīṭheśvaryo mahāghorā mohayanti muhurmuhuḥ  // 1.4:10
iti śrītimirodghāṭaproktanītyanusārataḥ  // 1.4:11
svarādivargādhiṣṭhātṛmātṛcakrapariṣkṛtā  // 1.4:12
apūrṇo 'ham ahaṃ pūrṇo 'haṃ kṛśo 'haṃ kṛśetaraḥ  // 1.4:13
iti śabdānuvedhena śokaharṣādikārikā  // 1.4:14
adhiṣṭhānam adhiṣṭhātrī tadadhiṣṭhānato nṛṇām  // 1.4:15
alabdhāntarmukhasvātmaviśrāntīni nirantaram  // 1.4:16
bahirmukhāni jñānāni kathyante bandhahetavaḥ  // 1.4:17
athedṛgbandhasambandhapraśamopāya ucyate  // 1.4:18
paramopeyaviśrāntisatattvaḥ parameṣṭhinā  // 1.4:19
```

### 〔1.5〕 udyamo bhairavaḥ

*註偈 8 首*

```
yo 'yaṃ vimarśarūpāyāḥ prasarantyāḥ svasaṃvidaḥ  // 1.5:1
jhaṭity ucchalanākārapratibhonmajjanātmakaḥ  // 1.5:2
udyamo 'ntaḥparispandaḥ pūrṇāhambhāvanātmakaḥ  // 1.5:3
sa eva sarvaśaktīnāṃ sāmarasyād aśeṣataḥ  // 1.5:4
viśvato bharitatvena vikalpānāṃ vibhedinām  // 1.5:5
alaṃ kavalanenāpīty anvarthād eva bhairavaḥ  // 1.5:6
athedṛgbhairavāpatter bandhapraśamakāraṇāt  // 1.5:7
vyutthānaṃ ca bhavec chāntabhedābhāsam itīryate  // 1.5:8
```

### 〔1.6〕 śakticakrasaṃdhāne viśvasaṃhāraḥ

*註偈 20 首*

```
yo 'yam uktaḥ svasaṃvitter udyamo bhairavātmakaḥ  // 1.6:1
asyāsti mahatī śaktir atikrāntakramākramā  // 1.6:2
niḥśeṣanijacicchakticakrākramaṇalampaṭā  // 1.6:3
riktāriktobhayākārāpy anetadrūpiṇī parā  // 1.6:4
yayaiva svātmacidbhittau prameyollāsanāditaḥ  // 1.6:5
parapramātṛviśrāntiparyantaspandarūpayā  // 1.6:6
sṛṣṭisthitilayānākhyābhāsaśaktiprasāraṇāt  // 1.6:7
prapañcaviṣayaṃ cañcatpañcakṛtyaṃ prapañcitam  // 1.6:8
tayā prasāritasyāsya śakticakrasya yat punaḥ  // 1.6:9
saṃdhānam āntarāmnāyāmnātakramavimarśanam  // 1.6:10
tasmin saty asya viśvasya kālāgnyādikalāvadheḥ  // 1.6:11
saṃhāraḥ syāt svasaṃvittivahnisadbhāvalakṣaṇaḥ  // 1.6:12
evaṃ svasaṃvitkālāgnipluṣṭabhedasya yoginaḥ  // 1.6:13
na syāt samādhivyutthānabhedaḥ ko 'pīti kathyate  // 1.6:14
jāgratsvapnasuṣuptabhede turyābhogasambhavaḥ  // 1.6:15
udyamo bhairava iti proktarūpaṃ sphuradvapuḥ  // 1.6:16
turyaṃ nāma paraṃ dhāma tadābhogaś camatkriyā  // 1.6:17
bhede 'pi jāgradādīnāṃ yoginas tasya sambhavaḥ  // 1.6:18
anusyūtiḥ parānandarūpā syād iti śiṣyate  // 1.6:19
jāgradāditrayaṃ sūtratrayeṇa lakṣyate kramāt  // 1.6:20
```

### 〔1.7〕 jñānaṃ jāgrat

> ⚠️ **本條無註偈。**

### 〔1.8〕 svapno vikalpāḥ

> ⚠️ **本條無註偈。**

### 〔1.9〕 aviveko māyā sauṣuptam

*註偈 21 首*

```
jñānaṃ bāhyākṣajaṃ jāgrat sarvasādhāraṇārthakam  // 1.9:1
svapnaḥ svātmaiva samprokto vikalpāḥ svātmasambhavāḥ  // 1.9:2
aviveko nijākhyātir māyā mohas tadātmakaḥ  // 1.9:3
sauṣuptaṃ yoginām etat tritayaṃ dhāraṇādikam  // 1.9:4
īśvarapratyabhijñāyāṃ jāgarādy api lakṣitam  // 1.9:5
śūnye buddhyādyabhāvātmany ahaṃtākartṛtāpade  // 1.9:6
asphuṭārūpasaṃskāramātriṇi jñeyaśūnyatā  // 1.9:7
sākṣāṇām āntarī vṛttiḥ prāṇādiprerikā matā  // 1.9:8
jīvanākhyāthavā prāṇe 'haṃtā puryaṣṭakātmikā  // 1.9:9
tāvan mātrasthitau proktaṃ sauṣuptaṃ pralayopamam  // 1.9:10
savedyam apavedyaṃ ca māyāmalayutāyutam  // 1.9:11
manomātrapathe 'py akṣaviṣayatvena vibhramāt  // 1.9:12
spaṣṭāvabhāsā bhāvānāṃ sṛṣṭiḥ svapnapadaṃ matam  // 1.9:13
sarvākṣagocaratvena yā tu bāhyatayā sthirā  // 1.9:14
sṛṣṭiḥ sādhāraṇī sarvapramātṇāṃ sa jāgaraḥ  // 1.9:15
iti vistarataḥ prokte lokayogyanusārataḥ  // 1.9:16
jāgarāditraye 'muṣminn avadhānena jāgrataḥ  // 1.9:17
śakticakrānusaṃdhānād viśvasaṃhārakāraṇāt  // 1.9:18
turyābhogamayābhedakhyātir akhyātihāriṇī  // 1.9:19
sphuraty avirataṃ yasya sa taddhārādhirohataḥ  // 1.9:20
turyātītamayaṃ yogī proktacaitanyam āmṛśan  // 1.9:21
```

### 〔1.10〕 tritayabhoktā vīreśaḥ

*註偈 13 首*

```
jāgarāditrayaṃ proktaśakticakrānusaṃdhitaḥ  // 1.10:1
turyānandarasāsārāc churitaṃ bhedavarjanāt  // 1.10:2
ānandarasanirmagnaṃ paramaṃ vyoma bhāvayan  // 1.10:3
tritayasyāsya yo bhoktā camatkartā sa yogirāṭ  // 1.10:4
triṣu dhāmasu yad bhogyaṃ bhoktā yaś ca prakīrtitaḥ  // 1.10:5
vidyāt tad ubhayaṃ yas tu sa bhuñjāno na lipyate  // 1.10:6
ity uktaniṣpratidvandvisaṃvitsāmrājyavaibhavaḥ  // 1.10:7
cidghanaḥ svātmavijñānaparamānandanirbharaḥ  // 1.10:8
vīreśo yena vīrāṇāṃ bhedagrasanakāriṇām  // 1.10:9
antarbahirvisaratām indriyāṇām adhīśvaraḥ  // 1.10:10
kim asya paracittattvārohaviśrāntisūcikāḥ  // 1.10:11
bhūmikāḥ santy ayaṃ yābhir yāti sarvottarāṃ sthitim  // 1.10:12
ity antevāsihṛcchaṅkāśāntyai santīty udīryate  // 1.10:13
```

### 〔1.11〕 vismayo yogabhūmikāḥ

*註偈 7 首*

```
yathā sātiśayānande kasyacid vismayo bhavet  // 1.11:1
tathāsya yogino nityaṃ tattadvedyāvalokane  // 1.11:2
niḥsāmānyaparānandānubhūtistimitendriye  // 1.11:3
pare svātmany atṛptyaiva yad āścaryaṃ sa vismayaḥ  // 1.11:4
sa eva khalu yogasya paratattvaikyarūpiṇaḥ  // 1.11:5
bhūmikās tatkramārohaparaviśrāntisūcikāḥ  // 1.11:6
īrdṛgvismayavadyogabhūmikārūḍhacetasaḥ  // 1.11:7
```

### 〔1.12〕 icchā śaktir umā kumārī

*註偈 13 首*

```
parabhairavatāṃ yuktyā samāpannasya śāśvatīm  // 1.12:1
tasyaiva yogino yecchā śaktiḥ saiva bhavaty umā  // 1.12:2
parā bhaṭṭārikā saiva kumārīti prakīrtitā  // 1.12:3
sadāśivādikṣityantaviśvasargādilīlayā  // 1.12:4
kumārī kuṃ mahāmāyābhūmiṃ mārayatīty api  // 1.12:5
kumārī copabhogyāsya yogino bhairavātmanaḥ  // 1.12:6
kumārī nānyabhogyā ca bhoktraikātmyena tiṣṭhati  // 1.12:7
umā kumārī saṃtyaktasarvāsaṅgā maheśituḥ  // 1.12:8
ārādhanaparā tadvad icchā śaktis tu yoginaḥ  // 1.12:9
ayam eva sphuṭaḥ pāṭho dṛṣṭo 'nuttaradaiśikaiḥ  // 1.12:10
vyākhyātaś ca paraiḥ śaktitametipaṭhanāt punaḥ  // 1.12:11
prakarṣo vyākṛto 'muṣyāḥ śakter jñānakriyātmataḥ  // 1.12:12
evam īdṛkprabhāvecchāśaktiyuktasya yoginaḥ  // 1.12:13
```

### 〔1.13〕 dṛśyaṃ śarīram

*註偈 19 首*

```
yad yad dṛśyam aśeṣaṃ tac charīraṃ tasya yoginaḥ  // 1.13:1
aham ity apṛthaktvena pativat pratibhāsanāt  // 1.13:2
śarīraṃ dehadhīprāṇaśūnyarūpaṃ ghaṭādivat  // 1.13:3
dṛśyam evāsya paśuvat draṣṭṛtvena na bhāsate  // 1.13:4
evaṃ dehe ca bāhye ca sarvatraivāsya yoginaḥ  // 1.13:5
mayūrāṇḍarasanyāyāt pratipattir abhedinī  // 1.13:6
dṛśyaṃ śarīratām eti śarīraṃ cāpi dṛśyatām  // 1.13:7
ity uktaṃ yogino yat tan na durghaṭam itīryate  // 1.13:8
hṛdaye cittasaṃghaṭṭād dṛśyasvāpadarśanam  // 1.13:9
hṛdayaṃ tad vijānīyād viśvasyāyatanaṃ mahat  // 1.13:10
ity uktanītyā hṛdayaṃ viśvaviśrāntibhittibhūḥ  // 1.13:11
svasaṃvit tatra saṃghaṭṭaś cittasya calataḥ sataḥ  // 1.13:12
tadaikātmyaparāmarśajāgarūkasvabhāvatā  // 1.13:13
tasmād dṛśyasya viśvasya nīladehādirūpiṇaḥ  // 1.13:14
svāpasyaitadabhāvasya śūnyasyāpi ca darśanam  // 1.13:15
svāṅgarūpeṣu bhāveṣu pramātā kathyate patiḥ  // 1.13:16
iti śrīpratyabhijñoktanītyā patyur iva prabhoḥ  // 1.13:17
svāṅgakalpatayā tasya yathāvatprathanaṃ bhavet  // 1.13:18
ukte 'py evaṃ prameye 'sminn upāyāntaram ucyate  // 1.13:19
```

### 〔1.14〕 śuddhatattvasaṃdhānād vāpaśuśaktiḥ

*註偈 5 首*

```
śuddhaṃ tattvaṃ paraṃ vastu yat tat paraśivātmakam  // 1.14:1
tatsaṃdhānaṃ prapañcasya tanmayatvena bhāvanam  // 1.14:2
tenaiva yasya paśvākhyā bandhaśaktir na vidyate  // 1.14:3
tat sadāśivavatso 'pi viśvasya jagataḥ patiḥ  // 1.14:4
śuddhatattvānusaṃdhānavata evāsya yoginaḥ  // 1.14:5
```

### 〔1.15〕 vitarka ātmajñānam

*註偈 4 首*

```
vitarkaḥ proktasaṃdhānadhvastabandhasya yoginaḥ  // 1.15:1
viśvātmā śiva evāham asmīty arthavicintanam  // 1.15:2
etad eva sphuradrūpam ātmano jñānam ucyate  // 1.15:3
kiṃ cāsya proktavaitarkasvātmavijñānaśālinaḥ  // 1.15:4
```

### 〔1.16〕 lokānandaḥ samādhisukham

*註偈 9 首*

```
lokyaṃ lokayitā ceti lokaś cetyacidātmani  // 1.16:1
tattadrūpatayā tasmiṃ loke sphurati yoginaḥ  // 1.16:2
grāhyagrāhakasaṃvittiḥ sāmānyā sarvadehinām  // 1.16:3
yogināṃ tu viśeṣo 'yaṃ sambandhe sāvadhānatā  // 1.16:4
ity uktanītyā tat sarvam aham ity anusaṃhiteḥ  // 1.16:5
ānando yo bhavaty antas tat samādhisukhaṃ smṛtam  // 1.16:6
yat samādhisukhaṃ tasya svātmārāmasya yoginaḥ  // 1.16:7
tad eva loke lokānām ānando 'ntarvicinvatām  // 1.16:8
vibhūtiyogam etasya darśayaty atha yoginaḥ  // 1.16:9
```

### 〔1.17〕 śaktisaṃdhāne śarīrotpattiḥ

*註偈 4 首*

```
icchā śaktir umety ādisūtroktā śaktir asya yā  // 1.17:1
saṃdhāne yoginas tasyās tanmayībhāvane sati  // 1.17:2
tadvaśāt tattadicchārhaśarīrotpattir iṣyate  // 1.17:3
anyāś ca siddhayas tasya sambhavantīty udīryate  // 1.17:4
```

### 〔1.18〕 bhūtasaṃdhānabhūtapṛthaktvaviśvasaṃghaṭṭāḥ

*註偈 8 首*

```
bhūtānāṃ dehadhīprāṇaśūnyānāṃ grāhakātmanām  // 1.18:1
grāhyāṇāṃ sthāvarāṇāṃ ca saṃdhānaṃ paripoṣaṇam  // 1.18:2
pṛthaktvam atha viśleṣo vyādhyādikleśaśāntaye  // 1.18:3
viśvasya deśakālādiviprakṛṣṭasya yat punaḥ  // 1.18:4
saṃghaṭṭaś cakṣurādyakṣapratyakṣīkaraṇādikam  // 1.18:5
etat sarvaṃ bhavec chaktisaṃdhāne sati yoginaḥ  // 1.18:6
yadā parimitāḥ siddhīr anicchan punar icchati  // 1.18:7
viśvātmatāprathārūpāṃ parāṃ siddhiṃ tadāsya tu  // 1.18:8
```

### 〔1.19〕 śuddhavidyodayāc cakreśatvasiddhiḥ

*註偈 11 首*

```
vaiśvātmyaprathanākāṅkṣī saṃdhatte śaktim ātmanaḥ  // 1.19:1
yadā yogī tadā tasya sadāśivapadaspṛśaḥ  // 1.19:2
īśvaro bahir unmeṣo nimeṣo 'ntaḥ sadāśivaḥ  // 1.19:3
sāmānādhikaraṇyaṃ ca sadvidyāhamidaṃdhiyoḥ  // 1.19:4
iti nītyā jagat sarvam aham eveti yā matiḥ  // 1.19:5
sā śuddhā nirmalā vidyā tadīyād udayāt sphuṭam  // 1.19:6
unmajjanāt sa cicchaktim ātmano nityam āmṛśet  // 1.19:7
yadā yogī tadā tasya cakreśatvam anuttaram  // 1.19:8
māheśvaryaṃ samāveśotkarṣāt sidhyati yoginaḥ  // 1.19:9
viśvātmakataduttīrṇasvātmārāmatvam eva saḥ  // 1.19:10
icchati svacchacidrūpo yadā yogī tadāsya tu  // 1.19:11
```

### 〔1.20〕 mahāhradānusaṃdhānān mantravīryānubhavaḥ

*註偈 20 首*

```
parā bhaṭṭārikā saṃvidicchāśaktipuraḥsaram  // 1.20:1
sthūlaprameyaparyantaṃ vamantī viśvam āntaram  // 1.20:2
pramātrantarbahīrūpahṛṣīkaviṣayātmanām  // 1.20:3
khecaryādipravāhāṇāṃ bāhyābhyantararūpiṇām  // 1.20:4
pravartakatvāt svacchatvagambhīratvādidharmataḥ  // 1.20:5
mahāhrado jagadvyāpī deśakālādyagocaraḥ  // 1.20:6
antas tasyānusaṃdhānāt tādātmyasyāvamarśanāt  // 1.20:7
akārādikṣakārāntaśabdarāśiprathātmanaḥ  // 1.20:8
kṣityādiśivaparyantatattvāntaḥkṣobhakāriṇaḥ  // 1.20:9
mantravīryasya sarveṣāṃ mantrāṇāṃ prāṇarūpiṇaḥ  // 1.20:10
parāhaṃtāparāmarśamayasyānubhavaḥ sphuṭam  // 1.20:11
akhilaṃ vācakaṃ vācyam aham ity avamarśanam  // 1.20:12
yoginaḥ sāvadhānasya bhavatīty eva śiṣyate  // 1.20:13
sphuṭīkaromi saṃkṣepāt tat prameyaṃ puroditam  // 1.20:14
mahāhrada iti proktā śaktir bhagavatī parā  // 1.20:15
anusaṃdhānam ity uktaṃ tattādātmyavimarśanam  // 1.20:16
mantravīryam iti proktaṃ pūrṇāhaṃtāvimarśanam  // 1.20:17
tadīyo 'nubhavas tasya sphuraṇaṃ svātmanaḥ sphuṭam  // 1.20:18
iti śrīśāmbhavopāyaprakāśanaparāyaṇaḥ  // 1.20:19
unmeṣaḥ prathamaḥ samyaksvarūponmeṣalakṣaṇaḥ  // 1.20:20
```


## 第二章 dvitīya unmeṣa

### 〔2.1〕 cittaṃ mantraḥ

*註偈 9 首*

```
cetyate 'nena paramaṃ svātmatattvaṃ vimṛśyate  // 2.1:1
iti cittaṃ sphurattātmaprāsādādivimarśanam  // 2.1:2
tad eva mantryate guptam abhedena vimṛśyate  // 2.1:3
svasvarūpam aneneti mantras tenāsya daiśikaiḥ  // 2.1:4
pūrṇāhaṃtānusaṃdhyātmasphūrjanmananadharmatā  // 2.1:5
saṃsārakṣayakṛttrāṇadharmatā ca nirucyate  // 2.1:6
tanmantradevatāmarśaprāptatatsāmarasyakam  // 2.1:7
ārādhakasya cittaṃ ca mantras taddharmayogataḥ  // 2.1:8
asya coktasya mantrasya mananatrāṇadharmiṇaḥ  // 2.1:9
```

### 〔2.2〕 prayatnaḥ sādhakaḥ

*註偈 5 首*

```
uktamantrānusaṃdhānāvaṣṭambhodyantṛtātmakaḥ  // 2.2:1
prayatno 'ntaḥsvasaṃrambhaḥ sa eva khalu sādhakaḥ  // 2.2:2
yato mantrayitur mantradevataikyapradaḥ smṛtaḥ  // 2.2:3
īdṛksādhakasādhyasya mantrasya prathamoditam  // 2.2:4
vīryaṃ vistarataḥ samyag varṇyate 'tha salakṣaṇam  // 2.2:5
```

### 〔2.3〕 vidyāśarīrasattā mantrarahasyam

*註偈 12 首*

```
vidyeti paramādvaitasampravedanarūpiṇī  // 2.3:1
śarīraṃ yasya bhagavān śabdarāśiḥ sa ucyate  // 2.3:2
tasya sattā samastādhvapūrṇāhaṃtāsvarūpiṇī  // 2.3:3
sphurattā saiva mantrāṇāṃ mananatrāṇadharmiṇām  // 2.3:4
guptārthatāyā jananaṃ rahasyam iti kathyate  // 2.3:5
etac chrīkṣemarājena tantrasārāt samuddhṛtaiḥ  // 2.3:6
saṃvādaiḥ saṃmataiḥ samyagvarṇitaṃ nijavṛttigaiḥ  // 2.3:7
samyag evaṃvidhaṃ mantravīryaṃ yeṣāṃ yathātatham  // 2.3:8
mahāhradānusaṃdhānaprakārāveditaṃ tv api  // 2.3:9
icchayaiva maheśasya hṛdayaṃgamatāṃ dṛḍham  // 2.3:10
na gacchaty atha tucchāyāṃ cittaṃ siddhau prarohati  // 2.3:11
bindunādādijātāyāṃ teṣāṃ tu mitayoginām  // 2.3:12
```

### 〔2.4〕 garbhe cittavikāso 'viśiṣṭavidyāsvapnaḥ

*註偈 6 首*

```
garbho 'khyātir mahāmāyā tanmaye siddhisaṃcaye  // 2.4:1
vikāso nāma cittasya tāvanmātre kṛtārthatā  // 2.4:2
saivāviśiṣṭā vidyeti kiṃcijjñatvasvarūpiṇī  // 2.4:3
aśuddhavidyā sā svapno vikalpapratyayāmakaḥ  // 2.4:4
āgatā api tāḥ siddhīḥ khalīkṛtya yadā punaḥ  // 2.4:5
avaṣṭabhnāty asau yogī parāṃ siddhiṃ tadāśnute  // 2.4:6
```

### 〔2.5〕 vidyāsamutthāne svābhāvike khecarī śivāvasthā

*註偈 8 首*

```
vidyāyāḥ prāksamākhyātarūpāyāḥ śaṃkarecchayā  // 2.5:1
svābhāvike samutthāne samullāse svabhāvaje  // 2.5:2
unmajjane sati kṣudrasiddhimajjanatatpare  // 2.5:3
avasthā yā śivasyāntaravasthātur abhedinī  // 2.5:4
sphurattā saiva sampūrṇasvānandocchalanātmikām  // 2.5:5
mudaṃ rātīty ato mudrā khecarī ca nabhaścarī  // 2.5:6
vyajyate yogino viśvag viśvottīrṇasvarūpiṇaḥ  // 2.5:7
evaṃprabhāvayor vīryāsādane mantramudrayoḥ  // 2.5:8
```

### 〔2.6〕 gurur upāyaḥ

*註偈 12 首*

```
samyagjñānakriyāprāṇamantramudrāyathāsthitim  // 2.6:1
gṛṇāty upadiśaty arthaṃ tadvīryaṃ cety ato guruḥ  // 2.6:2
sa eva mantramudrāṇāṃ vīryavyāptiprakāśanāt  // 2.6:3
upāyaḥ kathyate sākṣād upeyaṃ paramaṃ prati  // 2.6:4
yad vā guruḥ parā śaktir īśvarānugrahātmikā  // 2.6:5
avakāśapradānena saiva yāyād upāyatām  // 2.6:6
sa gurur matsamaḥ prokto mantravīryaprakāśakaḥ  // 2.6:7
ādimāntyavihīnās tu mantrāḥ syuḥ śaradabhravat  // 2.6:8
guror lakṣaṇam etāvad ādimāntyaṃ ca vedayet  // 2.6:9
iti śrīmālinīśāstrasiddhātantroktavaibhavāt  // 2.6:10
akṛtrimāhamāmarśasvarūpādyantavedakāt  // 2.6:11
parameṣṭhisamāt tasmāt paramopāyato guroḥ  // 2.6:12
```

### 〔2.7〕 mātṛkācakrasaṃbodhaḥ

*註偈 45 首*

```
mantramudrānusaṃdhānasaṃtatodyuktacetasaḥ  // 2.7:1
bhavaty uktaguroḥ prītāt sādhakasyeti śiṣyate  // 2.7:2
athādyās tithayaḥ sarve svarā bindvavasānagāḥ  // 2.7:3
tadantaḥ kālayogena somasūryau prakīrtitau  // 2.7:4
pṛthivyādīni tattvāni puruṣāntāni pañcasu  // 2.7:5
kramāt kādiṣu vargeṣu makārānteṣu suvrate  // 2.7:6
vāyvagnisalilendrāṇāṃ dhāraṇānāṃ catuṣṭayam  // 2.7:7
tadūrdhve śādi vikhyātaṃ purastād brahmapañcakam  // 2.7:8
amūlā tatkramāj jñeyā kṣāntā sṛṣṭir udāhṛtā  // 2.7:9
sarveṣāṃ caiva mantrāṇāṃ vidyānāṃ ca yaśasvini  // 2.7:10
iyaṃ yoniḥ samākhyātā sarvatantreṣu sarvadā  // 2.7:11
iti śrītrīśikāśāstraproktanyāyena mātṛkā  // 2.7:12
akārādivisargāntasvaraṣoḍaśagarbhiṇī  // 2.7:13
ata evādibindvantadaśapañcatithikramā  // 2.7:14
tadātmakataduttīrṇabindudvandvavibhūṣitā  // 2.7:15
ata eva jagat sarvaṃ sṛjaty antar anuttare  // 2.7:16
tat pañcadaśakasyāntaruddhṛtaiḥ pañcabhiḥ svaraiḥ  // 2.7:17
a i u ṛ ḷ vinyāsaiḥ kādimāntaṃ ca vācakam  // 2.7:18
kṣityādipuruṣāntaṃ ca vācyaṃ tattvakadambakam  // 2.7:19
pañcapañcakabhedena pañcapañcavijṛmbhitam  // 2.7:20
bahiś cānuttarād eva sṛjatī viśvam īdṛśam  // 2.7:21
vāyvagnisalilendrāṇāṃ kramād ya ra la vātmanām  // 2.7:22
anuttarecchonmeṣākhyatritayānyonyasaṃdhitaḥ  // 2.7:23
kiṃcānuttaraṣaṇḍhākhyadvayasaṃdhivaśād api  // 2.7:24
utthitānāṃ kalāvidyāmāyārāgābhidhāyinām  // 2.7:25
svarūpagopanāt sarvakartṛtvādyapasārataḥ  // 2.7:26
khaṇḍitasya paśoḥ kiṃcitkartṛtvādipradāyinām  // 2.7:27
māyordhvaśuddhavidyāditattvārohanirodhanāt  // 2.7:28
mūlād adho 'varohasya nirodhāc ca triśaṇkuvat  // 2.7:29
madhye saṃsthāpitasyāsya dhāraṇād dhāraṇātmanām  // 2.7:30
yatis tu bhāvābhāvānāṃ vyavasthodayadāyinī  // 2.7:31
kālo 'pi tāṃ mahāmāyāṃ svatantrām anuvartate  // 2.7:32
ityuktyā kālaniyatiyuktatvāt ṣaḍvidhātmanām  // 2.7:33
sphārayantī vapuḥ paścāt tadūrdhvaṃ śādipañcakam  // 2.7:34
sadyojātādikeśānaparyantabrahmavigraham  // 2.7:35
sūkṣmarūpamahīvārivahnivāyunabhomayam  // 2.7:36
krameṇa śuddhavidyeśasādaśaktiśivātmakam  // 2.7:37
visphārayantī svāntaḥsthaṃ visargakalayā bahiḥ  // 2.7:38
kādisāntākṣarāntasthaḥ kṣakāro 'py antimo yataḥ  // 2.7:39
ato 'kārahakārābhyām aham ity apṛthaktayā  // 2.7:40
prapaṃcaṃ śivaśaktibhyāṃ kroḍīkṛtya prakāśate  // 2.7:41
asyās tv evaṃprabhāvāyāś cakraṃ yat tad ihoditam  // 2.7:42
anuttarecchonmeṣādispandaśaktikadambakam  // 2.7:43
tatsaṃbodhaś cidānandaghanasvātmānusaṃhitiḥ  // 2.7:44
athedṛṅmātṛkācakrasaṃbodhodbodhitātmanaḥ  // 2.7:45
```

### 〔2.8〕 śarīraṃ haviḥ

*註偈 7 首*

```
śūnyaṃ dhīḥ prāṇa ity etat sṛjyate kṣīyate 'pi ca  // 2.8:1
sthairyam asti paraṃ dehāpekṣayā na tu tattvataḥ  // 2.8:2
ity uktanītyā śūnyādeḥ pramātā tv asya bhittibhūḥ  // 2.8:3
śarīraṃ sthūlasūkṣmādi cidagnau parayoginaḥ  // 2.8:4
hūyamānaṃ haviḥ proktaṃ tanmātṛtvanimajjanāt  // 2.8:5
paripūrṇaprakāśātmapramātrunmajjanapradāt  // 2.8:6
evaṃ śarīrahavyena jvaladbodhordhvarociṣaḥ  // 2.8:7
```

### 〔2.9〕 jñānam annam

*註偈 6 首*

```
jñānaṃ bandha iti proktaṃ yat prāk tat parayoginaḥ  // 2.9:1
anātmany ātmatājñaptir annaṃ grasyata ity ataḥ  // 2.9:2
kiṃ ca yad yat prakāśātmasvarūpāmarśanātmakam  // 2.9:3
jñānaṃ tatparamāhlādakāritvād annam ucyate  // 2.9:4
yadā tv avahitaḥ śaśvad yogī naivaṃ bhavaty asau  // 2.9:5
tadā jñānavato 'py asya samādhānāvalepataḥ  // 2.9:6
```

### 〔2.10〕 vidyāsaṃhāre tadutthasvapnadarśanam

*註偈 7 首*

```
vidyeti jñānavisphārarūpā yā tu puroditā  // 2.10:1
śuddhavidyātha saṃhāre 'nutthāne 'syā nimajjane  // 2.10:2
tadutthasya krameṇāñcadvidyāsaṃhārajanmanaḥ  // 2.10:3
svapnasya bhedaniṣṭhasya vikalpaughasya darśanam  // 2.10:4
unmajjanaṃ bhavaty asya prāgvyākhyātottamātmanaḥ  // 2.10:5
avadhāne 'valiptasya sādhakasyeti śiṣyate  // 2.10:6
iti dvitīya unmeṣaḥ śāktopāyaprakāśakaḥ  // 2.10:7
```


## 第三章 tṛtīya unmeṣa

### 〔3.1〕 ātmā cittam

*註偈 13 首*

```
viśeṣabhogyaśabdādivāsanāveśarūpitam  // 3.1:1
tattadadhyavasāyādivyāpārakaraṇonmukham  // 3.1:2
sattvādivṛttyavaṣṭambhi buddhyahaṃkṛnmanomayam  // 3.1:3
cittaṃ tat proktacaitanyasvarūpānavamarśanāt  // 3.1:4
tattatkarmānusāreṇa nānāyonīr anuvrajat  // 3.1:5
atatīty ata evātmā tataḥ so 'ṇuḥ prakīrtitaḥ  // 3.1:6
ātmanaś cātanaṃ nāsti saṃvidekasvarūpiṇaḥ  // 3.1:7
ataś caitanyam ātmeti dhīkriyātmakam ātmanaḥ  // 3.1:8
viśvasvabhāvabhūtaṃ tat tāttvikaṃ rūpam īritam  // 3.1:9
idānīm etadīyena svātantryeṇāvabhāsitāt  // 3.1:10
saṃkocād aṇutāyogāc cittam ātmeti lakṣitam  // 3.1:11
iti pūrvāparādeśavaiṣamyaṃ nāsti kiṃcana  // 3.1:12
asya cittasvarūpasya dehāder ātmanas tv aṇoḥ  // 3.1:13
```

### 〔3.2〕 jñānaṃ bandhaḥ

*註偈 11 首*

```
antaḥ sukhādisaṃvedyavyavasāyādivṛttimat  // 3.2:1
bahis tadyogyanīlādidehādiviṣayonmukham  // 3.2:2
bhedābhāsātmakaṃ cāsya jñānaṃ bandho 'ṇurūpiṇaḥ  // 3.2:3
tatpāśitatvād evāsāv aṇuḥ saṃsarati dhruvam  // 3.2:4
jñānaṃ prakāśakaṃ loke ātmā caiva prakāśakaḥ  // 3.2:5
anayor apṛthagbhāvāj jñānī jñāne prakāśate  // 3.2:6
ity uktanītyā jñānaṃ ca svasvarūpaprakāśakam  // 3.2:7
ātmavat tat kathaṃ tasya bandhakatvaprasaṅgitā  // 3.2:8
ity āśaṅkyāha yady evaṃ prasannāt parameśvarāt  // 3.2:9
pratyabhijñā bhavaty eṣā tadā satyaṃ tvadīritam  // 3.2:10
tanmāyāśaktito naiṣa vimarśo 'sya yadā tadā  // 3.2:11
```

### 〔3.3〕 kalādīnāṃ tattvānām aviveko māyā

*註偈 6 首*

```
antarantaḥsphurat kiṃcitkartṛtvādipradāyinām  // 3.3:1
kalādikṣitiparyantatattvānāṃ kañcukātmanām  // 3.3:2
puryaṣṭakamayatvena sthūladehādirūpataḥ  // 3.3:3
sthitānām avivekas teṣv ātmatvenānusaṃhitiḥ  // 3.3:4
saiva sammohinī māyā tattvākhyātimayaṃ jagat  // 3.3:5
ataś caitaj janyamāyāpraśamāyāsya yoginaḥ  // 3.3:6
```

### 〔3.4〕 śarīre saṃhāraḥ kalānām

*註偈 8 首*

```
mahābhūtātmake sthūle sūkṣme puryaṣṭakātmani  // 3.4:1
mūlādisamanānte ca śarīre yoginaḥ pare  // 3.4:2
kalānāṃ tatra bhāgānāṃ kāryāṇāṃ kāraṇe nije  // 3.4:3
saṃhāraḥ saṃvidekāgnisadbhāvo layacintayā  // 3.4:4
dāhādyāmarśayuktyā vā dhyātavya iti śiṣyate  // 3.4:5
evaṃ dhyānābhidhāno yaḥ saṃhāropāya īritaḥ  // 3.4:6
evam etat pradhānāṃś ca prāṇāyāmapuraḥsarān  // 3.4:7
anyān samādhiparyantān upāyān darśayaty asau  // 3.4:8
```

### 〔3.5〕 nāḍīsaṃhārabhūtajayabhūtakaivalyabhūtapṛthaktvāni

*註偈 16 首*

```
bhāvanīyāni yuktena sādhakeneti śiṣyate  // 3.5:1
prāṇādivāhināḍīnāṃ saṃhāraḥ prāṇasaṃyamāt  // 3.5:2
recakādikramotpādād udānadahanātmani  // 3.5:3
madhyanāḍyāṃ vilīnatvāpādanaṃ tanmayatvataḥ  // 3.5:4
bhūtānāṃ bhūjalādīnāṃ jayo yaḥ sa udīryate  // 3.5:5
vāyavī dhāraṇāṅguṣṭhe āgneyī nābhimadhyataḥ  // 3.5:6
māheyī kaṇṭhadeśe tu vāruṇī ghaṇṭikāśritā  // 3.5:7
ākāśadhāraṇā mūrdhni sarvasiddhikarī smṛtā  // 3.5:8
iti svacchandaśāstroktadhāraṇābhir vaśīkṛtiḥ  // 3.5:9
bhūtebhyaḥ kila kaivalyaṃ cittapratyāhṛtis tataḥ  // 3.5:10
pṛthaktvaṃ tadanāliptasvacchasvātmaikarūpatā  // 3.5:11
bhūtasaṃdhāna ityādisūtroktaṃ yat phalaṃ purā  // 3.5:12
aprayatnena sādhyaṃ tacchāmbhavopāyaśālinaḥ  // 3.5:13
āṇavopāyasādhyaṃ tu yatneneti viśiṣyate  // 3.5:14
ity evaṃ dehaśuddhyādyaiḥ samādhyantaiś ca yā bhavet  // 3.5:15
siddhiḥ sā mohavaraṇān nātmajñānād itīryate  // 3.5:16
```

### 〔3.6〕 mohāvaraṇāt siddhiḥ

*註偈 21 首*

```
moho vimohinī māyā tatkṛtāvaraṇāt kila  // 3.6:1
pūrvoktadhāraṇādyuktyā siddhiḥ parimitā bhavet  // 3.6:2
tattattattvopabhogātmā na tv asya paracitprathā  // 3.6:3
vinaṣṭamohāveśasya samādhau cāgrataḥ punaḥ  // 3.6:4
madhyamaṃ prāṇam āśritya prāṇāpānapathāntaram  // 3.6:5
ālambya jñānaśaktiṃ ca tatsthaṃ caivāsanaṃ labhet  // 3.6:6
prāṇādisthūlabhāvaṃ tu tyaktvā sūkṣmam athāntaram  // 3.6:7
sūkṣmātītaṃ tu paramaṃ spandanaṃ labhyate yataḥ  // 3.6:8
prāṇāyāmaḥ sa uddiṣṭo yasmān na cyavate punaḥ  // 3.6:9
śabdādiguṇavṛttir yā cetasā hy anubhūyate  // 3.6:10
tyaktvā tāṃ paramaṃ dhāma praviśet tatsvacetasā  // 3.6:11
pratyāhāra iti prokto bhavapāśanikṛntanaḥ  // 3.6:12
dhīguṇān samatikramya nirdhyeyaṃ cāvyayaṃ vibhum  // 3.6:13
dhyātvā dhyeyaṃ svasaṃvedyaṃ dhyānaṃ tac ca vidur budhāḥ  // 3.6:14
dhāraṇā paramātmatvaṃ dhāryate yena sarvadā  // 3.6:15
dhāraṇā sā vinirdiṣṭā bhavabandhavināśinī  // 3.6:16
svaparastheṣu bhūteṣu jagaty asmin samānadhīḥ  // 3.6:17
śivo 'ham advitīyo 'haṃ samādhiḥ sa paraḥ smṛtaḥ  // 3.6:18
ity evaṃ mṛtyujittantrabhaṭṭārakanirūpitaiḥ  // 3.6:19
prāṇasaṃyamanārambhaiḥ samādhyantaiḥ kramair api  // 3.6:20
paratattvasamāveśo bhavaty eveti kathyate  // 3.6:21
```

### 〔3.7〕 mohajayād anantābhogāt sahajavidyājayaḥ

*註偈 5 首*

```
moho māyā nijākhyātis tajjayāt tatparābhavāt  // 3.7:1
udyamārkotthito 'nantaḥ saṃskārapraśamāvadhiḥ  // 3.7:2
ābhogo yasya vistāra īdṛśād darśitātmanaḥ  // 3.7:3
bhavet sahajavidyāyā jayo lābho yoginaḥ  // 3.7:4
evaṃ mohajayopāttaśuddhavidyāmahodayaḥ  // 3.7:5
```

### 〔3.8〕 jāgrad dvitīyakaraḥ

*註偈 6 首*

```
bhaktvaivaṃ sahajāṃ vidyāṃ tadekatvāvalambane  // 3.8:1
jāgarūkaḥ sadā yogī jāgrad ity ayam ucyate  // 3.8:2
saṃpūrṇāhaṃvimarśātmasvāhaṃtāpekṣayā jagat  // 3.8:3
dvitīyam idam ākāraṃ karo yasya svadīdhitiḥ  // 3.8:4
tathābhūto bhavaty eṣa svakarībhūtaviṣṭapaḥ  // 3.8:5
īdṛśo 'yaṃ sadā svātmavimarśāveśitāśayaḥ  // 3.8:6
```

### 〔3.9〕 nartaka ātmā

*註偈 6 首*

```
nṛtyaty antaḥparicchannasvasvarūpāvalambanāḥ  // 3.9:1
svecchayā svātmacidbhittau svaparispandalīlayā  // 3.9:2
jāgarāsvapnasauṣuptarūpās tās tāḥ svabhūmikāḥ  // 3.9:3
ābhāsayati yat tasmād ātmā nartaka ucyate  // 3.9:4
evaṃvidhajagannāṭyanartakasyāsya yoginaḥ  // 3.9:5
bhūmikāgrahaṇasthānaṃ raṅgam āha jagadguruḥ  // 3.9:6
```

### 〔3.10〕 raṅgo 'ntarātmā

*註偈 5 首*

```
rajyate 'smin jagannāṭyakrīḍākautukinātmanā  // 3.10:1
iti raṅgo 'ntarātmeti jīvaḥ puryaṣṭakātmakaḥ  // 3.10:2
yogī kṛtapadas tatra svendriyaspandalīlayā  // 3.10:3
sadāśivādikṣityantajagannāṭyaṃ prakāśayet  // 3.10:4
dehāntaraṅge raṅge 'smin nṛtyataḥ svāntarātmani  // 3.10:5
```

### 〔3.11〕 prekṣakāṇīndriyāṇi

*註偈 3 首*

```
prekṣakāṇīti saṃsāranāṭyaprākaṭyakṛd vapuḥ  // 3.11:1
cakṣurādīndriyāṇy antaś camatkurvanti yoginaḥ  // 3.11:2
ity evaṃ prekṣakībhūtasvākṣacakrasya yoginaḥ  // 3.11:3
```

### 〔3.12〕 dhīvaśāt sattvasiddhiḥ

*註偈 4 首*

```
dhīs tāttvikasvacidrūpavimarśakuśalā matiḥ  // 3.12:1
tadvaśād eva sattvasya spandasyāntarvivartinaḥ  // 3.12:2
sphurattārūpiṇaḥ siddhir abhivyaktiḥ sphuṭaṃ bhavet  // 3.12:3
evaṃ nijasphurattātmasattvāsādanavaibhavāt  // 3.12:4
```

### 〔3.13〕 siddhaḥ svatantrabhāvaḥ

*註偈 4 首*

```
siddhaḥ sampanna evāsya bhavet paramayoginaḥ  // 3.13:1
svatantrabhāvaḥ sahajajñatvakartṛtvalakṣaṇaḥ  // 3.13:2
svātantryaṃ vaśino viśvasvavaśīkaraṇakṣamam  // 3.13:3
svatantrabhāva evāsya svānandabharitātmanaḥ  // 3.13:4
```

### 〔3.14〕 yathā tatra tathānyatra

*註偈 4 首*

```
yatra svābhāvike dehe sphuṭībhūtā svatantratā  // 3.14:1
yathā tatra tathānyatra dehe bhavati yoginaḥ  // 3.14:2
sphuṭībhavati yuktasya pūrṇāhaṃtāsvarūpiṇī  // 3.14:3
na caivam apy udāsīnena bhāvyaṃ yogināpi tu  // 3.14:4
```

### 〔3.15〕 bījāvadhānam

*註偈 4 首*

```
sphurattātmā parā śaktir bījaṃ viśvasya kāraṇam  // 3.15:1
tatrāvadhānaṃ cittasya bhūyobhūyo niveśanam  // 3.15:2
yoginā sāvadhānena kartavyam iti śiṣyate  // 3.15:3
evaṃvidho mahāyogī paraśaktyavadhānavān  // 3.15:4
```

### 〔3.16〕 āsanasthaḥ sukhaṃ hrade nimajjati

*註偈 12 首*

```
āsyate sthīyate yasminn aikātmyeneti cāsanam  // 3.16:1
śāktaṃ balaṃ yat tatrasthas tadevāntaḥ parāmṛśan  // 3.16:2
yogī parihṛtadhyānadhāraṇādipariśramaḥ  // 3.16:3
khecaryādimahāsrotovāhaprasarakāraṇe  // 3.16:4
svacchatvādiguṇair yukte svānandabharite hrade  // 3.16:5
saṃplutedaṃpadadvīpe sampūrṇe saṃvidarṇave  // 3.16:6
nirastasakalopāyo nimajjati yathāsukham  // 3.16:7
dehādibroḍanenaiva tanmayībhavati sphuṭam  // 3.16:8
ity evam āṇavopāyāsāditān mohanirjayāt  // 3.16:9
unmajjacchuddhavidyātmaśāktāveśaprakarṣataḥ  // 3.16:10
ātmīkṛtaparānandahradagāḍhāvagāhanāt  // 3.16:11
prasphuracchāmbhavāvaśavaibhavaḥ sādhakottamaḥ  // 3.16:12
```

### 〔3.17〕 svamātrānirmāṇam āpādayati

*註偈 6 首*

```
svasya sambandhinī mātrā caitanyasyoktarūpiṇaḥ  // 3.17:1
āśyānatā mitātmāṃśo grāhyagrāhakalakṣaṇaḥ  // 3.17:2
nirmāṇāpādanaṃ tasyā nirmitatvena darśanam  // 3.17:3
sampādayati yogīndro yatheṣṭaṃ spaṣṭam icchayā  // 3.17:4
evam īdṛśaśaktyutthaviśvarūpasya yoginaḥ  // 3.17:5
punarjanmādisambandho na kaścid iti kathyate  // 3.17:6
```

### 〔3.18〕 vidyāvināśe janmavināśaḥ

*註偈 6 首*

```
vidyeti sahajā tasyā avināśaḥ sadodayaḥ  // 3.18:1
tenaivājñānasahakṛttattatkarmānuṣaṅgiṇaḥ  // 3.18:2
dehaprāṇamanīṣādisamudāyasya janmanaḥ  // 3.18:3
vināśo mūlavidhvaṃso bhavaty asyeti śiṣyate  // 3.18:4
yadā tu śuddhavidyāyāḥ svarūpaṃ tasya majjati  // 3.18:5
tadā tanmohanāyaiva samuttiṣṭhanti śaktayaḥ  // 3.18:6
```

### 〔3.19〕 kavargādiṣu māheśvaryādyāḥ paśumātaraḥ

*註偈 14 首*

```
kavargādiṣu tiṣṭhantyas tadadhiṣṭhātṛtāṃ gatāḥ  // 3.19:1
māheśvaryādikāḥ proktakarandhracitimadhyagāḥ  // 3.19:2
paśūn pramāt āviśya tattatpratyayabhūmiṣu  // 3.19:3
tattacchabdānuvedhena mohanāt paśumātaraḥ  // 3.19:4
āvṛṇvānā nijaṃ rūpaṃ cidānandaghanātmakam  // 3.19:5
atimānaṃ vivṛṇvānāḥ śarīrādau jaḍe 'pi ca  // 3.19:6
paśuvatsādhakam api pramattaṃ mohayanty amūḥ  // 3.19:7
tasmād bhāvyaṃ sadānena sāvadhānena yoginā  // 3.19:8
uktaṃ sāmānyato jñānādhiṣṭhānaṃ mātṛkety ataḥ  // 3.19:9
idaṃ tu prāptatattvo 'pi pramādyan sādhakaḥ punaḥ  // 3.19:10
paśvadhiṣṭhānabhūtābhir mohyate mātṛbhis tv iti  // 3.19:11
yata evam ataḥ śuddhavidyā prāptāpi yuktibhiḥ  // 3.19:12
bahvībhiḥ sā punar mauḍhyādy athāsya na vinaśyati  // 3.19:13
tathā sarvāsv avasthāsu yukto bhūyād itīryate  // 3.19:14
```

### 〔3.20〕 triṣu caturthaṃ tailavad āsecyam

*註偈 16 首*

```
triṣv iti proktarūpeṣu jāgarādiṣu tailavat  // 3.20:1
caturtham iti pūrvoktaṃ śuddhavidyāprathātmakam  // 3.20:2
turyaṃ dhāma sadāsecyaṃ yathā syāt tanmayaṃ trayam  // 3.20:3
yathā tailaṃ kramāt svīyam āśrayaṃ vyāpnuyāt tathā  // 3.20:4
ādyantakoṭyoḥ sphuratā jāgarādeḥ parisphuṭam  // 3.20:5
turyānandarasenārdrīkuryān madhyadaśām api  // 3.20:6
jāgrad ityādisūtreṇa pūrvam udyamavattayā  // 3.20:7
śakticakrānusaṃdhānaśālinaḥ parayoginaḥ  // 3.20:8
svarasaprasarajjāgratsvapnasauṣuptabhūmiṣu  // 3.20:9
udīritaḥ svatoniryatturyaprasarasambhavaḥ  // 3.20:10
tritayetyādisūtreṇa śāmbhavopāyasādhitāt  // 3.20:11
haṭhapākakramāj jāgratsvapnasauṣuptasaṃhṛtiḥ  // 3.20:12
darśitānena sūtreṇa tv āṇavopāyayuktitaḥ  // 3.20:13
dalakalpatayāsthāyi jāgradādipadatrayam  // 3.20:14
siñcet turyaraseneti viśeṣaḥ samudīritaḥ  // 3.20:15
atropāyaṃ punaś cāha turyāmṛtaniṣecane  // 3.20:16
```

### 〔3.21〕 magnaḥ svacittena praviśet

*註偈 7 首*

```
prāṇāyāmādikaṃ tyaktvā sthūlopāyaṃ vikalpakam  // 3.21:1
avikalpakarūpeṇa svacittena svasaṃvidā  // 3.21:2
antarmukhaparāmarśacamatkārarasātmanā  // 3.21:3
magnas turyarasenātra svadehādipramātṛtām  // 3.21:4
majjanena praśamayan praviśet tat samāviśet  // 3.21:5
itthaṃ parapadāviṣṭabuddher vastusvabhāvataḥ  // 3.21:6
yadā bhūyaḥ prasaraṇaṃ yogino jāyate tadā  // 3.21:7
```

### 〔3.22〕 prāṇasamācāre samadarśanam

*註偈 8 首*

```
prāṇasya prasphuracchāktasaurabhāveśasaṃskṛtaḥ  // 3.22:1
samyagvikasitāśeṣagranthyavaṣṭambhadhībalāt  // 3.22:2
īṣad bahir mandamandaṃ cāre prasaraṇe sati  // 3.22:3
samaṃ cinmudghanātmatvāt sarvadābhedadarśanam  // 3.22:4
saṃvedanaṃ bhavaty arthāt sarvāvasthāsu yoginaḥ  // 3.22:5
turyāvaṣṭambhato labhyaṃ turyātītam anāmṛśan  // 3.22:6
pūrvāparātmanoḥ koṭyoḥ saṃvedye turyamātrake  // 3.22:7
āste yogī tadāmuṣya tāvan mātreṇa tuṣyataḥ  // 3.22:8
```

### 〔3.23〕 madhye 'varaprasavaḥ

*註偈 6 首*

```
pūrvasyām aparasyāṃ ca koṭau turyaniṣeviṇaḥ  // 3.23:1
avadhāne 'valiptasya kadācit tasya yoginaḥ  // 3.23:2
madhyāyām avaro 'śreṣṭhaḥ kutsitaḥ sarga āpatet  // 3.23:3
vyutthānātmā tato yogī sāvadhānaḥ sadā bhavet  // 3.23:4
avaraprasave vṛtte hy evaṃ madhyapade punaḥ  // 3.23:5
turyāvaṣṭambharasatas turyātītaṃ parāmṛśet  // 3.23:6
```

### 〔3.24〕 mātrāsv apratyayasaṃdhāne naṣṭasya punar utthānam

*註偈 7 首*

```
mātrāḥ padārthāḥ rūpādyās tāsv ebhiś cakṣurādibhiḥ  // 3.24:1
akṣaiḥ svapratyayo nāma tattatsvagrāhyavedanam  // 3.24:2
saṃdhānaṃ tu samastaṃ tad aham ity anusaṃhitiḥ  // 3.24:3
amuṣmin sati naṣṭāya hāritasyoktavargataḥ  // 3.24:4
turyasya punar utthānaṃ bhūya unmajjanaṃ bhavet  // 3.24:5
tadaikyasampatpūrṇatvaṃ yogīndrasyeti śiṣyate  // 3.24:6
evam udyatsamāveśaprakarṣaḥ sādhakarṣabhaḥ  // 3.24:7
```

### 〔3.25〕 śivatulyo jāyate

*註偈 10 首*

```
turyābhyāsaprakarṣeṇa turyātītātmakaṃ padam  // 3.25:1
samprāptaḥ sādhakaḥ sākṣāt sarvalokāntarātmanā  // 3.25:2
śivena cinmayasvacchasvacchadānandaśālinā  // 3.25:3
tulyo 'vigalanād dehakalāyā galane śivaḥ  // 3.25:4
arjitaṃ dīkṣayā dagdhaṃ bhaviṣyanti yamādibhiḥ  // 3.25:5
yenedaṃ sādhitaṃ yatra tadbhuktyā vinivartate  // 3.25:6
anekabhāvikaṃ karma dagdhaṃ bījam ivāgninā  // 3.25:7
bhaviṣyad api saṃruddhaṃ yenedaṃ tad dhi bhogataḥ  // 3.25:8
ity uktanītyā prārabdhaprāptabhogopabhogabhūḥ  // 3.25:9
kalevarasthitis tasya kartavyety upadiśyate  // 3.25:10
```

### 〔3.26〕 śarīravṛttir vratam

*註偈 8 首*

```
evaṃ pūrvoktayā nītyā śivatulyasya yoginaḥ  // 3.26:1
śaśvacchivātmakasvātmasaparyātatparātmanaḥ  // 3.26:2
antarullasadacchācchabhaktipīyūṣapoṣitam  // 3.26:3
bhavatpūjopayogāya śarīram idam astu me  // 3.26:4
iti lokottaraśrīmadutpalaproktayā diśā  // 3.26:5
śivabhaktisudhāpūrṇe śarīre vṛttir asya yā  // 3.26:6
vratam etad anuṣṭheyaṃ na tucchaṃ tasya dhāraṇam  // 3.26:7
evaṃvidhasya tasyāsya yā yā svālāparūpiṇī  // 3.26:8
```

### 〔3.27〕 kathā japaḥ

*註偈 14 首*

```
mahāmantramayaṃ naumi rūpaṃ te svacchaśītalam  // 3.27:1
apūrvāmodasubhagaṃ parāmṛtarasolvaṇam  // 3.27:2
iti śrīpratyabhijñākṛddaiśikaproktayā diśā  // 3.27:3
akṛtrimāhamāmarśamayasvātmāvamarśinaḥ  // 3.27:4
yā yā svairābhilāpātmā kathā yāthārthyavādinaḥ  // 3.27:5
bhūyobhūyaḥ pare bhāve bhāvanā bhāvyate hi yā  // 3.27:6
japaḥ so 'tra svayaṃ nādo mantrātmā japya īdṛśaḥ  // 3.27:7
ṣaṭśatāni divārātraṃ sahasrāṇy ekaviṃśatiḥ  // 3.27:8
japo devyāḥ samuddiṣṭaḥ sulabho durlabho jaḍaiḥ  // 3.27:9
ity uktanītyā sā sarvasvātmeśāmarśasampadaḥ  // 3.27:10
janipālanadharmatvāj japa ity abhidhīyate  // 3.27:11
athedṛgvidhayogīndraviṣayāpi ca yā kathā  // 3.27:12
japaḥ so 'pi janasyokto janipālanayogataḥ  // 3.27:13
atha cāsyocyate caryā maryādānuvidhāyinī  // 3.27:14
```

### 〔3.28〕 dānam ātmajñānam

*註偈 12 首*

```
proktacaitanyarūpasya sākṣātkaraṇamātmanaḥ  // 3.28:1
yat taj jñānaṃ tad evāsya dānaṃ yatnena dīyate  // 3.28:2
paripūrṇaṃ svarūpaṃ svaṃ dīyate khaṇḍyate bhidā  // 3.28:3
dāyate śodhyate rūpam ātmīyaṃ dīyate punaḥ  // 3.28:4
rakṣyate pratyabhijñātaḥ śivātmā svasvabhāvatā  // 3.28:5
dīyate ceti yatnena svātmajñānam anuttaram  // 3.28:6
kṛpayā svātmaśiṣyebhyas tad anenaiva dīyate  // 3.28:7
evaṃ samyagvrataṃ proktaṃ japaṃ caryā ca pālayan  // 3.28:8
śivatulyaḥ sadā svātmaśivārādhanatatparaḥ  // 3.28:9
ayam eva mahāyogī mahāmantradhuraṃdharaḥ  // 3.28:10
antevāsijanasyāntas tattvatas tattvabodhakaḥ  // 3.28:11
ity āha bhagavān īśo nityānugrahakārakaḥ  // 3.28:12
```

### 〔3.29〕 yo 'vipastho jñāhetuś ca

*註偈 11 首*

```
avīn paśujanān pātīty avipaṃ śaktimaṇḍalam  // 3.29:1
māheśvaryādikaṃ proktaṃ kavargādyadhidaivatam  // 3.29:2
adhitiṣṭhati yaḥ svairam avipasthaḥ sa ucyate  // 3.29:3
jānātīty akhilaṃ tat jñā jñānaśaktir udīryate  // 3.29:4
tasyā hetus tayā śiṣyān pratibodhayituṃ kṣamaḥ  // 3.29:5
anyas tu śakticakreṇa paratantrīkṛtatvataḥ  // 3.29:6
svātmany evāsamarthaḥ san katham anyān prabodhayet  // 3.29:7
yac chabdāpekṣayā sūtre tac chabdo 'dhyāhṛtaḥ svayam  // 3.29:8
caśabdo hy arthavācy atra yasmāj jñānaprabodhane  // 3.29:9
yogī hetus tato dānam ātmajñānam itīritam  // 3.29:10
ity evam avipasthasya jñāhetor asya yoginaḥ  // 3.29:11
```

### 〔3.30〕 svaśaktipracayo viśvam

*註偈 7 首*

```
śaktayo 'sya jagat kṛtsnaṃ śaktimāṃs tu maheśvaraḥ  // 3.30:1
ity āgamadiśā viśvaṃ svaśaktipracayo yathā  // 3.30:2
śivasya tatsamasyāpi tathāsya parayoginaḥ  // 3.30:3
svasyāḥ svātmāvimuktāyāḥ śakteḥ saṃvedanātmanaḥ  // 3.30:4
pracayaḥ sphuraṇārūpo vikāso viśvam iṣyate  // 3.30:5
na paraṃ sṛṣṭyavasthāyām amuṣya parayoginaḥ  // 3.30:6
svaśaktipracayo viśvaṃ yāvat tatpṛṣṭhapātinau  // 3.30:7
```

### 〔3.31〕 sthitilayau

*註偈 10 首*

```
svaśaktipracayau proktau tāv apīty anuvartate  // 3.31:1
vikāsitasya viśvasya kriyāmayyā svasaṃvidā  // 3.31:2
tattatpramātrapekṣātaḥ kiṃcit kālam idaṃtayā  // 3.31:3
yā sthitiś cinmayāhaṃtāviśrāntyātmā ca yo layaḥ  // 3.31:4
tāv ubhau yoginas tasya svaśaktipracayātmakau  // 3.31:5
vikasat saṃkucat sarvaṃ vedyaṃ yat saṃvidātmakam  // 3.31:6
anyathā tasya vedyasya vedanānupapattitaḥ  // 3.31:7
nanu sṛṣṭisthitidhvaṃseṣv evam anyonyabhediṣu  // 3.31:8
anyathātvaṃ samāyātaṃ svasvarūpasya yoginaḥ  // 3.31:9
ity āśaṅkānivṛttyarthaṃ sūtram āha maheśvaraḥ  // 3.31:10
```

### 〔3.32〕 tatpravṛttāv apy anirāsaḥ saṃvettṛbhāvāt

*註偈 13 首*

```
teṣāṃ sṛṣṭyādibhāvānāṃ pravṛttāv apy anāratam  // 3.32:1
unmajjane 'pi niṣkampayogāvaṣṭambhaśālinaḥ  // 3.32:2
avasthāyugalaṃ cātra kāryakartṛtvaśabditam  // 3.32:3
kāryatā kṣayiṇī tatra kartṛtvaṃ punar akṣayam  // 3.32:4
kāryonmukhaḥ prayatno yaḥ kevalaṃ so 'tra lupyate  // 3.32:5
tasmiṃl lupte vilupto 'smīty abudhaḥ pratipadyate  // 3.32:6
na tu yo 'ntarmukho bhāvaḥ sarvajñatvaguṇāspadam  // 3.32:7
tasya lopaḥ kadācit syād anyasyānupalambhanāt  // 3.32:8
iti śrīspandaśāstroktanītyā tasyāsya yoginaḥ  // 3.32:9
anirāsaḥ svasaṃvettṛbhāvād apracyutir nijāt  // 3.32:10
udyatturyacamatkārād upalabdhṛsvabhāvataḥ  // 3.32:11
nirāse tasya sṛṣṭyādeḥ sṛjyasyāpy aprakāśanāt  // 3.32:12
viśvasṛṣṭisthitidhvaṃseṣv aprakampasya yoginaḥ  // 3.32:13
```

### 〔3.33〕 sukhāsukhayor bahir mananam

*註偈 11 首*

```
uttīrṇadehaprāṇādipramātṛtvasya dhīmataḥ  // 3.33:1
vedyasparśajayos tasya mananaṃ sukhaduḥkhayoḥ  // 3.33:2
idaṃtābhāsarūpeṇa nīlapītādivad bahiḥ  // 3.33:3
ahaṃ sukhīti duḥkhīti lokavan na tv ahaṃtayā  // 3.33:4
svaśaktipracayo viśvam iti sūtrārthanītitaḥ  // 3.33:5
ahaṃtācchāditatvena sarvam asya prakāśate  // 3.33:6
yogino laukikasyeva sukhādy eva na kevalam  // 3.33:7
atikrāntamahāmohākrāntadehādyahaṃkṛtiḥ  // 3.33:8
lokavatsukhaduḥkhābhyāṃ kathaṃ spṛśyeta yogirāṭ  // 3.33:9
udañcaccitpramātṛtvanyañcatpuryaṣṭakasthiteḥ  // 3.33:10
yato na tatsukhādyantas tata evaiṣa sādhakaḥ  // 3.33:11
```

### 〔3.34〕 tadvimuktas tu kevalī

*註偈 5 首*

```
tābhyāṃ mukto viśeṣeṇa yogīndro yat tayor yataḥ  // 3.34:1
saṃskāreṇāpy asaṃspṛṣṭaḥ kevalī cinmayaḥ smṛtaḥ  // 3.34:2
tuśabdo 'ntaram ākhyāti vakṣyamāṇavyapekṣayā  // 3.34:3
evam uttarasūtrastho 'py etatsūtravyapekṣayā  // 3.34:4
tad evāha tuśabdoktam antaraṃ candraśekharaḥ  // 3.34:5
```

### 〔3.35〕 mohapratisaṃhatas tu karmātmā

*註偈 6 首*

```
mohaḥ svākhyātir ajñānaṃ tena yaḥ pratisaṃhataḥ  // 3.35:1
tadekaghanatāṃ prāptas tato duḥkhādyupāśrayaḥ  // 3.35:2
tata eva sa karmātmā śubhāśubhakalaṅkitaḥ  // 3.35:3
tasyaivam īdṛśasyāpi tattatkarmātmano yadā  // 3.35:4
anargalamaheśānaśaktipātāt samunmiṣan  // 3.35:5
svātantryayogaḥ sahajaḥ prādurasti tadāsya tu  // 3.35:6
```

### 〔3.36〕 bhedatiraskāre sargāntarakarmatvam

*註偈 7 首*

```
bhedasya dehaprāṇādimitāhaṃkṛtijanmanaḥ  // 3.36:1
kalādivalitabhrāntasakalādyucitātmanaḥ  // 3.36:2
tiraskāre sthitasyāpi svonmeṣād apahastane  // 3.36:3
mantramantreśatādātmyasvamāhātmyaprakāśanāt  // 3.36:4
syāt sargāntarakarmatvam amuṣya parayoginaḥ  // 3.36:5
yathābhilāṣanirmeyanirmātṛtvaṃ sphuṭaṃ bhavet  // 3.36:6
na caitad apy asaṃbhāvyaṃ sraṣṭṛtvaṃ yogino yataḥ  // 3.36:7
```

### 〔3.37〕 karaṇaśaktiḥ svato 'nubhavāt

*註偈 8 首*

```
svataḥ svasmād anubhavāt svapnasaṃkalpanādiṣu  // 3.37:1
karaṇaṃ nijasaṃvedyagrāhyagrāhakanirmitiḥ  // 3.37:2
śaktis tatkartṛtonmeṣaḥ svasaṃvittyaiva sidhyati  // 3.37:3
sambhavantīṃ tathā sṛṣṭiṃ yadi dārḍhyena bhāvayet  // 3.37:4
sarvasādhāraṇāśeṣanirmitiś ca bhavet tadā  // 3.37:5
yataḥ karaṇaśaktyātra śaktiḥ svātantryarūpiṇī  // 3.37:6
pramātur bodharūpasya sāraṃ tasmāt svamāyayā  // 3.37:7
tirohitāyāḥ svātantryaśakter uttejanaṃ prati  // 3.37:8
```

### 〔3.38〕 tripadādyanuprāṇanam

*註偈 15 首*

```
tripadaṃ jāgarāsvapnasauṣuptānām anukramāt  // 3.38:1
pratyekam ādimadhyāntarūpaṃ bhaṅgyā nirūpitam  // 3.38:2
bhāvaunmukhyatadāsaktitadekīkaraṇātmakam  // 3.38:3
sṛṣṭisthitilayākāraṃ turyeṇaiva tadādinā  // 3.38:4
tattrayāntaś camatkārarasānandaghanātmanā  // 3.38:5
māyayācchāditenāpi tirodhānasvarūpayā  // 3.38:6
tattadviṣayabhogeṣu vidyudvatsphuratā kṣaṇam  // 3.38:7
anuprāṇanam ādadhyād avadhānena sādhakaḥ  // 3.38:8
tenaiva jīvitenāpi jīvitasya nijātmanaḥ  // 3.38:9
samyaguttejanaṃ kuryād yenāsau tanmayo bhavet  // 3.38:10
turyānuprāṇanaṃ proktaṃ jāgarādau purā triṣu  // 3.38:11
caturtham iti sūtreṇa tripadetyādināmunā  // 3.38:12
jāgarādyādimadhyāntaparvasv iti viśiṣyate  // 3.38:13
antarmukhasvarūpāyām avasthāyāṃ na kevalam  // 3.38:14
tripadādiprāṇanam ity etad uktam athāpi tu  // 3.38:15
```

### 〔3.39〕 cittasthitivac charīrakaraṇabāhyeṣu

*註偈 10 首*

```
anuprāṇanam ity etad ādadyād iti śiṣyate  // 3.39:1
antarmukhasvarūpāyāṃ yathā cittasthitau tathā  // 3.39:2
anuprāṇanamuktena turyeṇānandarūpiṇā  // 3.39:3
kuryād bahirmukhatve 'pi dehākṣaviṣayātmani  // 3.39:4
tanmayaṃ bhavatīty arthāt tadā sarvaṃ carācaram  // 3.39:5
evaṃ svānandarūpāsya śaktiḥ svātantryalakṣaṇā  // 3.39:6
yatheṣṭabhāvanirmāṇakāriṇī bhavati sphuṭam  // 3.39:7
yadā punar asau yogī proktāṃ turyātmikāṃ daśām  // 3.39:8
āntarīṃ nāmṛśaty antas tadā dehādyahaṃkṛteḥ  // 3.39:9
apūrṇamanyatārūpād asyāṇavamalātmanaḥ  // 3.39:10
```

### 〔3.40〕 abhilāpād bahirgatiḥ saṃvāhyasya

*註偈 9 首*

```
tattvaiḥ śaktigaṇākrāntair dharaṇyantaiḥ kalādibhiḥ  // 3.40:1
yoner yonyantaraṃ neyaḥ saṃvāhyaḥ paśur ucyate  // 3.40:2
tasyāṇavamalākārāt tattatkarmānusāriṇaḥ  // 3.40:3
apūrṇamanyatārūpād abhilāṣād bahirgatiḥ  // 3.40:4
viṣayonmukhataivāsya nāntas tattvānusaṃhitiḥ  // 3.40:5
yadā punar maheśānaśaktipātavaśonmiṣat  // 3.40:6
ātmīyam eva vimṛśan nāste rūpaṃ tadāsya tu  // 3.40:7
abhāvād abhilāṣasya na bahirgatir āpatet  // 3.40:8
api tūktacarasvātmārāmataiveti kathyate  // 3.40:9
```

### 〔3.41〕 tadārūḍhapramites tatkṣayāj jīvasaṃkṣayaḥ

*註偈 9 首*

```
tad ityuktacare dhāmni saṃvettṛtvasvarūpiṇi  // 3.41:1
ārūḍhā pramitiḥ saṃvit tadvimarśanatatparā  // 3.41:2
yasya tasyāsya tad iti proktāṇavamalātmanaḥ  // 3.41:3
abhilāpasya rūḍhasya kṣayāj jīvasya saṃkṣayaḥ  // 3.41:4
puryaṣṭakasvabhāvasya praśamas tattvato bhavet  // 3.41:5
prāpnoti dehapāto 'sya nanv evaṃ jīvasaṃkṣaye  // 3.41:6
nāsau kadāpi kasyāpi dṛśyate 'trāpi yoginaḥ  // 3.41:7
tasmāt kathaṃ tadārūḍhapramitiḥ sādhako bhavet  // 3.41:8
ity āśaṅkyottaraṃ vakti bhagavān viśvadaiśikaḥ  // 3.41:9
```

### 〔3.42〕 bhūtakañcukī tadā vimukto bhūyaḥ patisamaḥ paraḥ

*註偈 9 首*

```
tadety uktābhilāṣasya praśamāj jīvasaṃkṣaye  // 3.42:1
puryaṣṭakapramātṛtvābhimānagalane 'py asau  // 3.42:2
dehārambhakarair bhūtair aspṛśadbhir ahaṃpadam  // 3.42:3
kañcukīva viśeṣeṇa mukto nirvāṇabhāgyataḥ  // 3.42:4
bhūyo bāhulyataḥ patyā samo 'yaṃ parameśinā  // 3.42:5
tatsvarūpasamāviṣṭacidānandaghanātmakaḥ  // 3.42:6
tata eva paraḥ pūrṇaḥ samyak tanmayatāṃ gataḥ  // 3.42:7
bhūtakañcukitāpy asya tadaiva na nivartate  // 3.42:8
kasmād ity api śaṅkāyām uttaraṃ vakti śaṃkaraḥ  // 3.42:9
```

### 〔3.43〕 naisargikaḥ prāṇasambandhaḥ

*註偈 20 首*

```
prāṇe pariṇatā saṃvit prāg iti proktayā diśā  // 3.43:1
nisargāt sahajāt svasya svātantryād anivāritāt  // 3.43:2
cañcatprapañcavaicitryaprakarṣakaraṇecchayā  // 3.43:3
saṃkocaṃ parigṛhṇānā saṃvid bhagavatī svayam  // 3.43:4
prāpnoti saṃkucattattatprāṇagrāhakabhūmikāḥ  // 3.43:5
uktam arthaṃ dṛḍhīkartuṃ saṃvādaḥ so 'yam atra tu  // 3.43:6
yā sā śaktiḥ parā sūkṣmā vyāpinī nirmalā śivā  // 3.43:7
śakticakrasya jananī parānandāmṛtātmikā  // 3.43:8
mahāghoreśvarī caṇḍā sṛṣṭisaṃhārakārikā  // 3.43:9
trivahaṃ trividhaṃ triṣṭhaṃ balāt kālaṃ prakarṣati  // 3.43:10
iti vājasaneyāyām iyam eva citiḥ parā  // 3.43:11
svātantryeṇāvaruhya prāk prāṇarūpe pramātari  // 3.43:12
candrabhāskaravahnyātmanāḍītritayavāhinam  // 3.43:13
antarbahirviśanniryanniśvāsocchvāsalakṣaṇam  // 3.43:14
atītavartamānāditrividhaṃ kālam ātmani  // 3.43:15
karṣanty antar bahiś ceti kathyate kālakarṣiṇī  // 3.43:16
tato naisargikas tasyāḥ prāṇasambandha āgataḥ  // 3.43:17
sthite 'pi prāṇasambandhe yas tadārūḍha āntarīm  // 3.43:18
saṃvidaṃ vimṛśann āste sa lokottaratāṃ vrajet  // 3.43:19
ity upāyopasaṃhāramukhenāha maheśvaraḥ  // 3.43:20
```

### 〔3.44〕 nāsikāntarmadhyasaṃyamāt kim atra savyāpasavyasauṣumneṣu

*註偈 17 首*

```
netrādiromarandhrāntanāḍīnāṃ niviḍātmanām  // 3.44:1
sarvāsāṃ mukhyabhūteṣu sarvāvaṣṭambhadāyiṣu  // 3.44:2
savyāpasavyasauṣumnanāḍīmārgeṣu sarvadā  // 3.44:3
nāḍīnāṃ nāsikā prāṇaśaktiḥ kuṭilavāhinī  // 3.44:4
antar ity āntarī saṃvit tatsvarūpasya yat punaḥ  // 3.44:5
madhyaṃ sarvāntaratvena pradhānaṃ viśvabhittikam  // 3.44:6
parāmarśamayaṃ rūpam uttīrṇaṃ tasya saṃyamāt  // 3.44:7
nibhālanaprakarṣotthāt svātmabuddhivimarśanāt  // 3.44:8
kim atra saṃyame vācyam iyam eva samāhitiḥ  // 3.44:9
dedīpyamānā sarvāsu daśāsv antarnirantaram  // 3.44:10
nirvyutthānāvadhānena yoginaivānubhūyate  // 3.44:11
mayy āveśya mano ye māṃ nityayuktā upāsate  // 3.44:12
śraddhayā parayopetās te me yuktatamā matāḥ  // 3.44:13
iti śrībhagavadgītāproktanītyanusārataḥ  // 3.44:14
viśvottīrṇanijāhaṃtāsamāveśitacetasaḥ  // 3.44:15
paryante yogino yogaphalaṃ samyak pradarśayan  // 3.44:16
upasaṃharati śrīmān uktaṃ prakaraṇaṃ śivaḥ  // 3.44:17
```

### 〔3.45〕 bhūyaḥ syāt pratimīlanam

*註偈 19 首*

```
punaś ca proktacaitanyasvarūponmīlanātmakam  // 3.45:1
parayogādhirūḍhasya bhavet paramayoginaḥ  // 3.45:2
bhūyaḥ syād iti vākyasya sphuṭam evāyam āśayaḥ  // 3.45:3
yac chivatvam amuṣyoktaṃ nāpūrvaṃ tat tu yoginaḥ  // 3.45:4
svabhāva eva tanmāyāśaktiprotthāpitān nijāt  // 3.45:5
nāyaṃ vikalpadaurātmyād bhāsamānam api svataḥ  // 3.45:6
vimraṣṭuṃ kṣama ity asya proktopāyakrameṇa tat  // 3.45:7
śivatvaṃ vyaktim etīti śivenodīritaṃ śivam  // 3.45:8
ity unmeṣas tṛtīyo 'yam āṇavopāyasūcakaḥ  // 3.45:9
iti śrīśivasūtrāṇāṃ rahasyārthopabṛṃhitam  // 3.45:10
prāguktavārttikāṃśena sahitaṃ vārttikāntaram  // 3.45:11
akhaṇḍasaṃvitsāmrājyayauvarājyādhikāriṇām  // 3.45:12
parākramahaṭhākrāntaṣaṭtriṃśattattvasampadām  // 3.45:13
madhurājakumārāṇāṃ mahāhaṃtādhirohiṇām  // 3.45:14
paścimena tadālokadhvastapaścimajanmanā  // 3.45:15
mayā varadarājena māyāmohāpasārakam  // 3.45:16
śrīkṣemarājanirṇītavyākhyānādhvānusāriṇā  // 3.45:17
kṛtinā kṛṣṇadāsena vyañjitaṃ kṛpayāñjasā  // 3.45:18
anugṛhṇantu nāmaitat santaḥ saṃtoṣam āgatāḥ  // 3.45:19
```


---

## 未核對

- ⚠️ **GRETIL header 未標註者名**；歸於 Bhāskara 依外部文獻，**未查 1925 年底本署名**。
- ⚠️ **未校勘**。另有 **J.C. Chatterji 1916 年 KSTS 本（Vols. IV & V）**，與本檔底本不同，**未對校**。
- ⚠️ **Kṣemarāja 的《濕婆經疏》（Vimarśinī）不在手**（GRETIL 無），所以無法做「同一本經、兩家註」的對等比較。
- ⚠️ **外部評價未平衡收錄**：查到一處學者評他的解釋「有時奇特而含混」（sometimes strange and ambiguous），**本檔未查該評價的原文與論據**。
- ⚠️ **Dyczkowski 的校譯本（SUNY）未取得。**
- ⚠️ **整理者不是梵文學者。** 經／註分層靠 GRETIL 的標記，**未逐條人工覆核歸屬**。

---

*本檔建立：2026-11-04。人格蒸餾：`人格庫/bhaskara-perspective/SKILL.md`*
*相關：《[濕婆經](濕婆經-Śivasūtra.md)》（本文）｜《[認出之心要](認出之心要-Pratyabhijñāhṛdaya-Kṣemarāja.md)》｜《[振動抉擇](振動抉擇-Spandanirṇaya-Kṣemarāja註.md)》｜《[至上義精要註](至上義精要註-Paramārthasāravivṛti-Yogarāja.md)》（另一個註者放大案例）*
