# LLM-based Knowledge Graph Builder

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://python.org)

A multi-agent pipeline that automatically constructs knowledge graphs from educational materials using LLMs.

**What it does:**
- Parses course slides, textbooks, and supplementary materials into structured knowledge points
- Extracts (head, relation, tail) triplets via LLM-powered agents
- Stores the resulting knowledge graph in Neo4j for querying and visualization
- Exposes a FastAPI service for pipeline orchestration

---

## Quick Start

### Prerequisites
- Python 3.10+
- [Neo4j](https://neo4j.com/download/) (5.x recommended)
- An LLM API endpoint (OpenAI-compatible, e.g., Qwen, DeepSeek, or local LLM)

### Installation

```bash
git clone https://github.com/ddddogshark/LLM_based_Knowledge_Graph-Dev.git
cd LLM_based_Knowledge_Graph-Dev
pip install -r requirements.txt
```

### Configuration

Copy the example environment file and fill in your credentials:

```bash
cp .env.example .env
# Edit .env with your LLM API key, Neo4j password, etc.
```

### Running the Pipeline

**Run the full pipeline** (single course):

```bash
python run_full_pipeline.py
```

**Start the API server:**

```bash
python -m src.main
# Server runs at http://localhost:8000
```

**API usage:**

```bash
curl -X POST http://localhost:8000/build \
  -H "Content-Type: application/json" \
  -d '{"course_name": "Machine Learning"}'

# Check build status
curl http://localhost:8000/build/status/{task_id}
```

---

## Architecture

```
User Request
    │
    ▼
┌─────────────────────────────────────────────┐
│              FastAPI Router                   │
└────────────────────┬────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────┐
│            Orchestrator                       │
│  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐     │
│  │Stage1│─▶│Stage2│─▶│Stage3│─▶│Stage4│     │
│  │Demand│  │ Data │  │  KG  │  │Final │     │
│  │Plan  │  │Collect│ │ Build│  │Report│     │
│  └──────┘  └──────┘  └──────┘  └──────┘     │
│        ▲ Quality Gates ▲                      │
└─────────────────────────────────────────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │    Neo4j Graph DB     │
         └───────────────────────┘
```

### Agent Pipeline

| Stage | Agents | Description |
|-------|--------|-------------|
| 1. Demand & Planning | DemandAnalysisAgent, SubjectOverviewAgent | Analyze requirements, create subject plan |
| 2. Data Collection | MultimodalParserAgent, ContentUnderstandingAgent | Parse materials → knowledge point drafts |
| 3. KG Construction | TheoreticalAnalysisAgent, PracticalAnalysisAgent, KgBuilderAgent | Extract triplets via LLM |
| 4. Integration | KgBuilderAgent (integrate) | Store integrated graph in Neo4j |
| 5. Delivery | ReportGenerationAgent | Generate final report |

---

## Project Structure

```
├── src/
│   ├── agents/          # Agent implementations
│   ├── api/             # FastAPI route definitions
│   ├── core/            # Orchestrator & Agent Manager
│   ├── database/        # Neo4j, MySQL, Redis drivers
│   ├── services/        # LLM API client (sync + async)
│   ├── utils/           # JSON parser, text splitter
│   ├── config.py        # Configuration & logging
│   └── main.py          # FastAPI entry point
├── scripts/             # Utility & test scripts
├── tests/               # Unit tests
├── docs/                # Additional documentation
├── requirements.txt     # Runtime dependencies
├── requirements-dev.txt # Dev dependencies
├── pyproject.toml       # Build & packaging configuration
├── .env.example         # Environment variable template
├── LICENSE              # MIT License
└── README.md            # This file
```

---

## Development

```bash
pip install -r requirements-dev.txt
pytest tests/
ruff check src/
```

---

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

---

## License

MIT License — see [LICENSE](./LICENSE) for details.

> **中文文档**: [README_zh.md](./README_zh.md)
