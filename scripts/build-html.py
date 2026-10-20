"""把講義、啟動包報告、高層簡報各建成一份單檔 HTML，雙擊就能在本機瀏覽器打開。

markdown 是唯一原稿；HTML 是產出，放 dist/（不進版控）。要 PDF 的話，在瀏覽器按列印：
講義與報告是 A4 直式，簡報是 16:9 橫式。

用法：
  python3 scripts/build-html.py            → dist/handbook.html、dist/starter-kit.html、dist/deck.html
  python3 scripts/build-html.py --outline  → 只印出所有行動標題，做 storyline 測試
需要：pip install markdown（3.x）

圖表寫法：在 markdown 裡用 ```exhibit 區塊放一段 JSON，建置時轉成 HTML 圖表。
欄位與支援的類型見 render_exhibit()；規則見 starter-kit/STYLE.md 第 3 節。
"""

import html
import json
import math
import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("找不到 markdown 套件。先裝：python3 -m pip install markdown")

ROOT = Path(__file__).resolve().parents[1]
ASSETS = Path(__file__).resolve().parent / "html"
OUT = ROOT / "dist"
BRAND = "桑尼資料科學 SUNNY DATA SCIENCE"
GITHUB = "https://github.com/Zenobia000/SDD-agent-coding-beginner/blob/main/"


def sorted_md(folder: str) -> list[str]:
    return sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / folder).glob("*.md"))


BOOKS = {
    "handbook": {
        "title": "規格驅動 × AI 開發實戰營",
        "subtitle": "學員講義",
        "chapters": [
            "handbook/00-setup.md",
            "handbook/01-overview.md",
            "handbook/02-day1.md",
            "handbook/03-day2.md",
            "handbook/appendix/prompt-book.md",
            "handbook/appendix/troubleshooting.md",
        ],
    },
    "starter-kit": {
        "title": "企業 AI 轉型啟動指南",
        "subtitle": "五個決策、四個階段，用 90 天驗證第一個值得投入的場景",
        "chapters": sorted_md("starter-kit/report") + sorted_md("starter-kit/functions") + sorted_md("starter-kit/tools"),
    },
}

DECK = {
    "name": "deck",
    "title": "企業 AI 轉型啟動指南",
    "source": "starter-kit/deck/slides.md",
}


# ── 連結與錨點 ─────────────────────────────────────────────────────────────

def chapter_id(path: str) -> str:
    return "ch-" + re.sub(r"[^a-z0-9]+", "-", path.lower().removesuffix(".md")).strip("-")


def slugify(value: str, separator: str) -> str:
    """和 GitHub 一樣：小寫、去標點、空白換成連字號，保留中文。"""
    value = re.sub(r"[^\w\s-]", "", value.strip().lower())
    return re.sub(r"\s+", separator, value)


def rewrite_links(body: str, src: str, chapters: list[str]) -> str:
    """站內連結改成書內錨點；書外的相對路徑改成 GitHub 網址；外部連結開新分頁。"""
    here = chapter_id(src)
    src_dir = Path(src).parent

    def fix(match: re.Match) -> str:
        href = html.unescape(match.group(1))
        if href.startswith(("http://", "https://", "mailto:")):
            return f'href="{html.escape(href)}" target="_blank" rel="noopener"'
        if href.startswith("#"):
            return f'href="#{here}--{href[1:]}"'
        path, _, anchor = href.partition("#")
        target = re.sub(r"(^|/)\./", r"\1", (src_dir / path).as_posix())
        while "/../" in "/" + target:
            target = re.sub(r"[^/]+/\.\./", "", target, count=1)
        if target.endswith("/") or (ROOT / target).is_dir():
            target = target.rstrip("/") + "/README.md"
        if target in chapters:
            ch = chapter_id(target)
            return f'href="#{ch}--{anchor}"' if anchor else f'href="#{ch}"'
        for other, spec in BOOKS.items():
            if target in spec["chapters"]:
                ch = chapter_id(target)
                return f'href="{other}.html#{ch}--{anchor}"' if anchor else f'href="{other}.html#{ch}"'
        return f'href="{GITHUB}{html.escape(target)}" target="_blank" rel="noopener"'

    body = re.sub(r'href="([^"]+)"', fix, body)
    return re.sub(r'id="([^"]+)"', lambda m: f'id="{here}--{m.group(1)}"', body)


# ── 圖表 ───────────────────────────────────────────────────────────────────

def esc(value) -> str:
    return html.escape(str(value))


def fmt(row: dict, value: float, unit: str, signed: bool = False) -> str:
    """數值標籤：有 display 就照寫；百分比加 %；其他單位寫在圖表的單位列。"""
    if "display" in row:
        return esc(row["display"])
    number = f"{value:g}"
    if signed and value > 0:
        number = "+" + number
    return esc(number + ("%" if unit == "%" else ""))


def chart_bar(spec: dict) -> str:
    """橫條：項目排序。有負值時自動改成以中線為軸的雙向條。"""
    rows, unit = spec["data"], spec.get("unit", "")
    values = [r["value"] for r in rows]
    span = spec.get("max") or max(abs(v) for v in values) or 1
    diverging = any(v < 0 for v in values)
    out = []
    for r in rows:
        v = r["value"]
        width = abs(v) / span * (50 if diverging else 100)
        left = (50 if v >= 0 else 50 - width) if diverging else 0
        cls = "bar__fill" + (" is-key" if r.get("highlight") else "") + (" is-neg" if v < 0 else "")
        out.append(
            f'<div class="bar__row"><span class="bar__label">{esc(r["label"])}</span>'
            f'<span class="bar__track{" is-diverging" if diverging else ""}">'
            f'<span class="{cls}" style="left:{left:.2f}%;width:{width:.2f}%"></span></span>'
            f'<span class="bar__value">{fmt(r, v, unit, signed=diverging)}</span></div>'
        )
    ticks = [-span, 0, span] if diverging else [0, span / 2, span]
    axis = "".join(f'<span>{fmt({}, value, unit)}</span>' for value in ticks)
    return (
        f'<div class="chart chart--bar">{"".join(out)}'
        f'<div class="bar__axis" aria-label="橫軸刻度">{axis}</div></div>'
    )


def chart_column(spec: dict) -> str:
    """柱狀：時間或階段的變化，支援負值。"""
    rows, unit = spec["data"], spec.get("unit", "")
    values = [r["value"] for r in rows]
    def ceiling(value: float) -> float:
        if not value:
            return 0
        step = 10 ** math.floor(math.log10(value))
        return math.ceil(value / step) * step

    top, bottom = ceiling(max(max(values), 0)), -ceiling(abs(min(min(values), 0)))
    if top == bottom:
        top = 1
    span = (top - bottom) or 1
    zero = top / span * 100
    cols = []
    for r in rows:
        v = r["value"]
        height = abs(v) / span * 100
        style = f"top:{(zero - height if v >= 0 else zero):.2f}%;height:{height:.2f}%"
        cls = "col__fill" + (" is-key" if r.get("highlight") else "") + (" is-neg" if v < 0 else "")
        cols.append(
            f'<div class="col"><div class="col__plot">'
            f'<span class="col__zero" style="top:{zero:.2f}%"></span>'
            f'<span class="{cls}" style="{style}"></span>'
            f'<span class="col__value{" is-neg" if v < 0 else ""}" style="top:{(zero - height if v >= 0 else zero + height):.2f}%">{fmt(r, v, unit, signed=bottom < 0)}</span></div>'
            f'<span class="col__label">{esc(r["label"])}</span></div>'
        )
    ticks = sorted({top, bottom, 0}, reverse=True)
    axis = "".join(
        f'<span style="top:{(top - value) / span * 100:.2f}%">{fmt({}, value, unit)}</span>'
        for value in ticks
    )
    return (
        f'<div class="chart chart--column" style="--cols:{len(rows)}">'
        f'<div class="column__desktop"><div class="col__axis">{axis}</div>'
        f'<div class="col__grid">{"".join(cols)}</div></div>'
        f'<div class="column__mobile">{chart_bar(spec)}</div></div>'
    )


def chart_stack(spec: dict) -> str:
    """堆疊橫條：成分。"""
    segs = spec["data"]
    total = sum(s["value"] for s in segs) or 1
    parts = "".join(
        f'<span class="stack__seg{" is-key" if s.get("highlight") else ""}" style="flex:{s["value"]}"></span>'
        for s in segs
    )
    legend = "".join(
        f'<div class="stack__item{" is-key" if s.get("highlight") else ""}">'
        f'<b>{fmt(s, s["value"], spec.get("unit", ""))}</b><span>{esc(s["label"])}</span></div>'
        for s in segs
    )
    return (
        f'<div class="chart chart--stack" data-total="{total}">'
        f'<div class="stack__bar" aria-hidden="true">{parts}</div>'
        f'<div class="stack__legend">{legend}</div></div>'
    )


def chart_funnel(spec: dict) -> str:
    """相容舊稿；現有資料分母不同，以獨立長條避免誤讀為轉換率。"""
    return chart_bar(spec)


def chart_matrix(spec: dict) -> str:
    """2×2：選項定位。cells 依序為左上、右上、左下、右下。"""
    x, y = spec["x"], spec["y"]
    cells = []
    for i, c in enumerate(spec["cells"]):
        y_value, x_value = y["high" if i < 2 else "low"], x["high" if i % 2 else "low"]
        cells.append(
            f'<div class="matrix__cell{" is-key" if c.get("highlight") else ""}" '
            f'data-x="{esc(x_value)}" data-y="{esc(y_value)}">'
            f'<small class="matrix__position">{esc(y_value)} · {esc(x_value)}</small>'
            f'<b>{esc(c["title"])}</b><span>{esc(c.get("text", ""))}</span></div>'
        )
    return (
        f'<div class="chart chart--matrix">'
        f'<p class="matrix__axis"><b>縱軸：{esc(y["label"])}</b>'
        f'<span>上列：{esc(y["high"])} ／ 下列：{esc(y["low"])}</span></p>'
        f'<div class="matrix__grid">{"".join(cells)}</div>'
        f'<div class="matrix__x"><b>橫軸：{esc(x["label"])}</b>'
        f'<span>左欄：{esc(x["low"])}</span><span>右欄：{esc(x["high"])}</span></div></div>'
    )


def chart_ladder(spec: dict) -> str:
    """階梯：階段演進。"""
    steps = spec["steps"]
    out = "".join(
        f'<div class="ladder__step{" is-key" if s.get("highlight") else ""}" style="--i:{i}">'
        f'<span class="ladder__no">{i + 1:02d}</span><b>{esc(s["name"])}</b>'
        f'<span class="ladder__text">{esc(s.get("text", ""))}</span>'
        + (f'<span class="ladder__signal">過關訊號：{esc(s["signal"])}</span>' if s.get("signal") else "")
        + (f'<span class="ladder__meta">{esc(s["meta"])}</span>' if s.get("meta") else "")
        + "</div>"
        for i, s in enumerate(steps)
    )
    return f'<div class="chart chart--ladder" style="--n:{len(steps)}">{out}</div>'


CHARTS = {
    "bar": chart_bar,
    "column": chart_column,
    "stack": chart_stack,
    "funnel": chart_funnel,
    "matrix": chart_matrix,
    "ladder": chart_ladder,
}


def render_exhibit(raw: str) -> str:
    """JSON 欄位：id、title（行動標題）、type、unit、data／x／y／cells／steps、source、note。"""
    try:
        spec = json.loads(raw)
        chart = CHARTS[spec["type"]](spec)
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        return f'<pre class="exhibit-error">圖表格式錯誤：{esc(error)}\n{esc(raw)}</pre>'
    unit = f'<span class="exhibit__unit">單位：{esc(spec["unit"])}</span>' if spec.get("unit") else ""
    notes = "；".join(filter(None, [spec.get("source") and f'資料來源：{spec["source"]}', spec.get("note") and f'註：{spec["note"]}']))
    data_table = ""
    if spec.get("data"):
        unit_label = f'（{esc(spec["unit"])}）' if spec.get("unit") else ""
        rows = "".join(
            f'<tr><th scope="row">{esc(row["label"])}</th>'
            f'<td>{fmt(row, row["value"], spec.get("unit", ""))}</td></tr>'
            for row in spec["data"]
        )
        data_table = (
            f'<details class="chart-data"><summary>查看數據表</summary>'
            f'<table><caption>{esc(spec["title"])}</caption>'
            f'<thead><tr><th scope="col">項目</th><th scope="col">數值{unit_label}'
            f'</th></tr></thead><tbody>{rows}</tbody></table></details>'
        )
    return (
        f'<figure class="exhibit" data-exhibit="{esc(spec.get("id", ""))}"><figcaption>'
        f'<span class="exhibit__no">圖表 {esc(spec.get("id", ""))}</span>'
        f'<span class="exhibit__title">{esc(spec["title"])}</span>{unit}</figcaption>'
        f'{chart}<p class="exhibit__source">{esc(notes)}</p>{data_table}</figure>'
    )


def render_markdown(text: str) -> str:
    text = re.sub(
        r"```exhibit\n(.*?)```",
        lambda m: "\n" + render_exhibit(m.group(1)) + "\n",
        text,
        flags=re.S,
    )
    text = re.sub(
        r"```mermaid\n(.*?)```",
        lambda m: '<pre class="mermaid">' + html.escape(m.group(1)) + "</pre>",
        text,
        flags=re.S,
    )
    return markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list", "md_in_html", "toc", "footnotes"],
        extension_configs={"toc": {"slugify": slugify}},
    )


# ── 組書 ───────────────────────────────────────────────────────────────────

def task_lists(body: str) -> str:
    body = re.sub(r"<li>\[ \]\s*", '<li class="task"><input type="checkbox"> ', body)
    return re.sub(r"<li>\[[xX]\]\s*", '<li class="task"><input type="checkbox" checked> ', body)


def first_heading(text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, flags=re.M)
    return re.sub(r"[`*]", "", match.group(1)).strip() if match else fallback


def nav_label(title: str) -> str:
    """目錄只放章號與前半句，完整的行動標題留在內文。"""
    return re.split(r"[，：；]", title, maxsplit=1)[0]


def fill(template: str, values: dict) -> str:
    for key, value in values.items():
        template = template.replace("{{" + key + "}}", value)
    return template


def reading_topics(body: str) -> str:
    """依既有 h2 分段，以原生 details 提供可列印、無 JS 也可用的漸進揭露。"""
    source_match = re.search(r'<div class="footnote">.*$', body, flags=re.S)
    source = ""
    if source_match:
        source = (
            '<details class="chapter-sources" open><summary>本章來源與註腳</summary>'
            + source_match.group(0) + "</details>"
        )
        body = body[:source_match.start()]
    chunks = re.split(r'(<h2\b[^>]*>.*?</h2>)', body, flags=re.S)
    parts = [f'<div class="chapter-intro">{chunks[0]}</div>']
    for i in range(1, len(chunks), 2):
        parts.append(
            '<details class="topic" open><summary>'
            + chunks[i]
            + '<span class="topic__cue" aria-hidden="true"></span></summary>'
            + f'<div class="topic__body">{chunks[i + 1]}</div></details>'
        )
    return "".join(parts) + source


def chapter_group(src: str) -> str:
    if "/functions/" in src:
        return "部門與場景"
    if "/tools/" in src:
        return "工作工具"
    name = Path(src).name
    if name < "04-":
        return "看懂現況"
    if name < "09-":
        return "五個決策"
    return "90 天行動"


def build_book(name: str, book: dict) -> Path:
    chapters = book["chapters"]
    sections, nav = [], []
    last_group = None
    for index, src in enumerate(chapters):
        text = (ROOT / src).read_text(encoding="utf-8")
        cid = chapter_id(src)
        body = task_lists(rewrite_links(render_markdown(text), src, chapters))
        if name == "starter-kit":
            body = reading_topics(body)
            previous = chapters[index - 1] if index else None
            following = chapters[index + 1] if index + 1 < len(chapters) else None
            next_title = nav_label(first_heading((ROOT / following).read_text(encoding="utf-8"), following)) if following else "回到封面"
            body += (
                '<nav class="chapter-pager" aria-label="章節導覽">'
                f'<a href="#{chapter_id(previous) if previous else "cover"}">← {"上一章" if previous else "封面"}</a>'
                f'<a href="#{chapter_id(following) if following else "cover"}">'
                f'<small>{"繼續閱讀" if following else "完成本指南"}</small>{esc(next_title)} →</a></nav>'
            )
            group = chapter_group(src)
            if group != last_group:
                nav.append(f'<p class="toc__group">{esc(group)}</p>')
                last_group = group
        sections.append(f'<section class="chapter" id="{cid}" data-source="{src}" aria-label="{esc(nav_label(first_heading(text, src)))}">{body}</section>')
        nav.append(f'<a href="#{cid}" title="{esc(first_heading(text, src))}">{html.escape(nav_label(first_heading(text, src)))}</a>')
    reader = name == "starter-kit"
    cover_actions = (
        f'<div class="cover__actions"><a class="action action--primary" href="#{chapter_id(chapters[0])}">開始導讀 <span aria-hidden="true">→</span></a>'
        f'<a class="action" href="#{chapter_id("starter-kit/functions/01-customer-service.md")}">依部門找場景</a>'
        f'<a class="action" href="#{chapter_id("starter-kit/tools/01-use-case-canvas.md")}">直接使用工具</a></div>'
    ) if reader else ""
    page = fill((ASSETS / "book.html").read_text(encoding="utf-8"), {
        "TITLE": html.escape(book["title"]),
        "SUBTITLE": html.escape(book["subtitle"]),
        "BRAND": html.escape(BRAND),
        "BOOK": name,
        "READER_TOOLS": '<button class="reader-mode" type="button" hidden>完整閱讀</button><button class="print-button" type="button" hidden>列印</button>' if reader else "",
        "COVER_ACTIONS": cover_actions,
        "COVER_NOTE": "先讀重點，再展開證據。你可以逐章前進、直接跳到自己的部門，或切換完整閱讀。列印時會自動展開全文。" if reader else "有勾選框的地方可以打勾，進度記在這台電腦的瀏覽器裡。要紙本或 PDF，請用瀏覽器列印。",
        "READER_BAR": '<div class="reader-bar" hidden><span class="reader-status" aria-live="polite"></span><button class="topic-toggle" type="button">展開本章</button><a class="reader-prev" href="#cover" aria-label="上一章">←</a><a class="reader-next" href="#cover" aria-label="下一章">→</a></div>' if reader else "",
        "NAV": "\n".join(nav),
        "CONTENT": "\n".join(sections),
        "CSS": (ASSETS / "theme.css").read_text(encoding="utf-8") + ((ASSETS / "reader.css").read_text(encoding="utf-8") if reader else ""),
        "JS": (ASSETS / "book.js").read_text(encoding="utf-8") + ((ASSETS / "reader.js").read_text(encoding="utf-8") if reader else ""),
    })
    return write(name, page)


def split_slides(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"^---\s*$", text, flags=re.M) if s.strip()]


def build_deck() -> Path:
    slides = split_slides((ROOT / DECK["source"]).read_text(encoding="utf-8"))
    out = []
    for number, raw in enumerate(slides, start=1):
        kind = re.search(r"<!--\s*(cover|divider)\s*-->", raw)
        body = render_markdown(re.sub(r"<!--.*?-->", "", raw, flags=re.S))
        title = ""
        heading = re.search(r"<h[12][^>]*>(.*?)</h[12]>", body, flags=re.S)
        if heading:
            title = heading.group(1)
            body = body.replace(heading.group(0), "", 1)
        source = ""
        found = re.search(r"<p>(來源：.*?)</p>", body, flags=re.S)
        if found:
            source = found.group(1)
            body = body.replace(found.group(0), "")
        cls = f"slide slide--{kind.group(1)}" if kind else "slide"
        out.append(
            f'<section class="{cls}" id="s{number}"><div class="slide__inner">'
            f'<h2 class="slide__title">{title}</h2><div class="slide__body">{body}</div>'
            f'<footer class="slide__foot"><span>{source}</span><span>{number:02d} / {len(slides):02d}</span></footer>'
            f"</div></section>"
        )
    page = fill((ASSETS / "deck.html").read_text(encoding="utf-8"), {
        "TITLE": html.escape(DECK["title"]),
        "SLIDES": "\n".join(out),
        "SLIDE_NAV": "".join(
            f'<option value="s{i}">{i:02d}　{esc(nav_label(first_heading(raw, "簡報")))}</option>'
            for i, raw in enumerate(slides, 1)
        ),
        "JS": (ASSETS / "deck.js").read_text(encoding="utf-8"),
        "CSS": (ASSETS / "theme.css").read_text(encoding="utf-8") + (ASSETS / "deck.css").read_text(encoding="utf-8"),
    })
    return write(DECK["name"], page)


def write(name: str, page: str) -> Path:
    OUT.mkdir(exist_ok=True)
    out = OUT / f"{name}.html"
    out.write_text(page, encoding="utf-8")
    return out


# ── storyline 測試 ─────────────────────────────────────────────────────────

def outline() -> None:
    """印出報告的章節標題與圖表標題、簡報每頁標題。只讀這些就該讀懂整份文件。"""
    for src in BOOKS["starter-kit"]["chapters"]:
        block = None
        for line in (ROOT / src).read_text(encoding="utf-8").splitlines():
            if block is not None:
                if line.startswith("```"):
                    try:
                        spec = json.loads("\n".join(block))
                        print(f"      ▸ 圖表 {spec.get('id', '')}  {spec['title']}")
                    except (json.JSONDecodeError, KeyError):
                        print("      ▸ （圖表格式錯誤）")
                    block = None
                else:
                    block.append(line)
            elif line.startswith("```exhibit"):
                block = []
            elif heading := re.match(r"^(#{1,3})\s+(.+)", line):
                print("  " * (len(heading.group(1)) - 1) + heading.group(2))
    deck = ROOT / DECK["source"]
    if deck.exists():
        print("\n── 高層簡報 ──")
        for number, raw in enumerate(split_slides(deck.read_text(encoding="utf-8")), start=1):
            heading = re.search(r"^#{1,2}\s+(.+)$", raw, flags=re.M)
            print(f"{number:02d}  {heading.group(1) if heading else '（沒有標題）'}")


def main() -> int:
    if "--outline" in sys.argv:
        outline()
        return 0
    for name, book in BOOKS.items():
        missing = [c for c in book["chapters"] if not (ROOT / c).exists()]
        if missing:
            print(f"✗ {name}：找不到 {missing}")
            return 1
        print(f"✓ {build_book(name, book).relative_to(ROOT)}")
    if (ROOT / DECK["source"]).exists():
        print(f"✓ {build_deck().relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
