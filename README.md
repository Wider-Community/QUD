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

### Open Source Resources
1. [Free API Layer | Integrations and Integratability in minutes](https://apilayer.com/)
2. [Open Router SDKs](https://github.com/OpenRouterTeam)
3. [Super Lite SQL Database Viewer Desktop Client](https://github.com/Rohithgilla12/data-peek)

---
## License

Research project for Quranic Technologies - see specs/ for details.
