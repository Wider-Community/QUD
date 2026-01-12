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

### Quranic NLP Resource Catalog (QUL)

Comprehensive catalog of Quranic NLP datasets and tools.

[QUL Tarteel NLP Resources Catalog](QUL_Tarteel_NLP_Resources_Catalog.md)

### Open-Source Tools

| Tool | Description |
|------|-------------|
| [API Layer Platform](https://apilayer.com/) | API marketplace |
| [OpenRouter SDKs](https://github.com/OpenRouterTeam) | LLM routing SDKs |
| [Data Peek](https://github.com/Rohithgilla12/data-peek) | Lightweight SQL viewer |

---

## [Related Paper] (https://pdf.sciencedirectassets.com/311593/1-s2.0-S2352340925X00056/1-s2.0-S235234092500664X/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLWVhc3QtMSJHMEUCIQDdiWHnmn4%2FYqe6zVoTmxlBhhCSqOmSh0KF%2FatCuqrbUAIgCoiWJt%2BCyL2OmpaFZfBkRx9uOykfLgoTMMZIAYsqeGUqvAUI7v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAFGgwwNTkwMDM1NDY4NjUiDLV0igRKNimAgRNg7iqQBf8aXB6Xr49nknd8Kz4ZIH2tNY1HGaxR6yLg5kev4U5nfyXwOkd5B0A0w%2BohNoNy1yXW59qzLYBjlTBYJqc68WXwEpBnLgP0alUBGtg7EvdRndC2Q6Yba%2Fp%2BjUm49lEuWFLB0LK28yO0W23O6R%2BMejAKKJu6DK55aqXFCjLJehSbz19OGuNh65pGaeDN3zQO30qxFie479WJ7blI2z5nXXXX%2BGe090gAFXr%2FD%2BP32UnYZbdWT0Vd676cexd0hZz6j9NA4i%2FBWMHOUfs5Uyut8T1PVt9%2F4W5to6S6I%2FhVJfTkNBl8fMGaHYaaQryUq3qnjOskxc93wb1kNljAcSdOaCB6R%2F8NeVsmPnCm%2BJNhQF0mlSdmenCd01t%2Bq5lpplzpAZHOcMkqkiHuvmkm7FnrmoQQQQGCUYUzw0Qs9gOx3RcfezoSNVp1WzB9V9QC%2Fpn%2BtZRRcHR1nKzu%2F5KFjvmr5AXYL58CMwpqaxac6kyWWqcOk8AJ41kQ4p27btPtQOIbZGxnHbmtwbvxP%2BNUUap6UqSQldDGndOGXICE6QKtLhc5tncfuj8gHr47uytWcUqjA7vlZ73BvX9VcwTlVdOCSti75bVNpfOSBzYgvwRCm%2FR5Wf1P5ELW7hovaswiwE34M7e%2BuIAVG4jJzQhqSw8l5NEqVLpFKBCtKi44YEzupyMA4UYGha582HaGPSDK%2B%2FzXxy0GPwRIZJFwDJ%2F75ShlQzoBZCQWJTGTH5qlUP4Qk7WBJI%2BPmOdzsUfFovJKOaCM1uThjChebkg66C8VSVSh1VacQStuA6g4sNyIx6pbboaWfoCDqkXLC1SfUeqr%2FkJqJSIZIf6i3GD1%2Fwf9%2B7zXHeYB4rrmIkJ04VVD12mBo3U9MJHkk8sGOrEBS2%2FzerMvgMULLkRVURhGToRe7pf32A3wDKKvfYGu8ydMiFnEeW9ZK%2BZlHxp4GNFcVchYpn6N81kMy62uB0eR1n4lfRJ6gOprZNbkzt5jV9nXXbWxcojTC4ZElksghq8ksWNlrLNRrxNw7kNNVdozym21DO3%2BY4mbp%2BMePSCQHoHUQ%2FXxhBIm%2F4gAbS45J6tjtKoSD1JT1Bw%2Bm5ivzlQ%2FJU5gmbQV3NjgpPvIjPoVnURi&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20260112T133442Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYXENIBL5J%2F20260112%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=89831c40cb9d8090142c6947d786c2d35c29c98aa231b878bbf280644985d008&hash=da117a69dd069056eae4b598d7c1288ebd9097b254a816b2799590bc32b0217f&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S235234092500664X&tid=spdf-93c4461a-b963-43c5-889c-d27b7b9b76a1&sid=5adcad578afbb944b05b7a6-94960f5bdcbfgxrqb&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&rh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=1f0156060d02575e595400&rr=9bcd0867e9bfe179&cc=eg)


## AI Coding Practices

> _Section under development_

Guidelines for AI-assisted development in this repository.

---

## Projects & Issues Conventions

We use **GitHub Projects** to track all research and development work.

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
5. **Set End Date** when complete
6. **Move to "Done"** and close the issue

### Adding a New Issue

1. Create issue with title format: `[PREFIX-###] Title`
   - Prefixes: `LF`, `SH`, `CLM`, `MJ`, `MD`, `QB`, `AI`, `MN`
2. Use this body structure (no metadata - that goes in fields):
   ```markdown
   ## Research Questions
   - **RQ1**: Question here?
   - **Related**: RR-001, RR-002

   ## Description
   Description in English.

   الوصف بالعربية.

   ## Acceptance Criteria
   - [ ] Criterion 1
   - [ ] Criterion 2

   ## References (Primary)
   - `/path/to/file.md` - Description
   ```
3. Add issue to project and set all 4 fields (System, Category, Priority, Issue Type)

---

## License

Research project for Quranic Technologies. See `specs/` for details.
