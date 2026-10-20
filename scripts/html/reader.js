// 單章導讀是漸進增強：無 JavaScript 時仍可閱讀及列印全文。
const chapters = [...document.querySelectorAll(".chapter")];
const cover = document.getElementById("cover");
const modeButton = document.querySelector(".reader-mode");
const printButton = document.querySelector(".print-button");
const readerBar = document.querySelector(".reader-bar");
const topicButton = document.querySelector(".topic-toggle");
const status = document.querySelector(".reader-status");
const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)");
let mode = "guided";
let activeChapter = null;
let lastPointer = false;
document.addEventListener("pointerdown", () => { lastPointer = true; });
document.addEventListener("keydown", () => { lastPointer = false; });

function setDetails(chapter, open) {
  chapter?.querySelectorAll(".topic, .chapter-sources").forEach((el) => { el.open = open; });
}

function updateTopicButton() {
  const topics = [...(activeChapter?.querySelectorAll(".topic") || [])];
  topicButton.hidden = topics.length === 0;
  const expanded = topics.length > 0 && topics.every((topic) => topic.open);
  topicButton.textContent = expanded ? "收合本章" : "展開本章";
  topicButton.setAttribute("aria-expanded", String(expanded));
}

function revealTarget(target) {
  for (let parent = target?.parentElement; parent; parent = parent.parentElement) {
    if (parent.tagName === "DETAILS") parent.open = true;
  }
}

function route({focus = false} = {}) {
  let id;
  try { id = decodeURIComponent(location.hash.slice(1)); } catch { id = ""; }
  const target = document.getElementById(id) || cover;
  activeChapter = target.closest(".chapter");
  document.body.dataset.readingMode = mode;
  chapters.forEach((chapter) => {
    chapter.hidden = mode === "guided" && chapter !== activeChapter;
  });
  cover.hidden = mode === "guided" && Boolean(activeChapter);
  readerBar.hidden = !activeChapter;
  modeButton.textContent = mode === "guided" ? "完整閱讀" : "逐章導讀";
  modeButton.setAttribute("aria-label", mode === "guided" ? "切換完整閱讀模式" : "切換逐章導讀模式");
  revealTarget(target);
  const index = chapters.indexOf(activeChapter);
  if (activeChapter) {
    const group = activeChapter.dataset.source.includes("/functions/") ? "部門與場景"
      : activeChapter.dataset.source.includes("/tools/") ? "工作工具" : "轉型導讀";
    status.textContent = group + " · " + (index + 1) + " / " + chapters.length;
    const previous = index > 0 ? chapters[index - 1] : cover;
    const next = chapters[index + 1] || cover;
    document.querySelector(".reader-prev").href = "#" + previous.id;
    document.querySelector(".reader-next").href = "#" + next.id;
    document.querySelector(".reader-prev").setAttribute("aria-label", index > 0 ? "上一章：" + previous.getAttribute("aria-label") : "回到封面");
    document.querySelector(".reader-next").setAttribute("aria-label", chapters[index + 1] ? "下一章：" + next.getAttribute("aria-label") : "回到封面");
  }
  document.querySelectorAll(".toc a").forEach((a) => {
    const selected = a.hash === "#" + (activeChapter || cover).id;
    a.classList.toggle("is-active", selected);
    if (selected) a.setAttribute("aria-current", "location");
    else a.removeAttribute("aria-current");
  });
  updateTopicButton();
  if (focus) {
    const destination = target.matches(".chapter") ? target.querySelector("h1") : target;
    destination?.setAttribute("tabindex", "-1");
    destination?.focus({preventScroll: true});
    destination?.scrollIntoView({block: "start", behavior: "instant"});
    // 章節切換只做短淡入；鍵盤操作與減少動態模式即時切換。
    if (lastPointer && !reduceMotion.matches && activeChapter) {
      activeChapter.getAnimations().forEach((animation) => animation.cancel());
      activeChapter.animate([{opacity: 0.65}, {opacity: 1}], {
        duration: 200, easing: "cubic-bezier(0.23, 1, 0.32, 1)"
      });
    }
  }
}

chapters.forEach((chapter) => {
  setDetails(chapter, false);
  const first = chapter.querySelector(".topic");
  if (first) first.open = true;
  chapter.querySelectorAll(".topic").forEach((topic) => topic.addEventListener("toggle", updateTopicButton));
});
modeButton.hidden = false;
printButton.hidden = false;
modeButton.addEventListener("click", () => {
  mode = mode === "guided" ? "full" : "guided";
  if (mode === "full") chapters.forEach((chapter) => setDetails(chapter, true));
  route();
});
printButton.addEventListener("click", () => window.print());
topicButton.addEventListener("click", () => {
  const topics = [...activeChapter.querySelectorAll(".topic")];
  const expand = !topics.every((topic) => topic.open);
  topics.forEach((topic) => { topic.open = expand; });
  updateTopicButton();
});
window.addEventListener("hashchange", () => route({focus: true}));

// 確保同一章的註腳、跨章工具連結及返回連結都能揭露隱藏內容。
document.addEventListener("click", (event) => {
  const anchor = event.target.closest('a[href^="#"]');
  if (!anchor || event.defaultPrevented || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
  if (anchor.hash === location.hash) {
    route({focus: true});
  }
});

let printState;
window.addEventListener("beforeprint", () => {
  printState = [...document.querySelectorAll("details")].map((el) => [el, el.open]);
  chapters.forEach((chapter) => { chapter.hidden = false; });
  cover.hidden = false;
  document.querySelectorAll("details").forEach((el) => { el.open = true; });
});
window.addEventListener("afterprint", () => {
  printState?.forEach(([el, open]) => { el.open = open; });
  route();
});
route();
