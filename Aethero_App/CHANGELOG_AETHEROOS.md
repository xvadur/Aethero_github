## [v0.2.4-beta] – 2025-06-01

### Pridané
- Nasadenie introspektívneho parsera (ASLMetaParser).
- Prvé testy Ena na kritickú cestu a modely.
- Scaffoldovanie dashboardu (Zerun).
- Deploy systému cez `npx vercel`.
- Zjednotenie všetkých modulov do jedného GitHub repozitára.
- Aktualizácia `.gitignore` na podporu Vercel a ďalších systémových súborov.
- ✅ **Finálna konfigurácia Vercel deploymentu**: Dashboard pripravený s `public/` zložkou, optimalizované `vercel.json` (v2 format), `package.json` s port 3000.
- Synchronizácia všetkých komponentov medzi GitHub a Hugging Face Space.
- Hostovanie syntaxátora AetheroOS cez FastAPI na porte 7860.

### Poznámka
Dashboard je teraz plne deployovateľný na Vercel s automatickým CI/CD cez GitHub. Táto verzia je priebežný commit a nie je finálna. Ďalšie iterácie budú nasledovať.

## [v0.2.1] – 2025-06-01
🔧 Refactor: parser.py, ASLMetaParser
✅ Validation: metrics.py covered
📄 Docs: FINAL_REPORT.md generated

## [v0.2.0] – 2025-05-15
✨ Feature: Introduced ASLCognitiveTag in models.py
📊 Metrics: Added cognitive load analysis in metrics.py

## [v0.1.0] – 2025-04-01
🚀 Initial release: Core modules for AetheroOS
