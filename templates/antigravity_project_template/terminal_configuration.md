# Terminal 工作站初始化指南

> 給「VS Code 為主、MobaXterm 為輔」的 AI 協作開發者

---

## TL;DR

- **VS Code = 駕駛艙**：Claude Code、Git、Editor、Build 全在這裡
- **MobaXterm = 儀表板**：3 格搞定，用 **RUN / WATCH / CHECK** 三角色設計
- **不要把格子綁功能**（前端 log / 後端 log / GPU），要綁角色（執行 / 觀測 / 驗證）

---

## 一、分工原則（記這個就好）

| 工具 | 角色 | 負責 |
|------|------|------|
| **VS Code** | 開發腦 | Claude Code、寫 code、git diff、commit、test |
| **UI Tools** | 資料眼睛 | DBeaver、Postman、MLflow、Docker Desktop |
| **MobaXterm** | 實驗手腳 | 啟動服務、跑任務、看 log、快速驗證 |
| **Claude Code** | 副駕駛 | 產出 / 修錯 / 規劃 |

**鐵律**：MobaXterm 不跟 VS Code 搶主控。它只做一件事 — **讓你看見系統真相**。

---

## 二、MobaXterm 3 格初始化（黃金配置）

```
┌──────────────────────────────┬──────────────────────────────┐
│  1. RUN                       │  2. WATCH                     │
│  當前主任務                    │  系統長 log / 錯誤觀測          │
├──────────────────────────────┴──────────────────────────────┤
│  3. CHECK                                                     │
│  GPU / 測試 / curl / 輸出驗證                                  │
└───────────────────────────────────────────────────────────────┘
```

### 三格各放什麼

| 格 | 角色 | 常用指令 |
|----|------|----------|
| **RUN** | 我正在跑什麼 | `npm run dev` / `uvicorn ...` / `make train` / `make pipeline` |
| **WATCH** | 有沒有噴錯 | `docker compose logs -f` / `tail -f logs/app.log` |
| **CHECK** | 結果對不對 | `nvidia-smi` / `curl /health` / `pytest` / `ls outputs/` |

---

## 三、依任務切換內容（layout 不變）

| 當下任務 | RUN | WATCH | CHECK |
|----------|-----|-------|-------|
| 全端開發 | `npm run dev` | backend log | `curl /health` |
| 後端 API | `uvicorn` | docker DB log | `pytest` |
| 模型訓練 | `make train` | `tail training.log` | `nvidia-smi` |
| RAG indexing | `make index` | vector DB log | query check |
| Docker 多服務 | main app | `docker compose logs -f` | `docker compose ps` |
| TDD | dev server | app logs | test watcher |

---

## 四、4 格升級版（多服務 / Agent / RAG）

當專案有 Docker + DB + n8n + Vector DB，升級成 4 格：

```
┌──────────────────────────────┬──────────────────────────────┐
│  1. ENV  環境啟動              │  2. RUN  任務執行              │
│  docker compose ps / up        │  make train / pipeline         │
├──────────────────────────────┼──────────────────────────────┤
│  3. WATCH  日誌觀測            │  4. CHECK  驗證測試            │
│  docker logs -f / tail         │  curl / nvidia-smi / pytest    │
└──────────────────────────────┴──────────────────────────────┘
```

口訣：**ENV → RUN → WATCH → CHECK**（小型 DSOps 循環）

---

## 五、為什麼這樣設計？

### 1. 不要把 Claude Code 放 MobaXterm
Claude 改 code → 你要立即在 VS Code 看 diff、開檔案、搜 symbol。放 MobaXterm 是繞遠路。

### 2. 不要把 Git 主控放 MobaXterm
VS Code Source Control 可視覺化 diff、逐段 stage、看 conflict。Terminal 跑 `git status` 是輔助，不是主場。

### 3. 不要把 DB CMD 當主力
資料庫複雜操作用 **DBeaver / TablePlus / pgAdmin**。CMD 只在三種情境用：
- 快速連線檢查（`pg_isready`）
- CI/CD 自動化（`psql -f migration.sql`）
- 貼錯誤給 AI 重現（`psql -c "SELECT ..."`）

### 4. Terminal 在 AI 協作下反而最簡單
- 指令可精準複製貼給 AI
- 天然就是 SOP（明天、同事都能重跑）
- 視覺雜訊少，錯誤訊息清楚

---

## 六、Makefile 封裝（降低門檻）

不要逼資料科學家記長指令。包成 Makefile：

```makefile
.PHONY: env run train eval logs check

env:
	docker compose ps
	python --version

run:
	python pipelines/run.py

train:
	python scripts/train.py --config configs/train.yaml

logs:
	tail -f logs/app.log

check:
	curl http://localhost:8000/health
	python -c "import torch; print('cuda:', torch.cuda.is_available())"
```

MobaXterm 三格就變成三個按鈕：`make run` / `make logs` / `make check`。

---

## 七、命名 MobaXterm Tab

切換時不用重新理解現在在哪：

```
[RUN]    當前任務
[WATCH]  系統日誌
[CHECK]  驗證資源
```

或 4 格版：

```
[ENV] [RUN] [WATCH] [CHECK]
```

---

## 八、決策樹（初始化時用）

```
我是不是 VS Code 為主？
  └─ 是 → MobaXterm 不放 Claude Code / Git 主控
       └─ 我做什麼類型？
            ├─ 全端 Web → 3 格 RUN/WATCH/CHECK
            ├─ 模型訓練 → 3 格，CHECK 固定 nvidia-smi
            ├─ Docker 多服務 → 升 4 格加 ENV
            └─ TDD → CHECK 固定 test watcher
```

---

## 九、三句口訣

> **VS Code 寫與控**
> **MobaXterm 看與測**
> **Claude Code 產出，人類驗收**

延伸版：

> **RUN 跑任務 → WATCH 看錯誤 → CHECK 驗結果**

---

## 十、一鍵啟動範本（跨 Mac / Linux / WSL / Windows）

不要每次都手動 `cd` + 開分割視窗。範本已包進 **`templates/antigravity_project_template/`**，學生複製整個資料夾時自動帶走：

```
templates/antigravity_project_template/
├── .workstation/
│   ├── layout.kdl       # 3 格 zellij layout (RUN / WATCH / CHECK)
│   ├── layout-4.kdl     # 4 格 (ENV / RUN / WATCH / CHECK)
│   └── README.md        # 完整安裝與使用說明
├── start                # Mac / Linux / WSL 啟動腳本
├── start.ps1            # Windows 原生啟動（自動跳 WSL）
└── start.bat            # Windows 雙擊版（包 PowerShell bypass）
```

**用法**（學生複製 template 並改名為自己的專案後）：
- Mac / Linux / WSL：`./start`（或 `./start 4`）
- Windows：雙擊 `start.bat`

**設計**：用 **zellij** 當 layout 抽象層，設定跨平台共用；Windows 啟動腳本自動偵測並進 WSL。

詳細安裝、自訂方式 → 見 [`templates/antigravity_project_template/.workstation/README.md`](templates/antigravity_project_template/.workstation/README.md)

---

## 附錄：什麼時候才需要升到 6 / 8 格？

**不要急著升。** 沒穩定駕馭 4 格之前，8 格只會讓你看不到重點。

- **4 格**：一般 side project / Docker Compose / n8n
- **6 格**：全端 + AI Agent + RAG + 多服務 POC
- **8 格**：類 DevOps 工作站（worker、queue、Redis monitor 全開）

升級條件：**現有格子的內容開始打架時**，再加格子。
