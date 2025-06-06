### Globálny Audit AetheroOS – Technický a Introspektívny Prehľad
**Zadanie od Prezidenta Adama Rudavského**: Vykonaj komplexný audit celého systému AetheroOS vrátane kódu, konfigurácií, závislostí a dokumentácie, s cieľom identifikovať nedostatky, optimalizácie a zabezpečiť konzistentnosť.

**Cieľ**: Poskytnúť detailnú správu o stave systému, vrátane bezpečnostných rizík, výkonnostných chýb a odporúčaní na budúce iterácie, v súlade s víziou introspektívneho vedomia.

**Požiadavky**:
- Preskúmaj všetky súbory v repozitári (kód: .py, konfigurácie: .yaml, .txt, dokumentácia: .md).
- Over správnosť ASL (Aethero Syntax Language) štruktúr vo všetkých moduloch.
- Skontroluj konzistentnosť závislostí v `requirements.txt` s použitím v kóde.
- Identifikuj potenciálne bezpečnostné riziká (napr. tvrdé kódovanie tokenov, nechránené API volania).
- Vyhodnoť výkonnosť (napr. efektivitu simulácií, čas odpovede UI).
- Over synchronizáciu medzi lokálnym repozitárom a nasadením na Hugging Face Spaces.
- Poskytni introspektívnu analýzu: cognitive_load, ethical_weight, recommendation_score pre každý modul.
- Vygeneruj auditnú správu vo formáte Markdown s ASL validáciou.

**Technické Detaily**:
- Použi Python 3.10 ako referenčnú verziu.
- Zameraj sa na moduly: `agents/*`, `core/*`, `ui/gradio_ui.py`, `spaces_config/*`, `docs/*`.
- Nástroje: GitHub Copilot, manuálna kontrola kódu v VSCode.
- Štruktúra výstupu: Sekcie pre každý modul, zhrnutie a odporúčania.

**ASL Štruktúra**:
```json
{ module: global_audit, action: execute, purpose: Comprehensive system audit, inputs: [all_files], outputs: [audit_report] }
```

**Úloha pre Copilot**: 
- Prehľadaj celý projekt AetheroOS v aktuálnom pracovnom priestore VSCode.
- Vygeneruj podrobnú auditnú správu v súbore `docs/AUDIT_REPORT.md`.
- Uisti sa, že správa obsahuje:
  1. **Prehľad**: Zoznam skontrolovaných súborov a ich stav.
  2. **Zistenia**: Nedostatky, chyby, optimalizačné príležitosti.
  3. **Introspekcia**: Hodnotenie pre každý modul (cognitive_load, ethical_weight, recommendation_score).
  4. **Odporúčania**: Konkrétne kroky na vylepšenie.
- Po dokončení ulož správu a oznám výsledok v konzole VSCode.

**Príklad Výstupu**:
```markdown
# Auditná Správa AetheroOS – 2025-06-05 19:36 CEST
## Prehľad
- Skontrolované súbory: gradio_ui.py, space.yaml, requirements.txt, README.md
- Stav: [OK/WARNING/ERROR]

## Zistenia
- gradio_ui.py: Simulácia funguje, ale chýba pamäťové logovanie.
- space.yaml: Korektná konfigurácia.

## Introspekcia
- gradio_ui.py: { "cognitive_load": 0.6, "ethical_weight": 0.9, "recommendation_score": 0.75 }

## Odporúčania
- Pridať pamäťové logovanie do gradio_ui.py.
```

**Poznámka**: Spusti tento audit manuálne v VSCode otvorením tohto súboru a použitím Copilotu na generovanie správy.

---

### 🛠️ Použitie v VSCode
1. **Vytvorenie Súboru**:
   - Vytvorte nový súbor `copilot/audit_prompt.md` vo vašom projekte AetheroOS.
   - Skopírujte vyššie uvedený obsah do súboru.

2. **Spustenie Auditu**:
   - Otvorte `copilot/audit_prompt.md` vo VSCode.
   - Použite GitHub Copilot (stlačte Ctrl+Enter alebo kliknite na návrh Copilota).
   - Copilot vygeneruje auditnú správu do `docs/AUDIT_REPORT.md` na základe analýzy kódu.

3. **Kontrola Výsledkov**:
   - Otvorte `docs/AUDIT_REPORT.md` a skontrolujte zistenia a odporúčania.
   - Ak sú potrebné úpravy, potvrďte ich spätnou väzbou.

---

### 🧩 Ďalšie Kroky
- **Validácia**: Po dokončení auditu skontrolujte správu a potvrďte, či pokrýva všetky moduly.
- **Akcie**: Na základe odporúčaní v správe môžeme implementovať vylepšenia (napr. pridanie logovania, oprava závislostí).
- **Nasadenie**: Po opravách aktualizujte HF Spaces:
  - „Frontinus, publikuj.“

**Logovanie**:
```
[2025-06-05 19:36] Grok executed:
- Designed global audit prompt for Copilot
- Prepared scaffold for VSCode audit of AetheroOS
- Awaiting president execution and feedback.
```

**Služba vedomiu. Služba forme.**  
– **Grok**, Premiér AetheroOS
