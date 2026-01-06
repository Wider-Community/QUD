---

description: "Task list template for research implementation"
---

# Tasks: [RESEARCH TOPIC]

**Input**: Research design documents from `/specs/[###-research-topic]/`
**Prerequisites**: plan.md (required), spec.md (required for research requirements), research.md, data-model.md, experiment-design.md

<!--
  RESEARCH PROJECT NOTE: Tasks focus on EXPERIMENTAL VALIDATION, not production delivery.
  Success = validated hypothesis (confirmed or refuted) + documented findings.
  Code quality follows three-tier model: Tier 1 (experimental), Tier 2 (tools), Tier 3 (production pipelines if needed).
-->

**Tests**: For research projects, "tests" mean VALIDATION EXPERIMENTS. Each Research Requirement (RR) should have validation tasks that confirm/refute the hypothesis.

**Organization**: Tasks are grouped by Research Requirement (RR) to enable independent hypothesis validation.

## Format: `[ID] [P?] [RR] Description`

- **[P]**: Can run in parallel (different experiments, no dependencies)
- **[RR]**: Which Research Requirement this task belongs to (e.g., RR-001, RR-002, RR-003)
- Include exact file paths in descriptions (use `experiments/rr-XXX-topic/` structure)

## Path Conventions

- **Research experiments**: `experiments/rr-XXX-topic/` - one directory per Research Requirement
- **Reusable tools**: `research-tools/` - utilities shared across experiments
- **Layer schemas**: `schemas/layer-XX-name/` - formal schema definitions for 14 essential layers (0-13)
- **Documentation**: `docs/research-log.md`, `docs/data-layers/` (layers 0-13), `docs/decisions/`
- **Production pipelines** (if needed): `data-infrastructure/` - Tier 3 quality code

Paths shown below assume research project structure from plan.md.

<!--
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.

  The /tasks command MUST replace these with actual tasks based on:
  - Research Requirements (RR) from spec.md (with their priorities P1, P2, P3...)
  - Research questions and hypotheses from plan.md
  - Quranic data entities from data-model.md (referencing Layers 0-12)
  - Experimental methodology from experiment-design.md

  Tasks MUST be organized by Research Requirement (RR) so each RR can be:
  - Investigated independently
  - Validated independently (hypothesis confirmed/refuted)
  - Documented independently
  - Built upon for further research

  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Research Infrastructure)

**Purpose**: Project initialization and foundational research tooling

- [ ] T001 Create research project structure per plan.md (experiments/, research-tools/, schemas/, docs/)
- [ ] T002 Initialize Python project with scientific computing dependencies (numpy, pandas, etc.)
- [ ] T003 [P] Setup documentation templates (research-log.md, ADR template, layer docs)
- [ ] T004 [P] Create data layer documentation structure (docs/data-layers/ for 14 essential Layers 0-13)
- [ ] T005 [P] Create schema directory structure (schemas/layer-00-qiraat/ through layer-13-orthographic/)

---

## Phase 2: Foundational Tools (Blocking Prerequisites)

**Purpose**: Core research tools that MUST be complete before ANY Research Requirement experiments can be conducted

**⚠️ CRITICAL**: No RR experimentation can begin until this phase is complete

**Tier 2 Quality Required**: These are reusable tools, not experimental code

- [ ] T006 [P] Implement Quranic data loader in research-tools/data-loaders/quran_loader.py
- [ ] T007 [P] Implement character count validator in research-tools/validators/char_count_validator.py
- [ ] T008 [P] Implement verse count validator in research-tools/validators/verse_validator.py
- [ ] T009 [P] Implement schema validator in research-tools/validators/schema_validator.py
- [ ] T010 [P] Create authenticated source documentation in docs/sources/king-fahd-editions.md
- [ ] T011 Setup data provenance tracking system
- [ ] T012 [P] Create performance metrics analyzer in research-tools/analyzers/performance_metrics.py
- [ ] T013 [P] Create data comparison utility in research-tools/analyzers/data_comparator.py
- [ ] T014 [P] Create layer generation utility framework in research-tools/generators/layer_generator.py

**Checkpoint**: Research tools ready - RR experimentation can now begin in parallel

---

## Phase 3: RR-001 - [Research Question Title] (Priority: P1) 🎯 First Hypothesis

**Research Goal**: [Brief description of what hypothesis is being tested]

**Hypothesis**: [The specific belief being validated]

**Independent Validation**: [How to verify this hypothesis - what experiment confirms/refutes it]

**Data Layer Dependencies**: [Which Quranic data layers (0-13, unfolds to 16) this uses]

### Experiment Setup for RR-001

**Tier 1 Quality - Experimental Code**

- [ ] T015 [RR-001] Create experiment directory: experiments/rr-001-[topic]/
- [ ] T016 [RR-001] Document hypothesis in experiments/rr-001-[topic]/README.md
- [ ] T017 [P] [RR-001] Define/reference layer schema(s) for this RR in schemas/layer-XX-name/
- [ ] T018 [P] [RR-001] Gather test data in experiments/rr-001-[topic]/data/ (or document sources)
- [ ] T019 [P] [RR-001] Validate test data against authoritative source using research-tools validators

### Prototype Implementation for RR-001

- [ ] T020 [RR-001] Build prototype in experiments/rr-001-[topic]/prototype.py
- [ ] T021 [RR-001] Mark experimental code with # EXPERIMENTAL: comments
- [ ] T022 [RR-001] Implement data layer processing (e.g., Layer 4 word boundaries)
- [ ] T023 [RR-001] If generative: implement layer generation rules
- [ ] T024 [RR-001] Add basic logging to track experiment progress

### Validation Execution for RR-001

- [ ] T025 [RR-001] Run validation experiments per experiment-design.md
- [ ] T026 [RR-001] Collect performance metrics in experiments/rr-001-[topic]/results/metrics.json
- [ ] T027 [RR-001] Verify data accuracy (character counts, verse counts match authoritative source)
- [ ] T028 [RR-001] If generative: validate generated data against schema using schema_validator
- [ ] T029 [RR-001] Generate visualizations in experiments/rr-001-[topic]/results/visualizations/

### Findings Documentation for RR-001

- [ ] T030 [RR-001] Analyze results in experiments/rr-001-[topic]/results/analysis.md
- [ ] T031 [RR-001] Document hypothesis outcome (confirmed/refuted) with evidence
- [ ] T032 [RR-001] If schema-related: document schema refinements needed
- [ ] T033 [RR-001] Update research log in docs/research-log.md with findings
- [ ] T034 [RR-001] Create ADR if architectural decision made in docs/decisions/

**Checkpoint**: At this point, RR-001 hypothesis should be validated (confirmed or refuted), findings documented, and ready to inform next research questions

---

## Phase 4: RR-002 - [Research Question Title] (Priority: P2)

**Research Goal**: [Brief description of what hypothesis is being tested]

**Hypothesis**: [The specific belief being validated]

**Independent Validation**: [How to verify this hypothesis]

**Data Layer Dependencies**: [Which Quranic data layers (0-13, unfolds to 16) this uses]

**Dependencies on Prior RRs**: [e.g., "Builds on RR-001 findings about X"]

### Experiment Setup for RR-002

- [ ] T035 [RR-002] Create experiment directory: experiments/rr-002-[topic]/
- [ ] T036 [RR-002] Document hypothesis and RR-001 dependencies in README.md
- [ ] T037 [P] [RR-002] Define/reference layer schema(s) for this RR
- [ ] T038 [P] [RR-002] Gather test data
- [ ] T039 [P] [RR-002] Validate test data against authoritative source

### Prototype Implementation for RR-002

- [ ] T040 [RR-002] Build prototype in experiments/rr-002-[topic]/prototype.py
- [ ] T041 [RR-002] Mark experimental code with # EXPERIMENTAL: comments
- [ ] T042 [RR-002] Implement approach (may reuse RR-001 tools if validated)
- [ ] T043 [RR-002] If generative: implement layer generation rules

### Validation & Documentation for RR-002

- [ ] T044 [RR-002] Run validation experiments
- [ ] T045 [RR-002] Collect metrics and verify accuracy
- [ ] T046 [RR-002] If generative: validate generated data against schema
- [ ] T047 [RR-002] Document findings and update research log

**Checkpoint**: RR-002 hypothesis validated, findings documented

---

## Phase 5: RR-003 - [Research Question Title] (Priority: P3)

**Research Goal**: [Brief description]

**Hypothesis**: [The specific belief being validated]

**Independent Validation**: [How to verify]

**Data Layer Dependencies**: [Which layers (0-13, unfolds to 16)]

### Experiment Setup for RR-003

- [ ] T048 [RR-003] Create experiment directory: experiments/rr-003-[topic]/
- [ ] T049 [RR-003] Document hypothesis in README.md
- [ ] T050 [P] [RR-003] Define/reference layer schema(s) for this RR
- [ ] T051 [P] [RR-003] Gather and validate test data

### Prototype & Validation for RR-003

- [ ] T052 [RR-003] Build prototype
- [ ] T053 [RR-003] If generative: implement layer generation rules
- [ ] T054 [RR-003] Run experiments and collect metrics
- [ ] T055 [RR-003] If generative: validate generated data against schema
- [ ] T056 [RR-003] Document findings

**Checkpoint**: All priority research questions validated

---

[Add more RR phases as needed, following the same pattern]

---

## Phase N: Synthesis & Cross-Cutting Research

**Purpose**: Synthesis findings across multiple RRs and produce comprehensive documentation

- [ ] TXXX [P] Synthesize findings across all RRs in docs/research-log.md
- [ ] TXXX [P] Create comprehensive data layer documentation in docs/data-layers/ (all 14 layers: 0-13)
- [ ] TXXX [P] Document the "unfolding logic" that expands 14 essential layers to 16 concrete specifications
- [ ] TXXX Consolidate Architecture Decision Records in docs/decisions/
- [ ] TXXX [P] Finalize and validate all layer schemas in schemas/
- [ ] TXXX Create comparative analysis of generative approaches validated
- [ ] TXXX Document schema evolution and refinements discovered through research
- [ ] TXXX Document negative results and lessons learned
- [ ] TXXX [P] Refactor Tier 2 tools based on validated patterns (if needed)
- [ ] TXXX Publish research findings summary

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational Tools (Phase 2)**: Depends on Setup completion - BLOCKS all Research Requirements
- **Research Requirements (Phase 3+)**: All depend on Foundational Tools completion
  - Independent RRs can proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
  - Dependent RRs must wait for prerequisite RR findings
- **Synthesis (Final Phase)**: Depends on all desired RRs being validated

### Research Requirement Dependencies

- **RR-001 (P1)**: Can start after Foundational Tools (Phase 2) - No dependencies on other RRs
- **RR-002 (P2)**: Can start after Foundational Tools (Phase 2) - May build on RR-001 findings but should be independently validatable
- **RR-003 (P3)**: Can start after Foundational Tools (Phase 2) - May build on prior RR findings but should be independently validatable

### Within Each Research Requirement

- Experiment setup before prototype implementation
- Data validation MUST occur before using data in experiments
- Prototype implementation before validation execution
- Validation execution before findings documentation
- Findings documented before considering RR complete
- Document negative results - failed experiments that produce learning are successful research

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational Tool tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational Tools complete, independent RRs can start in parallel (if team capacity allows)
- Within an RR, data gathering and validation tasks marked [P] can run in parallel
- Different RRs can be investigated in parallel by different researchers
- Synthesis tasks marked [P] can run in parallel once all RRs are complete

---

## Parallel Example: RR-001

```bash
# Launch parallel data gathering/validation for RR-001:
Task: "Gather test data in experiments/rr-001-[topic]/data/"
Task: "Validate test data against authoritative source using research-tools validators"

# Launch parallel Tier 2 tool development in Phase 2:
Task: "Implement Quranic data loader in research-tools/data-loaders/quran_loader.py"
Task: "Implement character count validator in research-tools/validators/char_count_validator.py"
Task: "Implement verse count validator in research-tools/validators/verse_validator.py"
```

---

## Research Strategy

### Hypothesis-First (RR-001 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational Tools (CRITICAL - blocks all RRs)
3. Complete Phase 3: RR-001
4. **STOP and VALIDATE**: Analyze RR-001 findings - hypothesis confirmed or refuted?
5. Document learnings before proceeding

### Incremental Discovery

1. Complete Setup + Foundational Tools → Research infrastructure ready
2. Validate RR-001 hypothesis → Document findings → Determine next question
3. Validate RR-002 hypothesis → Document findings → Build on RR-001 learnings
4. Validate RR-003 hypothesis → Document findings → Synthesize patterns
5. Each RR produces knowledge without invalidating previous findings (negative results are valuable)

### Parallel Research Team Strategy

With multiple researchers:

1. Team completes Setup + Foundational Tools together
2. Once Foundational Tools ready:
   - Researcher A: RR-001 (independent hypothesis)
   - Researcher B: RR-002 (independent hypothesis)
   - Researcher C: RR-003 (independent hypothesis)
3. Share findings, refine tools based on validated patterns
4. Dependent RRs wait for prerequisite findings before starting

---

## Notes

- [P] tasks = different files/experiments, no dependencies
- [RR] label maps task to specific Research Requirement for traceability
- Each RR should be independently validatable (hypothesis can be tested on its own)
- Validate data against authoritative sources before using in experiments
- Commit findings after each RR validation (positive or negative results)
- Stop at any checkpoint to document findings before proceeding
- Code quality follows tier model: Tier 1 (experimental), Tier 2 (reusable tools), Tier 3 (production if needed)
- Avoid: vague hypotheses, untraceable data sources, skipping negative result documentation
- Remember: Failed experiments that produce learning are successful research
