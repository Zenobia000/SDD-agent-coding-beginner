// 講義的互動：通過訊號打勾記進度、提示詞標出要自己改的地方、複製按鈕、目錄跟著捲動、Mermaid 圖。
// 進度只存在這台電腦的瀏覽器（localStorage），換電腦或清除瀏覽資料就沒了。

const book = document.body.dataset.book;

function storageGet(key) {
  try { return localStorage.getItem(key); } catch { return null; }
}
function storageSet(key, value) {
  try {
    if (value === null) localStorage.removeItem(key);
    else localStorage.setItem(key, value);
  } catch { /* 無痕視窗或封鎖儲存時，打勾只在這次有效 */ }
}

// 表格包一層，窄螢幕可以橫向捲
document.querySelectorAll(".chapter table").forEach((table) => {
  const wrap = document.createElement("div");
  wrap.className = "table-wrap";
  table.replaceWith(wrap);
  wrap.appendChild(table);
});

// 通過訊號
function renderProgress() {
  const all = document.querySelectorAll("li.task input");
  const done = [...all].filter((b) => b.checked).length;
  const top = document.querySelector(".topbar__progress");
  if (all.length) {
    top.hidden = false;
    top.textContent = `通過訊號 ${done} / ${all.length}`;
  }
  document.querySelectorAll(".chapter").forEach((chapter) => {
    const boxes = chapter.querySelectorAll("li.task input");
    if (!boxes.length) return;
    let badge = chapter.querySelector(".chapter-progress");
    if (!badge) {
      badge = document.createElement("span");
      badge.className = "chapter-progress";
      chapter.querySelector("h1")?.after(badge);
    }
    const n = [...boxes].filter((b) => b.checked).length;
    badge.textContent = `本章通過訊號 ${n} / ${boxes.length}`;
  });
}
document.querySelectorAll(".chapter").forEach((chapter) => {
  chapter.querySelectorAll("li.task input").forEach((box, i) => {
    const key = `sdd:${book}:${chapter.id}:${i}`;
    if (storageGet(key) === "1") box.checked = true;
    box.addEventListener("change", () => {
      storageSet(key, box.checked ? "1" : null);
      renderProgress();
    });
  });
});
renderProgress();

// 提示詞：<要你換的內容>、＜…＞、＿＿ 標底色；加複製按鈕
document.querySelectorAll("pre:not(.mermaid) > code").forEach((code) => {
  const raw = code.textContent;
  code.innerHTML = code.innerHTML.replace(/(&lt;[^&\n]{1,40}?&gt;|＜[^＞\n]{0,40}＞|＿{2,})/g, '<span class="fill" title="換成你自己的內容">$1</span>');
  const button = document.createElement("button");
  button.type = "button";
  button.className = "copy";
  button.textContent = "複製";
  button.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(raw);
      button.textContent = "已複製";
    } catch {
      button.textContent = "請手動選取";
    }
    setTimeout(() => { button.textContent = "複製"; }, 1500);
  });
  code.parentElement.appendChild(button);
});

// 目錄：手機開合、捲動時標出目前章節
const menu = document.querySelector(".menu");
menu.addEventListener("click", () => {
  const open = document.body.classList.toggle("toc-open");
  menu.setAttribute("aria-expanded", String(open));
});
document.querySelectorAll(".toc a").forEach((a) => a.addEventListener("click", () => document.body.classList.remove("toc-open")));

const links = new Map([...document.querySelectorAll(".toc a")].map((a) => [a.getAttribute("href").slice(1), a]));
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    links.forEach((a) => a.classList.remove("is-active"));
    links.get(entry.target.id)?.classList.add("is-active");
  });
}, { rootMargin: "-40% 0px -55% 0px" });
document.querySelectorAll(".cover, .chapter").forEach((s) => observer.observe(s));

// Mermaid：要連網才載得到；離線時保留原始文字
if (document.querySelector("pre.mermaid")) {
  import("https://cdn.jsdelivr.net/npm/mermaid@11.17.2/dist/mermaid.esm.min.mjs")
    .then(({ default: mermaid }) => {
      mermaid.initialize({ startOnLoad: false, theme: "base", themeVariables: { primaryColor: "#e8f5f4", primaryBorderColor: "#2c918c", lineColor: "#1e3a5f", fontFamily: "Noto Sans TC, sans-serif" } });
      mermaid.run({ querySelector: "pre.mermaid" });
    })
    .catch(() => { /* 離線：留著原始圖碼 */ });
}
