#!/usr/bin/env python3
"""
Archivia Audit Script – Audit a čistenie adresára ~/user

Pravidlá:
- Zachovať: Aethero projekty, aktívne repozitáre, súbory s poslednou aktivitou < 90 dní
- Navrhnúť na odstránenie: staré, neaktívne, dočasné alebo duplicitné súbory
- Výstup: JSON a CSV so zoznamom čo zachovať/odstrániť

Rozšíriteľné o interaktívne mazanie alebo logovanie.
"""
import os
import json
import csv
import argparse
from datetime import datetime, timedelta
from pathlib import Path

parser = argparse.ArgumentParser(description='Archivia Audit Script')
parser.add_argument('--dir', type=str, help='Cesta k adresáru na auditovanie (default: ~/user)')
args, _ = parser.parse_known_args()

USER_DIR = args.dir if args.dir else os.path.expanduser('~/user')
DAYS_ACTIVE = 90
OUTPUT_JSON = 'archivia_audit_output.json'
OUTPUT_CSV = 'archivia_audit_output.csv'
BASELINE_JSON = 'archivia_baseline.json'

# Kľúčové slová pre Aethero projekty a repozitáre
AETHERO_KEYWORDS = ['aethero', 'repo', 'project', 'orchestra', 'dashboard']


def is_aethero_project(path: Path) -> bool:
    name = path.name.lower()
    return any(kw in name for kw in AETHERO_KEYWORDS)

def is_git_repo(path: Path) -> bool:
    return (path / '.git').is_dir()

def last_activity(path: Path) -> datetime:
    if path.is_file():
        return datetime.fromtimestamp(path.stat().st_mtime)
    elif path.is_dir():
        latest = datetime.fromtimestamp(path.stat().st_mtime)
        for sub in path.rglob('*'):
            try:
                t = datetime.fromtimestamp(sub.stat().st_mtime)
                if t > latest:
                    latest = t
            except Exception:
                continue
        return latest
    return datetime.fromtimestamp(0)

def audit_user_dir():
    keep = []
    remove = []
    now = datetime.now()
    for item in Path(USER_DIR).iterdir():
        info = {
            'name': item.name,
            'path': str(item),
            'type': 'dir' if item.is_dir() else 'file',
            'last_activity': last_activity(item).isoformat(),
            'reason': ''
        }
        if is_aethero_project(item):
            info['reason'] = 'Aethero project keyword'
            keep.append(info)
        elif is_git_repo(item):
            info['reason'] = 'Git repository'
            keep.append(info)
        elif (now - last_activity(item)).days < DAYS_ACTIVE:
            info['reason'] = f'Active in last {DAYS_ACTIVE} days'
            keep.append(info)
        else:
            info['reason'] = 'Inactive/old – candidate for removal'
            remove.append(info)
    return keep, remove

def export_results(keep, remove):
    result = {
        'keep': keep,
        'remove': remove,
        'summary': {
            'total': len(keep) + len(remove),
            'to_keep': len(keep),
            'to_remove': len(remove)
        }
    }
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'path', 'type', 'last_activity', 'reason', 'action'])
        for entry in keep:
            writer.writerow([entry['name'], entry['path'], entry['type'], entry['last_activity'], entry['reason'], 'keep'])
        for entry in remove:
            writer.writerow([entry['name'], entry['path'], entry['type'], entry['last_activity'], entry['reason'], 'remove'])
    print(f"Výsledky uložené do {OUTPUT_JSON} a {OUTPUT_CSV}")

def save_baseline(keep):
    with open(BASELINE_JSON, 'w', encoding='utf-8') as f:
        json.dump({'keep': keep, 'timestamp': datetime.now().isoformat()}, f, indent=2, ensure_ascii=False)
    print(f"Východiskový stav uložený do {BASELINE_JSON}")

def restore_baseline():
    with open(BASELINE_JSON, 'r', encoding='utf-8') as f:
        baseline = json.load(f)
    # Tu by sa implementovalo obnovenie stavu podľa baseline['keep']
    print("Obnova východiskového stavu je zatiaľ len simulovaná (implementujte mazanie/pridávanie súborov podľa baseline).")
    return baseline

def main():
    keep, remove = audit_user_dir()
    export_results(keep, remove)
    print(f"Navrhnuté na zachovanie: {len(keep)} | Na odstránenie: {len(remove)}")
    if args.dir and 'desktop/aethero_github' in args.dir.lower():
        save_baseline(keep)

if __name__ == '__main__':
    main()
