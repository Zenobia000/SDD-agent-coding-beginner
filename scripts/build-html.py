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
        "title": "AI 的回報卡在組織",
        "subtitle": "AI-Native 企業的五個決策與四個階段",
        "chapters": sorted_md("starter-kit/report") + sorted_md("starter-kit/functions") + sorted_md("starter-kit/tools"),
    },
}

DECK = {
    "name": "deck",
    "title": "AI 的回報卡在組織",
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
    return f'<div class="chart chart--bar">{"".join(out)}</div>'


def chart_column(spec: dict) -> str:
    """柱狀：時間或階段的變化，支援負值。"""
    rows, unit = spec["data"], spec.get("unit", "")
    values = [r["value"] for r in rows]
    top, bottom = max(max(values), 0), min(min(values), 0)
    span = (top - bottom) or 1
    zero = top / span * 100
    cols = []
    for r in rows:
        v = r["value"]
        height = abs(v) / span * 100
        style = f"top:{(zero - height if v >= 0 else zero):.2f}%;height:{height:.2f}%"
        cls = "col__fill" + (" is-key" if r.get("highlight") else "") + (" is-neg" if v < 0 else "")
        cols.append(
            f'<div class="col"><div class="col__plot"><span class="{cls}" style="{style}"></span>'
            f'<span class="col__value" style="top:{(zero - height if v >= 0 else zero + height):.2f}%">{fmt(r, v, unit, signed=bottom < 0)}</span></div>'
            f'<span class="col__label">{esc(r["label"])}</span></div>'
        )
    axis = f'<span class="col__zero" style="top:{zero:.2f}%"></span>' if bottom < 0 else ""
    return f'<div class="chart chart--column" style="--cols:{len(rows)}"><div class="col__grid">{axis}{"".join(cols)}</div></div>'


def chart_stack(spec: dict) -> str:
    """堆疊橫條：成分。"""
    segs = spec["data"]
    total = sum(s["value"] for s in segs) or 1
    parts = "".join(
        f'<span class="stack__seg{" is-key" if s.get("highlight") else ""}" style="flex:{s["value"]}">'
        f'<b>{fmt(s, s["value"], spec.get("unit", ""))}</b><small>{esc(s["label"])}</small></span>'
        for s in segs
    )
    return f'<div class="chart chart--stack" data-total="{total}">{parts}</div>'


def chart_funnel(spec: dict) -> str:
    """漏斗：一路縮小的比例。"""
    rows, unit = spec["data"], spec.get("unit", "")
    span = max(r["value"] for r in rows) or 1
    out = "".join(
        f'<div class="funnel__row"><span class="funnel__bar{" is-key" if r.get("highlight") else ""}" '
        f'style="width:{max(r["value"] / span * 100, 8):.2f}%"><b>{fmt(r, r["value"], unit)}</b></span>'
        f'<span class="funnel__label">{esc(r["label"])}</span></div>'
        for r in rows
    )
    return f'<div class="chart chart--funnel">{out}</div>'


def chart_matrix(spec: dict) -> str:
    """2×2：選項定位。cells 依序為左上、右上、左下、右下。"""
    x, y = spec["x"], spec["y"]
    cells = "".join(
        f'<div class="matrix__cell{" is-key" if c.get("highlight") else ""}"><b>{esc(c["title"])}</b>'
        f'<span>{esc(c.get("text", ""))}</span></div>'
        for c in spec["cells"]
    )
    return (
        f'<div class="chart chart--matrix"><span class="matrix__y">{esc(y["label"])}<small>{esc(y["low"])} → {esc(y["high"])}</small></span>'
        f'<div class="matrix__grid">{cells}</div>'
        f'<span class="matrix__x">{esc(x["label"])}<small>{esc(x["low"])} → {esc(x["high"])}</small></span></div>'
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
    return (
        f'<figure class="exhibit" data-exhibit="{esc(spec.get("id", ""))}"><figcaption>'
        f'<span class="exhibit__no">圖表 {esc(spec.get("id", ""))}</span>'
        f'<span class="exhibit__title">{esc(spec["title"])}</span>{unit}</figcaption>'
        f'{chart}<p class="exhibit__source">{esc(notes)}</p></figure>'
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


def build_book(name: str, book: dict) -> Path:
    chapters = book["chapters"]
    sections, nav = [], []
    for src in chapters:
        text = (ROOT / src).read_text(encoding="utf-8")
        cid = chapter_id(src)
        body = task_lists(rewrite_links(render_markdown(text), src, chapters))
        sections.append(f'<section class="chapter" id="{cid}" data-source="{src}">{body}</section>')
        nav.append(f'<a href="#{cid}">{html.escape(nav_label(first_heading(text, src)))}</a>')
    page = fill((ASSETS / "book.html").read_text(encoding="utf-8"), {
        "TITLE": html.escape(book["title"]),
        "SUBTITLE": html.escape(book["subtitle"]),
        "BRAND": html.escape(BRAND),
        "BOOK": name,
        "NAV": "\n".join(nav),
        "CONTENT": "\n".join(sections),
        "CSS": (ASSETS / "theme.css").read_text(encoding="utf-8"),
        "JS": (ASSETS / "book.js").read_text(encoding="utf-8"),
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
            f'<footer class="slide__foot"><span>{source}</span><span>{BRAND}　{number:02d}</span></footer>'
            f"</div></section>"
        )
    page = fill((ASSETS / "deck.html").read_text(encoding="utf-8"), {
        "TITLE": html.escape(DECK["title"]),
        "SLIDES": "\n".join(out),
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
