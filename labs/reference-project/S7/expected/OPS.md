# 維運卡 — rate-digest

> 對照重點：**七格都填了**，特別是第 6 格的「不可回滾的操作」。
> 最狠的自我檢查：拿給同事看，問他「掛了你救得回來嗎」。他有任何問題要回頭問你 → 還沒寫完。

---

## 1. 這是什麼

每個工作日 08:50 抓三個網站的匯率，產出摘要寫進 `out/digest-YYYY-MM-DD.md`。
**壞掉的時候只有我一個人有感覺**（早上 09:00 打開檔案發現是舊的或空的）。

## 2. 長什麼樣

```
GitHub Actions cron (08:50 TW)
        │
        ▼
   fetch ×3 ──→ normalize ──→ validate ──→ SQLite (data/rates.db)
                                  │              │
                              不過就停            ▼
                                            out/digest-*.md
```

5 個節點。

## 3. 怎麼部署

```bash
git push origin main
# GitHub Actions 的 .github/workflows/daily.yml 會自動生效
```

手動觸發一次驗證：
```bash
gh workflow run daily.yml
gh run watch
```

預期看到：`Run completed with conclusion: success`
花多久：**2–4 分鐘**（含相依安裝）

## 4. 怎麼確認它活著

| 檢查 | 指令 | 正常的樣子 |
|---|---|---|
| **淺層**：workflow 有跑 | `gh run list --workflow=daily.yml --limit 3` | 最近一次 `completed success` |
| **深層**：真的有產出 | `ls -la out/ \| tail -3` | 今天日期的檔案存在且 > 200 bytes |
| **深層**：數字合理 | `head -5 out/digest-$(date +%F).md` | 匯率在 25–35 之間（USD/TWD 常態區間） |

> 只看第一條會出現「workflow 全綠但檔案是空的」。**深層檢查不能省。**

## 5. 壞了先看哪裡（依實際發生頻率）

1. **來源網站改版，selector 失效**（發生過 3 次）
   → 跑 `/check-sources`
   → 看哪個來源的 selector ❌
   → 更新 `config/sources.yaml`，跑 `pytest tests/test_fetchers.py`

2. **GitHub Actions 額度用完 / 排程沒觸發**（發生過 1 次）
   → `gh run list` 看最後一次執行時間
   → 超過 24 小時沒跑 → 手動 `gh workflow run daily.yml`

3. **來源網站限流（429）**（發生過 1 次）
   → 看 workflow log 的 `HTTP 429`
   → 把 retry 間隔從 2 秒調到 10 秒

4. **Validate 擋下但實際資料是對的**
   → 看 log 的 `Validate failed:` 那行
   → 通常是筆數變動觸發（例如新增幣別）
   → 確認後手動放行：`SKIP_COUNT_CHECK=1 python -m src.cli`

5. **程式本身的 bug**（還沒發生過）
   → 看 traceback，跑 `pytest`

## 6. 怎麼回滾

```bash
# 程式回滾
git revert <bad-commit> && git push origin main
```

回滾要多久：**3–5 分鐘**（下次排程或手動觸發後生效）
回滾會失去：無 —— 資料是每日獨立的，回滾程式不影響已寫入的歷史

**上次演練**：2026-07-30，耗時 3 分 40 秒 ✅

### ⚠️ 不可回滾的操作

| 操作 | 為什麼不可逆 | 怎麼降風險 |
|---|---|---|
| **`migrations/002_fix_delta_nullable.sql`** | 它 `DROP TABLE rates_old` —— **沒有 rollback script** | **執行前一定要 `cp data/rates.db data/rates.db.bak`** |
| 刪除 `data/rates.db` | 歷史匯率無法重新抓（來源只提供當日） | 每週備份到 `backups/` |
| 修改已寫入的歷史資料 | 沒有 audit log | 一律用新增修正列，不要 UPDATE |

> **第一條是這張卡最重要的資訊。** 未來的我（或接手的人）在跑 migration 前
> 一定要看到這行。

## 7. 什麼情況要找人

| 症狀 | 找誰 | 多急 |
|---|---|---|
| 連續 2 天沒產出 | 我自己 | 當天處理 |
| 匯率數字明顯離譜（< 20 或 > 40） | 我自己 | **立刻** —— 可能已經做了錯誤決策 |
| `data/rates.db` 損毀 | 我自己 + 從 `backups/` 還原 | **立刻** |

單人專案，沒有 oncall 輪值。**團隊使用時這格要改寫。**

---

## 自我檢查

| 問題 | ✅ / ❌ |
|---|---|
| 七格都填了？ | ✅ |
| 有「不可回滾的操作」那格？ | ✅ 三條 |
| 回滾**演練過**？ | ✅ 2026-07-30，3 分 40 秒 |
| 健康檢查有深層的？ | ✅ 三條裡兩條是深層 |
| 失敗模式依**實際頻率**排？ | ✅ 註明各自發生過幾次 |
| 指令都可以直接複製執行？ | ✅ 沒有 `<your-app>` 這種佔位符 |
| 一頁內？ | ✅ |
