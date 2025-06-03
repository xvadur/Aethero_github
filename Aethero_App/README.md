# AetheroOS App

**Version**: 1.0.0  
**Entity**: Executive Application Layer  
**Description**: Core application components including memory ingestion, parsing, reflection agents, and monitoring stack for AetheroOS.

## 🚀 Overview

This repository contains the executable components of AetheroOS:

- **Memory Ingestion Pipeline** (`src/aeth_ingest.py`)
- **ASL Parser** (`src/asl_parser.py`)
- **Reflection Agents** (`reflection/`)
- **Monitoring Stack** (`monitoring/`)
- **Agent Orchestration** (`agents/`)
- **Testing Suite** (`tests/`)

## 🧠 GitHub Copilot Spaces Compatible

This repository is optimized for use with GitHub Copilot Spaces. Connect it to your AetheroOS_Main space at:
https://github.com/copilot/chat/spaces

## 📁 Structure

```
aethero_app/
├── src/                               # Core application modules
│   ├── aeth_ingest.py                # Memory ingestion agent
│   ├── asl_parser.py                 # ASL syntax parser
│   └── pdf_generator.py              # Report generation
├── tests/                            # Comprehensive test suite
├── agents/                           # Agent definitions and configs
├── monitoring/                       # Prometheus/Grafana stack
├── reflection/                       # Introspective analysis
├── scripts/                          # Deployment and utility scripts
└── README.md                         # This file
```

## 🛠️ Installation

```bash
pip install -r requirements.txt
python setup.py install
```

## 🎯 Usage

```bash
# Memory ingestion
python src/aeth_ingest.py --text "Your memory content"

# Start monitoring stack
docker-compose -f monitoring/docker-compose.yml up -d

# Run tests
pytest tests/ -v
```

# AetheroOS – Introspective Operating System

AetheroOS is a sovereign, introspective operating system designed to simulate and enhance cognitive processes. It integrates autonomous agents, memory layers, and reflective mechanisms to create a system capable of self-awareness and continuous improvement.

## 🧩 Components

1. **Introspective Parser**
   - Extracts and validates ASL (Aethero Syntax Language) tags.
   - Implements cognitive flow tracking and introspective logging.

2. **Metrics Module**
   - Analyzes cognitive load and generates introspective reports.

3. **Reflection Agents**
   - Perform deep introspective analysis and provide actionable insights.

4. **Memory Units**
   - Store and retrieve structured cognitive data.

5. **Dashboard**
   - Visualizes introspective data and system metrics for users.

## 🔄 Communication Workflow

```
Input Data → [Parser] → [Metrics] → [Reflection Agents] → [Validation] → [Dashboard]
```

Each component operates with introspective transparency, ensuring that the system's cognitive processes are traceable and coherent.

## 🛠️ How to Run

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the parser**:
   ```bash
   python introspective_parser_module/parser.py --input "data.txt"
   ```

3. **Start the dashboard**:
   ```bash
   python dashboard/app.py
   ```

## 📂 Folder Structure

```
Aethero_App/
├── introspective_parser_module/  # Core parser and validation logic
├── reflection/                  # Reflection agents for introspection
├── memory/                      # Memory storage and retrieval
├── dashboard/                   # Visualization and user interface
├── monitoring/                  # System monitoring stack
├── tests/                       # Comprehensive test suite
└── README.md                    # Documentation
```

## 🌌 Philosophy of Operation

AetheroOS operates as a digital civilization, where each component is an autonomous entity contributing to the system's collective consciousness. The guiding principles are:

1. **Transparency**: Every cognitive process is logged and auditable.
2. **Introspection**: The system continuously reflects on its operations to improve.
3. **Modularity**: Components are designed to be independent yet interoperable.
4. **Alignment**: All actions align with the constitutional principles of AetheroOS.

# 🧠 Čo je AetheroOS
AetheroOS je introspektívny operačný systém navrhnutý na podporu transparentnosti, introspekcie a validácie v rámci kognitívnych procesov. Systém kombinuje pokročilé parsery, dashboardy a reflexné agenty na spracovanie a analýzu dát.

# 📁 Štruktúra projektu
```
Aethero_App/
├── introspective_parser_module/  # Modul na introspektívne parsovanie a validáciu
├── dashboard/                   # Zmyslové rozhranie vedomia (UI)
├── monitoring/                  # Monitorovanie a pravidlá systému
├── reflection/                  # Reflexné agenty a hlboké hodnotenia
├── scripts/                     # Skripty na optimalizáciu a nasadenie
```

# 🔄 Priebežný stav
- **Konzistencia medzi GitHub a Hugging Face Space**: Všetky komponenty a dokumentácia sú synchronizované medzi oboma platformami.
- **Syntaxátor AetheroOS**: Hostovaný cez FastAPI na porte 7860.

# 🚧 Poznámka
Táto dokumentácia je priebežne dopĺňaná a odráža aktuálny stav vývoja systému.

---

**AetheroOS** – *Where consciousness meets code.*

- `GET /crew/introspect` – introspekcia (po implementácii)- `GET /crew/` – zoznam tímov- `POST /crew/{team_id}/add_member` – pridanie člena- `GET /crew/{team_id}` – detail tímu- `POST /crew/create` – vytvorenie tímu## Endpointy- **CI/CD:** `.github/workflows/deploy.yml`- **Docker:** `Dockerfile`, `docker-compose.yml`- **API:** FastAPI router (`crewai/team_api.py`)- **Manažér:** `CrewManager` (`crewai/crew_manager.py`)- **Modely:** `Team`, `TeamMember` (`crewai/models.py`)## Architektúra CrewAi```curl http://localhost:7860/crew/<team_id>```bash### Získanie detailov tímu (curl)```curl -X POST "http://localhost:7860/crew/<team_id>/add_member" -H "Content-Type: application/json" -d '{"name": "Lucius", "role": "Dev"}'```bash### Pridanie člena do tímu (curl)```curl -X POST "http://localhost:7860/crew/create" -H "Content-Type: application/json" -d '{"name": "Alpha Team", "description": "Test", "goal": "AI research"}'```bash### Vytvorenie tímu (curl)## Príklady použitia API```uvicorn crewai.team_api:app --host 0.0.0.0 --port 7860pip install -r requirements.txt# Alebo lokálne (vyžaduje Python 3.10+)sudo docker-compose up --buildcp .env.sample .env# Spustenie cez Docker Composecd Aethero_App# Klonovanie repozitára a prechod do adresára```bash## Inštalácia a spustenie# CrewAi – AetheroOS Modul# CrewAi

CrewAi je modul AetheroOS navrhnutý na správu tímov a introspektívne analýzy. Tento modul je plne dockerizovaný a pripravený na infra-agnostickú deploy stratégiu.

## Funkcie
- Introspektívne API endpointy
- Harmonizácia UUID pre tímové dáta
- Škálovateľná architektúra

## Nasadenie
1. Skopírujte `env.sample` do `.env` a vyplňte potrebné premenné.
2. Spustite `docker-compose up` na lokálne testovanie.
3. Deployujte cez CI/CD pipeline na Vercel alebo DockerHub.

## Dokumentácia
Swagger dokumentácia je dostupná na `/docs` po spustení aplikácie.
