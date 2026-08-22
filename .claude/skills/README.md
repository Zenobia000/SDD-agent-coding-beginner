# 這個專案的工具鏈

36 個給 coding agent 用的工程技能。**fork 下來打開 Claude Code 就能用**，不需要安裝任何東西。

Claude Code 會自動載入專案的 `.claude/skills/`，GitHub Copilot 也讀同一個路徑。

```text
.claude/skills/<技能名>/SKILL.md
```

不確定該用哪個 → 打 **`/compass`**。

---

## 這些技能可以改

**這是本專案的工具鏈，不是唯讀的外部依賴。** 發現某個技能的流程不適合這門課，就改它 —— 那正是 `/writing-for-agents` 存在的理由。

改的時候記得三件事：

1. **`docs/SKILL-MAP.md` 和 `compass/SKILL.md` 都要同步。** 教材靠那兩張表指路，改了技能沒改表，學生會照著找不到的東西操作 —— 使用者觸發的技能更嚴重，它沒有 description 在模型 context 裡，表沒提到就只剩人的記憶能觸發它。
2. **frontmatter 前不能有任何字元**，包括空行。多一個空行，Claude Code 會靜默略過整個技能，而且不會告訴你。
3. **`name` 必須等於資料夾名。**

**這三條壞掉的時候都不會噴錯**，所以三條都有腳本擋。改完跑：

```bash
bash scripts/check-links.sh      # 死連結
bash scripts/check-skill-map.sh  # 漏路由、死路由、壞 frontmatter
```

兩支都是無輸出 = 全部有效，有問題才印，並 exit 1。

---

## 兩類技能，差別只有誰能叫它

| | 誰能叫 | 用途 | 例子 |
|---|---|---|---|
| **使用者觸發**（frontmatter 有 `disable-model-invocation: true`） | 只有你打字 | 編排流程 | `/to-spec`、`/to-tickets`、`/implement`、`/triage` |
| **模型觸發**（沒有那個欄位） | 你和 agent 都能叫 | 可重複使用的紀律 | `/tdd`、`/code-review`、`/grilling`、`/diagnosing-bugs` |

> ⚠️ **GitHub Copilot 與 Google Antigravity 都不支援 `disable-model-invocation`。**
> 在那兩邊，編排型技能會被 agent 自行啟動。緩解的是這些技能的 `description` 本來就寫成
> 不帶觸發語的人話摘要，但那是降低機率，不是關掉開關。

---

## 附帶的 guard hooks

`setup-skills/hooks/` 有三支 shell hook，由 `/setup-skills` 複製進**你自己的專案**（不是這個教材 repo）：

| Hook | 擋什麼 |
|---|---|
| `guard-git.sh` | `git add -A`／`git add .`、force push、越過 HEAD 的 `git reset --hard`、`--no-verify`、PR merge（merge 是你的按鈕） |
| `guard-secrets.sh` | staged diff 裡出現憑證字面值時擋下 `git commit` |
| `check-on-stop.sh` | 停止時的檢查 |

每支都有自帶測試（`test-*.sh`），本 repo 驗過三支全 pass。

**為什麼要 hook 而不是寫在 `CLAUDE.md`**：散文規則大約只有七成遵守率，這幾條紅線靠 exit code 2，不靠模型記得。這正是心法篇不變量 5「邊界是防線，不是建議」。

---

## 出處與授權

這套技能衍生自 [Luca0x5755/luca-skills](https://github.com/Luca0x5755/luca-skills)（MIT），取自 commit `1434be8`（2026-08-12）。

**本專案做過的修改**：

- 攤平目錄結構（上游分 `skills/core/` 與 `skills/draft/` 兩桶，靠安裝腳本連結時才攤平；這裡直接放好）
- `ask-luca` 改名為 `compass`
- 範例中的人名與執行代號改為中性佔位符
- `setup-skills` 的 Section E 改為從技能自己的 `hooks/` 取檔（原本要從上游 repo 的 symlink target 解析路徑，在複製而非連結的情況下解不出來）
- guard hooks 隨 `setup-skills` 一起打包
- 流程圖改繪為本課的站點劃分

完整授權聲明見 [`THIRD-PARTY-NOTICES.md`](../../THIRD-PARTY-NOTICES.md)。**那份聲明是 MIT 的要求，不要移除。**

### 想同步上游的修正

上游是活的，會修 bug 也會加技能。要跟進的話自己 diff：

```bash
git clone --depth 1 https://github.com/Luca0x5755/luca-skills.git /tmp/upstream
diff -ru /tmp/upstream/skills/core .claude/skills 2>/dev/null | less
diff -ru /tmp/upstream/skills/draft .claude/skills 2>/dev/null | less
```

已經分岔了，所以不會是無痛合併 —— 挑你要的改動手動搬過來，並更新 `docs/SKILL-MAP.md`。
