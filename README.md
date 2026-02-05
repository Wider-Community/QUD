# QUD — Quranic Unified Data

**Quranic Data Layer Architecture Research**

> **Status:** Experimental · Research-Focused · Not Production Code

---

## Overview

QUD is an experimental research project exploring the **separation, formalization, and simulation of Quranic data layers**. The goal is to decompose existing Quranic datasets into independent, well-defined layers with clear schemas and relationships.

---

## Research Questions

| ID | Question |
|----|----------|
| **RR-001** | What data layers are currently mixed in existing Quranic datasets? |
| **RR-002** | Can we formally define schemas for each separated layer? |
| **RR-003** | Can we build a working prototype demonstrating the architecture? |

---

## Project Structure

```
experiments/                        # Research experiments (Tier 1)
├── 00_setup_verification.ipynb       # Environment validation
└── rr-001-layer-analysis/
    ├── README.md                     # Experiment methodology & hypothesis
    └── field_mapper.py               # Layer analysis tool

research-tools/                     # Reusable utilities (Tier 2)
├── validators/
│   └── schema_validator.py           # JSON Schema validation
├── analyzers/
│   └── data_comparator.py            # Cross-Qiraat comparison
└── data-loaders/
    └── quran_loader.py               # Quranic text loader

schemas/                            # Layer schema definitions (18+)
├── README.md                         # Schema documentation v2.0
├── layer-05-verse-structure/
│   └── schema.json                   # Example layer schema
└── cross-layer-mappings/
    └── entity-mapping-schema.json    # 1:1, 1:N, N:1, N:M relationships

docs/                               # Documentation
├── research-log.md                   # Chronological findings
├── architecture/
│   └── architectural-principles-v1.md  # Core design principles
└── data-layers/
    └── README.md                     # Layer categorization

specs/                              # Research specifications
└── 001-quranic-layer-architecture/
    ├── spec.md                       # Main spec (RR-001 through RR-015)
    ├── data-model.md                 # Data structure definitions
    └── quickstart.md                 # Architecture onboarding
```

---

## Quick Start

**Prerequisites:** Python 3.11+, pip or uv

```bash
# Install core dependencies
pip install -e .

# Install development dependencies
pip install -e ".[dev]"
```

---

## Key Resources

| Resource | Description |
|----------|-------------|
| [MARQOUM Manual](MARQOUM%20Quranic%20Manual.md) | Naming & notation standard **(mandatory)** |
| [QS-QIRAAT Datasets](QS%20-%20QIRAAT/) | 6 narrations across multiple formats |
| [Layer Schemas](schemas/) | 16 base layers + sub-layers |
| [Quickstart Guide](specs/001-quranic-layer-architecture/quickstart.md) | Architecture onboarding |
| [Research Log](docs/research-log.md) | Chronological findings |
| [Quranic Data Layers Study](Quranic%20Data%20Layers%20Study.csv) | Layer explanations (Arabic) |

---

<details>
<summary><strong>Demo Videos</strong></summary>

Early prototype demos:

- [Demo Part 1](https://drive.google.com/file/d/1hwXCKfWG7Ezap8Zt0TfhRllIOZmd0CTd/view?usp=drive_link)
- [Demo Part 2](https://drive.google.com/file/d/1sjM7qK2CV7BoaWa9B13E9yDpbbofEZEI/view?usp=drive_link)
- [Demo Part 3](https://drive.google.com/file/d/1oPv1JvL9_PthSMnbw7YXii28xlNzHT3C/view?usp=drive_link)
- [Demo Part 4](https://drive.google.com/file/d/1leQT5g5JxkP08w0XtkQ0X7GTrbBUPf_5/view?usp=drive_link)
- [Demo Part 5](https://drive.google.com/file/d/1vVmY5N5qs_rZGzxsyZnQDsncOgrN-FlP/view?usp=drive_link)
- [Demo Part 6](https://drive.google.com/file/d/1qmnZsuGkzrynOVnHqH5YfxrJAWihN6dz/view?usp=drive_link)

</details>

---

## External Resources

- [Tarteel Quranic Universal Library](https://qul.tarteel.ai/resources)
- [QUL Tarteel NLP Resources Catalog](docs/QUL_Tarteel_NLP_Resources_Catalog.md)
- [Uloom Quran](https://github.com/h9-tec/uloom-quran): A comprehensive AI-powered platform for Quranic Sciences featuring semantic search, comparative tafsir analysis, and the ten Quranic readings
- [زيــد: النظام المرجعي المتكامل لإدارة محتوى علم القراءات وعلوم القرآن](https://community.itqan.dev/d/221)



## Research Papers
[Noor Project](https://www.sciencedirect.com/science/article/pii/S235234092500664X) (**Very relevant**): A complete, multi-layered quranic treebank dataset with hybrid syntactic annotations for classical arabic processing


### Open-Source Tools

| Tool | Description |
|------|-------------|
| [API Layer Platform](https://apilayer.com/) | API marketplace |
| [OpenRouter SDKs](https://github.com/OpenRouterTeam) | LLM routing SDKs |
| [Data Peek](https://github.com/Rohithgilla12/data-peek) | Lightweight SQL viewer |

## AI Coding Practices

> _Section under development_

Guidelines for AI-assisted development in this repository.

---

## Projects & Issues Conventions

We use **GitHub Projects** to track all research and development work. [QUD Research & Development Project](https://github.com/orgs/Wider-Community/projects/1)

### Project Fields

| Field | Options |
|-------|---------|
| **System** | `QUD-General`, `Mujarrad`, `Mudmaj`, `Munajjam`, `AI-Research` |
| **Category** | `Layer-Foundation`, `Semantic-Hashing`, `Cross-Layer-Mapping`, `Architecture`, `Database`, `Backend`, `AI-Research`, `Integration` |
| **Priority** | `P1-Critical`, `P2-High`, `P3-Medium`, `P4-Low` |
| **Issue Type** | `Research`, `Design`, `Implementation`, `Documentation`, `Review` |

### Working on an Issue

1. **Assign yourself** to the issue
2. **Set Start Date** in the project board
3. **Move to "In Progress"** status
4. Work on the issue, updating comments as needed
5. Submit a PR, request reviewers and move to "In Review"
6. Implement reviewer feedback
7. **Set End Date** when complete
8. **Move to "Done"** and close the issue

---

## License

Research project for Quranic Technologies. See `specs/` for details.
