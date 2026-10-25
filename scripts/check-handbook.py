"""Check course parity and local handbook links without third-party modules."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import argparse
import json
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__();self.ids=[];self.links=[];self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        for attr in ('href','src'):
            if attr in a:self.links.append(a[attr])

ap=argparse.ArgumentParser();ap.add_argument('--student-root',type=Path,default=ROOT.parent/'leavebot-bootcamp');args=ap.parse_args()
subprocess.run([sys.executable,str(ROOT/'scripts/sync-course.py'),'--student-root',str(args.student_root),'--check'],check=True)
html_files=list((ROOT/'handbook/site').glob('*.html'))
html_files += [ROOT/'開啟講義.html', ROOT/'starter-kit/index.html']
pages={p:Page(p.read_text(encoding='utf-8')) for p in html_files}
problems=[]
for path,page in pages.items():
    if len(page.ids)!=len(set(page.ids)):problems.append(f'duplicate IDs: {path}')
    for href in page.links:
        url=urlsplit(href)
        if url.scheme or href.startswith('//'):continue
        target=(path.parent/unquote(url.path)).resolve() if url.path else path
        if not target.exists():problems.append(f'{path.name}: missing {href}')
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            problems.append(f'{path.name}: missing anchor {href}')
plan=json.loads((ROOT/'handbook/course-plan.json').read_text(encoding='utf-8'))
for u in plan['day2']['units']:
    if f'unit-{u["number"]}' not in pages[ROOT/'handbook/site/day2.html'].ids:problems.append(f'missing unit {u["number"]}')
for c in plan['cards']:
    if 'card-'+c['id'].lower() not in pages[ROOT/'handbook/site/prompts.html'].ids:problems.append(f'missing card {c["id"]}')
for ident in ['project','workflow','stack','rescue']:
    if ident not in pages[ROOT/'handbook/site/day2.html'].ids:problems.append(f'missing HTML reference {ident}')
if problems:raise SystemExit('\n'.join(problems))
print(f'PASS: {len(pages)} pages, local assets/anchors and {len(plan["cards"])} prompt cards; version {plan["version"]}')
