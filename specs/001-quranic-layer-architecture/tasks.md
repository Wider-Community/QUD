# Tasks: Quranic Data Layer Architecture with Contextual Versioning System

**Input**: Research design documents from `/specs/001-quranic-layer-architecture/`
**Prerequisites**: plan.md ✓, spec.md ✓, research.md ✓, data-model.md ✓, experiment-design.md ✓

<!--
  RESEARCH PROJECT NOTE: Tasks focus on EXPERIMENTAL VALIDATION, not production delivery.
  Success = validated hypothesis (confirmed or refuted) + documented findings.
  Code quality follows three-tier model: Tier 1 (experimental), Tier 2 (tools), Tier 3 (production pipelines if needed).
-->

**Tests**: For research projects, "tests" mean VALIDATION EXPERIMENTS. Each Research Requirement (RR) has validation tasks that confirm/refute the hypothesis.

**Organization**: Tasks are grouped by Research Requirement (RR) to enable independent hypothesis validation.

## Format: `- [ ] [ID] [P?] [RR?] Description`

- **- [ ]**: Markdown checkbox (REQUIRED)
- **[ID]**: Sequential task number (T001, T002, etc.)
- **[P]**: Can run in parallel (different experiments, no dependencies)
- **[RR]**: Which Research Requirement this task belongs to (e.g., RR-001, RR-002, RR-003)
- Include exact file paths in descriptions (use `experiments/rr-XXX-topic/` structure)

## Path Conventions

- **Research experiments**: `experiments/rr-XXX-topic/` - one directory per Research Requirement
- **Reusable tools**: `research-tools/` - utilities shared across experiments
- **Layer schemas**: `schemas/layer-XX-name/` - formal schema definitions for all identified layers (currently 17)
- **Documentation**: `docs/research-log.md`, `docs/data-layers/` (layers 0-14), `docs/decisions/`, `docs/architecture/`
- **Production pipelines** (if needed): `data-infrastructure/` - Tier 3 quality code

Paths shown below assume research project structure from plan.md.

---

## Phase 1: Setup (Research Infrastructure)

**Purpose**: Project initialization and foundational research tooling

- [x] T001 Create research project structure per plan.md (experiments/, research-tools/, schemas/, docs/)
- [x] T002 Initialize Python 3.11+ project with pyproject.toml or requirements.txt
- [x] T003 Install scientific computing dependencies (numpy, pandas, NLTK, jsonschema, pydantic)
- [x] T004 [P] Setup documentation templates in docs/ (research-log.md, ADR template)
- [x] T005 [P] Create data layer documentation structure in docs/data-layers/ (currently 17 identified layers)
- [x] T006 [P] Create schema directory structure (schemas/layer-00-character-composition/ through schemas/layer-14-readers-narrators/)
- [x] T007 [P] Create cross-layer mappings schema directory (schemas/cross-layer-mappings/)
- [x] T008 [P] Create context and MUDMAJ schema directories (schemas/context-schema/, schemas/mudmaj-schema/)
- [x] T009 [P] Initialize Jupyter notebook environment for interactive analysis
- [x] T010 [P] Setup visualization libraries (matplotlib, seaborn, plotly)
- [x] T011 [P] Create architecture documentation structure in docs/architecture/ (qud-orchestrator.md, mudmaj-storage.md, contextual-versioning.md)

---

## Phase 2: Foundational Tools (Blocking Prerequisites)

**Purpose**: Core research tools that MUST be complete before ANY Research Requirement experiments can be conducted

**⚠️ CRITICAL**: No RR experimentation can begin until this phase is complete

**Tier 2 Quality Required**: These are reusable tools, not experimental code

### Data Loading & Parsing

- [x] T012 [P] Implement QS-QIRAAT JSON loader in research-tools/data-loaders/quran_loader.py
- [x] T013 [P] Implement Qiraah-specific parser in research-tools/data-loaders/narration_parser.py
- [x] T014 [P] Add support for CSV format loading for validation purposes

### Validators (Zero-Tolerance Quranic Data Integrity)

- [x] T015 [P] Implement character count validator in research-tools/validators/char_count_validator.py (323,015 chars for Hafs)
- [x] T016 [P] Implement verse count validator in research-tools/validators/verse_validator.py (6,236 Hafs, 6,214 Warsh)
- [ ] T017 [P] Implement Qiraah cross-validator in research-tools/validators/qiraah_validator.py
- [x] T018 [P] Implement JSON Schema validator wrapper in research-tools/validators/schema_validator.py
- [x] T019 [P] Implement Pydantic model validator in research-tools/validators/schema_validator.py
- [x] T020 [P] Implement context parameter validator in research-tools/validators/context_validator.py (validates parameter combinations)

### Generation & Analysis Tools

- [x] T021 [P] Create layer generation utility framework in research-tools/generators/layer_generator.py
- [x] T022 [P] Create performance metrics analyzer in research-tools/analyzers/performance_metrics.py
- [x] T023 [P] Create data comparison utility in research-tools/analyzers/data_comparator.py (character-level diff, verse-level diff)
- [x] T024 [P] Create UUID generator utility in research-tools/generators/uuid_generator.py (v4 random vs v5 name-based)
- [x] T025 [P] Create semantic hash generator in research-tools/generators/semantic_hasher.py (SHA-256 for relationship representation)

### Orchestration Utilities (for RR-014-016)

- [x] T026 [P] Create context resolution stub in research-tools/orchestration/context_resolver.py
- [x] T027 [P] Create version selection stub in research-tools/orchestration/version_selector.py
- [x] T028 [P] Create query routing stub in research-tools/orchestration/query_router.py

### Documentation & Provenance

- [x] T029 [P] Document King Fahd Complex editions in docs/sources/king-fahd-editions.md
- [x] T030 [P] Document authenticated reciters in docs/sources/authenticated-reciters.md
- [x] T031 Setup data provenance tracking system (source tags, transformation audit log)
- [x] T032 [P] Create ADR template in docs/decisions/000-template.md

**Checkpoint**: Research tools ready - RR experimentation can now begin in parallel

---

## Phase 3: RR-001 - Layer Separation Analysis (Priority: P1) 🎯 First Hypothesis

**Research Goal**: Identify which of the Quranic data layers (currently 17 identified layers) are currently mixed in the QS-QIRAAT dataset

**Hypothesis**: The QS-QIRAAT dataset conflates multiple distinct layers into a single flat data structure, and this conflation can be identified and quantified through schema analysis.

**Independent Validation**: Manual mapping of each QS-QIRAAT field to the layer taxonomy (currently 17 identified layers) produces a complete mapping table and layer conflation matrix.

**Data Layer Dependencies**: Requires understanding of all identified layers (currently 17) to perform mapping analysis. NOTE: The exact number is under investigation per 2025-11-04 update.

### Experiment Setup for RR-001

**Tier 1 Quality - Experimental Code**

- [x] T033 [RR-001] Create experiment directory: experiments/rr-001-layer-analysis/
- [x] T034 [RR-001] Document hypothesis in experiments/rr-001-layer-analysis/README.md
- [x] T035 [P] [RR-001] Gather QS-QIRAAT Hafs dataset (6,236 verses) in experiments/rr-001-layer-analysis/data/
- [x] T036 [P] [RR-001] Gather Hafs and Warsh datasets (12,450 verse records total) for Phase 1 cross-Qiraah analysis per Constitution VI. Note: Remaining 5 narrations deferred to Phase 2-3.
- [x] T037 [P] [RR-001] Validate source data using char_count_validator and verse_validator from research-tools

### Analysis Implementation for RR-001

- [ ] T038 [RR-001] Create analysis notebook in experiments/rr-001-layer-analysis/analysis.ipynb
- [x] T039 [RR-001] Mark experimental code with # EXPERIMENTAL: comments
- [x] T040 [RR-001] Build field→layer mapping analyzer in experiments/rr-001-layer-analysis/field_mapper.py
- [x] T041 [RR-001] Analyze QS-QIRAAT schema (11 fields: id, jozz, page, sura_no, sura_name_en, sura_name_ar, line_start, line_end, aya_no, aya_text, aya_text_emlaey)
- [x] T042 [RR-001] Map each field to one or more QUD layers (currently 17 identified layers) with confidence scores
- [x] T043 [RR-001] Identify conflated fields (e.g., aya_text conflates multiple layers)

### Cross-Recitation Analysis for RR-001 (Phase 1: Hafs & Warsh)

- [x] T044 [RR-001] Compare Hafs and Warsh datasets (Phase 1 scope) to identify field variance. Document findings that likely generalize to remaining narrations for Phase 2-3.
- [x] T045 [RR-001] Classify fields as Qiraah-specific vs shared (indicates layer concerns)
- [x] T046 [RR-001] Document verse count differences (Hafs 6,236 vs Warsh 6,214)

### Deliverables for RR-001

- [x] T047 [RR-001] Generate mapping table (QS-QIRAAT field → QUD layer) in experiments/rr-001-layer-analysis/results/mapping_table.csv
- [x] T048 [RR-001] Generate conflation matrix (NxN matrix of which layers mixed in which fields) in experiments/rr-001-layer-analysis/results/conflation_matrix.csv
- [x] T049 [RR-001] Generate gap analysis (which of the identified layers missing from QS-QIRAAT) in experiments/rr-001-layer-analysis/results/gap_analysis.md
- [x] T050 [RR-001] Generate cross-Qiraah variance report in experiments/rr-001-layer-analysis/results/narration_variance.md
- [ ] T051 [RR-001] Create visualizations (layer conflation heatmap, field→layer mapping diagram) in experiments/rr-001-layer-analysis/results/visualizations/

### Findings Documentation for RR-001

- [x] T052 [RR-001] Analyze results in experiments/rr-001-layer-analysis/results/analysis.md
- [x] T053 [RR-001] Document hypothesis outcome (confirmed/refuted) with evidence
- [x] T054 [RR-001] Update research log in docs/research-log.md with RR-001 findings
- [x] T055 [RR-001] Identify which layers are explicitly present, implicitly present, or missing

**Checkpoint**: RR-001 hypothesis validated - we know exactly what's mixed in QS-QIRAAT

---

## Phase 4: RR-002 - Schema Design for Separated Layers (Priority: P2)

**Research Goal**: Define formal schemas for each of the identified Quranic data layers (currently 17) that eliminate conflation, enable generative architecture, and include UUID-based cross-layer mappings.

**Hypothesis**: A schema-first approach defining all identified layers independently will reduce data redundancy by >40%, enable cross-Qiraah queries currently impossible in QS-QIRAAT, and support generative architecture.

**Independent Validation**: Transformation of QS-QIRAAT Hafs data into multi-layer format with zero information loss (reverse transformation reconstructs original).

**Data Layer Dependencies**: Defines schemas for all identified layers (currently 17).

**Dependencies on Prior RRs**: Builds on RR-001 field→layer mapping to design separated schemas.

### Experiment Setup for RR-002

- [ ] T056 [RR-002] Create experiment directory: experiments/rr-002-schema-design/
- [ ] T057 [RR-002] Document hypothesis and RR-001 dependencies in experiments/rr-002-schema-design/README.md
- [ ] T058 [RR-002] Use RR-001 mapping table as input for schema design

### Schema Definition for All Identified Layers (WITH UUID SUPPORT)

**NOTE**: Currently 17 identified layers; exact count under investigation per 2025-11-04 update

#### Layer 0: Character Composition

- [ ] T059 [P] [RR-002] Define JSON Schema for Layer 0 in schemas/layer-00-character-composition/schema.json
- [ ] T060 [P] [RR-002] Define Pydantic model for Layer 0 in schemas/layer-00-character-composition/models.py
- [ ] T061 [P] [RR-002] Document Layer 0 domain semantics in schemas/layer-00-character-composition/README.md (base letters, phonetic metadata, UUID for orthographic mapping)

#### Layer 1: Character Symbols and Rendering

- [ ] T062 [P] [RR-002] Define JSON Schema for Layer 1 in schemas/layer-01-rendering-symbols/schema.json
- [ ] T063 [P] [RR-002] Define Pydantic model for Layer 1 in schemas/layer-01-rendering-symbols/models.py
- [ ] T064 [P] [RR-002] Document Layer 1 domain semantics in schemas/layer-01-rendering-symbols/README.md (diacritics, rendering rules, UUID)

#### Layer 2: Character Paired Data

- [ ] T065 [P] [RR-002] Define JSON Schema for Layer 2 in schemas/layer-02-paired-data/schema.json
- [ ] T066 [P] [RR-002] Define Pydantic model for Layer 2 in schemas/layer-02-paired-data/models.py
- [ ] T067 [P] [RR-002] Document Layer 2 domain semantics in schemas/layer-02-paired-data/README.md (tajweed marks, pair relationships, UUID)

#### Layer 3: Word Structure

- [ ] T068 [P] [RR-002] Define JSON Schema for Layer 3 in schemas/layer-03-word-structure/schema.json
- [ ] T069 [P] [RR-002] Define Pydantic model for Layer 3 in schemas/layer-03-word-structure/models.py
- [ ] T070 [P] [RR-002] Document Layer 3 domain semantics in schemas/layer-03-word-structure/README.md (word boundaries, morphology, UUID)

#### Layer 4: Sentence Structure

- [ ] T071 [P] [RR-002] Define JSON Schema for Layer 4 in schemas/layer-04-sentence-structure/schema.json
- [ ] T072 [P] [RR-002] Define Pydantic model for Layer 4 in schemas/layer-04-sentence-structure/models.py
- [ ] T073 [P] [RR-002] Document Layer 4 domain semantics in schemas/layer-04-sentence-structure/README.md (grammar, waqf/ibtida, UUID)

#### Layer 5: Verse Structure

- [ ] T074 [P] [RR-002] Define JSON Schema for Layer 5 in schemas/layer-05-verse-structure/schema.json
- [ ] T075 [P] [RR-002] Define Pydantic model for Layer 5 in schemas/layer-05-verse-structure/models.py (MUST include canonical_verse_id for verse numbering resolution)
- [ ] T076 [P] [RR-002] Document Layer 5 domain semantics in schemas/layer-05-verse-structure/README.md (verse boundaries, canonical_verse_id, UUID for Hafs↔Warsh mapping)

#### Layer 6: Surah Structure

- [ ] T077 [P] [RR-002] Define JSON Schema for Layer 6 in schemas/layer-06-surah-structure/schema.json
- [ ] T078 [P] [RR-002] Define Pydantic model for Layer 6 in schemas/layer-06-surah-structure/models.py
- [ ] T079 [P] [RR-002] Document Layer 6 domain semantics in schemas/layer-06-surah-structure/README.md (surah metadata, verse grouping, UUID)

#### Layer 7: Division Structure

- [ ] T080 [P] [RR-002] Define JSON Schema for Layer 7 in schemas/layer-07-division-structure/schema.json
- [ ] T081 [P] [RR-002] Define Pydantic model for Layer 7 in schemas/layer-07-division-structure/models.py
- [ ] T082 [P] [RR-002] Document Layer 7 domain semantics in schemas/layer-07-division-structure/README.md (Juz/Hizb/Rub, UUID)

#### Layer 8: Chapter Structure

- [ ] T083 [P] [RR-002] Define JSON Schema for Layer 8 in schemas/layer-08-chapter-structure/schema.json
- [ ] T084 [P] [RR-002] Define Pydantic model for Layer 8 in schemas/layer-08-chapter-structure/models.py
- [ ] T085 [P] [RR-002] Document Layer 8 domain semantics in schemas/layer-08-chapter-structure/README.md (Makki/Madani, themes, UUID)

#### Layer 9: Qiraah Manuscript

- [ ] T086 [P] [RR-002] Define JSON Schema for Layer 9 in schemas/layer-09-narration-manuscript/schema.json
- [ ] T087 [P] [RR-002] Define Pydantic model for Layer 9 in schemas/layer-09-narration-manuscript/models.py
- [ ] T088 [P] [RR-002] Document Layer 9 domain semantics in schemas/layer-09-narration-manuscript/README.md (Qiraah/narration variants, UUID)

#### Layer 10: Edition Variants

- [ ] T089 [P] [RR-002] Define JSON Schema for Layer 10 in schemas/layer-10-edition-variants/schema.json
- [ ] T090 [P] [RR-002] Define Pydantic model for Layer 10 in schemas/layer-10-edition-variants/models.py
- [ ] T091 [P] [RR-002] Document Layer 10 domain semantics in schemas/layer-10-edition-variants/README.md (publisher variations, UUID)

#### Layer 11: Page Layout

- [ ] T092 [P] [RR-002] Define JSON Schema for Layer 11 in schemas/layer-11-page-layout/schema.json
- [ ] T093 [P] [RR-002] Define Pydantic model for Layer 11 in schemas/layer-11-page-layout/models.py
- [ ] T094 [P] [RR-002] Document Layer 11 domain semantics in schemas/layer-11-page-layout/README.md (page numbers, page breaks, UUID)

#### Layer 12: Line Layout

- [ ] T095 [P] [RR-002] Define JSON Schema for Layer 12 in schemas/layer-12-line-layout/schema.json
- [ ] T096 [P] [RR-002] Define Pydantic model for Layer 12 in schemas/layer-12-line-layout/models.py
- [ ] T097 [P] [RR-002] Document Layer 12 domain semantics in schemas/layer-12-line-layout/README.md (line breaks, character ranges, UUID)

#### Layer 13: Orthographic Systems

- [ ] T098 [P] [RR-002] Define JSON Schema for Layer 13 in schemas/layer-13-orthographic-systems/schema.json (Uthmani vs Qiasy)
- [ ] T099 [P] [RR-002] Define Pydantic model for Layer 13 in schemas/layer-13-orthographic-systems/models.py
- [ ] T100 [P] [RR-002] Document Layer 13 domain semantics in schemas/layer-13-orthographic-systems/README.md (script systems, transformation rules, UUID for expansion/contraction)

#### Layer 14: Readers and Narrators

- [ ] T101 [P] [RR-002] Define JSON Schema for Layer 14 in schemas/layer-14-readers-narrators/schema.json
- [ ] T102 [P] [RR-002] Define Pydantic model for Layer 14 in schemas/layer-14-readers-narrators/models.py
- [ ] T103 [P] [RR-002] Document Layer 14 domain semantics in schemas/layer-14-readers-narrators/README.md (reader biographical data, isnad chains, UUID)

### Cross-Layer Mapping Schema

- [ ] T104 [RR-002] Define EntityMapping JSON Schema in schemas/cross-layer-mappings/entity-mapping-schema.json
- [ ] T105 [RR-002] Define EntityMapping Pydantic model in schemas/cross-layer-mappings/mapping-models.py
- [ ] T106 [RR-002] Implement semantic hasher in schemas/cross-layer-mappings/semantic-hasher.py
- [ ] T107 [RR-002] Document cross-layer mapping strategies in schemas/cross-layer-mappings/README.md (expansion/contraction cases, bidirectional mappings)

### Schema Validation for RR-002

- [ ] T108 [RR-002] Create schema validation test suite in experiments/rr-002-schema-design/validate_schemas.py
- [ ] T109 [RR-002] Test all 15 layer schemas with sample data
- [ ] T110 [RR-002] Validate schema completeness (all QS-QIRAAT fields mapped to schemas)
- [ ] T111 [RR-002] Validate cross-layer references (UUIDs properly defined)

### Transformation Algorithm for RR-002

- [ ] T112 [RR-002] Design transformation algorithm (QS-QIRAAT → 15-layer format) in experiments/rr-002-schema-design/transformation_spec.md
- [ ] T113 [RR-002] Document reverse transformation (15-layer → QS-QIRAAT) to prove information preservation
- [ ] T114 [RR-002] Create transformation flowchart/diagram in experiments/rr-002-schema-design/results/transformation_flow.png

### Findings Documentation for RR-002

- [ ] T115 [RR-002] Document schema design rationale in experiments/rr-002-schema-design/results/design_rationale.md
- [ ] T116 [RR-002] Create ADR for dual schema approach (JSON Schema + Pydantic) in docs/decisions/001-dual-schema-approach.md
- [ ] T117 [RR-002] Update research log in docs/research-log.md with RR-002 findings
- [ ] T118 [RR-002] Document any schema refinements needed based on validation

**Checkpoint**: RR-002 complete - all 15 layer schemas defined with UUID support

---

## Phase 5: RR-003 - Layer Simulation Prototype (Priority: P3)

**Research Goal**: Build a working simulation that ingests QS-QIRAAT data, transforms it into the 15-layer architecture, demonstrates generative layer production (Layer 0→2), and validates against authoritative sources.

**Hypothesis**: A simulation processing **Hafs (6,236 verses) and Warsh (6,214 verses) = 12,450 total verse records** (Phase 1 per Constitution VI) can successfully separate layers, generate derivative layers via rules, conform to schemas with <1% error rate, and enable previously impossible cross-Qiraah queries. Phase 2-3 will scale to remaining narrations (43,652 total records).

**Independent Validation**: Simulation processes Hafs and Warsh (Phase 1), passes automated validation (character/verse counts), enables 3+ new query types, scholarly review confirms theological accuracy. Phase 2-3 extends to remaining narrations.

**Data Layer Dependencies**: Uses ALL 15 layers (0-14). Demonstrates both extraction from QS-QIRAAT and generation via rules.

**Dependencies on Prior RRs**: Depends on RR-001 (knows what's mixed) and RR-002 (has schemas to separate into).

### Experiment Setup for RR-003

- [ ] T119 [RR-003] Create experiment directory: experiments/rr-003-layer-simulation/
- [ ] T120 [RR-003] Document hypothesis and dependencies (RR-001, RR-002) in experiments/rr-003-layer-simulation/README.md
- [ ] T121 [P] [RR-003] Load Hafs (6,236 verses) and Warsh (6,214 verses) datasets = 12,450 verse records total (Phase 1 per Constitution VI)
- [ ] T122 [P] [RR-003] Validate all source data using research-tools validators

### Prototype Implementation for RR-003

- [ ] T123 [RR-003] Build main simulation script in experiments/rr-003-layer-simulation/simulation.py
- [ ] T124 [RR-003] Mark experimental code with # EXPERIMENTAL: comments
- [ ] T125 [RR-003] Implement QS-QIRAAT → Layer 0 (Character Composition) extraction
- [ ] T126 [RR-003] Implement QS-QIRAAT → Layer 1 (Symbols/Rendering) extraction
- [ ] T127 [RR-003] Implement QS-QIRAAT → Layer 2 (Paired Data) extraction
- [ ] T128 [RR-003] Implement QS-QIRAAT → Layer 3 (Word Structure) extraction
- [ ] T129 [RR-003] Implement QS-QIRAAT → Layer 5 (Verse Structure) extraction (with canonical_verse_id)
- [ ] T130 [RR-003] Implement QS-QIRAAT → Layer 6 (Surah Structure) extraction
- [ ] T131 [RR-003] Implement QS-QIRAAT → Layer 7 (Division Structure) extraction
- [ ] T132 [RR-003] Implement QS-QIRAAT → Layer 8 (Chapter Structure) extraction
- [ ] T133 [RR-003] Implement QS-QIRAAT → Layer 11 (Page Layout) extraction
- [ ] T134 [RR-003] Implement QS-QIRAAT → Layer 12 (Line Layout) extraction
- [ ] T135 [RR-003] Implement QS-QIRAAT → Layer 13 (Orthographic Systems) extraction

### Generative Layer Production for RR-003

- [ ] T136 [RR-003] Implement Layer 0 → Layer 2 generation (characters + tajweed rules → paired data)
- [ ] T137 [RR-003] Implement Qiraah-specific tajweed rules for Hafs
- [ ] T138 [RR-003] Test generative layer production on Al-Fatiha (7 verses)
- [ ] T139 [RR-003] Validate generated Layer 2 against QS-QIRAAT original data (>95% accuracy target)

### UUID Assignment and Cross-Layer Mapping

- [ ] T140 [RR-003] Assign UUIDs to all entities in all 15 layers (~400,000+ UUIDs)
- [ ] T141 [RR-003] Create EntityMapping records for Layer 0↔13 (orthographic mappings)
- [ ] T142 [RR-003] Create EntityMapping records for Layer 5 Hafs↔Warsh (verse boundary variations)
- [ ] T143 [RR-003] Generate semantic hashes for all mappings
- [ ] T144 [RR-003] Validate bidirectional mapping integrity

### Validation Execution for RR-003

- [ ] T145 [RR-003] Run simulation on Hafs and Warsh narrations (Phase 1 per Constitution VI). Note: Remaining 5 narrations deferred to Phase 2-3.
- [ ] T146 [RR-003] Validate character counts (Hafs: 323,015 characters - 100% match required)
- [ ] T147 [RR-003] Validate verse counts (Hafs: 6,236, Warsh: 6,214 - 100% match required)
- [ ] T148 [RR-003] Run schema validation on all generated layer data using schema_validator
- [ ] T149 [RR-003] Collect performance metrics (processing time, memory usage) in experiments/rr-003-layer-simulation/results/metrics.json
- [ ] T150 [RR-003] Document validation failures for analysis (schema violations, generation errors)

### Cross-Recitation Query Demonstration

- [ ] T151 [RR-003] Create sample SQLite database with separated layer data
- [ ] T152 [RR-003] Implement Query 1: "Find character-level differences between Hafs and Warsh for Surah Al-Baqarah"
- [ ] T153 [RR-003] Implement Query 2: "Extract page layout independent of textual content"
- [ ] T154 [RR-003] Implement Query 3: "Regenerate manuscript with different orthographic system"
- [ ] T155 [RR-003] Document query impossibility in QS-QIRAAT flat format vs success in layered format

### Redundancy Reduction Analysis

- [ ] T156 [RR-003] Measure QS-QIRAAT storage size (JSON format for Hafs and Warsh - Phase 1). Compare to 15-layer format storage.
- [ ] T157 [RR-003] Measure 15-layer format storage size (with normalized layers 6, 7, 8, 11, 12)
- [ ] T158 [RR-003] Calculate redundancy reduction percentage (hypothesis: >40%)
- [ ] T159 [RR-003] Document redundancy analysis in experiments/rr-003-layer-simulation/results/redundancy_analysis.md

### Visualizations for RR-003

- [ ] T160 [RR-003] Create layer relationship diagram showing 15 layers and dependencies
- [ ] T161 [RR-003] Create conflation pattern visualization (before/after layer separation)
- [ ] T162 [RR-003] Create cross-Qiraah difference visualization (Hafs vs Warsh)
- [ ] T163 [RR-003] Store visualizations in experiments/rr-003-layer-simulation/results/visualizations/

### Findings Documentation for RR-003

- [ ] T164 [RR-003] Analyze simulation results in experiments/rr-003-layer-simulation/results/analysis.md
- [ ] T165 [RR-003] Document hypothesis outcome (confirmed/refuted) with evidence
- [ ] T166 [RR-003] Document what worked, what failed, what schema refinements needed
- [ ] T167 [RR-003] Update research log in docs/research-log.md with RR-003 findings
- [ ] T168 [RR-003] Schedule scholarly review for theological accuracy validation
- [ ] T169 [RR-003] Create ADR for generation approach in docs/decisions/003-generative-architecture.md

**Checkpoint**: RR-003 complete - layered architecture validated with working prototype

---

## Phase 6: Supporting Research Requirements (RR-004 through RR-010)

**Purpose**: Validate specific aspects of the layered architecture discovered in RR-001-003

### RR-004: Cross-Recitation Field Variance Analysis

- [ ] T170 [RR-004] Create experiment directory: experiments/rr-004-field-mapping/
- [ ] T171 [RR-004] Compare Hafs and Warsh datasets (Phase 1 per Constitution VI) to identify field variance patterns. Document generalizability to remaining narrations.
- [ ] T172 [RR-004] Classify fields as Qiraah-specific vs shared
- [ ] T173 [RR-004] Document findings in experiments/rr-004-field-mapping/results/variance_report.md

### RR-005-006: Schema Validation and Generative Architecture

- [ ] T174 [RR-005] Validate that RR-002 schemas eliminate conflation identified in RR-001-003
- [ ] T175 [RR-005] Prove information preservation (reverse transformation test)
- [ ] T176 [RR-006] Validate generative architecture (Layer 0 + rules → Layer 2 with >95% accuracy)
- [ ] T177 [RR-006] Document generation rules for Qiraah-specific tajweed

### RR-007-008: Transformation and Validation

- [ ] T178 [RR-007] Validate complete Hafs transformation (6,236 verses) - already covered in RR-003
- [ ] T179 [RR-008] Validate 100% verse count accuracy - already covered in RR-003
- [ ] T180 [RR-008] Validate >99% character count accuracy - already covered in RR-003

### RR-009: Cross-Recitation Query Demonstration

- [ ] T181 [RR-009] Demonstrate 3+ impossible queries in QS-QIRAAT now possible - already covered in RR-003

### RR-010: Redundancy Reduction Measurement

- [ ] T182 [RR-010] Measure and document redundancy reduction - already covered in RR-003
- [ ] T183 [RR-010] Validate >40% hypothesis or document actual percentage

**Note**: RR-004 through RR-010 are largely validated through RR-001-003 experiments. This phase consolidates findings.

---

## Phase 7: RR-011 - UUID-Based Cross-Layer Mapping System

**Research Goal**: Design and implement UUID-based cross-layer mapping system that handles expansion/contraction cases (1-to-many, many-to-1 mappings), tracks versioned mappings, and generates semantic hashes.

**Hypothesis**: UUID-based entity identification with bidirectional mappings and semantic hashing can resolve verse numbering controversies and handle orthographic transformations with positional precision.

**Independent Validation**: All entities have UUIDs, EntityMapping records created for critical relationships, bidirectional traversal successful, correct cardinality representation.

**Data Layer Dependencies**: ALL 15 layers (all entities need UUIDs), critical for Layers 0, 5, 13 (orthographic and verse mapping).

**Dependencies on Prior RRs**: Depends on RR-002 (schemas must have UUID fields).

### Experiment Setup for RR-011

- [ ] T184 [RR-011] Create experiment directory: experiments/rr-011-uuid-system/
- [ ] T185 [RR-011] Document hypothesis in experiments/rr-011-uuid-system/README.md
- [ ] T186 [RR-011] Design UUID assignment strategy (v4 random vs v5 name-based) in experiments/rr-011-uuid-system/uuid_strategy.md

### UUID Assignment Implementation

- [ ] T187 [RR-011] Implement UUID generator for all layer entities in experiments/rr-011-uuid-system/uuid_assigner.py
- [ ] T188 [RR-011] Assign UUIDs to Layer 0 entities (323,015 characters for Hafs)
- [ ] T189 [RR-011] Assign UUIDs to Layer 5 entities (6,236 verses for Hafs, 6,214 for Warsh)
- [ ] T190 [RR-011] Assign UUIDs to all other layer entities (~400,000+ total UUIDs)

### EntityMapping Implementation

- [ ] T191 [RR-011] Implement EntityMapping creator in experiments/rr-011-uuid-system/mapping_creator.py
- [ ] T192 [RR-011] Create bidirectional mappings with forward and reverse references
- [ ] T193 [RR-011] Implement position_metadata for expansion/contraction cases
- [ ] T194 [RR-011] Implement semantic hash generation for relationships
- [ ] T195 [RR-011] Test cardinality representation (1:1, 1:N, N:1, N:M)

### Validation for RR-011

- [ ] T196 [RR-011] Validate all entities have unique UUIDs within their layer
- [ ] T197 [RR-011] Validate bidirectional traversal (forward and reverse mappings work)
- [ ] T198 [RR-011] Validate semantic hash generation (deterministic and unique per relationship)
- [ ] T199 [RR-011] Test UUID-based entity lookup performance
- [ ] T200 [RR-011] Document findings in experiments/rr-011-uuid-system/results/analysis.md

### ADR for RR-011

- [ ] T201 [RR-011] Create ADR for UUID mapping strategy in docs/decisions/004-uuid-mapping-strategy.md
- [ ] T202 [RR-011] Update research log with RR-011 findings

**Checkpoint**: UUID system validated - all entities identifiable, mappings bidirectional

---

## Phase 8: RR-012 - Multi-Layer Contextual Versioning

**Research Goal**: Demonstrate that ALL 15 layers (not just verses) can have context-specific versions determined by a set of contextual parameters (narration, orthography, edition, scholarly tradition).

**Hypothesis**: Multi-layer contextual versioning system can prove that verse numbering controversy is ONE instance of a broader problem, and canonical identity mappings work across context versions.

**Independent Validation**: Show that a single layer (e.g., Layer 0) has multiple versions (hafs-uthmani, hafs-qiasy, warsh-uthmani, warsh-qiasy), cross-context queries execute successfully, canonical_verse_id resolves Hafs↔Warsh numbering.

**Data Layer Dependencies**: ALL 15 layers (each can have context-specific versions).

**Dependencies on Prior RRs**: Depends on RR-002 (schemas with UUID), RR-011 (UUID mappings).

### Experiment Setup for RR-012

- [ ] T203 [RR-012] Create experiment directory: experiments/rr-012-contextual-versioning/
- [ ] T204 [RR-012] Document hypothesis in experiments/rr-012-contextual-versioning/README.md
- [ ] T205 [RR-012] Design context schema (HYPOTHETICAL) in experiments/rr-012-contextual-versioning/context_design.md

### Multi-Version Layer Demonstration

- [ ] T206 [RR-012] Create Layer 0 version for hafs-uthmani context
- [ ] T207 [RR-012] Create Layer 0 version for hafs-qiasy context
- [ ] T208 [RR-012] Create Layer 0 version for warsh-uthmani context
- [ ] T209 [RR-012] Create Layer 0 version for warsh-qiasy context
- [ ] T210 [RR-012] Create Layer 5 version for hafs context (6,236 verses)
- [ ] T211 [RR-012] Create Layer 5 version for warsh context (6,214 verses)

### Canonical Identity Mapping

- [ ] T212 [RR-012] Implement canonical_verse_id for cross-Qiraah verse identity
- [ ] T213 [RR-012] Map Hafs Surah 2 verses to Warsh Surah 2 verses using canonical_verse_id
- [ ] T214 [RR-012] Validate all 22 verse count differences between Hafs and Warsh are mapped

### Cross-Context Query Implementation

- [ ] T215 [RR-012] Implement query: "Compare Layer 5 (Verse) in hafs-context vs warsh-context"
- [ ] T216 [RR-012] Implement query: "Show same verse in all orthographic systems"
- [ ] T217 [RR-012] Validate cross-context queries return correct context-specific data

### Validation for RR-012

- [ ] T218 [RR-012] Validate that verse numbering controversy is resolved via canonical_verse_id
- [ ] T219 [RR-012] Validate that multi-layer versioning works (not just verses)
- [ ] T220 [RR-012] Document findings in experiments/rr-012-contextual-versioning/results/analysis.md
- [ ] T221 [RR-012] Update research log with RR-012 findings

**Checkpoint**: Multi-layer contextual versioning validated - verse numbering controversy is broader problem

---

## Phase 9: RR-013 - Orthographic Transformation Mapping

**Research Goal**: Demonstrate orthographic transformation handling by mapping character entities between Uthmani and Qiasy/Imla'i orthographies with positional precision, enabling reconstruction of either orthography from the other.

**Hypothesis**: Character-level UUID mappings can track expansion (1 Uthmani char → 2 Qiasy chars) and contraction cases with sufficient precision for bidirectional reconstruction.

**Independent Validation**: At least 10 expansion cases documented and mapped, bidirectional reconstruction successful, semantic hashes generated.

**Data Layer Dependencies**: Layers 0 (Character Composition), 13 (Orthographic Systems).

**Dependencies on Prior RRs**: Depends on RR-002 (schemas), RR-011 (UUID mappings).

### Experiment Setup for RR-013

- [ ] T222 [RR-013] Create experiment directory: experiments/rr-013-orthographic-mapping/
- [ ] T223 [RR-013] Document hypothesis in experiments/rr-013-orthographic-mapping/README.md
- [ ] T224 [RR-013] Research orthographic transformation rules (Uthmani↔Qiasy)

### Expansion/Contraction Case Documentation

- [ ] T225 [RR-013] Identify 10+ expansion cases (1 Uthmani → 2 Qiasy) in QS-QIRAAT data
- [ ] T226 [RR-013] Document transformation rules in experiments/rr-013-orthographic-mapping/transformation_rules.md
- [ ] T227 [RR-013] Create test dataset with known expansion/contraction cases

### Mapping Implementation

- [ ] T228 [RR-013] Implement character-level UUID mapping for orthographic transformations
- [ ] T229 [RR-013] Add position_metadata for ordering preservation
- [ ] T230 [RR-013] Implement bidirectional mapping (Uthmani→Qiasy and Qiasy→Uthmani)
- [ ] T231 [RR-013] Generate semantic hashes for orthographic mappings

### Reconstruction Validation

- [ ] T232 [RR-013] Test Uthmani → Qiasy reconstruction using UUID traversal
- [ ] T233 [RR-013] Test Qiasy → Uthmani reconstruction using UUID traversal
- [ ] T234 [RR-013] Validate byte-for-byte accuracy of reconstructed text
- [ ] T235 [RR-013] Document reconstruction success rate in experiments/rr-013-orthographic-mapping/results/reconstruction_report.md

### Validation for RR-013

- [ ] T236 [RR-013] Validate 10+ expansion cases correctly mapped
- [ ] T237 [RR-013] Validate bidirectional reconstruction successful
- [ ] T238 [RR-013] Validate semantic hashes unique per mapping
- [ ] T239 [RR-013] Document findings in experiments/rr-013-orthographic-mapping/results/analysis.md
- [ ] T240 [RR-013] Update research log with RR-013 findings

**Checkpoint**: Orthographic transformation validated - character-level mappings support bidirectional reconstruction

---

## Phase 10: RR-014 - QUD Orchestrator Context Resolution Design

**Research Goal**: Design QUD Orchestrator component that extracts context parameters from queries, resolves layer versions, and routes queries to appropriate MUDMAJ layer versions.

**Hypothesis**: A context resolution algorithm can map query parameters to specific layer versions with <100ms overhead, handle cross-context queries, and maintain context isolation.

**Independent Validation**: Context parameters validated against scholarly sources, context resolution produces correct layer versions, cross-context queries return correct results, performance targets met.

**Data Layer Dependencies**: Meta-layer (operates on top of all 15 layers).

**Dependencies on Prior RRs**: Depends on RR-002 (schemas), RR-011-013 (UUID mappings).

### Experiment Setup for RR-014

- [ ] T241 [RR-014] Create experiment directory: experiments/rr-014-orchestrator/
- [ ] T242 [RR-014] Document hypothesis in experiments/rr-014-orchestrator/README.md

### Context Parameter Discovery

- [ ] T243 [RR-014] Analyze QS-QIRAAT to identify actual context parameters (which narrations, orthographies, editions present)
- [ ] T244 [RR-014] Research Quranic scholarly literature to identify valid tajweed schools
- [ ] T245 [RR-014] Define minimal context parameters in experiments/rr-014-orchestrator/context_schema.json (HYPOTHETICAL - to be validated)
- [ ] T246 [RR-014] Document context parameter dependencies (e.g., tajweed_school → geographic_origin)

### Context Inheritance Rules Design

- [ ] T247 [RR-014] Map context parameters to layers (which params affect which layers)
- [ ] T248 [RR-014] Design inheritance hierarchy in experiments/rr-014-orchestrator/inheritance_rules.md
- [ ] T249 [RR-014] Implement parameter propagation algorithm

### Context Resolution Algorithm

- [ ] T250 [RR-014] Design context extraction from queries in experiments/rr-014-orchestrator/query_parser.py
- [ ] T251 [RR-014] Implement context hash generation (SHA-256 of sorted parameters)
- [ ] T252 [RR-014] Design version selection logic (context hash → layer version lookup)
- [ ] T253 [RR-014] Implement fallback strategy for ambiguous contexts

### Query Routing Design

- [ ] T254 [RR-014] Design query flow diagram in experiments/rr-014-orchestrator/results/query_flow.png
- [ ] T255 [RR-014] Implement routing logic for single-context queries
- [ ] T256 [RR-014] Implement routing logic for cross-context queries
- [ ] T257 [RR-014] Implement routing logic for cross-layer queries within context

### Cross-Context Query Handler

- [ ] T258 [RR-014] Implement cross-context comparison for "Compare verse X in Hafs vs Warsh"
- [ ] T259 [RR-014] Implement character-level diff for text comparisons
- [ ] T260 [RR-014] Implement UUID-based alignment for entity comparisons

### Orchestrator Prototype

- [ ] T261 [RR-014] Implement QUDOrchestrator class in experiments/rr-014-orchestrator/orchestrator.py
- [ ] T262 [RR-014] Test single-context query: "Get Surah Al-Fatiha in Hafs"
- [ ] T263 [RR-014] Test cross-context query: "Compare Al-Fatiha Hafs vs Warsh"
- [ ] T264 [RR-014] Test cross-layer query: "Get verse text with page layout info"
- [ ] T265 [RR-014] Measure context resolution performance (<100ms target)

### Validation for RR-014

- [ ] T266 [RR-014] Validate context parameter set against scholarly sources
- [ ] T267 [RR-014] Validate context resolution produces correct layer versions
- [ ] T268 [RR-014] Validate cross-context queries return correct results
- [ ] T269 [RR-014] Validate performance targets met (<100ms context resolution)
- [ ] T270 [RR-014] Validate context isolation (no data leakage between contexts)
- [ ] T271 [RR-014] Document findings in experiments/rr-014-orchestrator/results/analysis.md
- [ ] T272 [RR-014] Update research log with RR-014 findings
- [ ] T273 [RR-014] Create ADR for context schema design in docs/decisions/005-context-schema-design.md

**Checkpoint**: QUD Orchestrator validated - context resolution works, queries route correctly

---

## Phase 11: RR-015 - MUDMAJ Database Schema Design

**Research Goal**: Design MUDMAJ storage schema that organizes multiple layer versions per context, implements efficient delta storage, and optimizes for query performance.

**Hypothesis**: Well-designed storage schema can achieve >40% storage savings through delta optimization while maintaining <100ms query performance for context-based lookups.

**Independent Validation**: Storage technology choice justified with benchmarks, VersionRegistry achieves <100ms lookups, delta storage achieves savings target, provenance tracking complete.

**Data Layer Dependencies**: Meta-layer (storage for all 15 layers).

**Dependencies on Prior RRs**: Depends on RR-002 (layer schemas), RR-014 (context schema).

### Experiment Setup for RR-015

- [ ] T274 [RR-015] Create experiment directory: experiments/rr-015-mudmaj-schema/
- [ ] T275 [RR-015] Document hypothesis in experiments/rr-015-mudmaj-schema/README.md

### Storage Technology Selection

- [ ] T276 [RR-015] Evaluate SQL (PostgreSQL) for MUDMAJ storage
- [ ] T277 [RR-015] Evaluate NoSQL (MongoDB) for MUDMAJ storage
- [ ] T278 [RR-015] Evaluate Graph DB (Neo4j) for MUDMAJ storage
- [ ] T279 [RR-015] Evaluate Hybrid approach (SQL metadata + NoSQL layer data)
- [ ] T280 [RR-015] Benchmark context-based lookup queries across technologies
- [ ] T281 [RR-015] Benchmark cross-layer join queries across technologies
- [ ] T282 [RR-015] Benchmark cross-context comparison queries across technologies
- [ ] T283 [RR-015] Document technology selection decision in experiments/rr-015-mudmaj-schema/results/technology_selection.md
- [ ] T284 [RR-015] Create ADR for storage technology choice in docs/decisions/006-mudmaj-storage-technology.md

### Version Registry Design

- [ ] T285 [RR-015] Design VersionRegistry schema in experiments/rr-015-mudmaj-schema/version_registry_schema.sql
- [ ] T286 [RR-015] Implement context hash generator
- [ ] T287 [RR-015] Create indexes for (layer_number, context_hash) O(1) lookups
- [ ] T288 [RR-015] Test registry query performance (<100ms target)

### LayerVersion Metadata Schema

- [ ] T289 [RR-015] Design LayerVersion table schema in experiments/rr-015-mudmaj-schema/layer_version_schema.sql
- [ ] T290 [RR-015] Implement version lineage tracking (parent_version_id)
- [ ] T291 [RR-015] Design validation_status structure
- [ ] T292 [RR-015] Test version lineage queries (recursive CTE)

### Layer Data Storage Design

- [ ] T293 [RR-015] Evaluate Option A: One table per layer+version (fast, schema proliferation)
- [ ] T294 [RR-015] Evaluate Option B: Single table per layer with version_id (slower, single schema)
- [ ] T295 [RR-015] Evaluate Option C: Document store with version in document (flexible, requires NoSQL)
- [ ] T296 [RR-015] Select and implement layer data storage approach
- [ ] T297 [RR-015] Create sample Layer 5 (Verse) storage with versioning

### Delta Storage Mechanism

- [ ] T298 [RR-015] Analyze Layer 6 (Surah metadata) for shared entities across narrations
- [ ] T299 [RR-015] Analyze Layer 8 (Chapter structure) for shared entities across orthographies
- [ ] T300 [RR-015] Analyze Layer 11-12 (Page/line layout) for shared entities across editions
- [ ] T301 [RR-015] Design delta storage strategy in experiments/rr-015-mudmaj-schema/delta_storage_design.md
- [ ] T302 [RR-015] Implement entity deduplication algorithm
- [ ] T303 [RR-015] Measure storage savings without delta (baseline)
- [ ] T304 [RR-015] Measure storage savings with delta optimization
- [ ] T305 [RR-015] Calculate savings percentage (hypothesis: >40%)

### Cross-Layer Mapping Storage

- [ ] T306 [RR-015] Design EntityMapping table schema in experiments/rr-015-mudmaj-schema/entity_mapping_schema.sql
- [ ] T307 [RR-015] Create indexes for source and target entity lookups
- [ ] T308 [RR-015] Implement bidirectional traversal queries
- [ ] T309 [RR-015] Test cross-layer mapping query performance (<50ms target)

### Provenance and Audit Tracking

- [ ] T310 [RR-015] Design transformation_logs table in experiments/rr-015-mudmaj-schema/transformation_logs_schema.sql
- [ ] T311 [RR-015] Design validation_results table in experiments/rr-015-mudmaj-schema/validation_results_schema.sql
- [ ] T312 [RR-015] Implement audit trail queries
- [ ] T313 [RR-015] Test provenance tracking completeness

### Validation for RR-015

- [ ] T314 [RR-015] Validate storage technology choice with benchmark results
- [ ] T315 [RR-015] Validate VersionRegistry achieves <100ms lookups
- [ ] T316 [RR-015] Validate delta storage achieves >40% savings (or document actual)
- [ ] T317 [RR-015] Validate cross-layer mapping queries execute in <50ms
- [ ] T318 [RR-015] Validate provenance tracking captures complete audit trail
- [ ] T319 [RR-015] Document findings in experiments/rr-015-mudmaj-schema/results/analysis.md
- [ ] T320 [RR-015] Update research log with RR-015 findings

**Checkpoint**: MUDMAJ schema validated - multi-version storage designed, delta optimization validated

---

## Phase 12: RR-016 - Context-Aware Query System Validation

**Research Goal**: Validate the complete context-aware query system by executing sample queries requiring context resolution, demonstrating correct version selection, and proving context isolation.

**Hypothesis**: Integrated QUD Orchestrator + MUDMAJ system can correctly route queries to appropriate layer versions, handle cross-context comparisons, and maintain <200ms end-to-end query latency.

**Independent Validation**: Single-context queries return correct versions, cross-context queries correctly compare, cross-layer queries correctly join, context isolation verified, performance targets met.

**Data Layer Dependencies**: Meta-layer (operates on entire system).

**Dependencies on Prior RRs**: Depends on RR-014 (Orchestrator), RR-015 (MUDMAJ).

### Experiment Setup for RR-016

- [ ] T321 [RR-016] Create experiment directory: experiments/rr-016-context-queries/
- [ ] T322 [RR-016] Document hypothesis in experiments/rr-016-context-queries/README.md

### Single-Context Query Validation

- [ ] T323 [RR-016] Define test query Q1: "Get Surah Al-Fatiha in Hafs narration"
- [ ] T324 [RR-016] Define test query Q2: "Get verse 2:255 with Uthmani orthography"
- [ ] T325 [RR-016] Define test query Q3: "Get page 1 layout from King Fahd Complex edition"
- [ ] T326 [RR-016] Execute single-context queries with Orchestrator
- [ ] T327 [RR-016] Validate correct layer versions selected
- [ ] T328 [RR-016] Validate character/verse counts match expected
- [ ] T329 [RR-016] Measure query latency (<200ms target)

### Cross-Context Query Validation

- [ ] T330 [RR-016] Define test query Q4: "Compare Surah Al-Fatiha in Hafs vs Warsh"
- [ ] T331 [RR-016] Define test query Q5: "Show verse 2:255 in all orthographic systems"
- [ ] T332 [RR-016] Define test query Q6: "Find verse count differences between Hafs and Warsh"
- [ ] T333 [RR-016] Execute cross-context queries
- [ ] T334 [RR-016] Validate canonical identities correctly matched
- [ ] T335 [RR-016] Validate differences accurately identified
- [ ] T336 [RR-016] Validate character-level diffs correct
- [ ] T337 [RR-016] Validate verse boundary differences detected

### Cross-Layer Query Validation

- [ ] T338 [RR-016] Define test query Q7: "Get verse text with character composition breakdown"
- [ ] T339 [RR-016] Define test query Q8: "Get verse with page and line layout information"
- [ ] T340 [RR-016] Define test query Q9: "Get word with tajweed marks and rendering rules"
- [ ] T341 [RR-016] Execute cross-layer queries
- [ ] T342 [RR-016] Validate UUID references correctly resolved
- [ ] T343 [RR-016] Validate cross-layer data correctly assembled
- [ ] T344 [RR-016] Validate no missing entities
- [ ] T345 [RR-016] Measure query latency (<200ms target)

### Context Isolation Validation

- [ ] T346 [RR-016] Design isolation test: Query Hafs context, verify Warsh data NOT returned
- [ ] T347 [RR-016] Design isolation test: Query Uthmani orthography, verify Qiasy data NOT returned
- [ ] T348 [RR-016] Design isolation test: Query edition A, verify edition B layout NOT returned
- [ ] T349 [RR-016] Execute isolation tests
- [ ] T350 [RR-016] Validate negative cases (invalid context → error handling)
- [ ] T351 [RR-016] Validate incomplete context → defaults applied correctly
- [ ] T352 [RR-016] Validate conflicting parameters → conflict resolution correct

### Ambiguous Context Handling

- [ ] T353 [RR-016] Test ambiguous context: User doesn't specify orthography
- [ ] T354 [RR-016] Test ambiguous context: User specifies edition but not narration
- [ ] T355 [RR-016] Test ambiguous context: User specifies conflicting parameters
- [ ] T356 [RR-016] Validate correct defaults applied
- [ ] T357 [RR-016] Document default resolution strategy in experiments/rr-016-context-queries/default_strategy.md

### Performance Benchmarking

- [ ] T358 [RR-016] Run 100 single-context queries (different verses, surahs)
- [ ] T359 [RR-016] Run 100 cross-context queries (Hafs vs Warsh comparisons)
- [ ] T360 [RR-016] Run 100 cross-layer queries (verses with full layer breakdown)
- [ ] T361 [RR-016] Measure context resolution time (<100ms target)
- [ ] T362 [RR-016] Measure single-context query latency (<200ms target)
- [ ] T363 [RR-016] Measure cross-context query latency (<500ms target)
- [ ] T364 [RR-016] Measure cross-layer query latency (<300ms target)
- [ ] T365 [RR-016] Profile bottlenecks with Python cProfile
- [ ] T366 [RR-016] Document performance results in experiments/rr-016-context-queries/results/performance_benchmarks.md

### Validation for RR-016

- [ ] T367 [RR-016] Validate single-context queries return correct layer versions
- [ ] T368 [RR-016] Validate cross-context queries correctly compare across contexts
- [ ] T369 [RR-016] Validate cross-layer queries correctly join via UUID references
- [ ] T370 [RR-016] Validate context isolation (no data leakage)
- [ ] T371 [RR-016] Validate ambiguous contexts resolved with documented defaults
- [ ] T372 [RR-016] Validate performance targets met for all query types
- [ ] T373 [RR-016] Validate error handling gracefully manages invalid queries
- [ ] T374 [RR-016] Document findings in experiments/rr-016-context-queries/results/analysis.md
- [ ] T375 [RR-016] Update research log with RR-016 findings

**Checkpoint**: Context-aware query system validated - end-to-end system works

---

## Phase 13: Synthesis & Cross-Cutting Research

**Purpose**: Synthesize findings across all 16 RRs and produce comprehensive documentation

### Research Findings Synthesis

- [ ] T376 [P] Synthesize findings across RR-001-016 in docs/research-log.md
- [ ] T377 [P] Create comprehensive layer documentation for Layer 0 in docs/data-layers/layer-00-character-composition.md
- [ ] T378 [P] Create comprehensive layer documentation for Layer 1 in docs/data-layers/layer-01-symbols-rendering.md
- [ ] T379 [P] Create comprehensive layer documentation for Layer 2 in docs/data-layers/layer-02-paired-data.md
- [ ] T380 [P] Create comprehensive layer documentation for Layer 3 in docs/data-layers/layer-03-word-structure.md
- [ ] T381 [P] Create comprehensive layer documentation for Layer 4 in docs/data-layers/layer-04-sentence-structure.md
- [ ] T382 [P] Create comprehensive layer documentation for Layer 5 in docs/data-layers/layer-05-verse-structure.md
- [ ] T383 [P] Create comprehensive layer documentation for Layer 6 in docs/data-layers/layer-06-surah-structure.md
- [ ] T384 [P] Create comprehensive layer documentation for Layer 7 in docs/data-layers/layer-07-division-structure.md
- [ ] T385 [P] Create comprehensive layer documentation for Layer 8 in docs/data-layers/layer-08-chapter-structure.md
- [ ] T386 [P] Create comprehensive layer documentation for Layer 9 in docs/data-layers/layer-09-narration-manuscript.md
- [ ] T387 [P] Create comprehensive layer documentation for Layer 10 in docs/data-layers/layer-10-edition-variants.md
- [ ] T388 [P] Create comprehensive layer documentation for Layer 11 in docs/data-layers/layer-11-page-layout.md
- [ ] T389 [P] Create comprehensive layer documentation for Layer 12 in docs/data-layers/layer-12-line-layout.md
- [ ] T390 [P] Create comprehensive layer documentation for Layer 13 in docs/data-layers/layer-13-orthographic-systems.md
- [ ] T391 [P] Create comprehensive layer documentation for Layer 14 in docs/data-layers/layer-14-readers-narrators.md
- [ ] T392 [P] Document the distinction between "folded" (conceptual) and "unfolded" (concrete) layers; currently 17 identified layers with exact count under investigation

### Architecture Documentation

- [ ] T393 [P] Finalize QUD Orchestrator architecture in docs/architecture/qud-orchestrator.md
- [ ] T394 [P] Finalize MUDMAJ storage architecture in docs/architecture/mudmaj-storage.md
- [ ] T395 [P] Finalize contextual versioning system in docs/architecture/contextual-versioning.md

### ADR Consolidation

- [ ] T396 Consolidate all Architecture Decision Records in docs/decisions/
- [ ] T397 Review ADR-001 (dual schema approach) with final findings
- [ ] T398 Review ADR-003 (generative architecture) with final findings
- [ ] T399 Review ADR-004 (UUID mapping strategy) with final findings
- [ ] T400 Review ADR-005 (context schema design) with final findings
- [ ] T401 Review ADR-006 (MUDMAJ storage technology) with final findings

### Schema Finalization

- [ ] T402 [P] Finalize and validate all 15 layer schemas in schemas/ directories
- [ ] T403 [P] Finalize cross-layer mapping schemas in schemas/cross-layer-mappings/
- [ ] T404 [P] Finalize context schema in schemas/context-schema/ (validated from RR-014)
- [ ] T405 [P] Finalize MUDMAJ schema in schemas/mudmaj-schema/ (validated from RR-015)
- [ ] T406 Create comparative analysis of generative approaches validated
- [ ] T407 Document schema evolution and refinements discovered through research

### Negative Results Documentation

- [ ] T408 Document all validation failures and their root causes
- [ ] T409 Document approaches that didn't work (failed experiments)
- [ ] T410 Document lessons learned from negative results
- [ ] T411 Create recommendations for future research based on failures

### Tool Refinement (Optional - If Patterns Validated)

- [ ] T412 [P] Refactor Tier 2 tools based on validated patterns from RR-001-016
- [ ] T413 [P] Create production-ready validators if pattern validated
- [ ] T414 [P] Create production-ready generators if generative approach validated

### Research Findings Publication

- [ ] T415 Publish comprehensive research findings summary
- [ ] T416 Create visualization of complete multi-layer architecture (currently 17 identified layers)
- [ ] T417 Create demonstration of context-aware query system
- [ ] T418 Prepare demo materials for engineering-mediated scholarly review

---

## Phase 14: Phase 1 Completion & Transition Validation

**Purpose**: Validate Phase 1 completion criteria before transitioning to Phase 2

**Phase Transition Criteria** (per spec.md 2025-11-04 clarifications):
1. RR-001, RR-002, RR-003 complete with validated schemas
2. Working simulation for Hafs+Warsh
3. All validation criteria (VC-001 through VC-011) met for Hafs+Warsh
4. Engineering-mediated scholarly review completed
5. Theological accuracy confirmed and feedback incorporated into specs/data

### RR Completion Validation

- [ ] T419 Verify RR-001 complete with validated layer mapping analysis
- [ ] T420 Verify RR-002 complete with validated schemas for all identified layers (currently 17)
- [ ] T421 Verify RR-003 complete with working simulation transforming Hafs and Warsh data

### Validation Criteria Check (VC-001 through VC-011)

- [ ] T422 Verify VC-001: RR-001 mapping table complete with >90% confidence scores
- [ ] T423 Verify VC-002: RR-002 schema transformation with zero information loss
- [ ] T424 Verify VC-003: Schema validation for all layers across Hafs+Warsh
- [ ] T425 Verify VC-004: Character count validation (Hafs: 323,015 characters, >99% accuracy)
- [ ] T426 Verify VC-005: Verse count validation (Hafs: 6,236, Warsh: 6,214, 100% match)
- [ ] T427 Verify VC-006: Redundancy reduction >40% achieved
- [ ] T428 Verify VC-007: Cross-Qiraah query capability demonstrated (3+ example queries)
- [ ] T429 Verify VC-008: Generative layer production validated (>95% accuracy for Layer 0→2)
- [ ] T430 Verify VC-009: UUID-based cross-layer mapping system validated
- [ ] T431 Verify VC-010: Verse numbering resolution demonstrated (Hafs↔Warsh mapping)
- [ ] T432 Verify VC-011: Orthographic transformation demonstrated (Uthmani↔Qiasy)

### Engineering-Mediated Scholarly Review

**Process** (per spec.md 2025-11-04 clarifications):
- Engineering team creates demos and presents to scholars
- Scholars don't interact with system directly due to technical constraints
- Scholars provide feedback on theological accuracy
- Engineering team incorporates feedback and edits specs/data
- Reviews occur after R&D cycle completion

- [ ] T433 Prepare demo presentation materials for scholarly review
- [ ] T434 Create visual demonstrations of generated layer data (especially Layer 2 diacritics/tajweed, Layer 3 word boundaries)
- [ ] T435 Prepare comparison visualizations (Hafs vs Warsh differences)
- [ ] T436 Document theological claims made by the system for scholar validation
- [ ] T437 Conduct scholarly review session (engineering team presents to scholars)
- [ ] T438 Document scholar feedback on theological accuracy
- [ ] T439 Identify required changes based on scholar feedback
- [ ] T440 Implement spec/data changes based on scholar feedback
- [ ] T441 Verify theological accuracy confirmed by scholars

### Phase Transition Decision

- [ ] T442 Generate Phase 1 completion report
- [ ] T443 Document any incomplete items with justification
- [ ] T444 Create Phase 2 readiness assessment
- [ ] T445 Update research log with Phase 1→2 transition decision
- [ ] T446 Archive Phase 1 artifacts and findings

**Checkpoint**: Phase 1 Complete - Ready to transition to Phase 2 (expand to additional narrations)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational Tools (Phase 2)**: Depends on Setup completion - BLOCKS all Research Requirements
- **RR-001 (Phase 3)**: Depends on Foundational Tools - No dependencies on other RRs
- **RR-002 (Phase 4)**: Depends on Foundational Tools + RR-001 findings (field→layer mapping)
- **RR-003 (Phase 5)**: Depends on Foundational Tools + RR-001 (knows what's mixed) + RR-002 (has schemas)
- **RR-004-010 (Phase 6)**: Largely validated through RR-001-003, consolidation phase
- **RR-011 (Phase 7)**: Depends on Foundational Tools + RR-002 (schemas must have UUID fields)
- **RR-012 (Phase 8)**: Depends on Foundational Tools + RR-002 (schemas) + RR-011 (UUID mappings)
- **RR-013 (Phase 9)**: Depends on Foundational Tools + RR-002 (schemas) + RR-011 (UUID mappings)
- **RR-014 (Phase 10)**: Depends on Foundational Tools + RR-002 (schemas) + RR-011-013 (mappings)
- **RR-015 (Phase 11)**: Depends on Foundational Tools + RR-002 (layer schemas) + RR-014 (context schema)
- **RR-016 (Phase 12)**: Depends on Foundational Tools + RR-014 (Orchestrator) + RR-015 (MUDMAJ)
- **Synthesis (Phase 13)**: Depends on all desired RRs being validated
- **Phase Transition (Phase 14)**: Depends on RR-001, RR-002, RR-003 completion + all VC validation + scholarly review

### Research Requirement Independence

**Independent RRs** (can run in parallel after Foundational Tools):
- RR-001 (layer analysis) - completely independent
- RR-011 (UUID system) - independent after RR-002
- RR-004 (field variance) - can run alongside RR-001

**Sequential Dependencies**:
- RR-001 → RR-002 (mapping informs schema design)
- RR-002 → RR-003 (schemas needed for simulation)
- RR-002 → RR-011 (schemas need UUID fields)
- RR-011 → RR-012, RR-013 (UUID mappings needed for versioning and orthographic mapping)
- RR-002 + RR-011-013 → RR-014 (Orchestrator needs schemas and mappings)
- RR-014 → RR-015 (MUDMAJ needs context schema)
- RR-014 + RR-015 → RR-016 (query validation needs both components)

### Within Each Research Requirement

1. Experiment setup before prototype implementation
2. Data validation MUST occur before using data in experiments
3. Prototype implementation before validation execution
4. Validation execution before findings documentation
5. Findings documented before considering RR complete
6. Document negative results - failed experiments that produce learning are successful research

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel (T003-T011)
- All Foundational Tool tasks marked [P] can run in parallel within Phase 2 (T012-T032)
- Within RR-002: All 15 layer schema definitions marked [P] can run in parallel (T059-T103)
- Once Foundational Tools complete, independent RRs can start in parallel (if team capacity):
  - Team A: RR-001
  - Team B: RR-011 (after RR-002)
  - Team C: RR-004
- Synthesis tasks marked [P] can run in parallel once all RRs complete (T376-T405)

---

## Parallel Example: RR-002 Schema Design

```bash
# Launch parallel schema definition for all 15 layers:
# Each layer schema can be defined independently in parallel

Task T059-T061: Layer 0 schema (character composition)
Task T062-T064: Layer 1 schema (symbols/rendering)
Task T065-T067: Layer 2 schema (paired data)
Task T068-T070: Layer 3 schema (word structure)
Task T071-T073: Layer 4 schema (sentence structure)
Task T074-T076: Layer 5 schema (verse structure)
Task T077-T079: Layer 6 schema (surah structure)
Task T080-T082: Layer 7 schema (division structure)
Task T083-T085: Layer 8 schema (chapter structure)
Task T086-T088: Layer 9 schema (narration manuscript)
Task T089-T091: Layer 10 schema (edition variants)
Task T092-T094: Layer 11 schema (page layout)
Task T095-T097: Layer 12 schema (line layout)
Task T098-T100: Layer 13 schema (orthographic systems)
Task T101-T103: Layer 14 schema (readers/narrators)

# All 15 layer schemas can be developed in parallel
# Consolidate and validate once all complete
```

---

## Research Strategy

### Hypothesis-First (RR-001 Only - Minimum Viable Research)

1. Complete Phase 1: Setup (~1-2 days)
2. Complete Phase 2: Foundational Tools (~3-5 days) - CRITICAL BLOCKER
3. Complete Phase 3: RR-001 (~2-3 days)
4. **STOP and VALIDATE**: Analyze RR-001 findings - hypothesis confirmed or refuted?
5. Document learnings before proceeding

**This validates the core hypothesis**: Can we identify mixed layers in QS-QIRAAT?

### Incremental Discovery (RR-001 → RR-002 → RR-003)

1. Complete Setup + Foundational Tools → Research infrastructure ready (~4-7 days)
2. Validate RR-001 hypothesis → Document findings (~2-3 days)
3. Validate RR-002 hypothesis → Document findings, build on RR-001 (~3-5 days)
4. Validate RR-003 hypothesis → Document findings, demonstrate working system (~5-7 days)
5. **Total**: ~14-22 days for core layer architecture validation

### Full System Validation (All 16 RRs)

1. Complete core track (RR-001-003): Layer architecture validated
2. Complete UUID track (RR-011-013): Cross-layer mapping validated
3. Complete contextual versioning track (RR-014-016): QUD + MUDMAJ validated
4. Complete supporting RRs (RR-004-010): Specific validations
5. Synthesize all findings
6. **Total**: ~30-45 days for complete system validation

### Parallel Research Team Strategy

With multiple researchers (3+ people):

1. **Week 1**: Team completes Setup + Foundational Tools together
2. **Week 2-3**: Parallel research tracks:
   - Researcher A: RR-001 (layer analysis)
   - Researcher B: Starts RR-004 (field variance - can run alongside RR-001)
   - Researcher C: Prepares for RR-002 (schema design planning)
3. **Week 3-4**: After RR-001 complete:
   - Researchers A+C: RR-002 (schema design - many parallel tasks)
   - Researcher B: Continues RR-004, starts preparing RR-011
4. **Week 5-6**: After RR-002 complete:
   - Researcher A: RR-003 (simulation)
   - Researcher B: RR-011 (UUID system)
   - Researcher C: Starts RR-012 (contextual versioning)
5. **Week 7-8**: Parallel validation:
   - Researcher A: RR-014 (Orchestrator)
   - Researcher B: RR-015 (MUDMAJ)
   - Researcher C: Supports both
6. **Week 9**: Integration:
   - Team: RR-016 (query validation)
7. **Week 10**: Synthesis and documentation

**Potential timeline**: 10 weeks with 3-person team vs 20-30 weeks solo

---

## Notes

- `- [ ]` = Markdown checkbox (REQUIRED format)
- `[ID]` = Sequential task number (T001, T002, etc.)
- `[P]` tasks = different files/experiments, no dependencies, can run in parallel
- `[RR-###]` label maps task to specific Research Requirement for traceability
- Each RR should be independently validatable (hypothesis can be tested on its own)
- Validate data against authoritative sources before using in experiments (ZERO TOLERANCE for Quranic text errors)
- Commit findings after each RR validation (positive or negative results)
- Stop at any checkpoint to document findings before proceeding
- Code quality follows tier model: Tier 1 (experimental), Tier 2 (reusable tools), Tier 3 (production if needed)
- Avoid: vague hypotheses, untraceable data sources, skipping negative result documentation
- Remember: **Failed experiments that produce learning are successful research**
- ALL schemas and architectures marked as HYPOTHETICAL must be validated through their respective RRs
- Performance targets are hypotheses to be validated, not hard requirements - document actual performance
- Storage savings >40% is a hypothesis - if actual savings differ, document the real percentage
- Engineering-mediated scholarly review required at end of each research cycle (engineering team creates demos, presents to scholars, incorporates feedback)
- UUID assignment strategy (v4 vs v5) is a research question - document decision in ADR
- Phase 1 to Phase 2 transition requires: RR-001-003 complete, all validation criteria met, scholarly review completed with theological accuracy confirmed

---

## Task Summary

**Total Tasks**: 446 tasks (updated 2025-11-05)
- **Phase 1 (Setup)**: 11 tasks
- **Phase 2 (Foundational Tools)**: 21 tasks (CRITICAL - blocks all RRs)
- **Phase 3 (RR-001)**: 23 tasks (layer analysis)
- **Phase 4 (RR-002)**: 63 tasks (schema design - many parallelizable)
- **Phase 5 (RR-003)**: 51 tasks (simulation prototype)
- **Phase 6 (RR-004-010)**: 13 tasks (supporting validations)
- **Phase 7 (RR-011)**: 19 tasks (UUID system)
- **Phase 8 (RR-012)**: 19 tasks (contextual versioning)
- **Phase 9 (RR-013)**: 19 tasks (orthographic mapping)
- **Phase 10 (RR-014)**: 33 tasks (QUD Orchestrator)
- **Phase 11 (RR-015)**: 47 tasks (MUDMAJ schema)
- **Phase 12 (RR-016)**: 55 tasks (query validation)
- **Phase 13 (Synthesis)**: 44 tasks (documentation and consolidation)
- **Phase 14 (Phase Transition)**: 28 tasks (validation criteria check, scholarly review, Phase 1→2 transition)

**Parallel Opportunities**: 150+ tasks marked [P] can run in parallel

**Independent Test Criteria**: Each RR phase has clear validation scenarios and success criteria

**Suggested MVP Scope**: Complete through RR-001 (Phase 1-3, ~36 tasks) to validate core hypothesis

**Format Validation**: ✅ ALL tasks follow required checklist format (checkbox, ID, optional labels, file paths)
