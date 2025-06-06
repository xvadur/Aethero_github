# CHANGELOG

## [2025-06-06] AETH-EXEC: 2025-06-06 - clean, refactor, git architecture, requirements update

### Hlavné zmeny
- Kompletný refaktor infraštruktúry repozitára
- Odstránenie Forgejo backendu, návrat na GitHub-only režim
- Vyčistenie a štandardizácia repozitárového rámca AetheroOS
- Aktualizácia requirements.txt a audit skriptov
- Vytvorenie baseline snapshotu pre audit

### Dopad na infraštruktúru a vývoj
- Všetky vývojové a CI/CD procesy sú teraz viazané výhradne na GitHub
- Zjednodušený workflow, žiadne závislosti na lokálnych Forgejo službách
- Čistejšie prostredie pre ďalší vývoj a migrácie

### Čo skontrolovať alebo preinštalovať
- Po update spustiť: `pip install -r requirements.txt`
- Spustiť: `python archivia_audit.py --save-baseline` pre nový audit snapshot
- Overiť, že všetky workflowy na GitHub prechádzajú bez chýb
