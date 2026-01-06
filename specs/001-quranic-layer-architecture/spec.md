# Research Specification: Quranic Data Layer Architecture Declaration, Implementation & Simulation

**Research Branch**: `001-quranic-layer-architecture`
**Created**: 2025-11-03
**Status**: Draft
**Input**: Research description: "Quranic data layer declaration, implementation, and simulation - analyzing existing mixed-layer datasets and creating proper layer separation architecture"

<!--
  NOTE: This is a RESEARCH PROJECT focused on Quranic Technologies big data.
  We use Research Requirements (RR) instead of Feature Requirements (FR).
  The goal is VALIDATED KNOWLEDGE and EXPERIMENTAL DESIGN, not production software.
-->

## Clarifications

### Layer Count Status (Updated 2025-11-04)

**IMPORTANT**: The exact number of Quranic data layers is currently under investigation. As of 2025-11-04:
- **Current count**: 17 identified layers
- **Status**: Subject to refinement as research progresses
- **Uncertainty rationale**:
  - The distinction between "folded" (essential/conceptual) and "unfolded" (concrete/instantiated) layers is being clarified
  - Some essential layers may unfold into multiple concrete layers when accounting for different contexts (orthographies, editions, scholarly traditions)
  - There is a <10% probability that even the folded layer count may need adjustment
  - The unfolded layer count has a much higher probability of change
- **Research mission**: Determining the exact number of both folded and unfolded layers is now a formal research objective

Throughout this spec, references to specific layer counts should be understood as reflecting current understanding, not final determinations.

### Session 2025-11-03

- Q: For the QS-QIRAAT dataset analysis (RR-001), which data format(s) should the research primarily use? → A: JSON primary + CSV for validation, with SQLite sample database at end
- Q: The spec mentions both "100% schema validation pass rate" (VC-003) and ">99% accuracy for character counts" (VC-004). How should schema validation failures be handled? → A: Best-effort - Document all failures but proceed with research regardless
- Q: The spec mentions manual verification of 100 verses (VC-008, validation strategy) and expert review. Who performs this verification? → A: Automated validation during research cycles for speed; scholarly review at end of each cycle
- Q: What programming language/technology should be used for the simulation prototype (RR-003)? → A: Python, NLTK, other NLP related tech, Jupyter notebook, visualization tools for data layers simulations
- Q: For RR-002 schema design, which formal schema specification format should be used? → A: JSON Schema + Pydantic models

### Session 2025-11-04

- Q: How will scholarly review for theological accuracy be conducted, and who performs it? → A: Engineering team creates demos and presents to scholars (scholars don't interact with system directly due to technical constraints). After demo review, engineering team incorporates scholar feedback and edits. Additional reviews occur after each R&D cycle (or in between cycles as needed). Specs are updated accordingly based on feedback, and the engineering team operates on the data.
- Q: What are the specific completion criteria that must be met before transitioning from Phase 1 to Phase 2? → A: RR-001, RR-002, and RR-003 must all complete with validated schemas and working simulation for Hafs+Warsh, plus successful engineering-mediated scholarly review confirming theological accuracy

## Research Scenarios & Validation *(mandatory)*

### RR-001 - Layer Separation Analysis of Existing Datasets (Priority: P1)

**Research Question**: What specific data layers are currently mixed together in the QS-QIRAAT dataset, and can we algorithmically identify and separate them into the essential layer taxonomy (currently 17 identified layers, subject to refinement)?

**Hypothesis**: The QS-QIRAAT dataset conflates at least 6 distinct layers (Layer 5: Verse structure, Layer 6: Surah structure, Layer 8: Chapter structure, Layer 9: Qiraah manuscript, Layer 11: Page layout, Layer 12: Line layout) into a single flat data structure, and this conflation can be identified and quantified through schema analysis.

**Context**: The QS-QIRAAT dataset contains **6 narrations from 3-4 Qiraat** (Hafs, Warsh, Qalun, Shu'bah, Al-Duri, Al-Susi), representing 2 complete Qiraat (Asim with both narrations, Nafi' with both narrations) plus 1-2 additional Qiraat with partial narration coverage. **Phase 1 delivery focuses on Hafs and Warsh only** (12,450 verse records total: Hafs 6,236 + Warsh 6,214) per Constitution Principle VI, but **Phase 1 research SHOULD analyze multiple narrations from QS-QIRAAT** (ideally 3-4 Qiraat) to validate schema generalizability. The dataset currently mixes organizational metadata (jozz, page, line_start/end), textual content (aya_text in Uthmanic script, aya_text_emlaey in standard script), and manuscript-specific formatting into flat verse-level records. This mixing prevents proper layer-based querying, cross-Qiraah comparison, and generative architecture. Understanding WHAT is mixed is the foundational research question before we can design separation strategies.

**Qiraat Research Scope**: Analyze available narrations from QS-QIRAAT (6 narrations from 3-4 Qiraat) to validate schema generalizability across Qiraat

**Qiraat Delivery Scope**: Hafs and Warsh narrations only (2 narrations from 2 different Qiraat: Asim and Nafi') for Phase 1 per Constitution VI

**Why this priority**: This is P1 because we cannot design a layered architecture or build simulation until we understand the current state problem. All other RRs depend on this analysis mapping QS-QIRAAT fields to QUD layers.

**Independent Validation**: Can be validated by manually mapping each QS-QIRAAT dataset field to the layer taxonomy (currently 17 identified layers), documenting which layers are present (explicitly or implicitly), which are mixed, and which are missing. Success is measured by producing a complete mapping table and layer conflation matrix.

**Validation Scenarios**:

1. **Given** QS-QIRAAT Hafs JSON dataset (6,236 verse records), **When** schema analysis extracts field semantics (id, jozz, page, sura_no, sura_name_en, sura_name_ar, line_start, line_end, aya_no, aya_text, aya_text_emlaey), **Then** each field is mapped to one or more QUD layers with confidence score (e.g., "jozz" → Layer 7 Division Structure, "aya_text" conflates Layers 0-2 + Layer 3 Words + Layer 13 Orthography)

2. **Given** narrations from multiple Qiraat in QS-QIRAAT (Hafs from Asim, Warsh from Nafi', and optionally Qalun from Nafi', Shu'bah from Asim), **When** cross-Qiraah field comparison is performed, **Then** identify which fields vary across Qiraat (indicating Qiraah-specific concerns) vs which are structurally identical (indicating shared higher-layer concerns like Layers 5/6/7/8). Document findings about schema generalizability.

3. **Given** manually created ground truth for 10 sample verses mapping text to Layers 0-3 (character composition, symbols/rendering, paired data, words), **When** QS-QIRAAT "aya_text" field is analyzed for these verses, **Then** confirm that it conflates multiple layers by demonstrating inability to independently extract Layer 0 vs Layer 2 information

**Data Layer Dependencies**: Requires understanding of all identified layers (currently 17 layers) to perform mapping analysis. NOTE: The exact number of data layers is still under investigation and may change as research progresses.

**Schema Requirements**: None for this RR (analysis phase). Creates input for subsequent schema design RRs.

**Expected Findings Format**:
- **Mapping Table**: QS-QIRAAT field → QUD layer(s) mapping with confidence scores
- **Conflation Matrix**: NxN matrix showing which layers are mixed in which fields
- **Gap Analysis**: Which of the identified layers (currently 17) are completely missing from QS-QIRAAT
- **Cross-Qiraah Variance Report**: Which fields differ across narrations from different Qiraat (Hafs from Asim vs. Warsh from Nafi', and optionally other narrations) and what that reveals about layer concerns. Document findings about schema generalizability across the 10 canonical Qiraat.

---

### RR-002 - Schema Design for Separated Layers (Priority: P2)

**Research Question**: Can we define formal schemas for each of the identified Quranic data layers (currently 17 layers, subject to refinement) that: (1) eliminate the conflation identified in RR-001, (2) enable algorithmic generation of lower layers from higher layers, and (3) preserve all information currently in QS-QIRAAT while improving queryability?

**Hypothesis**: A schema-first approach defining all identified layers independently (currently 17 layers), designed to accommodate all 10 canonical Qiraat but validated with **Hafs and Warsh narrations** (2 narrations from 2 different Qiraat: Asim and Nafi'), will reduce data redundancy by >40%, enable cross-Qiraah queries currently impossible in QS-QIRAAT (e.g., "show all verses where Hafs and Warsh differ at the character level"), and support generative architecture where derivative layers can be computed from source layers + Qiraah-specific rules. Schema design tested with multiple narrations from QS-QIRAAT ensures generalizability across all 10 canonical Qiraat.

**Qiraat Research Scope**: Schema design validated by analyzing multiple narrations from QS-QIRAAT (ideally 3-4 Qiraat including Asim, Nafi', and optionally Abu Amr)

**Qiraat Delivery Scope**: Hafs and Warsh narrations only (2 narrations from 2 different Qiraat: Asim and Nafi') for Phase 1 per Constitution VI

**Context**: Builds on RR-001 findings. Once we know what's mixed, we need to design the "unmixed" architecture. This RR focuses on SCHEMA DEFINITION - what fields, types, constraints, and relationships exist in each layer. The constitution mandates schema-first development: define the schema before generating data. This RR produces those schemas based on: (1) what QS-QIRAAT currently provides, (2) what the layer taxonomy requires (currently 17 identified layers), (3) what generative rules will need as inputs/outputs.

**Why this priority**: P2 because it depends on RR-001's mapping. Cannot design separated schemas until we know what's currently conflated. But this must precede RR-003 (simulation) because simulation needs target schemas to simulate.

**Independent Validation**: Can be validated by: (1) defining JSON Schema or similar formal specifications for each identified layer (currently 17 layers), (2) demonstrating that QS-QIRAAT Hafs/Warsh data can be transformed into these schemas without information loss, (3) implementing schema validators and running them on sample data.

**Validation Scenarios**:

1. **Given** QS-QIRAAT verse record for Al-Fatiha verse 1, **When** transformation algorithm splits it into multi-layer format per designed schemas, **Then** all original information is preserved AND new queryability is gained (e.g., can independently query Layer 5 verse structure without Layer 11 page layout concerns)

2. **Given** schema definitions for Layers 0 (Character Composition) and 2 (Character Paired Data), **When** aya_text "بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ" is parsed, **Then** Layer 0 extracts base letters (ب س م ا ل ل ه...) separate from Layer 2 diacritics (kasra on ب, sukoon on س, hamzatul-wasl on الله, etc.)

3. **Given** schemas for all identified layers instantiated with Hafs Al-Fatiha data, **When** storage size is compared to QS-QIRAAT flat structure, **Then** redundancy reduction >40% achieved (hypothesis validation) because certain layers are normalized and not repeated per verse

**Data Layer Dependencies**: Defines schemas for ALL identified layers (currently 17 layers).

**Schema Requirements**:
- **Layer 0 Schema**: Character composition (base letters, phonetic metadata)
- **Layer 1 Schema**: Character symbols and rendering data (visual representation rules)
- **Layer 2 Schema**: Character Paired Data (diacritics, tajweed marks)
- **Layer 3 Schema**: Word structure (word boundaries, morphology)
- **Layer 4 Schema**: Sentence structure (grammar, waqf/ibtida)
- **Layer 5 Schema**: Verse structure (words numbers, boundaries)
- **Layer 6 Schema**: Surah structure (aya numbers, boundaries)
- **Layer 7 Schema**: Division structure (juz, hizb, rub)
- **Layer 8 Schema**: Chapter structure (sura metadata)
- **Layer 9 Schema**: Qiraah manuscript (complete text per riwayah)
- **Layer 10 Schema**: Edition variants (publisher-specific formatting)
- **Layer 11 Schema**: Page layout (page numbers, page breaks)
- **Layer 12 Schema**: Line layout (line numbers, line breaks)
- **Layer 13 Schema**: Orthographic systems (Uthmanic vs Standard script)
- **Layer 14 Schema**: Readers and narrators (biographical, isnad chains)

**Expected Findings Format**:
- **JSON Schema files**: One per layer in `schemas/layer-XX-name/schema.json` (formal specification for data interchange and validation)
- **Pydantic Models**: Python models in `schemas/layer-XX-name/models.py` (type-safe Python representations with runtime validation)
- **Schema Documentation**: README per layer explaining domain semantics, generation rules, dependencies
- **Transformation Algorithm Specification**: Pseudocode/flowchart showing how QS-QIRAAT maps to 14-layer format
- **Redundancy Analysis Report**: Storage size comparison, query performance theoretical analysis

---

### RR-003 - Layer Simulation Prototype (Priority: P3)

**Research Question**: Can we build a working simulation that: (1) ingests QS-QIRAAT Hafs and Warsh data, (2) transforms it into the multi-layer architecture (currently 17 identified layers) per RR-002 schemas, (3) demonstrates generative layer production (e.g., generating Layer 2 paired data from Layer 0 + Qiraah-specific rules), and (4) validates against authoritative sources?

**Hypothesis**: A simulation processing **Hafs (6,236 verses) and Warsh (6,214 verses) = 12,450 total verse records** (representing 2 narrations from 2 different Qiraat: Asim and Nafi') can successfully separate layers, generate derivative layers via rules, conform to defined schemas with <1% error rate, and enable previously impossible cross-Qiraah queries (e.g., "show character-level differences between Hafs and Warsh for Surah Al-Baqarah").

**Note**: Schemas are designed to accommodate all 10 canonical Qiraat. Phase 1 delivery fulfills data for 2 narrations from 2 Qiraat (Hafs from Asim, Warsh from Nafi'); Phase 2-3 expands to additional narrations per Constitution VI.

**Qiraat Research Scope**: Schema generalizability validated by testing with multiple narrations from QS-QIRAAT where feasible

**Qiraat Delivery Scope**: Hafs and Warsh narrations only (2 narrations from 2 different Qiraat: Asim and Nafi') for Phase 1 per Constitution VI

**Context**: Builds on RR-001 (knows what's mixed) and RR-002 (has schemas to separate into). This RR is the IMPLEMENTATION PROOF - does the architecture work in practice? The simulation is Tier 1 experimental code (per constitution's code quality tiers), focused on validating the architectural approach with Hafs and Warsh narrations (from 2 different Qiraat), not building production infrastructure. Success means demonstrating feasibility of layer separation and generation, proving the schemas work across Qiraah boundaries (Asim vs. Nafi'), providing a validated foundation for Phase 2-3 expansion to additional narrations and Qiraat.

**Why this priority**: P3 because it depends on RR-001 findings and RR-002 schemas. This is validation/demonstration, not foundational analysis. However, this produces the tangible artifact that proves or disproves the layered architecture hypothesis.

**Independent Validation**: Can be validated by: (1) running simulation on Hafs and Warsh datasets (2 narrations from 2 different Qiraat), (2) automated schema validation for all generated layer data, (3) automated character/verse count verification against authoritative sources, (4) successfully executing cross-Qiraah queries impossible in original QS-QIRAAT format. Scholarly review of results conducted at end of each research cycle. Phase 2-3 will extend data fulfillment to additional narrations and Qiraat.

**Validation Scenarios**:

1. **Given** QS-QIRAAT Hafs dataset (6,236 verses), **When** simulation ingests and transforms to multi-layer format (currently 17 identified layers), **Then** automated validators confirm character count matches authoritative source (323,015 characters for Hafs), verse count matches (6,236 for Hafs), and schema validation passes for all layers. Engineering team presents demo to scholars at cycle end; scholar feedback confirms theological accuracy.

2. **Given** Qiraah-specific tajweed rules (e.g., idgham, iqlab, ikhfa rules which may differ between Asim and Nafi'), **When** generative engine processes Layer 0 character data, **Then** Layer 2 tajweed marks are correctly generated and match QS-QIRAAT "aya_text" for same verses (proving generation works and original data preserves this information even if mixed)

3. **Given** separated Layer 5 verse structure data for both Hafs (from Asim) and Warsh (from Nafi') narrations, **When** cross-Qiraah diff query "find verse count differences" is executed, **Then** simulation correctly identifies known differences (Hafs: 6,236 verses, Warsh: 6,214 verses per constitution's domain knowledge) and can explain which suras differ between these two Qiraat

4. **Given** Layer 11 page layout and Layer 12 line layout data extracted from QS-QIRAAT (page, line_start, line_end fields), **When** page-reconstruction query "regenerate page 1 of Hafs Mushaf" is executed, **Then** simulation correctly places verses on correct lines matching original QS-QIRAAT structure (proving no information loss in layer separation)

**Data Layer Dependencies**: Uses ALL identified layers (currently 17 layers). Demonstrates both extraction from QS-QIRAAT and generation via rules.

**Schema Requirements**: Uses all schemas from RR-002. This RR validates those schemas work in practice.

**Expected Findings Format**:
- **Simulation Code**: Python prototype in `experiments/rr-003-layer-simulation/` using NLTK and NLP libraries for text processing
- **Interactive Analysis**: Jupyter notebooks documenting exploratory analysis, transformation logic, and validation results
- **Visualization**: Data layer visualization tools showing layer relationships, conflation patterns, and cross-Qiraah differences
- **Sample Database**: SQLite database containing transformed 15-layer architecture data for demonstration and query testing
- **Processing Metrics**: Time to process Hafs and Warsh (2 narrations from 2 Qiraat), memory usage, schema validation pass/fail counts. Phase 2-3 extends to additional narrations and Qiraat.
- **Validation Report**: Character count verification, verse count verification, automated validation results
- **Query Capability Demonstration**: Examples of queries enabled by layered architecture vs impossible in flat QS-QIRAAT
- **Generation Success Rate**: For layers marked as generative (e.g., Layer 0→2 character to diacritics), percentage of successfully generated vs manually encoded
- **Findings Analysis**: What worked, what failed, what schema refinements needed, ADR if architectural decisions made

---

### Domain Constraints

**Qiraat and Narrations**: The QS-QIRAAT dataset contains **6 narrations from 3-4 Qiraat**: Hafs (Asim), Warsh (Nafi'), Qalun (Nafi'), Shu'bah (Asim), Al-Duri (Abu Amr or Al-Kisa'i), Al-Susi (Abu Amr). This represents 2 complete Qiraat (Asim and Nafi' with both primary narrations each) plus partial coverage of 1-2 additional Qiraat. **Phase 1 delivery (Months 1-2) ships Hafs and Warsh ONLY** (2 narrations from 2 different Qiraat: Asim and Nafi') per Constitution Principle VI. **Phase 1 research SHOULD analyze multiple narrations from QS-QIRAAT** (ideally 3-4 Qiraat) to validate schema generalizability. Phase 2-3 (Months 2-6) will expand delivery to additional narrations. Constitution mandates eventual support for all 10 canonical Qiraat (القراءات العشر) and their 20 narrations, but Phase 1 delivery deliberately limits to 2 narrations from 2 Qiraat to prevent scope creep while ensuring schemas are validated across Qiraah boundaries.

**Phase Transition Criteria**: Phase 1 to Phase 2 transition requires: (1) RR-001 complete with validated layer mapping analysis, (2) RR-002 complete with validated schemas for all identified layers, (3) RR-003 complete with working simulation transforming Hafs and Warsh data, (4) All validation criteria (VC-001 through VC-011) met for Hafs+Warsh, (5) Engineering-mediated scholarly review completed with theological accuracy confirmed and feedback incorporated into specs/data.

**Cross-Layer Identity and Mapping**: CRITICAL REQUIREMENT for handling Qiraah variants and orthographic transformations:
- **UUID Assignment**: Every entity in all identified layers (currently 17 layers) MUST have a unique UUID identifier
- **Bidirectional Mapping**: Each entity maps to corresponding items in adjacent and related layers (previous, next, and cross-cutting layers)
- **Cardinality Handling**: Mappings support one-to-one, one-to-many, and many-to-one relationships across layers
- **Versioned Mappings**: All cross-layer mappings include version information to track schema evolution
- **Semantic Hashing**: After establishing UUID mappings, generate semantic hashes representing the semantic relationship between mapped entities

**Expansion/Contraction Cases** (core mapping challenges):

1. **Orthographic Expansion** (Character Layer):
   - **Case**: 2 characters in Qiasy/Imla'i (قياسي/إملائي) orthography → 1 character in Uthmani (عثماني) orthography
   - **Example**: Letter variants that collapse in Uthmani script (e.g., final taa variants, hamza forms)
   - **Mapping Strategy**: Single Layer 0 UUID (Uthmani character) maps to TWO Layer 0 UUIDs (Qiasy representation), using character position/order to precisely track expansion
   - **Layer Affected**: Layer 0 (Character Composition) when transforming between Layer 13 orthographic systems

2. **Verse Boundary Variation** (Verse/Surah Layers):
   - **Case**: 1 Ayah in Qira'ah A = 2 Ayahs in Qira'ah B (verse count differences across Qiraat)
   - **Example**: Hafs has 6,236 verses, Warsh has 6,214 verses - same content, different verse boundaries
   - **Mapping Strategy**: Layer 5 Verse entity UUID in Hafs maps to MULTIPLE Layer 5 Verse UUIDs in Warsh (or vice versa for contraction)
   - **Numbering Solution**: UUID-based identity resolves controversial verse numbering by maintaining canonical identity independent of positional numbering
   - **Layers Affected**: Layer 5 (Verse Structure), Layer 6 (Surah Structure) - verse-to-surah relationships differ across Qiraat

**Mapping Precision Requirements**:
- Character-level order tracking for expansion/contraction
- Positional metadata to reconstruct original ordering
- Provenance tracking: which Qiraah/narration/orthography the mapping originates from
- Bidirectional traversal: can navigate from any layer entity to related entities in other layers

**Character/Verse Count Validation**:
- **Hafs**: MUST validate 6,236 verses, 323,015 characters (or document authoritative count)
- **Warsh**: MUST validate 6,214 verses (known difference from Hafs)
- **Cross-Qiraah Differences**: Known differences in verse counts across Qiraat are CORE REQUIREMENTS, not edge cases (constitution Principle IV)

**Authoritative Sources**:
- **Primary Source for this Research**: QS-QIRAAT dataset v2.0 (6 narrations from 3-4 Qiraat from King Fahd Quranic Printing Complex)
- **Validation Sources**: King Fahd Complex published editions, Tanzil.net verified datasets
- **Font/Rendering**: kfgqpc_hafs_uthmanic_script (included in QS-QIRAAT) for Uthmanic rendering

**Theological Accuracy Requirements**:
- ZERO tolerance for errors in sacred text content (Principle IV of constitution)
- Generation applies to STRUCTURE and METADATA layers (1-4, symbols, boundaries), NOT to the sacred text words themselves
- Any generated layer MUST be validated against authoritative sources
- Conflation identified in RR-001 is acceptable for analysis; separation in RR-003 MUST NOT introduce errors

**Dataset-Specific Constraints**:
- QS-QIRAAT Version 2.0 format (11 fields per verse record as documented in readme)
- UTF-8 encoding (UTF-8-BOM for CSV)
- Aya marks encoded as symbols (ﰀ ﰁ ﰂ etc.) in aya_text field
- Non-breaking spaces used before aya marks and after jozz/hizb symbols (documented in QS-QIRAAT v2.0 update log)

---

## QUD Orchestrator and MUDMAJ Architecture

### Architectural Vision

**CRITICAL ARCHITECTURAL PRINCIPLE**: The layer versioning controversy is NOT limited to verse numbering - it affects ALL data layers (currently 17 identified layers). Each layer has multiple content versions determined by a **set of contextual parameters** (Qiraah/narration, orthographic system, edition, scholarly tradition, etc.). The architecture consists of two primary components:

1. **QUD (Layered Universal Big Data)**: The product/interface that maintains contextual information and orchestrates queries
2. **MUDMAJ (المدمج - "The Merged")**: The underlying merged database containing all interconnected and interrelated versions of the Quranic dataset with proper layer information

### The Contextual Versioning Problem

**Multi-Layer Version Explosion**: Every data layer can have different versions based on context:

- **Layer 0 (Character Composition)**: Different character sets for different Qiraat (Hafs vs Warsh pronunciation differences affect character representation)
- **Layer 1 (Symbols/Rendering)**: Different diacritics and tajweed marks across scholarly traditions
- **Layer 2 (Character Paired Data)**: Different tajweed pair rules across different schools of tajweed
- **Layer 3 (Word Structure)**: Word boundary variations across Qiraat
- **Layer 4 (Sentence Structure)**: Waqf/ibtida rule variations across scholarly traditions
- **Layer 5 (Verse Structure)**: Different verse numbering systems (Hafs 6,236 vs Warsh 6,214)
- **Layer 6 (Surah Structure)**: Verse count differences per surah across Qiraat
- **Layer 7-14**: Contextual variations in higher organizational layers

**Context Schema** (HYPOTHETICAL - TO BE VALIDATED IN RR-014): A "context" is hypothesized to be a **set of parameters** that collectively determine which version of each layer to use. The following is a SAMPLE structure for research exploration:

```json
{
  "context_id": "UUID",
  "qiraah_narration": "hafs_an_asim | warsh_an_nafi | qalun_an_nafi | ...",  // SAMPLE - Qiraah + narration identifier
  "orthographic_system": "uthmani | qiasy | imla'i",     // SAMPLE - may need refinement
  "edition": "king_fahd_complex | ...",                  // SAMPLE - may discover more editions
  "tajweed_school": "al_jazari | ibn_kathir | ...",      // SAMPLE - research will identify valid schools
  "scholarly_tradition": "...",                          // SAMPLE - placeholder, needs research
  "geographic_origin": "medina | kufa | basra | ...",    // SAMPLE - may not be relevant
  "time_period": "classical | modern",                   // SAMPLE - may not be relevant
  "custom_parameters": {}                                // Extensibility for discovered parameters
}
```

**RESEARCH NOTE**: RR-014 will determine:
- Which context parameters are actually necessary vs optional
- Valid values for each parameter (e.g., complete list of tajweed schools)
- Parameter dependencies (e.g., does tajweed_school depend on geographic_origin?)
- Which parameters affect which layers (context inheritance rules)
- Minimal context set required for unambiguous layer version resolution

### QUD Orchestrator: The Brain

**Purpose**: The QUD Orchestrator is the intelligent query router that:
1. Receives queries from clients
2. Analyzes required context parameters
3. Resolves which layer version(s) to query
4. Routes queries to appropriate MUDMAJ layer versions
5. Assembles results from multiple layer versions if needed

**Core Responsibilities**:

1. **Context Resolution**:
   ```
   Query: "Get verse 2:285 in Hafs narration with Uthmani script from King Fahd Complex edition"

   Orchestrator extracts context:
   - qiraah_narration: hafs_an_asim
   - orthographic_system: uthmani
   - edition: king_fahd_complex
   - layer_request: 5 (Verse)

   Orchestrator resolves layer versions:
   - Layer 5 version: hafs-context (6,236 verses)
   - Layer 0 version: hafs-uthmani-context (character composition)
   - Layer 12a version: uthmani-king_fahd-context (orthographic rendering)

   Returns: Assembled verse data from contextually-correct layer versions
   ```

2. **Layer Version Selection**:
   - Each layer asks QUD: "Which context am I operating in?"
   - QUD Orchestrator returns the appropriate context parameters
   - Layer retrieves its context-specific version from MUDMAJ

3. **Cross-Context Query Support**:
   ```
   Query: "Compare verse 2:285 across Hafs and Warsh narrations"

   Orchestrator must:
   - Resolve TWO contexts (hafs-context, warsh-context)
   - Query Layer 5 in both contexts
   - Use canonical_verse_id to find equivalent verses
   - Return comparative results
   ```

4. **Context Inheritance and Default Rules**:
   - Some context parameters apply to all layers (e.g., qiraah_narration)
   - Some are layer-specific (e.g., tajweed_school only affects Layers 1-2)
   - Orchestrator maintains context inheritance hierarchy

### MUDMAJ: The Merged Database

**Purpose**: MUDMAJ is the underlying storage system containing:
1. All layer versions for all contexts
2. Cross-layer mappings (EntityMapping structures)
3. Cross-context mappings (canonical identities like canonical_verse_id)
4. Context resolution metadata

**Schema Organization** (HYPOTHETICAL SAMPLE - TO BE VALIDATED IN RR-015):

The following is a SAMPLE directory structure for MUDMAJ storage. Actual implementation may differ based on research findings, storage technology choices (relational DB, document store, graph DB, etc.), and performance requirements:

```
MUDMAJ/  # SAMPLE STRUCTURE - subject to research validation
├── layer_versions/
│   ├── layer_00_character_composition/
│   │   ├── hafs_uthmani_version/        # EXAMPLE version
│   │   ├── hafs_qiasy_version/          # EXAMPLE version
│   │   ├── warsh_uthmani_version/       # EXAMPLE version
│   │   └── warsh_qiasy_version/         # EXAMPLE version
│   ├── layer_05_verse_structure/
│   │   ├── hafs_version/                # EXAMPLE: 6,236 verses
│   │   └── warsh_version/               # EXAMPLE: 6,214 verses
│   └── [... all layers with context-specific versions]
│
├── cross_layer_mappings/
│   ├── entity_mappings/                 # EntityMapping structures
│   ├── canonical_identities/            # canonical_verse_id, etc. (if validated by research)
│   └── semantic_hashes/                 # SHA-256 hashes (if this approach validated)
│
├── context_metadata/
│   ├── context_definitions/             # Valid context parameter combinations
│   ├── version_registry/                # Catalog of layer versions and contexts
│   └── resolution_rules/                # Context resolution algorithm rules
│
└── provenance/
    ├── transformation_logs/             # How each version was generated
    ├── validation_results/              # Character counts, verse counts per version
    └── scholarly_reviews/               # Expert validation per layer version
```

**RESEARCH NOTE**: RR-015 will determine:
- Optimal storage technology (SQL, NoSQL, graph DB, hybrid approach)
- Actual directory/table structure for layer versions
- Indexing strategy for efficient context-based queries
- Delta storage mechanism (how to avoid duplicating identical data across contexts)
- Version naming convention (deterministic hash vs semantic naming)
- Whether canonical_identities are stored separately or embedded in entities
- Granularity of provenance tracking (per-entity vs per-version vs per-layer)

**Version Naming Convention** (SAMPLE - TO BE VALIDATED IN RR-015):
- Proposed format: `layer-{number}_{context-hash}_version-{semver}`
- Example: `layer-05_hafs-uthmani-kfc_version-1.0.0`
- Context hash would be deterministic based on sorted context parameters
- **RESEARCH QUESTION**: Is deterministic hashing better than human-readable names? Should we support both?

**Storage Implications** (HYPOTHESIS - TO BE VALIDATED):
- **Without MUDMAJ**: Each context requires separate full dataset (massive redundancy)
- **With MUDMAJ**: Shared immutable data referenced by multiple contexts, only deltas stored
- **Example Hypothesis**: Layer 6 (Surah metadata) is 99% identical across Qiraat - could be stored once, versioned minimally
- **RR-015 MUST VALIDATE**: Actual redundancy patterns, optimal storage strategy, query performance trade-offs

### Context-Aware Layer Versioning

**Layer Version Entity** (HYPOTHETICAL META-SCHEMA - TO BE VALIDATED IN RR-015):

The following is a SAMPLE entity structure for tracking layer versions. Actual schema will be refined through research:

```json
{
  "layer_version_id": "UUID",
  "layer_number": "integer (0-14)",
  "context_parameters": {                    // SAMPLE - actual params from RR-014 research
    "qiraah_narration": "hafs_an_asim",
    "orthographic_system": "uthmani",
    "edition": "king_fahd_complex"
    // ... other context params as discovered
  },
  "version_semver": "1.0.0",
  "entity_count": "integer - how many entities in this version",
  "parent_version_id": "UUID - if derived from another version",  // HYPOTHESIS: version lineage tracking
  "generation_rules": "reference to rules that generated this version",
  "validation_status": {                     // SAMPLE validation metadata
    "character_count": 323015,               // if applicable to this layer
    "verse_count": 6236,                     // if applicable to this layer
    "schema_validation": "pass",
    "scholarly_review": "approved"
  },
  "provenance": {
    "source_dataset": "QS-QIRAAT-v2.0",
    "transformation_pipeline": "...",
    "created_timestamp": "ISO-8601"
  }
}
```

**RESEARCH NOTE**: RR-015 will validate:
- Whether this meta-schema structure is sufficient or needs extension
- How to efficiently query by context_parameters (indexing strategy)
- Whether parent_version_id lineage tracking is useful or over-engineered
- Granularity of validation_status (should it be per-entity or per-version?)
- How to handle schema evolution (what if context_parameters structure changes?)

**Query Flow Example** (HYPOTHETICAL ILLUSTRATION - TO BE VALIDATED IN RR-016):

The following illustrates HOW the system MIGHT work. Actual query flow will be designed and validated through research:

```
1. Client → QUD Orchestrator:
   "Get all verses in Surah 2, Hafs narration, Uthmani script"

2. QUD Orchestrator analyzes query (HYPOTHETICAL ALGORITHM):
   - Extract required context: {qiraah_narration: hafs_an_asim, orthography: uthmani}
   - Identify required layers: Layer 5 (Verse), Layer 6 (Surah)
   - Resolve layer versions from context parameters

3. Orchestrator consults MUDMAJ version registry (HYPOTHETICAL):
   - Lookup: "Which Layer 5 version matches context {hafs_an_asim, uthmani}?"
   - Result: layer-05_hafs_v1.0.0
   - Lookup: "Which Layer 6 version matches context {hafs_an_asim}?"
   - Result: layer-06_hafs_v1.0.0

4. Orchestrator queries MUDMAJ (SAMPLE QUERY - actual implementation TBD):
   SELECT * FROM layer_05_hafs_v1_0_0
   WHERE surah_ref IN (
     SELECT surah_id FROM layer_06_hafs_v1_0_0 WHERE surah_number = 2
   )
   // NOTE: Assumes SQL storage - research may choose different approach

5. Results assembled and returned to client
```

**RESEARCH QUESTIONS FOR RR-016**:
- How to parse natural language queries into context parameters?
- Should we support query DSL, GraphQL, or REST API?
- How to handle ambiguous contexts (e.g., user doesn't specify edition)?
- What's the performance overhead of version resolution?
- Should orchestrator cache version mappings or query registry each time?

### Research Requirements Impact

This architectural vision requires additional Research Requirements:

- **RR-012** (UPDATED): Multi-Layer Contextual Versioning System - Demonstrate that ALL layers (currently 17 identified) can be versioned by context, not just verses
- **RR-014** (NEW): QUD Orchestrator Design - Define context resolution rules, query routing logic, version selection algorithms
- **RR-015** (NEW): MUDMAJ Schema Design - Define storage organization for multi-version layers, cross-context mappings, and efficient delta storage
- **RR-016** (NEW): Context-Aware Query Validation - Demonstrate queries across multiple contexts with correct version resolution

---

## Research Requirements *(mandatory)*

### Research Requirements (RR)

- **RR-001**: Research MUST analyze QS-QIRAAT dataset structure to identify which of the Quranic data layers (currently 17 identified layers) are currently mixed together in the flat schema

- **RR-002**: Research MUST map every QS-QIRAAT field  e.g. schema sample as an initial sample for the current data: (id, jozz, page, sura_no, sura_name_en, sura_name_ar, line_start, line_end, aya_no, aya_text, aya_text_emlaey) to the QUD layer taxonomy (currently 17 identified layers), documenting which layers are explicitly present, implicitly present, or completely missing

- **RR-003**: Analysis MUST produce a conflation matrix showing which pairs of layers are mixed in the same fields (e.g., "aya_text" conflates Layers 0, 1, 2, 3, 13)

- **RR-004**: Research MUST compare Hafs and Warsh narration datasets (Phase 1 per Constitution VI) to identify which fields vary (indicating Qiraah/narration-specific concerns) vs which are structurally identical (indicating shared higher layers like 5/6/7/8). Document findings that likely generalize to remaining narrations and Qiraat for Phase 2-3.

- **RR-005**: Research MUST design JSON Schema specifications for each of the identified layers (currently 17) that eliminate the conflation identified in RR-001-003 while preserving all information currently in QS-QIRAAT

- **RR-006**: Schema design MUST support generative architecture where derivative layers can be computed from source layers + Qiraah-specific rules (e.g., Layer 2 paired data generated from Layer 0 characters + Qiraah-specific tajweed rules)

- **RR-007**: Prototype MUST demonstrate transformation of QS-QIRAAT data into the multi-layer format for at least one complete narration (Hafs, 6,236 verses)

- **RR-008**: Simulation MUST validate generated layer data against authoritative sources, achieving 100% accuracy for verse counts, >99% accuracy for character counts (allowing for encoding differences)

- **RR-009**: Prototype MUST demonstrate at least 3 cross-Qiraah queries that are impossible or impractical in the flat QS-QIRAAT format but are enabled by the layered architecture

- **RR-010**: Research MUST measure and document redundancy reduction achieved by layer separation (hypothesis: >40% reduction in total storage when layers 6, 7, 8, 11, 12 are normalized)

- **RR-011**: Research MUST design and implement UUID-based cross-layer mapping system that:
  - Assigns unique UUIDs to every entity in all identified layers (currently 17)
  - Establishes bidirectional mappings between related entities across layers
  - Handles expansion/contraction cases (1-to-many, many-to-1 mappings)
  - Tracks mapping versions for schema evolution
  - Generates semantic hashes for relationship representation

- **RR-012**: Research MUST demonstrate multi-layer contextual versioning system by:
  - Proving that ALL layers (not just verses) can have context-specific versions
  - Defining context schema with parameters (qiraah_narration, orthography, edition, scholarly_tradition, etc.)
  - Showing that a single layer (e.g., Layer 0 Character Composition) can have multiple versions:
    * hafs-uthmani version (Hafs narration from Asim, Uthmani script)
    * hafs-qiasy version (Hafs narration from Asim, Qiasy script)
    * warsh-uthmani version (Warsh narration from Nafi', Uthmani script)
  - Demonstrating cross-context queries like "compare Layer 5 (Verse) in hafs-context vs warsh-context"
  - Validating that verse numbering controversy is ONE instance of the broader contextual versioning problem
  - Proving canonical identity mappings (canonical_verse_id) work across context versions

- **RR-013**: Mapping system MUST demonstrate orthographic transformation handling by:
  - Mapping character entities between Uthmani and Qiasy/Imla'i orthographies
  - Tracking expansion (1 Uthmani char → 2 Qiasy chars) with positional precision
  - Enabling reconstruction of either orthography from the other via UUID traversal

- **RR-014**: Research MUST design QUD Orchestrator component that:
  - Defines context resolution algorithm (extracts context parameters from queries)
  - Implements layer version selection logic (maps context → specific layer version)
  - Routes queries to appropriate MUDMAJ layer versions
  - Handles cross-context queries (comparing data across different contexts)
  - Defines context inheritance rules (which parameters apply to which layers)
  - Supports context parameter validation and error handling

- **RR-015**: Research MUST design MUDMAJ database schema that:
  - Organizes storage of multiple layer versions per context
  - Implements efficient delta storage (shared immutable data across contexts)
  - Defines version registry (catalog of all layer versions and their contexts)
  - Specifies context metadata storage (valid parameter combinations, resolution rules)
  - Optimizes for query performance across versioned layers
  - Maintains provenance tracking for all layer versions

- **RR-016**: Research MUST validate context-aware query system by:
  - Executing sample queries requiring single-context resolution
  - Executing sample queries requiring multi-context comparison (e.g., Hafs vs Warsh)
  - Demonstrating correct version selection for ambiguous contexts
  - Measuring query performance across context versions
  - Validating that cross-layer queries work within a context
  - Proving context isolation (queries in one context don't accidentally return data from another)

### Cross-Layer Mapping Entities

**Layer Mapping Structure** (meta-layer for cross-layer relationships):

- **EntityMapping**: Core mapping entity linking entities across layers
  - `mapping_id`: UUID - Unique identifier for this mapping
  - `source_layer`: integer - Source layer number (0-14)
  - `source_entity_id`: UUID - Entity UUID in source layer
  - `target_layer`: integer - Target layer number (0-14)
  - `target_entity_ids`: array of UUIDs - One or more target entities (handles 1-to-many)
  - `mapping_type`: enum - expansion/contraction/identity/derivation
  - `cardinality`: string - "1:1", "1:N", "N:1", "N:M"
  - `position_metadata`: object - Ordering information for expansion/contraction cases
  - `mapping_version`: string - Schema version this mapping corresponds to
  - `semantic_hash`: string - Hash representing semantic relationship
  - `provenance`: object - Which Qiraah/narration/orthography/edition this mapping is specific to
  - `bidirectional_ref`: UUID - Reference to reverse mapping (for efficient traversal)

**Orthographic Mapping Example** (Uthmani ↔ Qiasy character mapping):
```json
{
  "mapping_id": "550e8400-e29b-41d4-a716-446655440000",
  "source_layer": 0,
  "source_entity_id": "char-uthmani-taa-marbuta-uuid",
  "target_layer": 0,
  "target_entity_ids": ["char-qiasy-ha-uuid", "char-qiasy-taa-uuid"],
  "mapping_type": "expansion",
  "cardinality": "1:2",
  "position_metadata": {"order": [0, 1], "context": "word-final"},
  "mapping_version": "1.0.0",
  "semantic_hash": "sha256:abc123...",
  "provenance": {"orthography": "uthmani-to-qiasy"},
  "bidirectional_ref": "reverse-mapping-uuid"
}
```

**Verse Boundary Mapping Example** (Hafs ↔ Warsh verse mapping):
```json
{
  "mapping_id": "660e8400-e29b-41d4-a716-446655440001",
  "source_layer": 5,
  "source_entity_id": "hafs-surah2-verse20-uuid",
  "target_layer": 5,
  "target_entity_ids": ["warsh-surah2-verse19-uuid", "warsh-surah2-verse20-uuid"],
  "mapping_type": "contraction",
  "cardinality": "1:2",
  "position_metadata": {"hafs_verse": 20, "warsh_verses": [19, 20], "split_point": "character-offset-45"},
  "mapping_version": "1.0.0",
  "semantic_hash": "sha256:def456...",
  "provenance": {"qiraah_narration_from": "hafs_an_asim", "qiraah_narration_to": "warsh_an_nafi"},
  "bidirectional_ref": "reverse-mapping-uuid"
}
```

**Semantic Hashing Strategy**:
- Combine entity content + structural position + relationship type
- Generate deterministic hash (SHA-256) representing semantic equivalence
- Enables query: "find all semantically equivalent entities across Qiraat"
- Version-aware: hash changes if semantic relationship changes

### Key Data Entities

**Current State (QS-QIRAAT Mixed Layers)**:

- **QS-Verse Record**: Single flat record per verse containing: jozz (Layer 7), page (Layer 11), sura metadata (Layer 8), line positioning (Layer 12), verse number (Layers 5+6), complete verse text in Uthmanic script conflating Layers 0+1+2+3+13, search text in standard script (Layer 13 variant)

**Target Architecture (QUD Separated Layers)** - All entities include UUID for cross-layer mapping:

- **Layer 0 - Character Composition**:
  - **Entity**: Character
  - **Fields**: `character_id` (UUID), base letter (حرف), phonetic metadata, character sequence position, orthography_type (uthmani/qiasy/imlaai)
  - **Cross-Layer Mapping**: Maps to Layer 1 (rendering), Layer 2 (paired data), Layer 13 (orthographic variants via expansion/contraction)
  - **Generation rules**: Extracted from authenticated source text, validated against character count requirements (323,015 for Hafs)
  - **UUID Purpose**: Enables precise tracking of orthographic transformations (1 Uthmani UUID ↔ 2 Qiasy UUIDs)

- **Layer 1 - Character Symbols and Rendering Data**:
  - **Entity**: CharacterRenderingSymbol
  - **Fields**: `rendering_id` (UUID), character_ref (UUID to Layer 0), positional forms, ligature rules, rendering metadata
  - **Cross-Layer Mapping**: Maps to Layer 0 (character composition), references Layer 2 (visual pairing with diacritics)
  - **Generation rules**: Derived from font metadata (kfgqpc_hafs_uthmanic_script) and Arabic typographic rules
  - **UUID Purpose**: Links visual representation to base character identity

- **Layer 2 - Character Paired Data**:
  - **Entity**: CharacterPairedData
  - **Fields**: `paired_data_id` (UUID), character_ref (UUID to Layer 0), diacritics (tashkeel), tajweed marks, hamza forms, maddah
  - **Cross-Layer Mapping**: Maps to Layer 0 (which character), Layer 1 (rendering context), generated from Qiraah-specific rules
  - **Generation rules**: CAN BE GENERATED from Layer 0 + Qiraah-specific tajweed rules (RR-003 hypothesis to validate)
  - **UUID Purpose**: Tracks diacritic-character relationships, enables comparison across Qiraat

- **Layer 3 - Word Structure**:
  - **Entity**: Word
  - **Fields**: `word_id` (UUID), character_refs (array of Layer 0 UUIDs), word boundaries, morphological data, position in verse
  - **Cross-Layer Mapping**: Aggregates Layer 0 (characters), maps to Layer 4 (sentence), Layer 5 (verse)
  - **Generation rules**: Word segmentation algorithm on Layer 0+2 output, validated against authoritative word counts (77,429 words Hafs)
  - **UUID Purpose**: Canonical word identity across Qiraat, even if character composition differs

- **Layer 4 - Sentence Structure**:
  - **Entity**: Sentence
  - **Fields**: `sentence_id` (UUID), word_refs (array of Layer 3 UUIDs), grammar, waqf rules, ibtida rules
  - **Cross-Layer Mapping**: Aggregates Layer 3 (words), maps to Layer 5 (verse)
  - **Generation rules**: Currently MISSING from QS-QIRAAT - would require external linguistic databases or manual encoding
  - **UUID Purpose**: Sentence identity for grammatical analysis

- **Layer 5 - Verse Structure**:
  - **Entity**: Verse
  - **Fields**: `verse_id` (UUID), verse_number (position-based), canonical_verse_id (UUID for cross-Qiraah identity), verse boundaries, qiraah_narration_ref
  - **Cross-Layer Mapping**: Contains Layer 3/4 (words/sentences), maps to Layer 6 (surah), CRITICAL for verse numbering resolution (1 Hafs verse ↔ 2 Warsh verses)
  - **Generation rules**: Directly extracted from QS-QIRAAT aya_no field, validated against known counts (6,236 Hafs, 6,214 Warsh)
  - **UUID Purpose**: **SOLVES VERSE NUMBERING CONTROVERSY** - canonical_verse_id maintains identity independent of positional numbering across Qiraat

- **Layer 6 - Surah Structure**:
  - **Entity**: Surah
  - **Fields**: `surah_id` (UUID), aya_refs (array of Layer 5 UUIDs), verse grouping, organization within surahs, surah-verse relationships
  - **Cross-Layer Mapping**: Aggregates Layer 5 (verses), maps to Layer 8 (chapter metadata)
  - **Generation rules**: Extracted from QS-QIRAAT combining aya_no and sura_no to establish verse positions within chapters
  - **UUID Purpose**: Surah identity with verse composition that varies by Qiraah

- **Layer 7 - Division Structure**:
  - **Entity**: Division (Juz/Hizb/Rub)
  - **Fields**: `division_id` (UUID), division_type, division_number, verse_refs (array of Layer 5 UUIDs)
  - **Cross-Layer Mapping**: References Layer 5 (verses), independent of page/line layout
  - **Generation rules**: Extracted from QS-QIRAAT jozz field + aya_text hizb symbols, normalized to remove redundancy
  - **UUID Purpose**: Division identity across different editions/layouts

- **Layer 8 - Chapter Structure**:
  - **Entity**: Chapter
  - **Fields**: `chapter_id` (UUID), sura_number, names (sura_name_en, sura_name_ar), Makki/Madani classification, themes, surah_ref (UUID to Layer 6)
  - **Cross-Layer Mapping**: References Layer 6 (surah structure with verses)
  - **Generation rules**: Extracted from QS-QIRAAT sura fields, enhanced with external metadata (Makki/Madani from traditional sources)
  - **UUID Purpose**: Canonical chapter identity

- **Layer 9 - Qiraah Manuscript**:
  - **Entity**: Manuscript
  - **Fields**: `manuscript_id` (UUID), qiraah_name, narration_name, narrator, composed_from_layers (references to Layers 0-8), complete_text
  - **Cross-Layer Mapping**: Composition of Layers 0-8, references Layer 14 (reader/narrator biographical data)
  - **Generation rules**: Composition of Layers 0-8 specific to each Qiraah/narration, validated against King Fahd Complex editions
  - **UUID Purpose**: Unique manuscript identity per Qiraah/narration combination

- **Layer 10 - Edition Variants**:
  - **Entity**: Edition
  - **Fields**: `edition_id` (UUID), publisher, edition_name, manuscript_ref (UUID to Layer 9), formatting_differences
  - **Cross-Layer Mapping**: References Layer 9 (manuscript), determines Layer 11/12 (page/line layout)
  - **Generation rules**: Currently implicit in QS-QIRAAT (assumes King Fahd Complex v2.0 formatting) - would extract differences when comparing to other publishers' editions
  - **UUID Purpose**: Edition identity for layout variations

- **Layer 11 - Page Layout**:
  - **Entity**: Page
  - **Fields**: `page_id` (UUID), page_number, edition_ref (UUID to Layer 10), verse_refs (array of Layer 5 UUIDs), page breaks
  - **Cross-Layer Mapping**: References Layer 10 (edition), contains Layer 5 (verses), contains Layer 12 (lines)
  - **Generation rules**: Extracted from QS-QIRAAT page field, normalized (page layout repeated per verse in flat format - major redundancy to eliminate)
  - **UUID Purpose**: Page identity within specific edition

- **Layer 12 - Line Layout**:
  - **Entity**: Line
  - **Fields**: `line_id` (UUID), line_number, page_ref (UUID to Layer 11), verse_refs (array of Layer 5 UUIDs), character_range (start/end Layer 0 UUIDs), line breaks
  - **Cross-Layer Mapping**: References Layer 11 (page), contains portions of Layer 5 (verses) via Layer 0 (characters)
  - **Generation rules**: Extracted from QS-QIRAAT line_start/line_end fields, normalized (line layout repeated per verse - another major redundancy)
  - **UUID Purpose**: Line identity within page, precise character-level positioning

- **Layer 13 - Orthographic Systems**:
  - **Entity**: OrthographicRepresentation
  - **Fields**: `orthography_id` (UUID), system_type (uthmani/qiasy/imlaai), verse_ref (UUID to Layer 5), character_refs (array of Layer 0 UUIDs with orthography-specific variants), transformation_rules
  - **Cross-Layer Mapping**: Maps Layer 5 (verse) to Layer 0 (characters) with orthography-specific representations, CRITICAL for expansion/contraction mappings
  - **Generation rules**: Uthmanic currently manually encoded in QS-QIRAAT; Standard CAN BE GENERATED via orthographic transformation rules (e.g., الصلوة → الصلاة)
  - **UUID Purpose**: **HANDLES ORTHOGRAPHIC EXPANSION/CONTRACTION** - enables mapping 1 Uthmani char UUID ↔ 2 Qiasy char UUIDs

- **Layer 14 - Readers and Narrators**:
  - **Entity**: ReaderNarrator
  - **Fields**: `reader_narrator_id` (UUID), name_ar, name_en, type (reader/narrator), biographical_data, isnad_chains, qiraah_rules, manuscript_refs (array of Layer 9 UUIDs)
  - **Cross-Layer Mapping**: Referenced by Layer 9 (manuscripts using this Qiraah/narration)
  - **Generation rules**: Currently MISSING from QS-QIRAAT - would require external scholarly databases (Ibn al-Jazari's "النشر في القراءات العشر")
  - **UUID Purpose**: Canonical reader/narrator identity across all Qiraah variants

### Layer Generation

**Current State Analysis** (what QS-QIRAAT provides):
- **Manually Encoded Layers**: 0, 2, 3, 5, 6, 7, 8, 11, 12, 13 (all present but many conflated)
- **Missing Layers**: 1 (implicit in font), 4 (not provided), 9 (composition of others), 10 (implicit in edition), 14 (not provided)
- **Conflation Problem**: aya_text field conflates Layers 0, 1, 2, 3, 13 into single unseparated text string

**Target Generative Architecture**:

- **Generation Approach**:
  1. **Extract and Normalize**: Separate the conflated QS-QIRAAT fields into individual layer data conforming to RR-002 schemas
  2. **Rule-Based Generation**: For layers marked as generative, implement transformation rules (e.g., Layer 0 → Layer 2 via tajweed rules)
  3. **Validation**: All generated layer data validated against authoritative sources using research-tools/validators
  4. **Provenance**: Track which data was extracted from QS-QIRAAT vs generated via rules vs manually encoded

- **Schema Definition**: Each of the identified layers (currently 17) will have dual schema representations (RR-002 deliverable):
  - **JSON Schema**: Formal specification in `schemas/layer-XX-name/schema.json` for data interchange, documentation, and cross-language validation
  - **Pydantic Models**: Python models in `schemas/layer-XX-name/models.py` for type-safe development, runtime validation, and IDE support
  - **Schema Content**: Both representations specify field names and types, required vs optional fields, constraints (e.g., verse_count for Layer 5 Hafs MUST equal 6236), cross-layer references (e.g., Layer 5 verse references Layer 8 chapter), and invariants that MUST hold (e.g., sum of all sura verse counts equals total verse count)

- **Validation Strategy**:
  - **Character Count Validation**: Automated comparison of Layer 0 character counts to authoritative sources (323,015 for Hafs)
  - **Verse Count Validation**: Automated comparison of Layer 5 verse counts to known values per narration
  - **Cross-Qiraah Consistency**: Automated verification that layers like 8 (chapter metadata) are identical across Qiraat except where Qiraah-specific rules dictate differences
  - **Generation Accuracy**: For generated layers (e.g., Layer 2 from Layer 0), automated comparison against QS-QIRAAT original data
  - **Schema Conformance**: Automated schema validators on all generated layer data; document all failures with root cause analysis. Validation failures inform schema refinement but do not block research progression (best-effort validation approach).
  - **Scholarly Validation**: Engineering team presents demo of generated data to domain scholars at end of each cycle. Scholars provide feedback on theological accuracy, especially for generated diacritics/tajweed marks and word boundaries. Engineering team incorporates feedback into subsequent iterations.

- **Provenance Tracking**:
  - Tag each layer data element with source: `extracted_from_qs_qiraat`, `generated_via_rule`, `manually_encoded`
  - For generated data, record generation rule ID and version
  - For extracted data, record source file path and record ID
  - Maintain transformation audit log: QS-QIRAAT record ID → QUD layer instances

### Data Sources & Validation

- **Primary Sources**:
  - QS-QIRAAT Dataset v2.0 (6 narrations from 3-4 Qiraat: Hafs, Warsh, Qalun, Shu'bah, Al-Duri, Al-Susi)
  - Location: `/Users/mac/Work/ITQAN Community/QUD/QS - QIRAAT/`
  - Format: JSON (primary for programmatic processing), CSV (for validation and manual inspection), with optional SQLite database creation for final sample/demo
  - Available formats: JSON, CSV, XML, SQL, XLSX per narration
  - Documentation: readme files per narration documenting structure and updates

- **Validation Sources**:
  - King Fahd Complex Quranic Printing Complex official editions (referenced in QS-QIRAAT readme as authoritative source)
  - Tanzil.net verified Quranic datasets (for cross-validation of verse counts and text accuracy)
  - Digital Khatt project (for character rendering rules, if available)

- **Supplementary NLP Resources** (for Phase 2-3 expansion):
  - **qul.tarteel.ai project**: Comprehensive Quranic NLP resources including:
    - Part-of-speech tagging corpora
    - Syntactical analysis datasets
    - Morphological analysis datasets
    - Multiple Quran corpora with standardization and mapping
  - **Important Note**: Majority of qul.tarteel.ai resources are HAFS narration. Qiraah/narration coverage needs verification before integration.
  - **Evaluation Criteria**: Research MUST verify which Qiraat and narrations are covered in qul.tarteel.ai resources before incorporating into QUD architecture
  - **Use Case**: Potential source for Layer 3 (Word Structure) morphological data and Layer 4 (Sentence Structure) syntactic data if Qiraah coverage aligns with Phase 2-3 goals

- **Validation Method**:
  1. **Automated Validation**: Schema validators for all identified layers (currently 17), character/verse count checks, cross-Qiraah consistency checks (executed during each research cycle for rapid iteration)
  2. **Scholarly Review**: Engineering team creates demo presentations of generated data and presents to domain scholars (scholars do not directly interact with the system). Scholars provide theological accuracy feedback, especially for Layer 2 diacritics/tajweed symbols and Layer 3 word boundaries. Engineering team incorporates feedback and updates specs/data accordingly. Reviews occur after each R&D cycle or in between cycles as needed.
  3. **Regression Testing**: As schemas and generation rules evolve, maintain automated test suite of known-good transformations
  4. **Cycle Definition**: Each RR (RR-001, RR-002, RR-003) constitutes one research cycle requiring engineering-mediated scholarly review

- **Provenance Documentation**:
  - Maintain source attribution: "Data derived from King Fahd Quranic Printing Complex Uthmanic Hafs v2.0 dataset, © KFGQPC"
  - Document all transformation rules with references to Quranic scholarship sources
  - Track version history: QS-QIRAAT v2.0 update log shows 13 updates with specific fixes - QUD must maintain similar traceability
  - Git commit history will track all schema changes, generation rule modifications, and validation results

### Technology Stack

- **Programming Language**: Python (Tier 1 experimental research code)
- **NLP Libraries**: NLTK and related NLP libraries for text processing, tokenization, and linguistic analysis
- **Interactive Development**: Jupyter notebooks for exploratory analysis, documentation of transformation logic, and iterative experimentation
- **Visualization**: Python visualization libraries (matplotlib, seaborn, plotly) for layer relationship diagrams, conflation matrices, cross-Qiraah difference analysis
- **Schema Definition & Validation**:
  - JSON Schema for formal layer specifications and cross-language interoperability
  - Pydantic for Python-native models with type hints, runtime validation, and IDE support
  - jsonschema library for validating data against JSON Schema definitions
- **Data Storage**: SQLite for sample database creation and query capability demonstrations
- **Version Control**: Git for tracking all code, schema definitions, and research findings

**Rationale**: Python ecosystem provides rich NLP capabilities essential for Quranic text processing (character segmentation, diacritic analysis, word boundary detection). Dual schema approach (JSON Schema + Pydantic) combines formal specification benefits with Python development ergonomics—JSON Schema ensures language-agnostic documentation while Pydantic provides type safety and IDE autocomplete for rapid development. Jupyter notebooks enable rapid experimentation cycles with inline documentation. Visualization tools support research communication and pattern discovery. This stack balances research velocity with sufficient rigor for reproducible findings.

---

## Research Success Criteria *(mandatory)*

### Validation Outcomes

- **VC-001**: RR-001 layer mapping analysis completed with 100% coverage - every QS-QIRAAT field mapped to QUD layer(s), conflation matrix produced showing which layers are mixed, gap analysis identifying missing layers (target: complete by end of RR-001 experiment phase)

- **VC-002**: RR-002 schema design validated by successful transformation of 100% of QS-QIRAAT Hafs data (6,236 verses) into multi-layer format with zero information loss verified by reverse transformation (original QS-QIRAAT can be reconstructed from separated layers)

- **VC-003**: RR-003 simulation performs schema validation for all identified layers (currently 17) across Hafs and Warsh narrations (total 12,450 verse records for Phase 1 per Constitution VI). Target: maximize pass rate; document all validation failures with root cause analysis. Failures do not block research progression but must be analyzed to inform schema refinement and architectural insights. Phase 2-3 extends to remaining narrations (total 43,652 records).

- **VC-004**: Character count validation shows 100% match with authoritative sources for Hafs narration (expected: 323,015 characters or document authoritative count if different), >99% match for Warsh (allowing for minor encoding variations documented in QS-QIRAAT update logs). Phase 2-3 extends validation to remaining narrations.

- **VC-005**: Verse count validation shows 100% match for Hafs (6,236) and Warsh (6,214) in Phase 1, correctly identifying known verse count differences as core requirements rather than errors. Phase 2-3 extends to remaining narrations with their respective verse counts.

- **VC-006**: Redundancy reduction hypothesis validated - layered architecture achieves >40% storage reduction compared to QS-QIRAAT flat format (measured by comparing total JSON size of multi-layer format vs QS-QIRAAT JSON for Hafs and Warsh in Phase 1). Phase 2-3 validates across all narrations.

- **VC-007**: Cross-Qiraah query capability demonstrated with at least 3 example queries that are impossible or impractical in flat QS-QIRAAT but execute successfully on layered architecture (e.g., "find character-level differences between Hafs and Warsh", "extract page layout independent of textual content", "regenerate manuscript with different orthographic system variants")

- **VC-008**: Generative layer production validated for at least one layer pair - demonstrate that Layer 2 (character paired data/diacritics) can be generated from Layer 0 (character composition) + Qiraah-specific tajweed rules with >95% accuracy compared to QS-QIRAAT manually encoded data (measured via automated comparison across all verses). Engineering team presents demo to scholars; scholar feedback confirms theological correctness.

- **VC-009**: UUID-based cross-layer mapping system validated by:
  - All entities in all identified layers (currently 17) assigned unique UUIDs
  - EntityMapping records created for critical cross-layer relationships (minimum: Layer 0↔13 orthographic, Layer 5 Hafs↔Warsh verse)
  - Bidirectional traversal successful (can navigate from any entity to related entities and back)
  - Mapping cardinality correctly represents expansion/contraction (1:2 for Uthmani→Qiasy, variable for Hafs↔Warsh verses)

- **VC-010**: Verse numbering controversy resolution demonstrated by:
  - Canonical verse UUIDs established independent of positional numbering
  - Successfully mapping Hafs Surah Al-Baqarah verses to equivalent Warsh verses despite numbering differences
  - Query "find Warsh equivalent of Hafs 2:20" executes successfully using UUID mappings
  - All 22 verse count differences between Hafs (6,236) and Warsh (6,214) mapped and documented

- **VC-011**: Orthographic transformation handling validated by:
  - Character-level mappings between Uthmani and Qiasy orthographies with positional precision
  - At least 10 documented expansion cases (1 Uthmani char → 2 Qiasy chars) correctly mapped
  - Bidirectional reconstruction: generate Qiasy from Uthmani and vice versa via UUID traversal
  - Semantic hashes generated for all mappings, enabling semantic equivalence queries

### Findings Documentation

- **Research Log Entry**: Chronological documentation in `docs/research-log.md` of:
  - RR-001 findings: Complete mapping table, conflation matrix, gap analysis, cross-Qiraah variance report
  - RR-002 findings: Schema design rationale, transformation algorithm decisions, redundancy analysis
  - RR-003 findings: Simulation results, validation metrics, query capability examples, generation success rates

- **Architecture Decision Records**: In `docs/decisions/` for key architectural choices:
  - ADR-001: Dual schema approach (JSON Schema + Pydantic models) - rationale: formal specification + Python development ergonomics
  - ADR-002: Granularity of Layer 0 character composition (codepoint vs grapheme cluster vs phoneme)
  - ADR-003: Strategy for handling Qiraah/narration variants that differ in verse count (Layer 5 schema design)
  - ADR-004: Approach to missing data (Layers 4, 14) - document as missing vs attempt to generate vs encode from external sources

- **Data Model Specification**: Complete specification of 15-layer architecture in `schemas/` directory:
  - JSON Schema files (layer-00-character-composition through layer-14-readers-narrators) for formal specification
  - Pydantic model files (models.py per layer) for Python type-safe implementation
  - README per layer explaining domain semantics, generation rules, dependencies
  - Cross-layer relationship diagram showing dependencies between layers

- **Negative Results**: Document what approaches DIDN'T work (failures are valuable research findings):
  - If character-level separation from aya_text proves impossible due to Unicode normalization issues - document why
  - If certain layers cannot be generated and require manual encoding - document evidence for this conclusion
  - If redundancy reduction falls short of >40% hypothesis - analyze why and what percentage was achieved
  - All validation failures (character count mismatches, schema validation errors, generation inaccuracies) - document root cause analysis, frequency, and impact on research conclusions. Validation failures are learning opportunities that inform architectural refinement.

- **QS-QIRAAT Problem Analysis Report**: Formal documentation of the conflation problem that motivated this research, serving as the "before" snapshot for future "after" comparisons:
  - Specific examples of queries difficult/impossible in flat format
  - Quantification of redundancy (e.g., "page number 1 repeated 25 times in Hafs dataset, once per verse on that page")
  - Analysis of what domain knowledge is implicit vs explicit (e.g., "tajweed rules for generating symbols are implicit - only the symbols themselves are stored")
  - Recommendations for QS-QIRAAT maintainers if this research proves value of layered approach
