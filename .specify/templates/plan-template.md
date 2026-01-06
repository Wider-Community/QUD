# Research Plan: [RESEARCH TOPIC]

**Branch**: `[###-research-topic]` | **Date**: [DATE] | **Spec**: [link]
**Input**: Research specification from `/specs/[###-research-topic]/spec.md`

**Note**: This template is filled in by the `/plan` command. See `.claude/commands/plan.md` for the execution workflow.

<!--
  RESEARCH PROJECT NOTE: This is an experimental research project for Quranic Technologies.
  The goal is VALIDATED KNOWLEDGE and DESIGN EXPLORATION, not production code.
  Code exists to TEST HYPOTHESES and VALIDATE APPROACHES.
-->

## Summary

[Extract from research spec: primary research questions + experimental approach + expected findings]

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: [e.g., Python 3.11, Swift 5.9, Rust 1.75 or NEEDS CLARIFICATION]  
**Primary Dependencies**: [e.g., FastAPI, UIKit, LLVM or NEEDS CLARIFICATION]  
**Storage**: [if applicable, e.g., PostgreSQL, CoreData, files or N/A]  
**Testing**: [e.g., pytest, XCTest, cargo test or NEEDS CLARIFICATION]  
**Target Platform**: [e.g., Linux server, iOS 15+, WASM or NEEDS CLARIFICATION]
**Project Type**: [single/web/mobile - determines source structure]  
**Performance Goals**: [domain-specific, e.g., 1000 req/s, 10k lines/sec, 60 fps or NEEDS CLARIFICATION]  
**Constraints**: [domain-specific, e.g., <200ms p95, <100MB memory, offline-capable or NEEDS CLARIFICATION]  
**Scale/Scope**: [domain-specific, e.g., 10k users, 1M LOC, 50 screens or NEEDS CLARIFICATION]

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### I. Research-First Methodology
- [ ] Research questions clearly articulated (not feature requests)
- [ ] Hypotheses stated explicitly with validation criteria
- [ ] Acceptance that experiments may fail (failure that produces learning is success)
- [ ] Documentation plan for findings (positive and negative results)

### II. Data Layer Architecture
- [ ] Quranic data layer dependencies identified (14 essential layers: 0-13, unfolds to 16)
- [ ] Work respects semantic layer boundaries (no layer-violating shortcuts)
- [ ] Generative architecture understood (layers computed via rules, not manually curated)
- [ ] Schema conformance plan defined for generated layer data
- [ ] Cross-narration compatibility considered
- [ ] Scholarly validity preserved

### III. Experimental Validation
- [ ] Validation method specified for each hypothesis
- [ ] Success criteria are measurable
- [ ] Code quality tier identified (Tier 1 experimental / Tier 2 tools / Tier 3 production)
- [ ] Experimental code clearly marked

### IV. Quranic Domain Integrity
- [ ] Authoritative data sources identified (King Fahd Complex editions, etc.)
- [ ] Data validation method specified (character counts, verse counts, narration variants)
- [ ] Source provenance documentation plan in place
- [ ] Zero tolerance for Quranic text errors acknowledged
- [ ] Recitation variants (القراءات العشر) treated as core requirements, not edge cases

### V. Incremental Discovery
- [ ] Research broken into small, independently validatable hypotheses
- [ ] Dependencies between research requirements clear
- [ ] Plan for preserving failed approach documentation
- [ ] Avoiding premature abstraction (build patterns from experience, not speculation)

## Project Structure

### Documentation (this research topic)

```text
specs/[###-research-topic]/
├── plan.md              # This file (/plan command output)
├── research.md          # Phase 0 output (/plan command) - literature review, prior work
├── data-model.md        # Phase 1 output (/plan command) - Quranic data structures explored
├── experiment-design.md # Phase 1 output (/plan command) - experimental methodology
├── findings/            # Experimental results, analysis, visualizations
└── tasks.md             # Phase 2 output (/tasks command - NOT created by /plan)
```

### Research Code Organization (repository root)

<!--
  ACTION REQUIRED: For research projects, we use experiment-based organization.
  Replace placeholders with actual research requirement IDs and topics.
-->

```text
# Research Project Structure (QUD)

experiments/
├── rr-001-[topic]/           # One directory per Research Requirement
│   ├── README.md             # Hypothesis, validation method, findings
│   ├── prototype.py          # Experimental code (Tier 1 quality)
│   ├── data/                 # Test data or data source links
│   │   ├── hafs-sample.json  # Small test datasets
│   │   └── sources.md        # Links to authoritative data sources
│   └── results/              # Experiment outputs
│       ├── metrics.json      # Performance/accuracy measurements
│       ├── analysis.md       # Findings analysis
│       └── visualizations/   # Charts, graphs, comparisons
│
├── rr-002-[topic]/
│   └── [same structure]
│
└── rr-003-[topic]/
    └── [same structure]

research-tools/                # Reusable utilities (Tier 2 quality)
├── data-loaders/
│   ├── quran_loader.py       # Load from authoritative sources
│   └── narration_parser.py  # Parse narration-specific formats
├── validators/
│   ├── char_count_validator.py
│   ├── verse_validator.py
│   └── narration_validator.py
├── generators/                # Layer generation utilities
│   └── layer_generator.py    # Rule-based layer data generation
└── analyzers/
    ├── performance_metrics.py
    └── data_comparator.py

schemas/                       # Layer schema definitions (CRITICAL)
├── layer-00-qiraat/
│   ├── schema.json            # Formal schema specification
│   └── README.md              # Domain semantics explanation
├── layer-01-characters/
│   ├── schema.json
│   └── README.md
└── [...]                      # Schemas for layers 0-13

docs/
├── research-log.md            # Chronological research findings
├── data-layers/               # Documentation per Quranic data layer
│   ├── layer-00-qiraat.md     # Reading definitions (Layer 0)
│   ├── layer-01-characters.md # Character structure (Layer 1)
│   ├── layer-02-rendering.md  # Rendering data (Layer 2)
│   ├── layer-03-symbols.md    # Character symbols (Layer 3)
│   └── [...]                  # Layers 4-13 documentation
├── decisions/                 # Architecture Decision Records (ADRs)
│   ├── 001-storage-approach.md
│   ├── 002-layer-boundaries.md
│   └── 003-generative-architecture.md
└── sources/                   # Authoritative source documentation
    ├── king-fahd-editions.md
    └── authenticated-reciters.md

# ONLY if building production data pipelines (Tier 3)
data-infrastructure/           # Production-quality code (if needed)
├── pipelines/
├── validators/
└── tests/
```

**Structure Decision**: Research project using experiment-based organization. Each Research Requirement (RR) gets its own `experiments/rr-XXX-topic/` directory for rapid prototyping (Tier 1 quality). Reusable tools go in `research-tools/` (Tier 2 quality). Production infrastructure only created if research validates need for operational data pipelines (Tier 3 quality).

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
