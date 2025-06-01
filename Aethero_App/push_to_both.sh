#!/bin/zsh

# Skript na paralelné pushovanie commitov na GitHub a Hugging Face Space

# Definovanie vzdialených repozitárov
GITHUB_REMOTE="origin"
HF_REMOTE="hf"

# Kontrola aktuálneho stavu git
if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "\n\033[1;33mUpozornenie: Máte neuložené zmeny. Commitujte ich pred spustením skriptu.\033[0m\n"
  exit 1
fi

# Push na GitHub
echo "\n\033[1;34mPushujem na GitHub...\033[0m\n"
git push $GITHUB_REMOTE main

# Push na Hugging Face Space
echo "\n\033[1;34mPushujem na Hugging Face Space...\033[0m\n"
git push $HF_REMOTE main

echo "\n\033[1;32mPushovanie dokončené na oboch platformách.\033[0m\n"
