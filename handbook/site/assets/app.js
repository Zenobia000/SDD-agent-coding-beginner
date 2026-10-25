// Shared behaviour for every handbook page: nav, pager, saved checklists, copy buttons.
(function () {
  const PAGES = [
    { id: "home",     href: "index.html",           title: "首頁",        color: "var(--ink-2)" },
    { id: "overview", href: "overview.html",        title: "1 總覽",      color: "var(--mist)" },
    { id: "setup",    href: "setup.html",           title: "2 課前準備",  color: "var(--sand)" },
    { id: "day1",     href: "day1.html",            title: "3 D1",        color: "var(--sage)" },
    { id: "day2",     href: "day2.html",            title: "4 D2",        color: "var(--rose)" },
    { id: "prompts",  href: "prompts.html",         title: "5 提示詞",    color: "var(--lav)" },
    { id: "trouble",  href: "troubleshooting.html", title: "6 問題排解",  color: "var(--clay)" },
  ];
  const FULL = {
    home: "首頁", overview: "總覽：兩天在做什麼", setup: "課前準備：環境檢核",
    day1: "D1｜Vibe Coding 到 PRD", day2: "D2｜SDD 實作與驗收",
    prompts: "Prompt 魔法書", trouble: "問題排解手冊",
  };
  const current = document.body.dataset.page;

  // Reveal linked lessons and prompt cards, including direct links on page load.
  function revealTarget() {
    let target;
    try { target = document.getElementById(decodeURIComponent(location.hash.slice(1))); }
    catch (_) { return; }
    if (!target) return;
    for (let parent = target.parentElement; parent; parent = parent.parentElement) {
      if (parent.tagName === 'DETAILS') parent.open = true;
    }
    target.querySelectorAll(':scope > details').forEach(detail => { detail.open = true; });
    requestAnimationFrame(() => target.scrollIntoView({ block: 'start' }));
  }
  window.addEventListener('hashchange', revealTarget);
  document.addEventListener('click', event => {
    const link = event.target.closest('a[href]');
    if (!link) return;
    const url = new URL(link.href, location.href);
    if (url.pathname === location.pathname && url.hash && url.hash === location.hash) {
      revealTarget();
    }
  });
  if (location.hash) revealTarget();
  document.querySelectorAll('[data-lessons]').forEach(button => {
    button.addEventListener('click', () => {
      document.querySelectorAll('details.lesson').forEach(detail => {
        detail.open = button.dataset.lessons === 'open';
      });
    });
  });

  const store = {
    get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch (e) { /* private mode */ } },
  };

  // ---- nav ----
  const nav = document.createElement("header");
  nav.className = "topnav";
  nav.innerHTML =
    '<div class="wrap"><a class="brand" href="index.html"><img src="assets/cat-face.jpg" alt=""><span>SDD × AI 實戰營講義</span></a>' +
    '<nav class="navlinks" aria-label="章節">' +
    PAGES.filter(p => p.id !== "home").map(p =>
      `<a href="${p.href}"${p.id === current ? ' aria-current="page"' : ""}><i class="dot" style="background:${p.color}"></i>${p.title}</a>`
    ).join("") + "</nav></div>";
  document.body.prepend(nav);

  // ---- pager ----
  const main = document.querySelector("main");
  const idx = PAGES.findIndex(p => p.id === current);
  if (main && idx >= 0) {
    const prev = PAGES[idx - 1], next = PAGES[idx + 1];
    const pager = document.createElement("div");
    pager.className = "wrap";
    pager.innerHTML = '<div class="pager">' +
      (prev ? `<a href="${prev.href}"><span>← 上一章</span><b>${FULL[prev.id]}</b></a>` : "") +
      (next ? `<a class="next" href="${next.href}"><span>下一章 →</span><b>${FULL[next.id]}</b></a>` : "") +
      "</div>";
    main.appendChild(pager);
    const foot = document.createElement("footer");
    foot.className = "site";
    foot.innerHTML = '<div class="wrap">SDD × AI Coding Agent 實戰營 · 桑尼資料科學 · 打勾的進度只存在你這台電腦的瀏覽器裡</div>';
    document.body.appendChild(foot);
  }

  // ---- saved checklists + progress ----
  const boxes = [...document.querySelectorAll('.checks input[type="checkbox"]')];
  boxes.forEach((b, i) => {
    const key = `hb:${current}:${b.dataset.k || i}`;
    b.checked = store.get(key) === "1";
    b.addEventListener("change", () => { store.set(key, b.checked ? "1" : "0"); paint(); });
  });
  function paint() {
    document.querySelectorAll("[data-progress]").forEach(el => {
      const scope = el.dataset.progress ? document.querySelectorAll(el.dataset.progress) : boxes;
      const all = [...scope].filter(x => x.type === "checkbox");
      const done = all.filter(x => x.checked).length;
      const bar = el.querySelector(".bar i"), txt = el.querySelector(".n");
      if (bar) bar.style.width = all.length ? (done / all.length * 100) + "%" : "0";
      if (txt) txt.textContent = `${done} / ${all.length}`;
    });
    if (boxes.length) store.set(`hb:${current}:__count`, `${boxes.filter(b => b.checked).length}/${boxes.length}`);
  }
  paint();

  // landing page: show per-chapter progress saved by other pages
  document.querySelectorAll("[data-chapter-progress]").forEach(el => {
    const v = store.get(`hb:${el.dataset.chapterProgress}:__count`);
    el.textContent = v ? `已完成驗收 ${v.replace("/", " / ")}` : "還沒開始";
  });

  // ---- copy buttons ----
  document.querySelectorAll(".code, .prompt").forEach(block => {
    const btn = document.createElement("button");
    btn.type = "button"; btn.className = "copy"; btn.textContent = "複製";
    btn.addEventListener("click", async () => {
      const text = block.dataset.copy || [...block.childNodes].filter(n => n !== btn).map(n => n.textContent).join("");
      try { await navigator.clipboard.writeText(text.trim()); btn.textContent = "已複製"; btn.classList.add("done"); }
      catch (e) { btn.textContent = "請手動選取"; }
      setTimeout(() => { btn.textContent = "複製"; btn.classList.remove("done"); }, 1600);
    });
    block.appendChild(btn);
  });
})();
