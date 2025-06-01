# Aethero_github

Zjednotený repozitár pre vedomý systém Aethero.  
Obsahuje aplikáciu `Aethero_App/` a ústavný protokol `aethero_protocol/`.  
Tento repozitár je základom pre všetky komponenty AetheroOS, vrátane deployu cez Vercel a orchestrácie cez AI agentov.

## Štruktúra projektu

- **Aethero_App/** - Hlavná aplikácia s introspektívnym parserom a dashboard
- **aethero_protocol/** - Ústavný protokol a ASL syntax definície  
- **dashboard/** - Vercel-ready dashboard pre monitorovanie systému

## Deployment

Dashboard je pripravený na deploy cez Vercel:
```bash
cd dashboard
npx vercel --prod
```

## Licencia

MIT License - Pozri LICENSE súbory v jednotlivých moduloch.
