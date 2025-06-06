# AETHERO DEPLOY PROTOCOL v1.0 (AETH-PROT-2025-0003)

Názov: Aethero Living Build Protocol
Účel: Zaviesť štandardizovaný postup pre vývoj, testovanie a nasadenie nových AetheroOS modulov
Platnosť: Od 2025-06-04, záväzné pre všetky vývojové vetvy, ktoré implementujú AI agentov, vizualizácie alebo introspektívne komponenty.

---

## 🧭 FÁZY PROTOKOLU

1. Iniciačná fáza – Projektová seederizácia
   - Naklonovanie vzorovej šablóny (aethero_nextjs_seed)
   - Nastavenie tailwind.config.js, postcss.config.js, globals.css
   - Overenie bežiaceho Next.js servera (npm run dev)
   - Inicializácia branchu (napr. living_mindscape, dashboard_analytics)

2. Modularizačná fáza – Rozklad UI/Logiky
   - Vytvorenie komponentov podľa paradigmy Aethero (napr. MinisterCard.tsx, MindTree.tsx)
   - API endpointy podľa schémy /api/analyze-[modul].ts
   - Konfigurácia orchestrácie agentov (CrewAI, mindscape_config.json)
   - Validácia výstupu v JSON (logika, emócie, typológia…)

3. Automatizačná fáza – CI/CD a monitoring
   - Nastavenie vercel.json, deploy.yml (GitHub Actions)
   - Logovanie do logs/AETH-EXEC-XXXX.md
   - Pravidelné commity a opisné správy (napr. [AETH-0003] Init agent orchestrator)
   - Pull Request otvorený na main (ako tvoj PR #2)

4. Schvaľovanie a audit
   - Vyžaduje overenie (napr. Prezident, Grok alebo GitHub reviewer)
   - Merge do hlavnej vetvy až po accept log zápise
   - Pridanie projektu do výkonného záznamu (deployment_manifest.json)

5. Nasadenie a feedback loop
   - Deployment cez Vercel (automaticky po merge)
   - Notifikácia do GitHub Issues / Slack / Discord / agentov
   - Iteračná spätná väzba (formulár alebo z dashboardu)
   - Zápis do aethero_impact_log.md

---

## 🔐 POVINNÉ ZÁKONY PROTOKOLU

| Názov                   | Pravidlo                                                                 |
|-------------------------|-------------------------------------------------------------------------|
| Zákon modularity        | Každý komponent a endpoint musí byť samostatne testovateľný              |
| Zákon logovania         | Každý krok iterácie musí byť zapísaný do logu (timestamp + summary)      |
| Zákon pull requestu     | Žiadna zmena nejde do main, kým nie je PR schválený                      |
| Zákon reverzibility     | Každý krok musí byť spätne sledovateľný (git history + logs)             |
| Zákon agentnej zodpovednosti | Každý agent má vlastný výstup, ktorý je prepojený na danú vetvu systému |
| Zákon 3-úrovňového testu| Jednotkový test, integračný test a manual check musia byť zaznamenané    |

---

## 🛠️ ŠABLÓNA: deployment_protocol.md (auto-generovaná pre každý nový modul)

# AETHERO DEPLOYMENT PROTOCOL – [modul_nazov]

## 1. Cieľ modulu:
...

## 2. Komponenty:
- [x] UI komponenty
- [x] API endpointy
- [ ] Vizualizácie
- [ ] Agent orchestration

## 3. CI/CD:
- Branch: `feature/[modul]`
- Deploy: `Vercel`
- CI: `GitHub Actions`
- Logy: `logs/AETH-EXEC-XXXX.md`

## 4. Stav:
✅ Build Passed  
🔁 Review Pending  
📦 Merge Ready

---

## Poznámky:
- Tento protokol je záväzný pre všetky nové moduly a iterácie.
- Pravidelne aktualizovať podľa potrieb projektu a spätnej väzby.
