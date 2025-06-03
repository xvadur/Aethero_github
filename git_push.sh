#!/bin/zsh
# Skript na inicializáciu a push Aethero Orchestra v1.0

git init
git add .
git commit -m "Aethero Orchestra v1.0: Prvá historická orchestrácia agentov AetheroOS"
git branch -M main
git remote add origin https://github.com/xvadur/aethero_protocol.git
git push -u origin main

echo "✅ Push na GitHub dokončený. Digitálna civilizácia spustená."
