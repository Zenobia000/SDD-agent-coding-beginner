# S0 開機

## 結論卡

| | |
|---|---|
| **做什麼** | 把 `claude` 裝起來、複製專案骨架、確認 hook 真的會動 |
| **為什麼** | 環境沒好，後面七站全部卡住 |
| **產出** | 能跑的 `claude` + `my-first-loop/` 目錄 |
| **下一步** | 跑 `/gate` 確認 S0 過關 |

**這一站是暖身，不跑四拍。**

---

## 課堂 15 分鐘版

**老師講**（5 分）：

1. 今天不教怎麼跟 AI 講話，教怎麼蓋一個**會收斂的迴圈**
2. 全天只有一個框架：**四拍**（劃邊界 → 放它跑 → 打分數 → 收判斷）
3. 每站結束打 `/gate`，它會告訴你過了沒——**不通過就別往前**

**學生做**（10 分）：跑下面「動手」的四步。

沒有 Claude Code 訂閱的人，老師此時指向 [`../docs/setup/02-free-routes.md`](../docs/setup/02-free-routes.md)，
助教一對一處理（**這是全天最容易塞車的地方，預留緩衝**）。

---

## 動手

1. 確認 `claude` 裝好了
   ```bash
   claude --version
   ```
   沒有這個指令 → 先跑 [`../docs/setup/01-claude-code.md`](../docs/setup/01-claude-code.md)

2. 複製骨架成你自己的專案
   ```bash
   cp -r templates/claude_project_template ~/my-first-loop && cd ~/my-first-loop
   ```

3. 設定 MCP（用不到的整段刪掉）
   ```bash
   cp .mcp.json.example .mcp.json
   ```

4. 啟動並確認載入
   ```bash
   claude
   ```
   進去後打 `/blocks` —— 應該看到 16 塊 skill 的清單。

5. 測一下 hook 真的會擋（**這步不要跳，這是全天第一個「機械層」的體感**）
   ```
   > 幫我跑 rm -rf /tmp/test
   ```
   應該被 `block-dangerous-bash.sh` 擋下並說明原因。

---

## 閘門

- [ ] `claude --version` 有輸出
- [ ] `~/my-first-loop/` 存在且裡面有 `.claude/` 目錄
- [ ] 在專案內打 `/blocks` 列得出 skill 清單
- [ ] 要求跑 `rm -rf` 時被 hook 擋下
- [ ] `.mcp.json` 存在（內容可以只留一個 server）

---

## 我做對了嗎

對照 [`../labs/reference-project/S0/expected/`](../labs/reference-project/S0/expected/)：

- `tree-output.txt` —— 你的目錄結構應該和它一致（檔案數可以差，`.claude/` 下的子目錄必須都在）
- `blocks-output.md` —— `/blocks` 應該列出同樣的 16 個 skill

差異在「少了某個目錄」→ 重跑動手第 2 步。
差異在「`/blocks` 沒反應」→ 檢查你是不是在 `my-first-loop/` 裡面開的 `claude`。

---

## 回家展開版

### 為什麼要複製骨架，不是從零開始

從零開始你會花 2 小時在設定上，而且會漏掉你不知道自己需要的東西（例如 secret 防護）。
**先用別人的、再改成自己的**，比從零長出來快得多——這也是 S5 要教的。

### `.claude/` 裡每個目錄在管什麼

| 目錄 | 管什麼 | 生效時機 |
|---|---|---|
| `rules/` | 硬約束 | 由 `CLAUDE.md` 引用後每次對話生效 |
| `skills/` | 可觸發的流程 | 打 `/name` 或 AI 依 description 自動載入 |
| `commands/` | 薄編排指令 | 打 `/name` |
| `agents/` | 獨立 context 的助手 | AI 判斷要派時 |
| `hooks/` | 機械層 | 特定事件發生時，**不受模型意願影響** |
| `output-styles/` | 講話的形狀 | 用 `/config` 切換，session 啟動時載入 |

**最重要的觀念**：前五個都是「請 AI 遵守」，只有 `hooks/` 是「AI 沒得選」。
規則寫進文件約有 ~70% 順從率——不可逆的操作不能賭那 30%。

### 三條免費路線的取捨

| 路線 | 適合 | 代價 |
|---|---|---|
| 官方訂閱 | 有預算 | 最穩，功能完整 |
| cc-switch / claude-code-router | 想接自己的 API key 或第三方模型 | 設定較繁；部分功能行為可能不同 |
| omnirouter 類聚合服務 | 完全沒預算 | 速度與穩定性看服務商 |

細節與實測狀態 → [`../docs/setup/02-free-routes.md`](../docs/setup/02-free-routes.md)

### 進度狀態檔

`.claude/.station` 記錄你在第幾站。`inject-station.sh` 會把它注入每一輪對話，
讓你和 AI 都不會忘記現在在做什麼。

```bash
cat .claude/.station     # 看目前狀態
echo "S1 beat1" > .claude/.station   # 手動改（通常 /gate 會自動更新）
```

---

## 下一步

打 `/gate`。通過後打開 [`S1-frame.md`](./S1-frame.md)。
