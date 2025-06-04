#!/bin/bash
# emergency_deploy.sh :: Núdzový deploy protokol AETH-PUB-2025-0043
# Cieľ: nasadiť ParserLogsSection.jsx s výstupom DEV_0178 na dashboard aetherogithub.vercel.app

set -e

COMPONENT="components/ParserLogsSection.jsx"

# 1. Kontrola existencie a úpravy súboru
echo "[1/5] Kontrola existencie a zmien v $COMPONENT..."
if [ ! -f "$COMPONENT" ]; then
  echo "❌ Súbor $COMPONENT neexistuje!"
  exit 1
fi
git status | grep "$COMPONENT" || { echo "❌ Súbor $COMPONENT nie je upravený!"; exit 1; }

echo "✅ Súbor $COMPONENT pripravený na deploy."

# 2. Commit a push
echo "[2/5] Pridávam a commitujem zmeny..."
git add "$COMPONENT"
git commit -m "Deploy DEV_0178 introspective log to dashboard" || echo "(Commit preskočený, ak nie sú nové zmeny)"
git push origin main

echo "✅ Zmeny pushnuté na GitHub."

# 3. Deploy na Vercel
echo "[3/5] Kontrola Vercel CLI..."
if ! command -v vercel &> /dev/null; then
  echo "Vercel CLI sa nenašiel, inštalujem..."
  npm install -g vercel
fi

echo "[4/5] Spúšťam produkčný deploy na Vercel..."
vercel --prod

echo "✅ Deploy na Vercel spustený."

echo "[5/5] Over nasadenie na https://vercel.com/dashboard (projekt: aetherogithub)"
echo "Hotovo."
