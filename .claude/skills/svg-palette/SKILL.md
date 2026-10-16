---
name: svg-palette
description: SVG 繪圖的色盤與用色規則 — 預設靛青深淺＋橘強調，可用使用者指定色票（公司 CI 色）覆蓋。當要繪製任何 SVG 圖、挑「配色」「色票」「圖表顏色」，或使用者提供品牌色要套進圖裡時使用。
---

# SVG Palette

Color roles and rules for every SVG diagram. Palettes are defined as **roles**, not
loose swatches — any palette (including a user-supplied one) maps into the same
role slots, so swapping palettes never changes the drawing logic.

## Roles

| Role | Purpose | Default (Indigo) |
| --- | --- | --- |
| `primary-1` (darkest) | Main nodes, strongest tier | `#28406B` |
| `primary-2` | Second tier | `#4A648F` |
| `primary-3` | Third tier | `#7E93B4` |
| `primary-4` | Fourth tier / fills | `#B9C6D9` |
| `primary-5` (lightest) | Background washes, bands | `#E3EAF3` |
| `accent` | The one thing to emphasize | `#E07B39` |
| `ink` | Text on light ground | `#1F2933` |
| `muted` | Secondary text, arrows, borders | `#5B6B78` |
| `line` | Gridlines, dividers | `#D9E0E6` |
| `bg` | Canvas ground | `#FFFFFF` |

## Rules

- **One accent per diagram.** The accent marks the single point the audience must
  see — a highlighted node, the current milestone, the changed component. Two
  accents means no accent: demote one to a primary tier.
- **Depth over hue.** Distinguish categories with primary-1..5 shades first.
  Reach for extra hues only when shades genuinely cannot separate the categories
  (see Fallback below).
- **Text is ink on light, white on dark.** On `primary-1`/`primary-2` fills use
  `#FFFFFF` text; on `primary-3` and lighter use `ink`. Never gray text:
  projector-measured, gray text at 60% brightness is barely legible and
  anything lighter vanishes on a bad projector.
- **No red/green semantics.** Status is not encoded in red/green (user decision,
  also colorblind-hostile). As-Is/To-Be encoding is fixed:
  - **added / changed** → `accent`
  - **removed / deprecated** → `primary-5` fill with `muted` dashed border
  - **unchanged** → primary tiers as normal
- **Ground is white.** `bg` stays `#FFFFFF` for anything that may land on a
  slide — screenshots must paste clean into PowerPoint.

## Override: user-supplied palette

When the user names brand/CI colors, map them into the roles and use them
**instead of** the default — the default is only a fallback for silence.

1. Take the user's main color as the hue; generate `primary-1..5` as a
   dark-to-light ramp of that hue (keep lightness steps roughly even).
2. Take their secondary/highlight color as `accent`; if they gave only one
   color, pick a warm tone that contrasts with the ramp and say so.
3. Neutrals (`ink`/`muted`/`line`/`bg`) stay as defined here unless the user
   overrides them too.
4. Echo the mapped role table back to the user before drawing.

## Alternate themes

Use only when the user asks for that mood by name or description:

| Theme | primary-1..5 | accent |
| --- | --- | --- |
| 企業藍灰 (corporate) | `#1F4E79` `#456A8C` `#5B7C99` `#94A7B7` `#D3DDE4` | `#C9A227` |
| 深墨螢光 (tech/dark-slide) | `#2B3440` `#4A5866` `#77879A` `#A6B2BF` `#DCE2E8` | `#00B4D8` |

## Fallback: many unrankable categories

When a diagram needs 4+ categorical colors that shades cannot separate (e.g.
swimlane owners with no hierarchy), use Okabe-Ito order — colorblind-safe:
`#0072B2` `#E69F00` `#009E73` `#D55E00` `#56B4E9`. This mode has no accent:
`#E07B39` reads as a sixth category next to the Okabe-Ito oranges, so
emphasize with weight or outline instead.
