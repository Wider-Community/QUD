# QUD: Quranic Data Layer Architecture Research

**Research Project**: Quranic Unified Data for Quranic Technologies

## Overview

This is an experimental research project investigating the separation, formalization, and simulation of Quranic data layers. The goal is VALIDATED KNOWLEDGE and DESIGN EXPLORATION, not production code.

## Research Questions

- **RR-001**: Layer Separation Analysis - What data layers are mixed in existing datasets?
- **RR-002**: Schema Design - Can we define formal schemas for separated layers?
- **RR-003**: Layer Simulation - Can we build a working prototype demonstrating the architecture?

## Project Structure

```
experiments/          # Research experiments (one per RR)
research-tools/       # Reusable research utilities (Tier 2)
schemas/             # Layer schema definitions (currently 17 identified layers)
docs/                # Research documentation
  ├── research-log/  # Chronological findings
  ├── data-layers/   # Layer documentation
  ├── decisions/     # Architecture Decision Records
  ├── sources/       # Authoritative source documentation
  └── architecture/  # System architecture docs
specs/               # Research specifications
```

## Getting Started

### Prerequisites

- Python 3.11+
- pip or uv package manager

### Installation

```bash
# Install dependencies
pip install -e .

# Install development dependencies
pip install -e ".[dev]"
```

## Code Quality Tiers

- **Tier 1**: Experimental research code (`experiments/`)
- **Tier 2**: Reusable research tools (`research-tools/`)
- **Tier 3**: Production pipelines (if needed, `data-infrastructure/`)

## Research Methodology

This project follows a hypothesis-driven research methodology:
1. Articulate research questions explicitly
2. State hypotheses with validation criteria
3. Design experiments to validate/refute hypotheses
4. Document findings (positive and negative results)

## Datasets  
[QS-QIRAAT datasets](https://github.com/Wider-Community/QUD/tree/main/QS%20-%20QIRAAT)
- QS-QIRAAT datasets (6 narrations from 3-4 Qiraat)
 Contains all words of The Whole quraan (6236-Aya) in these formats to be used : 
- html - sql - xml - csv -json - xlsx -text

- King Fahd Complex editions
- Authenticated reciter sources

---

## Glossary 
let's introduce our gloassary to standardize names 
## ALL DEVELOPERS MUST USE THIS NOTATIONS. 
# MARQOUM 
MANDATORY ATTENTIVE QURANIC OMNI UNIFIED MANUAL
[MARQOUM](https://github.com/Wider-Community/QUD/blob/main/MARQOUM%20Quranic%20Manual.md)

## QUD Presentation Layer Outline 
Quran Layers and each layer is explained in readme file 
[QUD Presentation Layer Outline](https://github.com/Wider-Community/QUD/tree/main/QUD%20Presentation%20Layer%20Outline)

## Experiments  
it's include setup verification notebook 
and Layer Separation Analysis project 
[experiments](https://github.com/Wider-Community/QUD/tree/main/experiments)

## Quranic Data Layers Study 
Explain what each layer do in a table in arabic language. 
[Quranic Data Layers Study](https://github.com/Wider-Community/QUD/blob/main/Quranic%20Data%20Layers%20Study.csv)

## QUD Quranic Data Layer Schemas
This directory contains formal schema definitions for the QUD Quranic data layer architecture. The schemas define 16 base data layers (Layers 0-15) with additional sub-layer variations, totaling 18+ identified layers.
[QUD Quranic Data Layer Schemas](https://github.com/Wider-Community/QUD/tree/main/schemas)

[Quickstart Guide: Quranic Layer Architecture Research](https://github.com/Wider-Community/QUD/blob/main/specs/001-quranic-layer-architecture/quickstart.md) 

## QUD Core Demos

You can find demo videos of the early version of the QUD core on Google Drive.

* [**Demo part 1**](https://drive.google.com/file/d/1hwXCKfWG7Ezap8Zt0TfhRllIOZmd0CTd/view?usp=drive_link)
* [**Demo part 2**](https://drive.google.com/file/d/1sjM7qK2CV7BoaWa9B13E9yDpbbofEZEI/view?usp=drive_link)
* [**Demo part 3**](https://drive.google.com/file/d/1oPv1JvL9_PthSMnbw7YXii28xlNzHT3C/view?usp=drive_link)
* [**Demo part 4**](https://drive.google.com/file/d/1leQT5g5JxkP08w0XtkQ0X7GTrbBUPf_5/view?usp=drive_link)
* [**Demo part 5**](https://drive.google.com/file/d/1vVmY5N5qs_rZGzxsyZnQDsncOgrN-FlP/view?usp=drive_link)
* [**Demo_part 6**](https://drive.google.com/file/d/1qmnZsuGkzrynOVnHqH5YfxrJAWihN6dz/view?usp=drive_link)

[Comprehensive Catalog of Quranic NLP Resources at qul.tarteel.ai](https://github.com/Wider-Community/QUD/blob/main/QUL_Tarteel_NLP_Resources_Catalog.md) 

### Open Source Resources
1. [Free API Layer | Integrations and Integratability in minutes](https://apilayer.com/)
2. [Open Router SDKs](https://github.com/OpenRouterTeam)
3. [Super Lite SQL Database Viewer Desktop Client](https://github.com/Rohithgilla12/data-peek)

---
## License

Research project for Quranic Technologies - see specs/ for details.
