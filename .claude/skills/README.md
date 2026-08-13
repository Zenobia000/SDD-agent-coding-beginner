# 這些技能是別人的，不要在這裡改

這個目錄的 36 個技能是 [Luca0x5755/luca-skills](https://github.com/Luca0x5755/luca-skills) 的副本。

| | |
|---|---|
| 來源 | `https://github.com/Luca0x5755/luca-skills.git` |
| 凍結 commit | `1434be8ff814b51f0e7fa166bc2e767075e71d83` |
| 凍結日期 | 2026-08-12 |
| 抓取日期 | 2026-08-13 |
| 授權 | MIT，見根目錄 [`THIRD-PARTY-NOTICES.md`](../../THIRD-PARTY-NOTICES.md) |

## 為什麼直接放在這裡

**fork 下來就能用，不用跑安裝腳本。** Claude Code 會自動載入專案的 `.claude/skills/`，GitHub Copilot 也讀同一個路徑。

代價是這份副本**不會自動更新**。上游修了 bug，你不會知道。

## 對原始 repo 做的唯一改動：攤平目錄

上游把技能分成 `skills/core/` 與 `skills/draft/` 兩個桶，靠安裝腳本連結時攤平。這裡直接攤平放好：

```text
上游  skills/core/ask-luca/SKILL.md
      skills/draft/feasibility/SKILL.md
              ↓ 攤平
這裡  .claude/skills/ask-luca/SKILL.md
      .claude/skills/feasibility/SKILL.md
```

**檔案內容一個字都沒改。** 只有位置變了。

原本的 `core` / `draft` 分類意義是「對外發佈與否」，不是「能不能用」—— 兩桶都會被安裝，所以攤平不影響行為。想知道哪些是 draft，見 [`docs/SKILL-MAP.md`](../../docs/SKILL-MAP.md)。

## 想改行為的話

不要改這裡。在**你自己的專案**建一個同名技能覆蓋它 —— 專案層級優先於個人層級。改了這裡，上游修 bug 你合不回來，而教材會同時對不上兩邊。

## 要更新到上游最新版

```bash
git clone --depth 1 https://github.com/Luca0x5755/luca-skills.git /tmp/luca-new
rm -rf .claude/skills/*/
for b in core draft; do
  for s in /tmp/luca-new/skills/$b/*/; do cp -r "$s" ".claude/skills/$(basename "$s")"; done
done
# 保留這個 README，更新上面的 commit 與日期
```

更新後**必須**重對 [`docs/SKILL-MAP.md`](../../docs/SKILL-MAP.md)：教材提到的每個技能還在不在、描述有沒有變、`disable-model-invocation` 有沒有增減。

## 沒有一起帶進來的東西

上游還有 hooks（`guard-git`、`guard-secrets`、`check-on-stop`）與它自己的 `.claude/settings.json`。**刻意沒帶** —— 那是為它自己的 repo 設計的，掛進來會多出這門課不需要的變數。要用的話去上游拿。

本 repo 的 Git 層防護在 [`.githooks/`](../../.githooks/)，與 agent 無關，兩者不衝突。
