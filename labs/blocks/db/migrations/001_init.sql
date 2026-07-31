-- 001_init.sql —— 這張表預先擋掉五個最常見的 schema 錯誤
--
-- ① 什麼都 nullable       → 只有真的可空的才 nullable
-- ② 沒有 created_at       → 一定要有，而且用 UTC
-- ③ 用浮點數存錢          → 用整數存最小單位（見 db.py 的 SCALE）
-- ④ 硬刪除                → 用 deleted_at 軟刪除
-- ⑤ 沒有唯一約束          → 該唯一的在 DB 層加 UNIQUE，不靠應用層防

CREATE TABLE IF NOT EXISTS rates (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,

    run_date    TEXT    NOT NULL,   -- ISO 日期 YYYY-MM-DD
    currency    TEXT    NOT NULL,   -- ISO 4217，例 USD
    rate        INTEGER NOT NULL,   -- ③ 整數存最小單位，不是 REAL

    -- 這欄可空是刻意的：首次執行時沒有「昨日」可比。
    -- 不確定要不要 NOT NULL 時先設 NOT NULL —— 之後放寬比收緊容易。
    -- 這欄是有 spec 依據才放寬的（PRD Constraints）。
    delta_1d    INTEGER,

    source      TEXT    NOT NULL,

    created_at  TEXT    NOT NULL,   -- ② UTC ISO8601
    deleted_at  TEXT,               -- ④ 軟刪除；NULL = 還在

    -- ⑤ 同一天同一幣別只能有一筆 —— 這是冪等性的保證來源
    UNIQUE (run_date, currency)
);

-- 索引對應實際查詢：get_rates() 用 run_date 撈
CREATE INDEX IF NOT EXISTS idx_rates_run_date ON rates (run_date);
