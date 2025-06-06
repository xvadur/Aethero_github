"""
DeploySentinel Agent
-------------------
Ministerský agent pre monitoring a audit deployu AetheroOS.
- Detekuje každú deploy snahu (Vercel, lokálne, CI/CD)
- Validuje konfigurácie (tokeny, API routy, manifesty)
- Loguje výsledky do logs/deploy_audit/
- Upozorňuje na zlyhania a navrhuje/realizuje opravy
- Pravidelne testuje deploy flow a použiteľnosť rozhraní
"""
import os
import time
import glob
import subprocess
from datetime import datetime
import yaml
import json

LOG_DIR = "logs/deploy_audit/"
MANIFEST_PATH = "Aethero_App/aethero_manifest.yaml"
VERCEL_CONFIG = ".vercel"
DEPLOY_LOG = os.path.join(LOG_DIR, f"deploy_audit_{datetime.now().strftime('%Y%m%d')}.log")

os.makedirs(LOG_DIR, exist_ok=True)

def detect_deploy():
    # Detekcia podľa zmien v .vercel, CI/CD workflow, alebo podľa git push
    vercel_exists = os.path.exists(VERCEL_CONFIG)
    ci_cd = any(glob.glob(".github/workflows/*.yml"))
    return vercel_exists or ci_cd

def validate_config():
    issues = []
    # Kontrola manifestu
    if not os.path.exists(MANIFEST_PATH):
        issues.append(f"Chýba manifest: {MANIFEST_PATH}")
    else:
        try:
            with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
                yaml.safe_load(f)
        except Exception as e:
            issues.append(f"Chyba v manifest yaml: {e}")
    # Kontrola Vercel configu
    if not os.path.exists(VERCEL_CONFIG):
        issues.append("Chýba .vercel konfigurácia")
    # Príklad: kontrola API rout
    api_dir = "api/"
    if not os.path.exists(api_dir):
        issues.append("Chýba adresár api/ pre endpointy")
    return issues

def test_frontend():
    # Skúsi spustiť Next.js build/test (alebo iný základný test)
    try:
        result = subprocess.run(["npm", "run", "build"], cwd="aethero_nextjs", capture_output=True, timeout=120)
        if result.returncode != 0:
            return False, result.stderr.decode()
        return True, "Build úspešný"
    except Exception as e:
        return False, str(e)

def log_result(status, issues, frontend_ok, frontend_log):
    with open(DEPLOY_LOG, 'a', encoding='utf-8') as f:
        f.write(f"\n## DeploySentinel run {datetime.now().isoformat()}\n")
        f.write(f"Status: {status}\n")
        if issues:
            f.write(f"Konfiguračné problémy: {issues}\n")
        f.write(f"Frontend build: {'OK' if frontend_ok else 'ZLYHAL'}\n")
        if not frontend_ok:
            f.write(f"Log: {frontend_log}\n")

if __name__ == "__main__":
    status = "OK"
    if detect_deploy():
        issues = validate_config()
        frontend_ok, frontend_log = test_frontend()
        if issues or not frontend_ok:
            status = "ZLYHANIE"
        log_result(status, issues, frontend_ok, frontend_log)
        if status == "ZLYHANIE":
            print("[DeploySentinel] Deploy zlyhal alebo má problémy. Pozri logy v logs/deploy_audit/.")
        else:
            print("[DeploySentinel] Deploy prebehol úspešne.")
    else:
        print("[DeploySentinel] Nebola detegovaná žiadna deploy snaha.")
