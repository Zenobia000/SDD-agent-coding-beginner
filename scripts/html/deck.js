const slides = [...document.querySelectorAll(".slide")];
const controls = document.querySelector(".deck-controls");
const viewButton = document.querySelector(".deck-view");
const jump = document.querySelector(".deck-jump select");
let currentIndex = Math.max(0, slides.findIndex((slide) => slide.id === location.hash.slice(1)));
let allSlides = false;

function showSlide({focus = false} = {}) {
  slides.forEach((slide, index) => { slide.hidden = !allSlides && index !== currentIndex; });
  jump.value = slides[currentIndex].id;
  document.querySelector(".deck-position").textContent = (currentIndex + 1) + " / " + slides.length;
  document.querySelector(".deck-prev").disabled = currentIndex === 0;
  document.querySelector(".deck-next").disabled = currentIndex === slides.length - 1;
  viewButton.textContent = allSlides ? "逐頁導讀" : "完整瀏覽";
  if (focus) {
    const title = slides[currentIndex].querySelector(".slide__title");
    title.tabIndex = -1;
    title.focus({preventScroll: true});
    slides[currentIndex].scrollIntoView({block: "start", behavior: "instant"});
  }
}
function navigate(index) {
  currentIndex = Math.max(0, Math.min(slides.length - 1, index));
  if (location.hash === "#" + slides[currentIndex].id) showSlide({focus: true});
  else location.hash = slides[currentIndex].id;
}
controls.hidden = false;
viewButton.hidden = false;
document.querySelector(".deck-print").hidden = false;
viewButton.addEventListener("click", () => { allSlides = !allSlides; showSlide(); });
document.querySelector(".deck-print").addEventListener("click", () => print());
document.querySelector(".deck-prev").addEventListener("click", () => navigate(currentIndex - 1));
document.querySelector(".deck-next").addEventListener("click", () => navigate(currentIndex + 1));
jump.addEventListener("change", () => navigate(slides.findIndex((slide) => slide.id === jump.value)));
window.addEventListener("hashchange", () => {
  const index = slides.findIndex((slide) => slide.id === location.hash.slice(1));
  if (index >= 0) currentIndex = index;
  const target = document.getElementById(location.hash.slice(1));
  if (target?.closest(".slide")) {
    currentIndex = slides.indexOf(target.closest(".slide"));
    for (let parent = target.parentElement; parent; parent = parent.parentElement) {
      if (parent.tagName === "DETAILS") parent.open = true;
    }
  }
  showSlide({focus: true});
});
document.addEventListener("keydown", (event) => {
  if (event.defaultPrevented || event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
  if (event.target.closest("button, a, input, textarea, select, summary, [contenteditable]")) return;
  if (event.key === "Home") { event.preventDefault(); navigate(0); return; }
  if (event.key === "End") { event.preventDefault(); navigate(slides.length - 1); return; }
  const step = {ArrowRight: 1, PageDown: 1, " ": 1, ArrowLeft: -1, PageUp: -1}[event.key];
  if (!step || allSlides) return;
  event.preventDefault();
  navigate(currentIndex + step);
});
document.querySelectorAll(".slide table").forEach((table) => {
  const wrap = document.createElement("div");
  wrap.className = "table-wrap";
  wrap.tabIndex = 0;
  wrap.setAttribute("role", "region");
  wrap.setAttribute("aria-label", "資料表格，可水平捲動");
  const count = table.rows[0]?.cells.length || 1;
  wrap.style.setProperty("--table-cols", count);
  if (count > 3) wrap.classList.add("table-wrap--wide");
  table.replaceWith(wrap);
  wrap.appendChild(table);
  new ResizeObserver(() => wrap.classList.toggle("is-scrollable", wrap.scrollWidth > wrap.clientWidth + 1)).observe(wrap);
});
let printDetails;
window.addEventListener("beforeprint", () => {
  slides.forEach((slide) => { slide.hidden = false; });
  printDetails = [...document.querySelectorAll("details")].map((el) => [el, el.open]);
  document.querySelectorAll("details").forEach((el) => { el.open = true; });
});
window.addEventListener("afterprint", () => {
  printDetails?.forEach(([el, open]) => { el.open = open; });
  showSlide();
});
showSlide();
