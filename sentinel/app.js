/**
 * 天目 · 靈台守門人 (Tianmu Sentinel) — 核心業務邏輯與互動引擎
 * 模組一：身心不良反應與氣功偏差量表評估
 * 模組二：不諂媚的鏡子（三重視角自欺刺破引擎）
 * 模組三：每日心性省察五維雷達繪製與本地存檔
 */

document.addEventListener('DOMContentLoaded', () => {
  initTabs();
  initSentinel();
  initMirror();
  initReflection();
});

/* ==========================================================================
   1. 頁籤導航切換
   ========================================================================== */
function initTabs() {
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-target');

      tabBtns.forEach(b => b.classList.remove('active'));
      tabContents.forEach(c => c.classList.remove('active'));

      btn.classList.add('active');
      const targetContent = document.getElementById(targetId);
      if (targetContent) {
        targetContent.classList.add('active');
      }
    });
  });
}

/* ==========================================================================
   2. 模組一：修行安全守門員評估邏輯
   ========================================================================== */
function initSentinel() {
  const runBtn = document.getElementById('btn-run-sentinel');
  const resetBtn = document.getElementById('btn-reset-sentinel');
  const checkboxes = document.querySelectorAll('.symptom-checkbox');

  function calculateRisk() {
    let totalScore = 0;
    let domainACount = 0;
    let domainBCount = 0;
    let domainCCount = 0;
    let triggeredItems = [];

    checkboxes.forEach(chk => {
      if (chk.checked) {
        const weight = parseInt(chk.getAttribute('data-weight'), 10) || 1;
        const domain = chk.getAttribute('data-domain');
        totalScore += weight;

        if (domain === 'A') domainACount++;
        if (domain === 'B') domainBCount++;
        if (domain === 'C') domainCCount++;

        const labelStrong = chk.closest('.checkbox-item').querySelector('strong').textContent;
        triggeredItems.push({ domain, label: labelStrong });
      }
    });

    updateRiskUI(totalScore, domainACount, domainBCount, domainCCount, triggeredItems);
  }

  function updateRiskUI(score, domA, domB, domC, items) {
    const riskBadge = document.getElementById('risk-badge');
    const meterBar = document.getElementById('risk-meter-bar');
    const scoreVal = document.getElementById('risk-score-val');
    const summary = document.getElementById('sentinel-status-summary');
    const prescList = document.getElementById('presc-list');

    scoreVal.textContent = score;
    const percentage = Math.min(Math.round((score / 35) * 100), 100);
    meterBar.style.width = Math.max(percentage, 5) + '%';

    // 依分數與嚴重項目劃分四級風險
    riskBadge.className = 'risk-badge';
    let prescriptions = [];

    if (score === 0) {
      riskBadge.textContent = '🟢 狀態平穩安全 (Safe & Clear)';
      summary.innerHTML = '<strong>目前狀況良好</strong>：暫未檢出顯著之神經失調、丹道火氣或認知著魔指針。';
      prescriptions = [
        '維持神闕穴（肚臍）下丹田溫和守候，吸短呼長，切記「似守非守、莫即莫離」。',
        '每次坐功結束前檢查口腔玉液（唾液），分三口緩緩嚥下以滋潤五臟。',
        '動功跳動排濁時全腳掌著地，以微汗為度，不可硬用腳尖透支元氣。'
      ];
    } else if (score <= 5) {
      riskBadge.classList.add('yellow');
      riskBadge.textContent = '🟡 輕度留意 (Early Alert)';
      summary.innerHTML = '<strong>身心出現輕微緊繃反應</strong>：可能伴隨初期火氣或輕度作息波動，建議放慢練功節奏。';
      prescriptions = [
        '【調息降速】減少每次靜坐時間，由意守神闕改為純粹觀察腹部起伏，不可用意念強行引氣。',
        '【補充水潤】適量飲用溫水或百合蓮子清心之品，檢查是否口乾舌燥。',
        '【加強散步】下座後在綠樹戶外散步 20 分鐘，腳踏實地釋放頭部浮陽。'
      ];
    } else if (score <= 14) {
      riskBadge.classList.add('orange');
      riskBadge.textContent = '🟠 中度預警 (High Caution - 存在氣滯與神經亢奮)';
      summary.innerHTML = `<strong>偵測到明確身心警訊</strong>（觸發 ${items.length} 項指針）：存在局部經絡充血或神經感受過載，需立即採取干預措施！`;
      
      prescriptions = [
        '【立即停止提腎術與閉氣】凡有便秘腹脹者，來靜師父嚴格叮囑：立即停練提腎，大劑量補充維他命 C 與高纖蔬果！',
        '【布朗大學接地協定（Britton Protocol）】暫停密集打坐 3–5 天，進行有負重之肌力運動，吃溫熱重口味正餐以重建軀體感受。',
        '【見如不見】打坐中出現之任何光斑異象一概閉目不理，絕不可向他人炫耀或探求其意義。'
      ];
    } else {
      riskBadge.classList.add('red');
      riskBadge.textContent = '🔴 高危禁行 (Emergency Stop - 立即停止修煉)';
      summary.innerHTML = `<strong>⚠️ 觸發嚴重走火入魔 / 神經病理過載指針！</strong> 檢出解離感、失眠或妄見，請立即終止一切靜修！`;

      prescriptions = [
        '【絕對終止打坐】立刻停止一切呼吸法、觀想法與靜坐！此時繼續用功只會加深神經迴路紊亂與大腦皮質失控。',
        '【回歸世俗現實生活】離開封閉禪修環境，尋求親友陪伴，從事具體體力勞動（打掃、烹飪、跑步），與土地保持物理接觸。',
        '【尋求專業精神醫學評估】若空中耳語、現實感喪失或恐慌持續超過 48 小時，請務必至正規醫院精神科就診，切莫聽信靈修圈「業障覺醒」之迷信藉口！'
      ];
    }

    // 渲染處方列表
    prescList.innerHTML = '';
    prescriptions.forEach(p => {
      const li = document.createElement('li');
      li.textContent = p;
      prescList.appendChild(li);
    });
  }

  runBtn.addEventListener('click', calculateRisk);
  checkboxes.forEach(chk => chk.addEventListener('change', calculateRisk));

  resetBtn.addEventListener('click', () => {
    checkboxes.forEach(chk => (chk.checked = false));
    calculateRisk();
  });
}

/* ==========================================================================
   3. 模組二：不諂媚的鏡子質詢邏輯
   ========================================================================== */
function initMirror() {
  const txtExperience = document.getElementById('txt-experience');
  const btnPierce = document.getElementById('btn-pierce-mirror');
  const btnClear = document.getElementById('btn-clear-mirror');
  const resultsContainer = document.getElementById('pierce-results');

  const btnPresetLight = document.getElementById('btn-preset-light');
  const btnPresetArrogance = document.getElementById('btn-preset-arrogance');
  const btnPresetChosen = document.getElementById('btn-preset-chosen');

  btnPresetLight.addEventListener('click', () => {
    txtExperience.value = '我今天打坐到第二十分鐘，眉心突然看見一團金光高速旋轉，感覺全身細胞都在同頻震顫，呼吸幾乎停止了，整個人像泡在溫暖的光海裡，我是不是已經突破結丹了？';
  });

  btnPresetArrogance.addEventListener('click', () => {
    txtExperience.value = '自從開始每天靜坐兩小時，我回到公司看著身邊同事為了那點薪水和權力勾心鬥角，只覺得他們無知可憐。我覺得自己已經超脫了世俗的情感，看透了所有人性的虛偽。';
  });

  btnPresetChosen.addEventListener('click', () => {
    txtExperience.value = '我最近入定後，感覺頭頂百會穴有一股強大的熱流在灌頂，耳邊似乎能感應到某種神聖意識在向我傳遞高維信息，我覺得自己身上肩負著喚醒更多人的神聖使命。';
  });

  btnClear.addEventListener('click', () => {
    txtExperience.value = '';
    resultsContainer.style.display = 'none';
  });

  btnPierce.addEventListener('click', () => {
    const text = txtExperience.value.trim();
    if (!text) {
      alert('請先輸入您今天的靜坐體驗或境界自述！');
      return;
    }

    // 動態分析關鍵字並客製化質詢
    const hasLight = /光|金光|旋轉|亮|發光|白光/i.test(text);
    const hasArrogance = /庸俗|虛偽|超脫|看透|可憐|凡夫/i.test(text);
    const hasChosen = /使命|神聖|頂輪|灌頂|耳語|被選中|高維/i.test(text);

    const yangmingEl = document.getElementById('mirror-yangming-text');
    const feynmanEl = document.getElementById('mirror-feynman-text');
    const krishnamurtiEl = document.getElementById('mirror-krishnamurti-text');
    const laijingEl = document.getElementById('mirror-laijing-text');

    if (hasArrogance) {
      yangmingEl.textContent = '「看透別人容易，看透自己的傲慢最難！你自覺超脫世俗，殊不知『覺得自己超脫』本身就是最隱蔽的私欲大盜。你在事上磨礪了嗎？走出房間，面對父母時你是否耐心？面對刁難時你是否不怒？若以冷眼俯視眾生，你的修行連起點都還沒進去！」';
      feynmanEl.textContent = '「你覺得自己掌握了客觀真理？在科學裡，任何自視甚高的理論如果無法經受嚴酷的現實反饋，就是垃圾。你所謂的『看透他人』，只不過是大腦給自己製造的優越感多巴胺反饋回路。別騙自己，你只是找到了逃避人際複雜性的哲學藉口。」';
      krishnamurtiEl.textContent = '「當你把世界分為『庸俗的他們』和『清醒的我』時，分裂便已誕生，暴力便已開始。觀察者自居為高人一等的評判者，正是自我（Ego）在靈性外衣下的最高級膨脹。在純然的覺知中，沒有庸俗與聖潔的對立，只有如實的看。」';
      laijingEl.textContent = '「全真重陽祖師立教十五論，第一條就是『出家先修人倫』！自視清高、目空一切，這在龍門派叫『心志散亂，著魔之兆』！連身邊活生生的人都包容不了，你肚子裡的氣機全是孤陽冷火，如何能得水火既濟？」';
    } else if (hasChosen) {
      yangmingEl.textContent = '「良知本在當下孝悌忠信處，何須向外尋求高維密旨？若生出『唯我獨醒、肩負救世』之念，正是妄心借神聖之名作崇。堯舜治天下，不過盡其常道；若心念不求日常本分，反盼奇異託夢，便是心體不正。」';
      feynmanEl.textContent = '「如果你真的收到了高維信息，請讓那個高維存在先幫你解開黎曼猜想，或者預測一下明天隨機硬幣的連續二十次正反。如果它只會給你一些含糊其辭的『大愛』『使命』口號，那就是你的下丘腦和大腦顳葉在玩神經信號雜音！」';
      krishnamurtiEl.textContent = '「權威是心靈的致命毒藥，而自封為權威更是毒中之毒。人類歷史上無數的苦難，都始於有人自以為被神聖力量選中。真理無路，真理不挑選特權代表。放下那個神聖使命的重擔吧，那只是小我恐懼平庸的臨終掙扎。」';
      laijingEl.textContent = '「《楞嚴經》講得斬釘截鐵：『口中好言佛魔神力，使人聽從，若作聖解，即受群邪！』凡有神秘聲音傳遞指令，立刻斷喝一聲『呸！』見怪不怪，其怪自敗！舌頂上齶，氣沉肚臍神闕，多吃三碗米飯，別讓腦子裡的鬼話騙了你的命！」';
    } else {
      // 預設或光影範例
      yangmingEl.textContent = '「你且捫心自問：當這團光影出現時，你心底深處是不是早就在暗暗期盼看見點什麼？這個所謂的殊勝體驗，是讓你在走出房門時對父母妻兒更溫柔寬厚，還是讓你更想找個人說說、發個文章炫耀自己與眾不同？若夾了一絲自矜，這便是心中的盜賊！」';
      feynmanEl.textContent = '「第一原則是你絕對不能欺騙自己，而你自己正是最容易被騙的那個人！閉上眼睛看見光斑，大概率只是視網膜感光細胞在低氧或眼球微壓下的生理放電。如果把你關在沒有任何預期的全黑房間做雙盲測試，你還敢拿身家性命押注那是宇宙能量嗎？大腦最擅長製造迎合期望的假數據。」';
      krishnamurtiEl.textContent = '「你看見的那個神聖圖像，是不是剛好就是你的傳統、你的導師預先描述給你的符號？基督教修士看見聖母，道士看見丹鼎，這不是超脫，這是記憶的投影儀在牆上放映幻燈片。觀察者本身就是被觀察之物，只要還有一個『我』在享受『境界』，你就依然被鎖在虛榮的牢籠裡。」';
      laijingEl.textContent = '「凡有所象，皆是虛妄！乃自己識神所化！舌頂上齶，口中有無清香甘甜的玉液湧出？下座後大便乾不乾？若肚子發脹、嘴巴發苦，只有腦袋發熱，這不叫神仙境界，這叫虛火上炎識神著魔！立刻下地散步，喝大杯溫水，見如不見，自然消災！」';
    }

    resultsContainer.style.display = 'block';
    resultsContainer.scrollIntoView({ behavior: 'smooth' });
  });
}

/* ==========================================================================
   4. 模組三：每日心性省察雷達圖與手記本地儲存
   ========================================================================== */
function initReflection() {
  const sldHumility = document.getElementById('sld-humility');
  const sldContentment = document.getElementById('sld-contentment');
  const sldPeace = document.getElementById('sld-peace');
  const sldSincerity = document.getElementById('sld-sincerity');
  const sldDiligence = document.getElementById('sld-diligence');

  const valHumility = document.getElementById('val-humility');
  const valContentment = document.getElementById('val-contentment');
  const valPeace = document.getElementById('val-peace');
  const valSincerity = document.getElementById('val-sincerity');
  const valDiligence = document.getElementById('val-diligence');

  const txtNote = document.getElementById('txt-reflection-note');
  const btnSave = document.getElementById('btn-save-reflection');
  const btnExport = document.getElementById('btn-export-reflections');
  const historyContainer = document.getElementById('history-items-container');
  const radarSvg = document.getElementById('radar-chart-svg');

  const sliders = [
    { el: sldHumility, valEl: valHumility, name: '謙遜(破傲慢)' },
    { el: sldContentment, valEl: valContentment, name: '清心(戒貪求)' },
    { el: sldPeace, valEl: valPeace, name: '和顏(化嗔怒)' },
    { el: sldSincerity, valEl: valSincerity, name: '誠意(破自欺)' },
    { el: sldDiligence, valEl: valDiligence, name: '精進(消懈怠)' }
  ];

  // 監聽數值變更
  sliders.forEach(s => {
    s.el.addEventListener('input', () => {
      s.valEl.textContent = `${s.el.value} / 5`;
      renderRadarChart();
    });
  });

  // 繪製五邊形星芒雷達圖
  function renderRadarChart() {
    const cx = 200;
    const cy = 200;
    const r = 130;
    const totalAxes = 5;
    const angleStep = (Math.PI * 2) / totalAxes;
    const startAngle = -Math.PI / 2; // 正上方開始

    let svgHtml = '';

    // 1. 繪製背景同心五邊形網格 (5層)
    for (let level = 1; level <= 5; level++) {
      const currentR = (r / 5) * level;
      let points = [];
      for (let i = 0; i < totalAxes; i++) {
        const angle = startAngle + i * angleStep;
        const x = cx + currentR * Math.cos(angle);
        const y = cy + currentR * Math.sin(angle);
        points.push(`${x.toFixed(1)},${y.toFixed(1)}`);
      }
      svgHtml += `<polygon points="${points.join(' ')}" fill="none" stroke="rgba(255, 255, 255, ${level === 5 ? 0.2 : 0.08})" stroke-width="1.2" />`;
    }

    // 2. 繪製 5 條軸線與文字標籤
    let dataPoints = [];
    for (let i = 0; i < totalAxes; i++) {
      const angle = startAngle + i * angleStep;
      const xMax = cx + r * Math.cos(angle);
      const yMax = cy + r * Math.sin(angle);

      // 軸線
      svgHtml += `<line x1="${cx}" y1="${cy}" x2="${xMax.toFixed(1)}" y2="${yMax.toFixed(1)}" stroke="rgba(255, 255, 255, 0.12)" stroke-width="1" />`;

      // 標籤位置
      const labelR = r + 26;
      const xLabel = cx + labelR * Math.cos(angle);
      const yLabel = cy + labelR * Math.sin(angle) + 4;
      const anchor = Math.abs(Math.cos(angle)) < 0.2 ? 'middle' : Math.cos(angle) > 0 ? 'start' : 'end';
      svgHtml += `<text x="${xLabel.toFixed(1)}" y="${yLabel.toFixed(1)}" fill="#cbd5e1" font-size="11" font-weight="600" text-anchor="${anchor}">${sliders[i].name}</text>`;

      // 數值多邊形頂點
      const val = parseInt(sliders[i].el.value, 10);
      const valR = (r / 5) * val;
      const xData = cx + valR * Math.cos(angle);
      const yData = cy + valR * Math.sin(angle);
      dataPoints.push(`${xData.toFixed(1)},${yData.toFixed(1)}`);
    }

    // 3. 繪製數據覆蓋多邊形 (金黃光澤)
    svgHtml += `
      <polygon points="${dataPoints.join(' ')}" 
               fill="rgba(245, 158, 11, 0.35)" 
               stroke="#f59e0b" 
               stroke-width="2.5" 
               filter="drop-shadow(0px 0px 8px rgba(245, 158, 11, 0.6))" />
    `;

    // 4. 繪製數據頂點小圓點
    dataPoints.forEach(pt => {
      const [px, py] = pt.split(',');
      svgHtml += `<circle cx="${px}" cy="${py}" r="4" fill="#ffffff" stroke="#f59e0b" stroke-width="2" />`;
    });

    radarSvg.innerHTML = svgHtml;
  }

  // 儲存省察日記至 LocalStorage
  function saveReflection() {
    const scores = sliders.map(s => ({ name: s.name, val: parseInt(s.el.value, 10) }));
    const note = txtNote.value.trim();
    const dateStr = new Date().toLocaleString('zh-TW', { hour12: false });

    const newEntry = {
      date: dateStr,
      scores,
      note: note || '（今日未錄詳細自白，僅記錄心性指標）'
    };

    let history = [];
    try {
      history = JSON.parse(localStorage.getItem('tianmu_reflections') || '[]');
    } catch (e) {
      history = [];
    }

    history.unshift(newEntry);
    if (history.length > 50) history.pop(); // 保持最多 50 筆

    localStorage.setItem('tianmu_reflections', JSON.stringify(history));
    alert('今日心性省察手記已成功存檔！');
    renderHistory();
  }

  // 渲染歷史列表
  function renderHistory() {
    let history = [];
    try {
      history = JSON.parse(localStorage.getItem('tianmu_reflections') || '[]');
    } catch (e) {
      history = [];
    }

    if (history.length === 0) {
      historyContainer.innerHTML = '<p class="empty-hint">尚無歷史手記，完成今天的第一篇省察吧！</p>';
      return;
    }

    let html = '';
    history.forEach(item => {
      const avg = (item.scores.reduce((acc, cur) => acc + cur.val, 0) / 5).toFixed(1);
      html += `
        <div class="history-item">
          <div class="history-date">📅 ${item.date} ｜ 五德均分：${avg} / 5.0</div>
          <p class="history-note">"${item.note}"</p>
        </div>
      `;
    });
    historyContainer.innerHTML = html;
  }

  // 導出 JSON 紀錄
  function exportHistory() {
    const historyJson = localStorage.getItem('tianmu_reflections') || '[]';
    const blob = new Blob([historyJson], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `tianmu_reflections_${Date.now()}.json`;
    a.click();
    URL.revokeObjectURL(url);
  }

  btnSave.addEventListener('click', saveReflection);
  btnExport.addEventListener('click', exportHistory);

  // 初始化繪製
  renderRadarChart();
  renderHistory();
}
