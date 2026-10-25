"""Instructor's deterministic rehearsal. Run only in a new isolated git worktree.

Builds local cp1..cp5 refs; never publishes or overwrites an existing ref.
This is a worked reference, not evidence that every model finishes in class time.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import json
import os
import subprocess
import sys

ap=argparse.ArgumentParser()
ap.add_argument('--worktree',type=Path,required=True)
ap.add_argument('--python',type=Path,required=True)
args=ap.parse_args()
root=args.worktree.resolve()
if not (root/'.git').is_file():raise SystemExit('Use an isolated git worktree, not the student main checkout.')
def run(argv,expected=0):
 r=subprocess.run([str(a) for a in argv],cwd=root,text=True,encoding='utf-8',errors='replace',stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 if r.returncode!=expected:raise RuntimeError(' '.join(map(str,argv))+'\n'+r.stdout)
 return r.stdout
for ref in ['cp1-requirements','cp2-design','cp3-tests','cp4-working-feature','cp5-delivered']:
 if subprocess.run(['git','show-ref','--verify','--quiet','refs/heads/'+ref],cwd=root).returncode==0:raise SystemExit('Ref already exists: '+ref)
if run(['git','status','--porcelain']).strip():raise SystemExit('Rehearsal worktree must be clean.')
base=run(['git','rev-parse','HEAD']).strip()
def put(path,text):
 p=root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.strip()+'\n',encoding='utf-8')
def checkpoint(ref,scope,evidence,paths):
 put('course/CHECKPOINT-RECEIPT.md',f'''# {ref}：講師參考快照

課程版本2026.10-unified-1；教材基底 `{base}`。建立時間 {datetime.now(timezone.utc).isoformat()}。
這是一組講師明確選定的決策與參考實作，不代表所有Agent都能在同樣時間產出。

## 可接續內容
{scope}

## 實際證據
```text
{evidence.strip()}
```

測試在本機Python3.12的隔離venv執行；原始結果只證明所列案例，不代表已做所有平台／Agent的互動彩排。查閱課程CHECKPOINTS後再接續。
''')
 run(['git','add',*paths,'course/CHECKPOINT-RECEIPT.md'])
 run(['git','commit','-m',f'demo({ref}): {scope}'])
 run(['git','branch',ref])
 print(ref+': '+run(['git','rev-parse','--short','HEAD']).strip(),flush=True)

put('docs/01-brief.md','''# 01 Brief — LeaveBot講師參考
虛構公司用訊息收假單，員工無法確認登記。這是課堂假設。
| 編號 | 目標 | 如何驗證 |
|---|---|---|
| G-01 | 員工知道請假已登記 | 成功送出後及重新整理可見pending假單 |
| NG-01 | 不做主管、額度、LLM、登入 | 一天先完成表單切片 |
已定決策：理由選填最多200個Unicode字元；接受過去日期；不自動去重，送出期間鎖按鈕；半天只限單日工作日。
''')
put('docs/02-prd.md','''# 02 PRD — LeaveBot講師參考
主要使用者為員工，先選自己、填表、送出，再查看自己的假單。
### US-01 送出請假（G-01）
- **AC-01.1** Given 有效員工與工作日 When 送出合法表單 Then 存成pending並顯示程式計算的天數。
- **AC-01.2** Given 必填缺漏或日期反向 When 送出 Then 顯示錯誤且不存檔。
- **AC-01.3** Given 週末或跨日半天 When 送出 Then 依規則計天數或拒絕，零工作日不存檔。
- **AC-01.4** Given 超過200字的理由 When 送出 Then 拒絕且不存檔；空白理由可用。
- **AC-01.5** Given 客戶端指定狀態或天數 When 送出 Then 拒絕，不允許自行核准。
### US-02 查看自己的假單（G-01）
- **AC-02.1** Given 已有假單 When 重新整理或切換員工 Then 可見所選員工的持久資料，其他員工的資料不混入。
不做主管、額度、LLM、登入。理由當純文字，提交期間鎖按鈕。
''')
put('docs/03-srs.md','''# 03 SRS — LeaveBot講師參考
| 編號 | 行為 | 來源 |
|---|---|---|
| FR-01 | 合法輸入存成pending，天數由程式算 | AC-01.1 |
| FR-02 | 缺欄位、非法值、反向日期、無員工時拒絕且不存檔 | AC-01.2 |
| FR-03 | 起迄皆包含，僅週一至週五，半天只限單日工作日，零工作日拒絕 | AC-01.3 |
| FR-04 | 理由選填，最多200個Unicode字元 | AC-01.4 |
| FR-05 | 客戶端不能指定天數與狀態 | AC-01.5 |
| FR-06 | 假單以員工隔離，重啟後資料可見 | AC-02.1 |
| NFR-01 | 理由以純文字呈現，不執行HTML | US-01 |
| NFR-02 | 測試使用隔離資料庫 | 課程規則 |
接受過去日期，不做額度與國定假日。重複送出可建立另一筆，送出期間按鈕禁用。
流程圖在下一階段建立。
''')
checkpoint('cp1-requirements','Brief、PRD與SRS已確認；接卡D、E','Reviewed fixed classroom decisions; no app or test success claimed.',['docs'])

put('docs/04-sad.md','''# 04 SAD — 最小架構
```mermaid
flowchart LR
    B[HTML/CSS/JavaScript] -->|同來源API| A[FastAPI]
    A --> V[格式與日期驗證]
    V --> D[(SQLite)]
```
前端顯示、後端驗證與存檔、rules算天數。資料庫接縫由create_app(database_path)注入。
沿用STACK，沒有額外技術選型。API錯誤不新增資料；畫面保留錯誤訊息。
''')
put('docs/05-sds.md','''# 05 SDS — API與資料
| API | 用途 | 回應／錯誤 | 來源 |
|---|---|---|---|
| API-01 GET /api/health | 骨架 | 200 ok | 骨架 |
| API-02 GET /api/employees | 員工選單 | 200 id/name列表 | FR-02 |
| API-03 POST /api/leaves | 送出employee_id/leave_type/start_date/end_date/period/reason | 201假單；422驗證錯誤 | FR-01至05 |
| API-04 GET /api/leaves?employee_id=1 | 個人假單 | 200列表；404未知員工 | FR-06 |
employees(id整數主鍵,name文字)；leaves(id主鍵,employee_id外鍵,leave_type,start_date,end_date,period,reason,days實數,status固定pending)。
假別annual/personal/sick；時段full/am/pm。每次連線開foreign_keys，contextmanager確保關閉。
create_app(database_path=None)先讀LEAVEBOT_DB，測試傳tmp_path。rules.leave_days(start,end,period)為公開計算接縫。
UI-01同頁表單與我的假單，用相對/api、textContent呈現資料；送出期間鎖按鈕，切員工重新查列表。
''')
put('docs/06-test-plan.md','''# 06 Test Plan — 代表案例
| TC | 需求 | 情境 | 預期 |
|---|---|---|---|
| TC-01 | AC-01.1 FR-01 | 合法一天 | 201 pending 1天 |
| TC-02 | AC-01.2 FR-02 | 缺假別 | 422且筆數不變 |
| TC-03 | AC-01.2 FR-02 | 反向日期 | 422且不存檔 |
| TC-04 | AC-01.3 FR-03 | 跨週末、單日半天、非法半天、全週末 | 天數正確或拒絕 |
| TC-05 | AC-01.4 FR-04 | 201字理由 | 拒絕且不存檔 |
| TC-06 | AC-01.5 FR-05 | 自帶approved或days | 拒絕且不存檔 |
| TC-07 | AC-02.1 FR-06 | 切員工、重開app | 持久且資料隔離 |
| TC-08 | AC-01.2 FR-02 | 非法員工／假別／時段 | 拒絕且不存檔 |
| TC-09 | NFR-01 | 理由有HTML字串 | 當文字顯示 |
退出：pytest綠；瀏覽器成功、拒絕、刷新與換員工有證據。不跑LLM eval。
追溯證據：未實作，等各票結束更新。
''')
put('docs/LESSONS.md','# 經驗\n\n先確認開場、課程檔案與日期規則。未實作先不宣稱測試通過。')
put('issues/000-skeleton.md','''# 000 骨架
依course/STACK.md生成pyproject、FastAPI、靜態頁與health測試。完成時首頁可見health，pytest綠，停後可重啟。無業務邏輯。依賴：docs/04、05。
''')
put('issues/001-submit-leave.md','''# 001 可驗收的表單切片
依docs/02至06，完成API-02至04、UI-01及rules.leave_days。逐個TC01至09做TDD，第一個業務紅燈先給人確認。完成後pytest綠、瀏覽器操作、追溯與LESSONS更新。依賴000。
''')
candidate={'schema_version':2,'diagram_type':'workflow','meta':{'title':'請假表單：送出、驗證與結果','locale':'zh-TW','quality_profile':'showcase','output':'diagrams/submit-leave.html'},'lanes':[{'id':'employee','label':'員工操作'},{'id':'server','label':'後端與儲存'},{'id':'error','label':'錯誤回饋','variant':'exception'}],'mainPath':['select','form','validate','save','list'],'nodes':[{'id':'select','lane':'employee','col':0,'type':'external','label':'選員工'},{'id':'form','lane':'employee','col':1,'type':'frontend','label':'填表送出'},{'id':'validate','lane':'server','col':2,'type':'security','label':'驗證欄位與日期'},{'id':'save','lane':'server','col':3,'type':'database','label':'存成待審核'},{'id':'list','lane':'employee','col':4,'type':'frontend','label':'我的假單'},{'id':'reject','lane':'error','col':3,'type':'security','label':'錯誤且不存檔'}],'edges':[{'from':'select','to':'form'},{'from':'form','to':'validate'},{'from':'validate','to':'save','label':'有效'},{'from':'save','to':'list'},{'from':'validate','to':'reject','label':'無效','variant':'security'}]}
put('diagrams/submit-leave.workflow.json',json.dumps(candidate,ensure_ascii=False,indent=2))
diagram=run(['node','.claude/skills/archify/bin/archify.mjs','finalize','workflow','diagrams/submit-leave.workflow.json','diagrams/submit-leave.html','--browser-check','--json'])
put('diagrams/archify-run.txt',diagram)
checkpoint('cp2-design','設計、流程圖、測試案例與兩張票；接卡H骨架',diagram,['docs','issues','diagrams'])

put('pyproject.toml','''[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"
[project]
name = "leavebot-classroom"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["fastapi", "uvicorn", "httpx"]
[project.optional-dependencies]
dev = ["pytest"]
[tool.setuptools]
package-dir = {"" = "backend"}
[tool.setuptools.packages.find]
where = ["backend"]
[tool.setuptools.package-data]
app = ["static/*"]
[tool.pytest.ini_options]
testpaths = ["backend/tests"]
pythonpath = ["backend"]
addopts = "--import-mode=importlib"
markers = ["req(*ids): classroom requirement and TC identifiers"]
''')
put('backend/app/__init__.py','')
put('backend/app/main.py','''from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
def create_app(database_path=None):
    app = FastAPI()
    @app.get('/api/health')
    def health(): return {'status':'ok'}
    app.mount('/', StaticFiles(directory=Path(__file__).parent/'static',html=True), name='static')
    return app
app=create_app()
''')
put('backend/app/static/index.html','''<!doctype html><html lang="zh-Hant-TW"><meta charset="utf-8"><title>LeaveBot骨架</title><h1>LeaveBot骨架</h1><p id="health">連線中</p><script src="/app.js"></script></html>''')
put('backend/app/static/app.js',"fetch('/api/health').then(r=>r.json()).then(d=>document.querySelector('#health').textContent=d.status);")
put('backend/app/static/style.css','body { font-family: sans-serif; }')
put('backend/tests/acceptance/test_health.py','''from fastapi.testclient import TestClient
from app.main import create_app
def test_health():
    with TestClient(create_app()) as c:
        assert c.get('/api/health').json()=={'status':'ok'}
''')
run([args.python,'-m','venv','.venv'])
py=root/'.venv/Scripts/python.exe' if os.name=='nt' else root/'.venv/bin/python'
install=[py,'-m','pip','install']
if (root/'course/constraints.txt').exists():install+=['-c','course/constraints.txt']
run(install+['-e','.[dev]'])
green=run([py,'-m','pytest','-q'])
put('backend/tests/acceptance/test_leaves.py','''import pytest
from fastapi.testclient import TestClient
from app.main import create_app
@pytest.fixture
def client(tmp_path):
    with TestClient(create_app(tmp_path/'test.db')) as c: yield c
def valid(**updates):
    data=dict(employee_id=1,leave_type='annual',start_date='2026-10-20',end_date='2026-10-20',period='full',reason='休息一天')
    data.update(updates);return data
@pytest.mark.req('TC-01','AC-01.1','FR-01')
def test_submit_valid_leave_is_pending(client):
    r=client.post('/api/leaves',json=valid())
    assert r.status_code==201
    assert r.json()['status']=='pending'
    assert r.json()['days']==1
''')
red=run([py,'-m','pytest','-q'],expected=1)
checkpoint('cp3-tests','骨架綠、第一個業務測試預期紅；接卡H逐個綠燈',green+'\nEXPECTED RED:\n'+red,['pyproject.toml','backend'])

put('backend/app/rules.py','''from datetime import date, timedelta
def leave_days(start: date,end: date,period: str)->float:
    if end<start: raise ValueError('結束日期不得早於開始日期')
    if period not in {'full','am','pm'}: raise ValueError('時段不合法')
    if period!='full' and start!=end: raise ValueError('半天假只接受單日')
    days=sum((start+timedelta(days=i)).weekday()<5 for i in range((end-start).days+1))
    if days==0: raise ValueError('請選擇工作日')
    return float(days) if period=='full' else 0.5
''')
put('backend/app/main.py','''from contextlib import asynccontextmanager, contextmanager
from datetime import date
from pathlib import Path
import os, re, sqlite3
from fastapi import Body, FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from .rules import leave_days

REASON_MAX=200
@contextmanager
def connect(path):
    c=sqlite3.connect(path);c.row_factory=sqlite3.Row;c.execute('PRAGMA foreign_keys=ON')
    try:
        yield c
        c.commit()
    except Exception:
        c.rollback();raise
    finally: c.close()

def create_app(database_path=None):
    path=Path(database_path or os.getenv('LEAVEBOT_DB','backend/data/leavebot.db'))
    @asynccontextmanager
    async def lifespan(app):
        path.parent.mkdir(parents=True,exist_ok=True)
        with connect(path) as c:
            c.executescript("""CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY,name TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS leaves(id INTEGER PRIMARY KEY,employee_id INTEGER NOT NULL REFERENCES employees(id),leave_type TEXT NOT NULL,start_date TEXT NOT NULL,end_date TEXT NOT NULL,period TEXT NOT NULL,reason TEXT NOT NULL,days REAL NOT NULL,status TEXT NOT NULL CHECK(status='pending'));""")
            c.executemany('INSERT OR IGNORE INTO employees VALUES(?,?)',[(1,'小安'),(2,'小晴')])
        yield
    app=FastAPI(lifespan=lifespan)
    @app.get('/api/health')
    def health(): return {'status':'ok'}
    @app.get('/api/employees')
    def employees():
        with connect(path) as c:return [dict(r) for r in c.execute('SELECT id,name FROM employees ORDER BY id')]
    @app.get('/api/leaves')
    def leaves(employee_id:int):
        with connect(path) as c:
            if not c.execute('SELECT id FROM employees WHERE id=?',(employee_id,)).fetchone():raise HTTPException(404,'找不到員工')
            return [dict(r) for r in c.execute('SELECT * FROM leaves WHERE employee_id=? ORDER BY id DESC',(employee_id,))]
    @app.post('/api/leaves',status_code=201)
    def submit(body:dict=Body(...)):
        required={'employee_id','leave_type','start_date','end_date','period'}
        if not required.issubset(body) or set(body)-required-{'reason'}:raise HTTPException(422,'欄位缺漏或含不允許欄位')
        if type(body['employee_id']) is not int or body['leave_type'] not in ['annual','personal','sick'] or body['period'] not in ['full','am','pm']:raise HTTPException(422,'員工、假別或時段不合法')
        reason=body.get('reason','')
        if not isinstance(reason,str) or len(reason)>REASON_MAX:raise HTTPException(422,f'理由最多{REASON_MAX}字')
        try:
            if any(not isinstance(body[k],str) or not re.fullmatch(r'\\d{4}-\\d{2}-\\d{2}',body[k]) for k in ['start_date','end_date']):raise ValueError('請使用YYYY-MM-DD日期')
            start=date.fromisoformat(body['start_date']);end=date.fromisoformat(body['end_date'])
            days=leave_days(start,end,body['period'])
        except ValueError as e:raise HTTPException(422,str(e)) from e
        with connect(path) as c:
            if not c.execute('SELECT id FROM employees WHERE id=?',(body['employee_id'],)).fetchone():raise HTTPException(422,'找不到員工')
            cur=c.execute('INSERT INTO leaves(employee_id,leave_type,start_date,end_date,period,reason,days,status) VALUES(?,?,?,?,?,?,?,?)',(body['employee_id'],body['leave_type'],body['start_date'],body['end_date'],body['period'],reason,days,'pending'))
            return dict(c.execute('SELECT * FROM leaves WHERE id=?',(cur.lastrowid,)).fetchone())
    app.mount('/',StaticFiles(directory=Path(__file__).parent/'static',html=True),name='static')
    return app
app=create_app()
''')
f=root/'backend/tests/acceptance/test_leaves.py'
put('backend/tests/acceptance/test_leaves.py',f.read_text(encoding='utf-8')+'''
def count(client):return len(client.get('/api/leaves?employee_id=1').json())
@pytest.mark.req('TC-02','AC-01.2','FR-02')
def test_required_field_rejected_without_save(client):
    d=valid();d.pop('leave_type');before=count(client)
    assert client.post('/api/leaves',json=d).status_code==422
    assert count(client)==before
@pytest.mark.req('TC-03','AC-01.2','FR-02')
def test_reverse_date_rejected_without_save(client):
    assert client.post('/api/leaves',json=valid(end_date='2026-10-19')).status_code==422
    assert count(client)==0
@pytest.mark.req('TC-05','AC-01.4','FR-04')
def test_long_reason_rejected_without_save(client):
    assert client.post('/api/leaves',json=valid(reason='字'*201)).status_code==422
    assert count(client)==0
@pytest.mark.req('TC-06','AC-01.5','FR-05')
@pytest.mark.parametrize('extra',[{'status':'approved'},{'days':99}])
def test_client_cannot_set_trusted_values(client,extra):
    assert client.post('/api/leaves',json=valid(**extra)).status_code==422
    assert count(client)==0
@pytest.mark.req('TC-07','AC-02.1','FR-06')
def test_employees_do_not_mix(client):
    client.post('/api/leaves',json=valid())
    assert len(client.get('/api/leaves?employee_id=1').json())==1
    assert client.get('/api/leaves?employee_id=2').json()==[]
@pytest.mark.req('TC-07','AC-02.1','FR-06')
def test_data_persists_across_app_restart(tmp_path):
    path=tmp_path/'persist.db'
    with TestClient(create_app(path)) as c:assert c.post('/api/leaves',json=valid()).status_code==201
    with TestClient(create_app(path)) as c:assert len(c.get('/api/leaves?employee_id=1').json())==1
@pytest.mark.req('TC-08','AC-01.2','FR-02')
@pytest.mark.parametrize('changes',[{'employee_id':99},{'leave_type':'unknown'},{'period':'unknown'},{'start_date':'bad'}])
def test_invalid_values_do_not_save(client,changes):
    assert client.post('/api/leaves',json=valid(**changes)).status_code==422
    assert count(client)==0
''')
put('backend/tests/unit/test_rules.py','''from datetime import date
import pytest
from app.rules import leave_days
@pytest.mark.req('TC-04','AC-01.3','FR-03')
@pytest.mark.parametrize('start,end,period,expected',[('2026-10-23','2026-10-26','full',2),('2026-10-20','2026-10-20','am',.5),('2026-10-20','2026-10-20','pm',.5)])
def test_workdays_and_half_day(start,end,period,expected):
    assert leave_days(date.fromisoformat(start),date.fromisoformat(end),period)==expected
@pytest.mark.req('TC-04','AC-01.3','FR-03')
@pytest.mark.parametrize('start,end,period',[('2026-10-24','2026-10-25','full'),('2026-10-20','2026-10-21','am'),('2026-10-24','2026-10-24','pm')])
def test_invalid_day_ranges(start,end,period):
    with pytest.raises(ValueError):leave_days(date.fromisoformat(start),date.fromisoformat(end),period)
''')
put('backend/app/static/index.html','''<!doctype html><html lang="zh-Hant-TW"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>LeaveBot請假</title><link rel="stylesheet" href="/style.css"></head><body><main><h1>請假登記</h1><p>送出後即可查看自己的待審核假單。</p><form id="leave-form"><label>員工<select name="employee_id" id="employee" required></select></label><label>假別<select name="leave_type"><option value="annual">特休</option><option value="personal">事假</option><option value="sick">病假</option></select></label><label>開始日期<input type="date" name="start_date" required></label><label>結束日期<input type="date" name="end_date" required></label><label>時段<select name="period"><option value="full">整天</option><option value="am">上午</option><option value="pm">下午</option></select></label><label>理由（選填，最多200字）<textarea name="reason" maxlength="200"></textarea></label><button type="submit">送出請假</button></form><p id="message" role="status" aria-live="polite"></p><h2>我的假單</h2><ul id="leaves"></ul></main><script src="/app.js"></script></body></html>''')
put('backend/app/static/style.css','''body{font:17px/1.7 system-ui,sans-serif;background:#f2eee8;color:#343b36;margin:0}main{max-width:720px;margin:40px auto;padding:24px}form{display:grid;grid-template-columns:1fr 1fr;gap:16px}label{display:flex;flex-direction:column;gap:6px}input,select,textarea,button{font:inherit;padding:10px;border:1px solid #aaa;border-radius:6px}button{background:#405b49;color:white;cursor:pointer}button:disabled{opacity:.6;cursor:wait}#message{min-height:2em}li{margin-bottom:12px;overflow-wrap:anywhere}:focus-visible{outline:3px solid #405b49;outline-offset:3px}@media(max-width:540px){main{margin:0;padding:20px}form{grid-template-columns:1fr}}''')
put('backend/app/static/app.js','''const form=document.querySelector('#leave-form'),employee=document.querySelector('#employee'),message=document.querySelector('#message'),list=document.querySelector('#leaves');
let listing=0;
async function refresh(){const generation=++listing;const id=employee.value;const r=await fetch('/api/leaves?employee_id='+id);if(!r.ok)throw Error('讀取假單失敗');const rows=await r.json();if(generation!==listing)return;list.replaceChildren();for(const row of rows){const li=document.createElement('li');li.textContent=`${row.start_date}～${row.end_date} · ${row.days}天 · ${row.status==='pending'?'待審核':row.status} · ${row.reason}`;list.append(li);}if(!rows.length){const li=document.createElement('li');li.textContent='目前沒有假單';list.append(li);}}
employee.addEventListener('change',()=>refresh().catch(e=>message.textContent=e.message));
form.addEventListener('submit',async event=>{event.preventDefault();const button=form.querySelector('button');if(button.disabled)return;button.disabled=true;message.textContent='送出中';const data=Object.fromEntries(new FormData(form));data.employee_id=Number(data.employee_id);try{const r=await fetch('/api/leaves',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});const body=await r.json();if(!r.ok)throw Error(typeof body.detail==='string'?body.detail:'請檢查輸入欄位');message.textContent='已送出，待審核';await refresh();}catch(e){message.textContent=e.message;}finally{button.disabled=false;}});
(async()=>{try{const r=await fetch('/api/employees');if(!r.ok)throw Error('讀取員工失敗');for(const row of await r.json()){const option=document.createElement('option');option.value=row.id;option.textContent=row.name;employee.append(option);}await refresh();}catch(e){message.textContent=e.message;}})();''')
green=run([py,'-m','pytest','-q'])
put('docs/06-test-plan.md',(root/'docs/06-test-plan.md').read_text(encoding='utf-8').replace('追溯證據：未實作，等各票結束更新。','追溯：TC01/02/03/05/06/07/08 → backend/tests/acceptance/test_leaves.py；TC04 → backend/tests/unit/test_rules.py。上述已執行綠；TC09瀏覽器純文字驗收待操作，不標通過。'))
checkpoint('cp4-working-feature','表單主線與自動化測試綠；接卡I/J或人工驗收',green,['backend','docs'])

put('issues/002-reason-limit.md','''# 002 理由上限200→100
人確認的需求變更，沿用AC-01.4與FR-04並修訂文字，新增TC-10（101字拒絕且不存檔）。先紅後綠，UI同步max與標籤，不改既有斷言以掩蓋錯誤。依賴001。
''')
for name in ['02-prd.md','03-srs.md']:
 p=root/'docs'/name;put('docs/'+name,p.read_text(encoding='utf-8').replace('200','100'))
p=root/'backend/tests/acceptance/test_leaves.py'
put('backend/tests/acceptance/test_leaves.py',p.read_text(encoding='utf-8')+'''
@pytest.mark.req('TC-10','AC-01.4','FR-04')
def test_new_reason_limit_100(client):
    assert client.post('/api/leaves',json=valid(reason='字'*101)).status_code==422
    assert count(client)==0
''')
change_red=run([py,'-m','pytest','-q'],expected=1)
p=root/'backend/app/main.py';put('backend/app/main.py',p.read_text(encoding='utf-8').replace('REASON_MAX=200','REASON_MAX=100'))
p=root/'backend/app/static/index.html';put('backend/app/static/index.html',p.read_text(encoding='utf-8').replace('200','100'))
change_green=run([py,'-m','pytest','-q'])
versions=run([py,'-m','pip','list','--format=json'])
put('docs/06-test-plan.md',(root/'docs/06-test-plan.md').read_text(encoding='utf-8')+'\nTC-10：101字拒絕且不存檔；backend/tests/acceptance/test_leaves.py，實際紅→綠。TC09與完整瀏覽器流程需見DELIVERY的後續操作證據。')
put('docs/DELIVERY.md','''# 交付參考
依course/STACK.md安裝、啟動與測試。預設http://127.0.0.1:8000/；測試資料庫獨立，不含app內LLM或登入。
## 需求變更的實際紅燈
```text
'''+change_red+'''\n```
## 變更後綠燈
```text
'''+change_green+'''\n```
## 實測套件
```json
'''+versions+'''\n```
瀏覽器操作證據由講師在建立快照後補上，未操作前不宣稱通過。不同OS及不同Agent的完整課堂耗時未量測。
''')
checkpoint('cp5-delivered','需求變更紅→綠與交付參考；瀏覽器證據後補',change_red+'\nGREEN:\n'+change_green,['backend','docs','issues'])
print('Created five local checkpoint refs without publishing. Worktree retained for browser verification.',flush=True)
