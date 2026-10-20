// 課程網站的互動：通過訊號打勾記進度、提示詞標出要自己改的地方、V-model 點選對照。
// 只在網站上作用；在 GitHub 上看 markdown 時這支不會載入，內容一樣完整。

(function () {
  "use strict";

  function storageGet(key) {
    try { return window.localStorage.getItem(key); } catch (e) { return null; }
  }
  function storageSet(key, value) {
    try {
      if (value === null) window.localStorage.removeItem(key);
      else window.localStorage.setItem(key, value);
    } catch (e) { /* 無痕模式或封鎖儲存時，打勾只在這次瀏覽有效 */ }
  }

  // ── 通過訊號：讓 task list 可以打勾，記在這台瀏覽器 ───────────────────
  function setupChecklists() {
    var boxes = document.querySelectorAll(".md-content .task-list-item input[type=checkbox]");
    if (!boxes.length) return;
    var page = location.pathname.replace(/index\.html$/, "");

    boxes.forEach(function (box, i) {
      var key = "sdd-course:" + page + ":" + i;
      box.disabled = false;
      box.checked = storageGet(key) === "1";
      box.addEventListener("change", function () {
        storageSet(key, box.checked ? "1" : null);
        renderProgress(boxes);
      });
    });
    renderProgress(boxes);
  }

  function renderProgress(boxes) {
    var done = Array.prototype.filter.call(boxes, function (b) { return b.checked; }).length;
    var bar = document.querySelector(".course-progress");
    if (!bar) {
      bar = document.createElement("div");
      bar.className = "course-progress";
      bar.innerHTML = '<span class="course-progress__label"></span><span class="course-progress__track"><span class="course-progress__fill"></span></span>';
      var h1 = document.querySelector(".md-content h1");
      if (h1) h1.insertAdjacentElement("afterend", bar);
      else return;
    }
    bar.querySelector(".course-progress__label").textContent = "這一頁的通過訊號 " + done + " / " + boxes.length;
    bar.querySelector(".course-progress__fill").style.width = (100 * done / boxes.length) + "%";
  }

  // ── 提示詞：把 <要你換的內容> 標出來 ─────────────────────────────────
  function markPlaceholders() {
    document.querySelectorAll(".md-content pre code").forEach(function (code) {
      if (code.dataset.placeholders) return;
      code.dataset.placeholders = "1";
      var walker = document.createTreeWalker(code, NodeFilter.SHOW_TEXT);
      var nodes = [];
      while (walker.nextNode()) nodes.push(walker.currentNode);
      nodes.forEach(function (node) {
        var re = /<[^<>\n]{1,40}>|＿{2,}/g;
        var text = node.nodeValue;
        if (!re.test(text)) return;
        re.lastIndex = 0;
        var frag = document.createDocumentFragment();
        var last = 0, m;
        while ((m = re.exec(text))) {
          frag.appendChild(document.createTextNode(text.slice(last, m.index)));
          var mark = document.createElement("mark");
          mark.className = "course-fill";
          mark.title = "換成你自己的內容";
          mark.textContent = m[0];
          frag.appendChild(mark);
          last = m.index + m[0].length;
        }
        frag.appendChild(document.createTextNode(text.slice(last)));
        node.parentNode.replaceChild(frag, node);
      });
    });
  }

  // ── V-model：點左邊的規格，看右邊哪一層測試接住它 ─────────────────────
  var VMODEL = [
    {
      id: "prd", doc: "01 Brief／02 PRD", ids: "G、NG、P、EP、US、AC",
      what: "為什麼做、為誰做、怎樣算做完", d1: "D1 單元 2–3",
      test: "驗收測試", where: "backend/tests/acceptance/",
      how: "打 API，照 AC 的 Given／When／Then 驗使用者看得到的結果", d2: "D2 I1–I3，每張票的 AC"
    },
    {
      id: "srs", doc: "03 SRS", ids: "UC、FR、NFR",
      what: "系統必須做到的行為與品質", d1: "D1 單元 4",
      test: "系統測試＋eval", where: "backend/tests/system/、scripts/run_eval.py",
      how: "FR 用測試驗；「解析一句話」這條用 eval 量準確率；注入攻擊是安全 NFR", d2: "D2 I1–I4"
    },
    {
      id: "sad", doc: "04 SAD", ids: "ADR、C4、資訊流",
      what: "系統怎麼組起來、AI 和規則各負責什麼", d1: "D1 單元 5",
      test: "整合測試", where: "backend/tests/integration/",
      how: "驗元件之間的接縫：API → LLM（用 FakeLLM）→ 規則 → 資料庫", d2: "D2 I1–I3"
    },
    {
      id: "sds", doc: "05 SDS", ids: "API、UI、ER、模組",
      what: "每一塊怎麼做", d1: "D1 單元 6",
      test: "單元測試", where: "backend/tests/unit/",
      how: "一個模組一個函式地驗，例如額度計算、狀態轉換", d2: "D2 I2–I3"
    }
  ];

  function setupVModel() {
    var host = document.getElementById("vmodel");
    if (!host || host.dataset.ready) return;
    host.dataset.ready = "1";

    var rows = VMODEL.map(function (r, i) {
      return '<div class="vm-row" style="--vm-indent:' + i + '">' +
        '<button type="button" class="vm-node vm-left" data-i="' + i + '"><b>' + r.doc + '</b><small>' + r.ids + '</small></button>' +
        '<span class="vm-link" aria-hidden="true"></span>' +
        '<button type="button" class="vm-node vm-right" data-i="' + i + '"><b>' + r.test + '</b><small>' + r.where + '</small></button>' +
        '</div>';
    }).join("");

    host.innerHTML =
      '<div class="vm-head"><span>V 的左邊：D1 寫規格</span><span>V 的右邊：D2 寫測試、寫程式</span></div>' +
      rows +
      '<div class="vm-bottom"><b>06 Test Plan</b><small>TC 編號。D1 單元 7 先寫好右邊要驗什麼；D2 每個測試標 <code>@pytest.mark.req("TC-xx")</code></small></div>' +
      '<div class="vm-panel" aria-live="polite"></div>' +
      '<p class="vm-chain">一條需求的旅程：<code>US-01</code> → <code>AC-01.1</code> → <code>FR-02</code> → <code>API-01</code> → <code>TC-03</code> → <code>@pytest.mark.req("TC-03", "AC-01.1")</code>　斷在哪一環，<code>trace.py</code> 會告訴你。</p>';

    var panel = host.querySelector(".vm-panel");
    function select(i) {
      var r = VMODEL[i];
      host.querySelectorAll(".vm-row").forEach(function (row, j) {
        row.classList.toggle("is-active", j === i);
      });
      panel.innerHTML =
        '<div><h4>' + r.doc + '　<small>' + r.d1 + '</small></h4><p>寫的是：' + r.what + '</p><p>編號：<code>' + r.ids + '</code></p></div>' +
        '<div><h4>' + r.test + '　<small>' + r.d2 + '</small></h4><p>' + r.how + '</p><p>放在：<code>' + r.where + '</code></p></div>';
    }
    host.addEventListener("click", function (e) {
      var btn = e.target.closest(".vm-node");
      if (btn) select(Number(btn.dataset.i));
    });
    select(0);
  }

  function init() {
    setupChecklists();
    markPlaceholders();
    setupVModel();
  }

  // 開了 navigation.instant 時換頁不會重新載入，要跟著主題的 document$ 重跑
  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(init);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
