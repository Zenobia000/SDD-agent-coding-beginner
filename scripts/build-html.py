"""把 handbook/ 與 starter-kit/ 各自建成一份單檔 HTML，雙擊就能在本機瀏覽器打開。

markdown 是唯一原稿；HTML 是產出，放 dist/（不進版控）。要 PDF 的話，在瀏覽器按列印存成 PDF，
樣式已經處理好 A4 分頁。

用法：python3 scripts/build-html.py        → dist/handbook.html、dist/starter-kit.html
需要：pip install markdown（3.x）
"""

import html
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
        "title": "AI 開發企業啟動包",
        "subtitle": "白皮書・導入評估・防呆檢核",
        "chapters": [
            "starter-kit/README.md",
            "starter-kit/book/02-why-stuck.md",
            "starter-kit/whitepaper/README.md",
            "starter-kit/whitepaper/attendance.md",
            "starter-kit/whitepaper/expense-claim.md",
            "starter-kit/whitepaper/support-ticket.md",
            "starter-kit/whitepaper/quotation.md",
            "starter-kit/whitepaper/inventory.md",
            "starter-kit/whitepaper/vendor-comparison.md",
            "starter-kit/whitepaper/marketing-dashboard.md",
            "starter-kit/assessment.md",
            "starter-kit/checklist.md",
        ],
    },
}

GITHUB = "https://github.com/Zenobia000/SDD-agent-coding-beginner/blob/main/"


def chapter_id(path: str) -> str:
    return "ch-" + re.sub(r"[^a-z0-9]+", "-", path.lower().removesuffix(".md")).strip("-")


def slugify(value: str, separator: str) -> str:
    """和 GitHub 一樣：小寫、去標點、空白換成連字號，保留中文。"""
    value = re.sub(r"[^\w\s-]", "", value.strip().lower())
    return re.sub(r"\s+", separator, value)


def render_markdown(text: str) -> str:
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
        target = (src_dir / path).as_posix()
        target = str(Path(target)).replace("\\", "/")
        target = re.sub(r"(^|/)\./", r"\1", target)
        while "/../" in "/" + target:
            target = re.sub(r"[^/]+/\.\./", "", target, count=1)
        if target.endswith("/"):
            target += "README.md"
        if Path(ROOT / target).is_dir():
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


def task_lists(body: str) -> str:
    body = re.sub(r"<li>\[ \]\s*", '<li class="task"><input type="checkbox"> ', body)
    return re.sub(r"<li>\[[xX]\]\s*", '<li class="task"><input type="checkbox" checked> ', body)


def first_heading(text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, flags=re.M)
    return re.sub(r"[`*]", "", match.group(1)).strip() if match else fallback


def build(name: str, book: dict) -> Path:
    chapters = book["chapters"]
    sections, nav = [], []
    for src in chapters:
        text = (ROOT / src).read_text(encoding="utf-8")
        cid = chapter_id(src)
        title = first_heading(text, src)
        body = task_lists(rewrite_links(render_markdown(text), src, chapters))
        sections.append(f'<section class="chapter" id="{cid}" data-source="{src}">{body}</section>')
        nav.append(f'<a href="#{cid}">{html.escape(title)}</a>')

    page = (ASSETS / "book.html").read_text(encoding="utf-8")
    replacements = {
        "{{TITLE}}": html.escape(book["title"]),
        "{{SUBTITLE}}": html.escape(book["subtitle"]),
        "{{BRAND}}": html.escape(BRAND),
        "{{BOOK}}": name,
        "{{NAV}}": "\n".join(nav),
        "{{CONTENT}}": "\n".join(sections),
        "{{CSS}}": (ASSETS / "book.css").read_text(encoding="utf-8"),
        "{{JS}}": (ASSETS / "book.js").read_text(encoding="utf-8"),
    }
    for key, value in replacements.items():
        page = page.replace(key, value)
    OUT.mkdir(exist_ok=True)
    out = OUT / f"{name}.html"
    out.write_text(page, encoding="utf-8")
    return out


def main() -> int:
    for name, book in BOOKS.items():
        missing = [c for c in book["chapters"] if not (ROOT / c).exists()]
        if missing:
            print(f"✗ {name}：找不到 {missing}")
            return 1
        print(f"✓ {build(name, book).relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
