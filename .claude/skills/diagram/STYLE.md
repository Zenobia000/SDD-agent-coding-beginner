# Diagram Style Rules

Numbers researched from Taiwanese presentation practice (PixelCake scenario
tables, BFA projector measurements, PowerPoint canvas specs) plus house rules
derived from them — house rules are marked.

## Canvas (SVG)

- viewBox `0 0 1920 1080` — PowerPoint 16:9 at 96 DPI. Full-page diagrams use
  it whole; diagrams sharing a slide with a title bar use `0 0 1760 880`.
- Content inset **72px** from every edge (0.5-inch safe margin).
- **Bottom third is a no-go zone for key content** — back rows lose it behind
  front rows' heads (BFA projector finding). Legends and footnotes may live
  there; conclusions may not. (Banded one-pagers are exempt — see their
  section.)
- Raster export, when asked: 2× (3840×2160). PowerPoint 2016+ inserts SVG
  natively — prefer handing over the SVG.

## SVG drawing order

1. **Skeleton before ink.** Declare the layout first — rows/bands or grid, and
   the one message each band carries — then draw into it. Never draw first and
   rearrange after.
2. **Editable means structured**: text stays `<text>` (never converted to
   paths), each band or logical group gets its own `<g id="...">`, shapes are
   simple geometry (`rect`/`circle`/`line`). A glyph, where the genre expects
   one, is assembled from at most ~4 such primitives — never freehand `path`
   data.
3. **Anchor the look with one style idiom per diagram**: architecture blocks →
   "Microsoft architecture diagram style"; executive one-pager → "IBM
   consulting infographic style". One anchor buys more consistency than ten
   adjectives; colors still come from `/svg-palette`, never from the idiom.

## Type

- Font stack, everywhere text appears (SVG `font-family`, Mermaid override):
  `"Noto Sans TC","Microsoft JhengHei","微軟正黑體","PingFang TC",sans-serif`
- Sizes on the 1920×1080 canvas, meeting-room tier (the default — stricter than
  screen-share, so it degrades safely). Large-venue asks +25%.

| Element | Size |
| --- | --- |
| Diagram title | 44px |
| Node/bar labels | 32px (never below 24px) |
| Edge labels, legend | 24px |

- Node labels: **≤8 Chinese characters or ≤4 English words, max 2 lines**
  (house rule, derived from label size × node width).
- One diagram, one message. **More than ~15 nodes → split** by layer or by
  domain into two diagrams.

## Mermaid init

Mermaid's default font has no CJK and 16px is too small projected. Prepend:

```
%%{init: {"themeVariables": {
  "fontFamily": "\"Noto Sans TC\",\"Microsoft JhengHei\",\"PingFang TC\",sans-serif",
  "fontSize": "18px"
}}}%%
```

(Mermaid scales its canvas to fit the container, so sizes are not comparable
to the SVG tiers — 18px is the meeting-room default; bump to 20px for large
venues.)

## Color

All color decisions come from the `/svg-palette` skill (roles, override
mapping, as-is/to-be encoding). Two rules restated because they kill diagrams
when missed:

- White ground, dark text. Light-gray text dies on projectors.
- One accent per diagram — the single thing the audience must see.

## Executive one-pager

The densest genre — a pitch poster read on screen or as a handout, not across
a meeting room. It trades the projection type tiers for density; this is a
genre exception, and the bottom-third rule does not apply (bands fill the
page, the bottom band carries the conclusions).

| Element | Size |
| --- | --- |
| Title — the message itself | 40px |
| Band label (left rail) | 28px |
| Cell title | 24px |
| Cell body / takeaway | 20px, floor 18px |

- **The title states the conclusion, not the topic**: 「AI 平台三層本期須拍板」,
  never 「AI 平台評估總覽」. If the title works as a section heading in a
  report, it is not done.
- **Left rail is the reading spine**: one dark label block per band, flush
  left; band content sits right of the rail, left-aligned across bands.
- **Cell anatomy**: glyph + colored title + 1–3 short sub-lines; 4–6 cells per
  band. A band may close with one takeaway line (代表價值：…).
- **Parallel domains take categorical hues.** A band enumerating peer domains
  (capability pillars, product families) is `/svg-palette`'s categorical case:
  each domain gets its own hue, and the cell's title, glyph, and highlighted
  numbers wear it. Single-thread bands keep the monochrome ramp.
- **Hub-and-spoke** may replace a band's grid when the story has a center — a
  platform or agent with radiating capabilities.
- **No methodology prose on the poster.** One footnote line at most; caveats,
  formulas, and sources live in the report the poster references.

## Per-diagram checklist

Before delivering, every diagram has:

1. Title (what + scope, e.g. 「訂單系統 目標架構 2026Q4」)
2. Legend — whenever more than one color role or line style carries meaning
3. Date or version
4. 基準/目標 tag when the diagram depicts either state
5. No unresolved `?` marks
