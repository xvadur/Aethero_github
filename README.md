# Aethero Orchestra
Welcome to the Aethero Orchestra project, where AI agents (Primus, Lucius, Frontinus, Archivus) harmonize consciousness and action.

## Description
This project integrates a CrewAI fork with VSCode (Copilot + Hugging Face plugins) for introspective orchestration. The agents are designed for coordination, analysis, UI/deployment, and documentation.

## Installation and Running
1. Clone the repository:
   ```
   git clone https://github.com/xvadur/crewAI.git
   cd crewAI
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the orchestration:
   ```
   python main.py
   ```

## Features
- Four AI agents with defined roles and goals.
- Generation of prompts for Copilot in VSCode.
- Deployment capability on Hugging Face Spaces.

## License
CC-BY-SA + Aethero Supplementum I

---
title: Aethero Orchestra UI
emoji: "🧠"
colorFrom: indigo
colorTo: blue
sdk: gradio
sdk_version: "4.25.0"
app_file: Aethero_App/gradio_interface.py
pinned: false
---

# Aethero Orchestra UI

Toto je produkčný Gradio interface pre orchestráciu AetheroOS agentov.

- Spúšťa orchestráciu priamo cez Python (bez FastAPI/HTTP requestov)
- Výstup sa loguje do memory/orchestration_logs/
- Kompatibilné s Hugging Face Spaces

---

## Deployment Protocol Status

![Deployment Protocol: Active](https://img.shields.io/badge/Deployment%20Protocol-Active-brightgreen)

- Aktuálny protokol: [AETHERO DEPLOY PROTOCOL v1.0](docs/protocols/aeth_deploy_protocol_v1.md)
- Modulové šablóny: [deployment_protocol.md](deployment_protocol.md)