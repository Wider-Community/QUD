# Research Specification: [RESEARCH TOPIC NAME]

**Research Branch**: `[###-research-topic]`
**Created**: [DATE]
**Status**: Draft
**Input**: Research description: "$ARGUMENTS"

<!--
  NOTE: This is a RESEARCH PROJECT focused on Quranic Technologies big data.
  We use Research Requirements (RR) instead of Feature Requirements (FR).
  The goal is VALIDATED KNOWLEDGE and EXPERIMENTAL DESIGN, not production software.
-->

## Research Scenarios & Validation *(mandatory)*

<!--
  IMPORTANT: Research scenarios should be PRIORITIZED hypotheses ordered by criticality.
  Each research scenario must be INDEPENDENTLY TESTABLE - meaning if you validate just ONE hypothesis,
  you should still gain valuable research insights.

  Assign priorities (P1, P2, P3, etc.) to each scenario, where P1 is the most critical hypothesis.
  Think of each scenario as a standalone research question that can be:
  - Investigated independently
  - Validated independently
  - Documented independently
  - Built upon for further research
-->

### RR-001 - [Research Question Brief Title] (Priority: P1)

**Research Question**: [What specific question are we investigating?]

**Hypothesis**: [What do we believe to be true that we will test?]

**Context**: [Why this question matters for Quranic Technologies, what prior work exists]

**Why this priority**: [Explain why this is the most critical research question]

**Independent Validation**: [How this hypothesis can be tested independently - e.g., "Can be validated by building a prototype that processes [X] recitations and measuring [Y] metric"]

**Validation Scenarios**:

1. **Given** [test data/conditions], **When** [experiment performed], **Then** [expected measurable outcome]
2. **Given** [test data/conditions], **When** [experiment performed], **Then** [expected measurable outcome]

**Data Layer Dependencies**: [Which Quranic data layers (0-13, unfolds to 16) this research depends on]

**Schema Requirements**: [Which layer schemas must be defined/validated for this RR]

**Expected Findings Format**: [How results will be documented - e.g., "Performance metrics table", "Comparative analysis chart", "Design decision record"]

---

### RR-002 - [Research Question Brief Title] (Priority: P2)

**Research Question**: [What specific question are we investigating?]

**Hypothesis**: [What do we believe to be true that we will test?]

**Context**: [Why this question matters, relationship to RR-001]

**Why this priority**: [Explain priority relative to other research questions]

**Independent Validation**: [How this can be validated independently]

**Validation Scenarios**:

1. **Given** [test data/conditions], **When** [experiment performed], **Then** [expected measurable outcome]

**Data Layer Dependencies**: [Which Quranic data layers (0-13, unfolds to 16) this research depends on]

**Schema Requirements**: [Which layer schemas must be defined/validated for this RR]

**Expected Findings Format**: [How results will be documented]

---

### RR-003 - [Research Question Brief Title] (Priority: P3)

**Research Question**: [What specific question are we investigating?]

**Hypothesis**: [What do we believe to be true that we will test?]

**Context**: [Why this question matters]

**Why this priority**: [Explain priority]

**Independent Validation**: [How this can be validated independently]

**Validation Scenarios**:

1. **Given** [test data/conditions], **When** [experiment performed], **Then** [expected measurable outcome]

**Data Layer Dependencies**: [Which Quranic data layers (0-13, unfolds to 16) this research depends on]

**Schema Requirements**: [Which layer schemas must be defined/validated for this RR]

**Expected Findings Format**: [How results will be documented]

---

[Add more research requirements as needed, each with an assigned priority]

### Domain Constraints

<!--
  ACTION REQUIRED: Document Quranic domain-specific constraints that MUST be respected.
  These are NOT edge cases - they are core requirements of the domain.
-->

- What Qiraat (قراءات) must be supported?
- What are the character count/verse count validation requirements?
- Which authoritative sources will be used for data validation?
- What are the theological accuracy requirements?

## Research Requirements *(mandatory)*

<!--
  ACTION REQUIRED: The content in this section represents placeholders.
  Fill them out with specific research requirements.
-->

### Research Requirements (RR)

- **RR-001**: Research MUST investigate [specific research question, e.g., "optimal data structure for cross-Qiraah verse lookup"]
- **RR-002**: Experiment MUST validate [specific hypothesis, e.g., "layer-based storage reduces data redundancy by >30%"]
- **RR-003**: Analysis MUST compare [specific alternatives, e.g., "graph vs relational models for Qiraah relationships"]
- **RR-004**: Prototype MUST demonstrate [specific capability, e.g., "character-level tajweed rule application"]
- **RR-005**: Validation MUST confirm [specific accuracy requirement, e.g., "verse counts match King Fahd Complex editions"]

*Example of marking unclear requirements:*

- **RR-006**: Research MUST explore [NEEDS CLARIFICATION: which specific narrations - all 20, or subset? Which Qiraat?]
- **RR-007**: Experiment MUST use data from [NEEDS CLARIFICATION: which authoritative source - King Fahd Complex? Which edition?]

### Key Data Entities *(include if research involves Quranic data structures)*

<!--
  Reference the 14-layer data model (unfolds to 16) from constitution when defining entities.
  Remember: Layers are GENERATIVE - they are computed through rules, not manually curated.
  All generated data MUST conform to predefined schemas.
-->

- **[Layer N - Entity Name]**: [What it represents in Quranic domain, key attributes, relationships to other layers]
- **[Layer M - Entity Name]**: [What it represents, cross-layer dependencies, generation rules (if applicable)]

### Layer Generation *(include if research involves generative layer work)*

- **Generation Approach**: [How will layer data be generated - rules, algorithms, transformations?]
- **Schema Definition**: [What schema will generated data conform to?]
- **Validation Strategy**: [How will generated data be validated against authoritative sources?]
- **Provenance Tracking**: [How will generation process be documented?]

### Data Sources & Validation

- **Primary Sources**: [King Fahd Complex editions, authenticated Qiraah databases, etc.]
- **Validation Method**: [How data accuracy will be verified against authoritative sources]
- **Provenance Documentation**: [How source attribution will be maintained]

## Research Success Criteria *(mandatory)*

<!--
  ACTION REQUIRED: Define measurable validation criteria for research hypotheses.
  These should focus on KNOWLEDGE GAINED and DESIGN VALIDATED, not production metrics.
-->

### Validation Outcomes

- **VC-001**: [Validation metric, e.g., "Hypothesis confirmed/refuted with >95% confidence based on [specific test]"]
- **VC-002**: [Performance metric, e.g., "Prototype demonstrates <100ms query latency for 77,000+ words across 3 narrations"]
- **VC-003**: [Accuracy metric, e.g., "Data integrity validation shows 100% match with authoritative source for verse counts"]
- **VC-004**: [Learning metric, e.g., "Design decision documented with comparative analysis of 3+ alternative approaches"]

### Findings Documentation

- **Research Log Entry**: [Chronological record of experiment and findings]
- **Architecture Decision Record**: [If design pattern validated/rejected]
- **Data Model Specification**: [If new data structure validated]
- **Negative Results**: [Document what DIDN'T work and why - equally valuable]
