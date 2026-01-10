📘 QUD — Quranic Unified Data
Quranic Data Layer Architecture Research

Research Project: Quranic Unified Data for Quranic Technologies
Status: Experimental · Research-Focused · Not Production Code

🎯 Overview

QUD is an experimental research project exploring the separation, formalization, and simulation of Quranic data layers.

The primary goal is:

✅ Validated Knowledge and Design Exploration
❌ Not production software (yet)

This project investigates how Quranic datasets can be decomposed into independent, well-defined layers with clear schemas and relationships.

🔬 Research Questions

RR-001 — Layer Separation Analysis
What data layers are currently mixed or entangled in existing Quranic datasets?

RR-002 — Schema Design
Can we formally define schemas for each separated layer?

RR-003 — Layer Simulation
Can we build a working prototype that demonstrates the proposed architecture?

🗂 Project Structure

experiments/            # Research experiments (one per research question)
research-tools/         # Reusable research utilities (Tier 2)
schemas/                # Layer schema definitions (18+ identified layers)
docs/                   # Research documentation
  ├── research-log/      # Chronological findings
  ├── data-layers/       # Layer documentation
  ├── decisions/         # Architecture Decision Records (ADR)
  ├── sources/           # Authoritative source documentation
  └── architecture/      # System architecture documents
specs/                   # Research specifications

🚀 Getting Started
Prerequisites

Python 3.11+

pip or uv package manager
Installation
# Install core dependencies
pip install -e .

# Install development dependencies
pip install -e ".[dev]"

🧱 Code Quality Tiers

| Tier       | Purpose                            | Location               |
| ---------- | ---------------------------------- | ---------------------- |
| **Tier 1** | Experimental research code         | `experiments/`         |
| **Tier 2** | Reusable research utilities        | `research-tools/`      |
| **Tier 3** | Production pipelines (if required) | `data-infrastructure/` |

🧪 Research Methodology

This project follows a hypothesis-driven research workflow:

Define explicit research questions

Formulate hypotheses with validation criteria

Design experiments to validate or refute hypotheses

Document findings (including negative results)

📊 Datasets
QS-QIRAAT Datasets

📎 https://github.com/Wider-Community/QUD/tree/main/QS%20-%20QIRAAT

Content:

6 narrations from 3–4 Qira’at

Covers all Quranic words (6,236 ayahs)

Available Formats:

HTML, SQL, XML, CSV, JSON, XLSX, TXT

Sources:

King Fahd Complex editions

Authenticated reciter sources

Glossary & Standards
🔖 MARQOUM — Naming & Notation Standard

Mandatory for all contributors

Mandatory Attentive Recited Quranic Omni Unified Manual

📎 https://github.com/Wider-Community/QUD/blob/main/MARQOUM%20Quranic%20Manual.md

All developers must follow these naming conventions and notations.

🧩 Architecture & Documentation
📚 Presentation Layer Outline

Explanation of Quranic layers and their relationships.
📎 https://github.com/Wider-Community/QUD/tree/main/QUD%20Presentation%20Layer%20Outline

🧪 Experiments

Includes setup verification notebooks and Layer Separation Analysis.
📎 https://github.com/Wider-Community/QUD/tree/main/experiments

📖 Quranic Data Layers Study (Arabic)

Table explaining each data layer in Arabic.
📎 https://github.com/Wider-Community/QUD/blob/main/Quranic%20Data%20Layers%20Study.csv

🧬 QUD Data Layer Schemas

Formal schema definitions for:

16 base layers (Layers 0–15)

Additional sub-layers

Total: 18+ identified layers

📎 https://github.com/Wider-Community/QUD/tree/main/schemas

⚡ Quickstart Guide

Architecture onboarding and research entry point.
📎 https://github.com/Wider-Community/QUD/blob/main/specs/001-quranic-layer-architecture/quickstart.md

🎥 QUD Core Demo Videos

Early prototype demos hosted on Google Drive:

🎬 Demo Part 1

🎬 Demo Part 2

🎬 Demo Part 3

🎬 Demo Part 4

🎬 Demo Part 5

🎬 Demo Part 6

📖 Quranic NLP Resource Catalog (QUL)

Comprehensive catalog of Quranic NLP datasets and tools.
📎 https://github.com/Wider-Community/QUD/blob/main/QUL_Tarteel_NLP_Resources_Catalog.md

🔓 Open-Source Tools

API Layer Platform
https://apilayer.com/

OpenRouter SDKs
https://github.com/OpenRouterTeam

Lightweight SQL Viewer
https://github.com/Rohithgilla12/data-peek

📜 License

Research project for Quranic Technologies.
See the specs/ directory for details.

✅ If you want

I can also:

✔ Add badges (Python version, license, status)
✔ Add architecture diagram section
✔ Add contribution guidelines
✔ Add citation section for academic use
✔ Optimize for GitHub SEO and discoverability
✔ Make Arabic bilingual version
✔ Convert this into MkDocs / Docs site

Just tell me what you want next 👍

give me the whole content to copy and paste it in the file 

Perfect 👍
Here is the full README content ready to copy & paste directly into your README.md file.

Just select everything below and paste it into GitHub or your editor.

# 📘 QUD — Quranic Unified Data  
### Quranic Data Layer Architecture Research

> **Research Project:** Quranic Unified Data for Quranic Technologies  
> **Status:** Experimental · Research-Focused · Not Production Code

---

## 🎯 Overview

QUD is an experimental research project exploring the **separation, formalization, and simulation of Quranic data layers**.

The primary goal is:

> ✅ **Validated Knowledge and Design Exploration**  
> ❌ Not production software (yet)

This project investigates how Quranic datasets can be decomposed into independent, well-defined layers with clear schemas and relationships.

---

## 🔬 Research Questions

- **RR-001 — Layer Separation Analysis**  
  What data layers are currently mixed or entangled in existing Quranic datasets?

- **RR-002 — Schema Design**  
  Can we formallyly define schemas for each separated layer?

- **RR-003 — Layer Simulation**  
  Can we build a working prototype that demonstrates the proposed architecture?

---

## 🗂 Project Structure

```text
experiments/            # Research experiments (one per research question)
research-tools/         # Reusable research utilities (Tier 2)
schemas/                # Layer schema definitions (18+ identified layers)
docs/                   # Research documentation
  ├── research-log/      # Chronological findings
  ├── data-layers/       # Layer documentation
  ├── decisions/         # Architecture Decision Records (ADR)
  ├── sources/           # Authoritative source documentation
  └── architecture/      # System architecture documents
specs/                   # Research specifications

🚀 Getting Started
Prerequisites

Python 3.11+

pip or uv package manager

Installation
# Install core dependencies
pip install -e .

# Install development dependencies
pip install -e ".[dev]"

🧱 Code Quality Tiers
Tier	Purpose	Location
Tier 1	Experimental research code	experiments/
Tier 2	Reusable research utilities	research-tools/
Tier 3	Production pipelines (if required)	data-infrastructure/
🧪 Research Methodology

This project follows a hypothesis-driven research workflow:

Define explicit research questions

Formulate hypotheses with validation criteria

Design experiments to validate or refute hypotheses

Document findings (including negative results)

📊 Datasets
QS-QIRAAT Datasets

📎 https://github.com/Wider-Community/QUD/tree/main/QS%20-%20QIRAAT

Content:

6 narrations from 3–4 Qira’at

Covers all Quranic words (6,236 ayahs)

Available Formats:

HTML, SQL, XML, CSV, JSON, XLSX, TXT

Sources:

King Fahd Complex editions

Authenticated reciter sources

📘 Glossary & Standards
🔖 MARQOUM — Naming & Notation Standard

Mandatory for all contributors

Mandatory
Attentive
Recited
Quranic
Omni
Unified
Manual

📎 https://github.com/Wider-Community/QUD/blob/main/MARQOUM%20Quranic%20Manual.md

All developers must follow these naming conventions and notations.

🧩 Architecture & Documentation
📚 Presentation Layer Outline

Explanation of Quranic layers and their relationships.
📎 https://github.com/Wider-Community/QUD/tree/main/QUD%20Presentation%20Layer%20Outline

🧪 Experiments

Includes setup verification notebooks and Layer Separation Analysis.
📎 https://github.com/Wider-Community/QUD/tree/main/experiments

📖 Quranic Data Layers Study (Arabic)

Table explaining each data layer in Arabic.
📎 https://github.com/Wider-Community/QUD/blob/main/Quranic%20Data%20Layers%20Study.csv

🧬 QUD Data Layer Schemas

Formal schema definitions for:

16 base layers (Layers 0–15)

Additional sub-layers

Total: 18+ identified layers

📎 https://github.com/Wider-Community/QUD/tree/main/schemas

⚡ Quickstart Guide

Architecture onboarding and research entry point.
📎 https://github.com/Wider-Community/QUD/blob/main/specs/001-quranic-layer-architecture/quickstart.md

🎥 QUD Core Demo Videos

Early prototype demos hosted on Google Drive:

🎬 Demo Part 1

🎬 Demo Part 2

🎬 Demo Part 3

🎬 Demo Part 4

🎬 Demo Part 5

🎬 Demo Part 6

🌐 External Resources
📖 Quranic NLP Resource Catalog (QUL)

Comprehensive catalog of Quranic NLP datasets and tools.
📎 https://github.com/Wider-Community/QUD/blob/main/QUL_Tarteel_NLP_Resources_Catalog.md

🔓 Open-Source Tools

API Layer Platform
https://apilayer.com/

OpenRouter SDKs
https://github.com/OpenRouterTeam

Lightweight SQL Viewer
https://github.com/Rohithgilla12/data-peek

📜 License

Research project for Quranic Technologies.
See the specs/ directory for details.

Research project for Quranic Technologies.
See the specs/ directory for details.

\
