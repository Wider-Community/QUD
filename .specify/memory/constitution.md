<!--
SYNC IMPACT REPORT - Constitution Amendment
============================================
Version Change: 1.4.1 → 1.4.2

Modified Sections:
  - PATCH UPDATE: IV. Quranic Domain Integrity - Usage Examples
    - Added ✅ CORRECT: "Hafs and Warsh are from different Qiraat" (clarifies they come from 2 different Qiraat)
    - Changed ❌ INCORRECT to specifically target "Hafs and Warsh ARE Qiraat" (the narrations are not Qiraat themselves)
    - Emphasized that Hafs and Warsh DO represent different Qiraat (Asim vs. Nafi')
  - PATCH UPDATE: IV. Quranic Domain Integrity - Common Shorthand Clarification
    - Strengthened: "2 narrations from **2 DIFFERENT Qiraat**" (emphasis added)
    - Added "Key distinction" bullet clarifying they are narrations BUT represent 2 different Qiraat
    - Added "Strategic importance" explaining why choosing from different Qiraat matters
  - PATCH UPDATE: VI. Project Scope and Phasing - Why Hafs and Warsh Specifically
    - Made "Different Qiraat" the CRITICAL first reason with expanded explanation
    - Added counter-example: Hafs + Shu'bah would be same Qiraah (Asim), not cross-Qiraah validation
    - Emphasized strategic benefit of cross-Qiraah boundary testing

Added Sections: None (clarifications only)

Removed Sections: None

Templates Requiring Updates:
  ⚠️ Same as v1.4.1 follow-ups

Follow-up TODOs:
  - Same as v1.4.1 follow-ups

Rationale for PATCH version bump (1.4.1 → 1.4.2):
  - Clarification only - emphasizes existing truth that Hafs and Warsh are from different Qiraat
  - Removes potential confusion from ambiguous phrasing in v1.4.1
  - Strengthens strategic rationale for Phase 1 narration selection
  - Backward compatible - does not change any requirements or principles
  - Critical for ensuring readers understand Hafs/Warsh = 2 DIFFERENT Qiraat (not same Qiraah)

Last Updated: 2025-11-04
-->

# QUD: Layered Universal Big Data for Quranic Technologies Constitution

## Core Principles

### I. Research-First Methodology

This is a research and experimentation project where:
- The primary deliverable is KNOWLEDGE and VALIDATED DESIGN, not production software
- Code exists solely to TEST IDEAS and VALIDATE HYPOTHESES
- Research Requirements (RR) replace Feature Requirements (FR)
- Each RR MUST articulate: (1) the research question, (2) the hypothesis, (3) the validation criteria
- Experiments may fail - failure that produces learning is success
- Documentation of findings is as important as code artifacts

**Rationale**: Traditional software development optimizes for production readiness. Research projects optimize for learning velocity and hypothesis validation. This principle ensures we don't prematurely optimize experimental code or treat exploratory implementations as production artifacts.

### II. Data Layer Architecture

**CENTRAL PRINCIPLE**: The layered data model IS the architectural foundation of this research. All work MUST respect the Quranic data layer hierarchy as foundational truth.

The model consists of **15 essential layers** (Layers 0-14), which when accounting for variants and sub-types, **may unfold to 16+ concrete layer specifications**:

- **Layer 0**: Character Composition (التركيب الحرفي) - base letter sequences, phonetic metadata, atomic units of Quranic text
- **Layer 1**: Character Symbols and Rendering Data (الرموز والرسم) - diacritical marks, tajweed symbols, visual rendering rules
- **Layer 2**: Character Paired Data (البيانات المزدوجة للأحرف) - character pair relationships, tajweed rules requiring context (idgham, ikhfa, etc.)
- **Layer 3**: Word Structure (الكلمة) - word boundaries, morphological composition, word-level semantics
- **Layer 4**: Sentence Structure (الجملة) - sentence boundaries, grammatical composition, syntactic relationships, waqf/ibtida rules
- **Layer 5**: Verse Structure (الآية) - verse enumeration, verse boundaries, canonical verse identity (solves verse numbering controversy)
- **Layer 6**: Surah Structure (السورة) - chapter metadata, Makki/Madani classification, chapter themes
- **Layer 7**: Qiraat Structure (القراءات) - Qiraah system metadata (which of the 10 canonical Qiraat, which narration, Qiraah-specific pronunciation/application rules), references Layer 14 for reader/narrator person entities but does NOT duplicate biographical data
- **Layer 8**: Mushaf Structure (المصحف) - complete manuscript for each Qiraah/narration combination
- **Layer 9**: Division Structure (التحزيب) - organizational segments (Hizb/Juz/Rub), recitation scheduling units
- **Layer 10**: Page Layout (الصفحة) - page-level composition, pagination rules per edition
- **Layer 11**: Line Layout (السطر) - line-level composition, line breaks, line-specific formatting
- **Layer 12**: Orthographic Systems (الرسم) - writing system rules
  - **Variant 12a**: Uthmani Script (الرسم العثماني) - classical Uthmanic orthography
  - **Variant 12b**: Qiasy/Imla'i Script (الرسم القياسي/الإملائي) - modern standard orthography
- **Layer 13**: Edition Variants (طبعة المصحف) - edition-specific formatting, publisher variations
- **Layer 14**: Readers and Narrators (القراء والرواة) - biographical data about the Imams who established each Qiraah and the students who narrated each transmission, transmission chains (isnad), scholarly credentials

**Layer 7 vs. Layer 14 Distinction**:
- **Layer 7**: WHAT Qiraah is being used, WHICH narration, and the RULES/CHARACTERISTICS of that Qiraah-narration combination
- **Layer 14**: WHO the reader/narrator was as a person (biography, birth/death dates, teachers, students, scholarly works)
- **Relationship**: Layer 7 contains reference UUIDs pointing to Layer 14 person entities, but stores only the identity reference, not the biographical data itself

**Unfolding Logic**: The 15 essential layers may expand to 16+ concrete specifications when accounting for orthographic system variants (12a, 12b) and other domain-specific subdivisions discovered through research.

**UUID-Based Identity**: CRITICAL REQUIREMENT - Every entity in all 15 layers MUST have a unique UUID identifier, with bidirectional cross-layer mappings using EntityMapping structures to handle expansion/contraction cases (e.g., 1 Uthmani char → 2 Qiasy chars, 1 Hafs verse → 2 Warsh verses).

#### Schema Design vs. Data Fulfillment

**CRITICAL DISTINCTION**: There is a fundamental difference between:

1. **Schema Design Thoroughness**: Defining complete, rigorous schemas for ALL 15 layers that can accommodate ALL potential Qiraat and narrations
   - Schemas SHOULD be designed comprehensively to support the full domain model (10 Qiraat × 20 narrations)
   - Schema definitions are research artifacts that document the STRUCTURE needed for complete coverage
   - A thorough schema is forward-looking and prepares for eventual data expansion

2. **Data Fulfillment**: Actually populating those schemas with validated data for specific Qiraat/narrations
   - Data fulfillment follows the phased approach (Hafs & Warsh in Phase 1, expansion in later phases)
   - Schemas may be designed to support 10 Qiraat, but data is only filled for 2 narrations (from 2 Qiraat) initially
   - Research validates schemas with available data while documenting how schemas generalize

**Concrete Layer-by-Layer Examples**:

| Layer | Schema Design Scope | Phase 1 Data Fulfillment | Phase 2-3 Data Fulfillment |
|-------|---------------------|-------------------------|---------------------------|
| **L0** (Character) | Support character sets for all 10 Qiraat | Fulfill character data for Hafs + Warsh only (~323,015 + ~323,000 chars) | Add character data for 3-5 more narrations |
| **L5** (Verse) | Support verse numbering variations across all 10 Qiraat | Fulfill verse data for Hafs (6,236) + Warsh (6,214) | Add verse data for Qalun, Shu'bah, etc. |
| **L7** (Qiraat) | Define metadata structure for all 10 Qiraat | Populate metadata for Asim Qiraah (Hafs narration) + Nafi' Qiraah (Warsh narration) | Add metadata for 3-4 more Qiraat |
| **L14** (Readers) | Define biographical schema for all canonical readers/narrators | Populate biographies for Asim, Hafs, Nafi', Warsh | Add biographies for 6-8 more readers/narrators |

**Example**:
- ✅ CORRECT: "Design Layer 7 (Qiraat Structure) schema to accommodate all 10 canonical Qiraat, but fulfill data only for Asim Qiraah (Hafs narration) and Nafi' Qiraah (Warsh narration) in Phase 1"
- ❌ INCORRECT: "Design Layer 7 schema only for Hafs and Warsh, ignoring other Qiraat"
- ❌ INCORRECT: "Populate Layer 7 with data for all 10 Qiraat in Phase 1"

**Rationale**: Thorough schema design prevents future rework and ensures architectural consistency. However, data fulfillment is resource-intensive and must respect phased delivery. This distinction allows research to be architecturally complete while pragmatically scoped for delivery.

#### Generative Data Architecture

**CRITICAL REQUIREMENT**: Layers are GENERATIVE - they are computed/derived through rules and algorithms, NOT manually curated exhaustively.

However, all generated layer data MUST:
- **Conform to predefined schemas**: Each layer has a formal schema specifying structure, constraints, and validation rules
- **Be reproducible**: Generation process must be deterministic and documentable
- **Be validatable**: Generated data must be verifiable against authoritative sources
- **Preserve provenance**: Track which rules/algorithms generated which data elements

The research explores the DUAL nature of layers:
1. **Generative Process**: How layers are computed (rules, algorithms, transformations)
2. **Schema Conformance**: What structure generated data must satisfy (types, constraints, relationships)

Both aspects are research subjects. Experiments may test:
- Can Layer X be fully generated from Layer Y using rules R?
- Does generated Layer Z data conform to schema S within tolerance T?
- What is the computational cost of generating Layer A for all Qiraat?

**Rationale**: The 15-layer architecture represents decades of Islamic scholarly work codified into a computational model. This is the CORE of the QUD research - exploring how generative processes can produce schema-conformant data for each layer while maintaining theological accuracy and cross-Qiraah interoperability. Any technical solution MUST preserve these semantic boundaries to maintain scholarly validity.

### III. Experimental Validation

Every Research Requirement (RR) MUST include:
- **Hypothesis**: What we believe to be true
- **Validation Method**: How we will test the hypothesis (code, data analysis, simulation)
- **Success Criteria**: Measurable outcomes that confirm/refute the hypothesis
- **Findings Documentation**: What we learned, whether hypothesis confirmed or refuted

Code quality standards are RELAXED for experimental code:
- Experimental code MAY lack production error handling
- Experimental code MAY use hardcoded test data
- Experimental code MUST be clearly marked with `# EXPERIMENTAL:` comments
- Production-grade code (for data pipelines, tooling) MUST meet higher standards

**Rationale**: Research code serves a different purpose than production code. Requiring production-grade quality slows experimentation. Clear labeling allows us to distinguish experimental proofs-of-concept from reusable infrastructure.

### IV. Quranic Domain Integrity

All implementations MUST:
- Preserve the sanctity and accuracy of Quranic text
- Validate data against authoritative sources (مجمع الملك فهد editions, authenticated Qiraat databases)
- Handle character counts, verse counts, and Qiraah variants with ZERO tolerance for error
- Document source provenance for all Quranic data
- Never generate or infer Quranic text content - only process authenticated sources
- Generation applies to layer STRUCTURES and METADATA, not sacred text content itself

**Edge cases in Qiraat (القراءات العشر) are NOT edge cases - they are CORE requirements.**

#### Qiraat and Narrations Terminology

**CRITICAL TERMINOLOGY REQUIREMENT**: The term "Qiraat" (القراءات) MUST be used correctly throughout all documentation, specifications, and code.

**Correct Terminology**:
- **Qiraat** (القراءات) - plural form referring to the authenticated reading traditions of the Quran
  - This is NOT equivalent to "recitations" or "readings" in English
  - Qiraat is a theologically validated term with specific scholarly meaning
  - Use "Qiraat" untranslated in technical documentation
- **Qiraah** (قراءة) - singular form, one reading tradition established by a specific Imam (e.g., "the Qiraah of Nafi'", "the Qiraah of Asim")
- **10 Canonical Qiraat** (القراءات العشر) - the ten authenticated Quraat traditions accepted by Islamic scholarship
- **Narration** (رواية / Riwayah) - transmission variant within a Qiraah, transmitted by a specific student of the Imam
  - Each Qiraah has 2 primary narrations (some have additional sub-narrations)
  - Total: 10 Qiraat × 2 primary narrations = 20 canonical narrations
  - Example: Hafs and Shu'bah are the two narrations of the Qiraah of Asim
  - Narration represents how a student learned and transmitted the Imam's Qiraah method

**Qiraah-Narration Hierarchy** (CRITICAL FOR UNDERSTANDING):
```
Imam (Reader) → Establishes Qiraah (reading method with pronunciation/application rules)
    ↓
Student (Narrator) → Transmits Qiraah with minor variations → Creates Narration (Riwayah)
    ↓
Result: Narrations within same Qiraah share >95% commonality, differ in specific pronunciation/stopping points
```

**Example**:
- **Asim** (Imam, d. 127 AH) → Established the **Qiraah of Asim**
  - **Hafs** (student, d. 180 AH) → Narrated as **Hafs 'an Asim** (Hafs from Asim)
  - **Shu'bah** (student, d. 193 AH) → Narrated as **Shu'bah 'an Asim** (Shu'bah from Asim)
- **Nafi'** (Imam, d. 169 AH) → Established the **Qiraah of Nafi'**
  - **Warsh** (student, d. 197 AH) → Narrated as **Warsh 'an Nafi'** (Warsh from Nafi')
  - **Qalun** (student, d. 220 AH) → Narrated as **Qalun 'an Nafi'** (Qalun from Nafi')

**Canonical Qiraat and Their Narrations**:
1. **Nafi'** (d. 169 AH, Medina) - Narrations: Warsh, Qalun
2. **Ibn Kathir** (d. 120 AH, Mecca) - Narrations: Al-Bazzi, Qunbul
3. **Abu Amr** (d. 154 AH, Basra) - Narrations: Al-Duri, Al-Susi
4. **Ibn Amir** (d. 118 AH, Damascus) - Narrations: Hisham, Ibn Dhakwan
5. **Asim** (d. 127 AH, Kufa) - Narrations: Hafs, Shu'bah
6. **Hamzah** (d. 156 AH, Kufa) - Narrations: Khalaf, Khallad
7. **Al-Kisa'i** (d. 189 AH, Kufa) - Narrations: Al-Duri, Abul-Harith
8. **Abu Ja'far** (d. 130 AH, Medina) - Narrations: Ibn Wardan, Ibn Jammaz
9. **Ya'qub** (d. 205 AH, Basra) - Narrations: Ruways, Rawh
10. **Khalaf** (d. 229 AH, Baghdad) - Narrations: Ishaq, Idris

**Prohibited Terminology** (DO NOT USE):
- ❌ "Recitations" - imprecise English term, lacks theological grounding
- ❌ "Readings" - generic term that doesn't capture the authenticated nature of Qiraat
- ❌ "Variants" - implies error or deviation; Qiraat are equally valid authenticated traditions
- ❌ Conflating "narration" with "Qiraah" - they are different levels of the tradition hierarchy (Qiraah = Imam's method, Narration = student's transmission)

**Usage Examples**:
- ✅ CORRECT: "QUD v0.1 will ship with Hafs and Warsh narrations in MUDMAJ"
- ✅ CORRECT: "Hafs and Warsh represent 2 narrations from 2 different Qiraat: Hafs from Asim's Qiraah, Warsh from Nafi's Qiraah"
- ✅ CORRECT: "Hafs and Warsh are from different Qiraat" (meaning: they come from 2 different Qiraat - Asim and Nafi')
- ✅ CORRECT: "Research will analyze multiple Qiraat to validate schema design"
- ✅ CORRECT: "The Qiraah of Asim has two primary narrations: Hafs (most widely used globally) and Shu'bah (widely used in parts of Africa)"
- ❌ INCORRECT: "Research will cover all 7 recitations" (use "narrations" or "Qiraat", not "recitations")
- ❌ INCORRECT: "Hafs and Warsh ARE Qiraat" (they are narrations, not Qiraat - but they DO come from different Qiraat)

**Common Shorthand Clarification**:
When we say "Hafs and Warsh" in project documentation:
- **Full form**: "Hafs narration (from Asim's Qiraah) and Warsh narration (from Nafi's Qiraah)"
- **Represents**: 2 narrations from **2 DIFFERENT Qiraat** (Asim + Nafi')
- **Key distinction**: Hafs and Warsh are NOT Qiraat themselves, they are narrations, BUT they represent 2 different Qiraat
- **Strategic importance**: Choosing narrations from 2 different Qiraat (not 2 narrations from the same Qiraah) ensures cross-Qiraah schema validation

**QS-QIRAAT Dataset Contents** (IMPORTANT CORRECTION):
The QS-QIRAAT dataset contains **6 narrations from 3-4 Qiraat** (not "7 complete Qiraat"):
1. **Hafs** (narration of Asim's Qiraah)
2. **Warsh** (narration of Nafi's Qiraah)
3. **Qalun** (narration of Nafi's Qiraah)
4. **Shu'bah** (narration of Asim's Qiraah)
5. **Al-Duri** (narration of Abu Amr's Qiraah OR Al-Kisa'i's Qiraah - needs verification)
6. **Al-Susi** (narration of Abu Amr's Qiraah)

This represents partial coverage: 2 complete Qiraat (Asim with both narrations, Nafi' with both narrations) plus 1-2 additional Qiraat with 1-2 narrations each.

**Rationale**: This is sacred text used by billions. Precise theological terminology is not pedantic - it's essential for scholarly credibility and prevents conceptual errors. Using "Qiraat" correctly:
1. Respects Islamic scholarship terminology
2. Prevents confusion between Qiraah-level (Imam's method) vs. narration-level (student's transmission) differences
3. Ensures the 10 Qiraat × 2 narrations = 20 total authenticated traditions are properly understood
4. Demonstrates domain expertise to scholarly reviewers and community partners
5. Clarifies that narrations within same Qiraah share >95% commonality (same pronunciation rules, differ in specific applications)

### V. Incremental Discovery

Research proceeds in small, validated steps:
- Break complex research questions into smaller hypotheses
- Validate each hypothesis before building on it
- Document decision points and rationale
- Preserve failed approaches in documentation (negative results have value)
- Build "throw-away" prototypes frequently

Avoid:
- Large, monolithic research efforts without intermediate validation
- Premature abstraction before patterns are clear
- Rewriting working experimental code without research justification

**Rationale**: Big data Quranic research is a novel domain. We don't yet know what architectural patterns will emerge. Incremental discovery prevents us from building elaborate frameworks before we understand the problem space.

### VI. Project Scope and Phasing

**CENTRAL PRINCIPLE**: QUD follows a phased delivery approach aligned with the project charter. Research and development MUST respect scope boundaries to ensure focused progress and prevent scope creep.

#### Research Scope vs. Delivery Scope

**CRITICAL DISTINCTION**: There is a fundamental difference between:

1. **Research Scope**: What Qiraat/narrations we analyze to validate schemas and architecture
   - Research SHOULD analyze multiple Qiraat (minimum 2 Qiraat, ideally 3+ Qiraat) from available source datasets like QS-QIRAAT
   - Research analysis uses multiple narrations from different Qiraat as SAMPLES to ensure schemas generalize
   - Goal: Prove that the 15-layer architecture works for the FULL DOMAIN of Qiraat (all 10 Qiraat, 20 narrations)
   - Schemas MUST be designed to accommodate all 10 Qiraat even if only 2-3 are analyzed in Phase 1
   - Example: "Analyze QS-QIRAAT dataset (which contains 6 narrations from 3-4 Qiraat) to validate Layer 5 verse boundary schema handles verse count variations"

2. **Delivery Scope (MUDMAJ/QUD v0.1)**: What Qiraat/narrations we ship with validated data in the production database
   - **Phase 1 Delivery**: Hafs and Warsh narrations ONLY (representing 2 narrations from 2 Qiraat: Asim + Nafi')
   - These are the two narrations that will be data-fulfilled, validated, and shipped in MUDMAJ release 1
   - Goal: Deliver a production-quality database with 2 narrations first, then expand in later releases
   - Example: "QUD v0.1 ships with MUDMAJ containing Hafs narration (from Asim's Qiraah) and Warsh narration (from Nafi's Qiraah)"

**Research-Delivery Relationship**:
```
Research Phase 1 (Months 1-2):
├─ Research Scope: Analyze 6 narrations from QS-QIRAAT (from 3-4 Qiraat) to validate schemas
├─ Schema Design: Create schemas that accommodate all 10 Qiraat (20 narrations)
└─ Delivery Scope: Fulfill data for Hafs & Warsh only (2 narrations from 2 Qiraat) → ship in MUDMAJ v1.0

Phase 2-3 (Months 2-6):
├─ Research Scope: Continue validating with all available narrations in QS-QIRAAT and other sources
├─ Schema Refinement: Adjust schemas based on new Qiraah-specific edge cases discovered
└─ Delivery Scope: Add 2-3 more narrations (e.g., Qalun, Shu'bah) → ship in MUDMAJ v2.0
```

**Example Scenarios**:
- ✅ CORRECT: "RR-001 will analyze all 6 narrations in QS-QIRAAT (from 3-4 Qiraat) to map fields to QUD layers, but MUDMAJ v1.0 will only ship Hafs & Warsh data (2 narrations from 2 Qiraat)"
- ✅ CORRECT: "Schema for Layer 5 (Verse Structure) is designed to handle verse count differences across all 10 Qiraat, but we validate with Hafs/Warsh first, then test with Qalun/Shu'bah"
- ❌ INCORRECT: "Research is limited to Hafs and Warsh only - we will not analyze other narrations in QS-QIRAAT"
- ❌ INCORRECT: "MUDMAJ v1.0 will ship with all 10 Qiraat (20 narrations) fully fulfilled"

**Rationale**:
1. **Research breadth ensures architectural completeness** - analyzing narrations from multiple Qiraat prevents designing schemas specific to only Asim/Nafi'
2. **Delivery focus ensures quality** - shipping 2 narrations with 100% validation is better than 6 narrations with 60% validation
3. **Phased delivery manages risk** - prove the architecture works with 2 narrations before investing in 18 more
4. **Resource efficiency** - data fulfillment (sourcing, validating, mapping all 15 layers) is labor-intensive; research analysis is faster

#### Initial Qiraat Focus (Phase 1: Foundation Setup)

**CRITICAL CONSTRAINT**: Initial delivery (MUDMAJ/QUD v0.1) is LIMITED to **Hafs and Warsh narrations only** (2 narrations from 2 Qiraat: Asim and Nafi').

All Research Requirements MUST:
- Design schemas to accommodate the full domain (all 10 Qiraat)
- Analyze available narrations from QS-QIRAAT (minimum 2 Qiraat, ideally analyze 3-4 Qiraat represented in dataset) to validate schema generalizability
- Focus data fulfillment on Hafs (حفص عن عاصم) - the most widely used narration globally
- Include Warsh (ورش عن نافع) as the secondary narration for cross-Qiraah validation (different Qiraah from Hafs, demonstrates verse boundary variations)
- Document findings that generalize to other Qiraat, but defer full data fulfillment

**Data Collection Targets (Month 1-2)**:
- **Hafs narration** (from Asim's Qiraah): 6,236 verses, 323,015 characters (from QS-QIRAAT or King Fahd Complex)
- **Warsh narration** (from Nafi's Qiraah): 6,214 verses (demonstrates verse boundary variations between Qiraat)
- Both narrations in Uthmani and Qiasy orthographies (validates Layer 12 transformations)

**Why Hafs and Warsh Specifically**:
1. **CRITICAL: Different Qiraat**: Hafs is from Asim's Qiraah (Kufa tradition), Warsh is from Nafi's Qiraah (Medina tradition)
   - This means we're testing with **2 different Qiraat**, not just 2 narrations from the same Qiraah
   - If we chose Hafs + Shu'bah, that would be 2 narrations from the SAME Qiraah (Asim), which wouldn't validate cross-Qiraah compatibility
   - **Strategic benefit**: Ensures schemas work across Qiraah boundaries, not just within one Qiraah
2. **Geographic diversity**: Represents 2 of the 4 major centers of Quranic learning (Kufa + Medina)
3. **Global usage**: Hafs is most widely used (>90% of Muslims), Warsh is primary in North/West Africa
4. **Verse boundary variation**: 6,236 vs. 6,214 verses tests verse numbering resolution mechanisms across Qiraat
5. **Available in authoritative sources**: Both have King Fahd Complex editions and are in QS-QIRAAT

#### Out of Scope (Phase 1 Delivery)

The following features are **EXPLICITLY OUT OF SCOPE** for Phase 1 DELIVERY (MUDMAJ v1.0) and MUST NOT be included in initial shipment:

- **Multi-language transliteration** for narrations other than Hafs
  - Rationale: Hafs transliteration is widely available; other narrations require separate linguistic research
  - Defer to: Phase 4 (Month 6-12) or later

- **Audio-to-text alignment** for narrations other than Hafs
  - Rationale: Audio synchronization requires separate NLP/ML research track
  - Defer to: Phase 3 (Month 4-6) after core database established

- **Interactive Mushaf visualization** for narrations other than Hafs
  - Rationale: UI/UX development is separate from core data architecture research
  - Defer to: Phase 3-4 (Month 4-12) as community integration feature

- **Additional narrations** beyond Hafs and Warsh (e.g., Qalun, Shu'bah, Al-Duri, Al-Susi)
  - Rationale: Prove architecture works with 2 narrations from 2 Qiraat first, then expand
  - Defer to: Phase 2-3 (Month 2-6) after Hafs/Warsh validation complete
  - Note: Research SHOULD analyze these narrations (available in QS-QIRAAT) to validate schemas, but they won't be fully data-fulfilled for delivery

- **Production-grade NLP engine integration**
  - Rationale: Research phase focuses on data structure validation, not production AI systems
  - Defer to: Phase 2-3 (Month 2-6) with partner support per charter

#### Phased Expansion Strategy

**Phase 1 (Month 1-2): Foundation Setup**
- Research Scope: Analyze 6 narrations in QS-QIRAAT (from 3-4 Qiraat) to validate schemas generalize across Qiraat
- Delivery Scope: Hafs + Warsh data collection (2 narrations from 2 Qiraat), standardization with MARQOUM guidelines
- Research Work: RR-001 through RR-003 (layer separation, schema design, simulation)
- Deliverable: MUDMAJ v1.0 with validated 15-layer architecture containing Hafs & Warsh (2 narrations from Asim + Nafi' Qiraat)

**Phase 2 (Month 2-4): Core Development**
- Research Scope: Continue validating schemas with all narrations in QS-QIRAAT + potentially new sources
- Delivery Scope: Add 2-3 more narrations to MUDMAJ (e.g., Qalun and Shu'bah - completing Nafi' + Asim Qiraat)
- Research Work: RR-011 through RR-013 (UUID system, contextual versioning, orthographic mapping)
- Deliverable: MUDMAJ v2.0 with 4-5 narrations (2 complete Qiraat), working cross-Qiraah queries

**Phase 3 (Month 4-6): Community Integration**
- Research Scope: Validate edge cases across all 10 Qiraat (seek additional sources beyond QS-QIRAAT if needed)
- Delivery Scope: Expand to 6-8 narrations (adding 2-3 more Qiraat), QUD Orchestrator + MUDMAJ optimization
- Research Work: RR-014 through RR-016 (orchestrator, storage schema, query validation)
- Deliverable: MUDMAJ v3.0 with 6-8 narrations (3-4 Qiraat coverage), context-aware query system

**Phase 4 (Month 6-12): Expansion & Ecosystem Growth**
- Research Scope: Complete domain coverage research (all 20 canonical narrations from all 10 Qiraat)
- Delivery Scope: Complete 10 Qiraat (20 narrations), NLP integration, external project integrations
- Research Work: Production-grade pipeline development (if validated), community adoption
- Deliverable: MUDMAJ v4.0 with complete Qiraat coverage (20 narrations), ecosystem-ready QUD

#### Community Integration Requirements

QUD research MUST engage with ITQAN community and external stakeholders per charter Objective 2-3:

**MUST DO**:
- Document integration points with ITQAN community projects (Open Mushaf, etc.)
- Design adapter/wrapper layers for external project consumption (Phase 2)
- Create contribution channels (GitHub, documentation) by Month 2
- Host scholarly review sessions at end of each research cycle
- Produce visual/educational content about findings (YouTube, LinkedIn)

**SHOULD DO**:
- Collaborate with partners (Quran.com, Tarteel, ZAD) for data validation
- Run webinars/workshops to share research progress (Month 3-4)
- Establish quality assurance processes for community contributions (Phase 3)

**Scope Violation Examples** (to be rejected in specifications):
- ❌ "MUDMAJ v1.0 MUST ship with all 10 Qiraat (20 narrations) fully data-fulfilled" → Violates Phase 1 delivery scope
- ❌ "Research is limited to Hafs and Warsh only - no analysis of other narrations in QS-QIRAAT" → Violates research scope (schemas must be validated across multiple Qiraat)
- ❌ "Implement production NLP engine in Phase 1" → Out of scope, deferred to Phase 2-3
- ❌ "Build interactive Mushaf UI for Warsh" → Out of scope Phase 1, deferred to Phase 3-4
- ❌ "Add Qalun narration to MUDMAJ v1.0" → Violates phased delivery (defer to Phase 2)

**Rationale**: The distinction between research scope (analyze narrations from multiple Qiraat to validate schemas) and delivery scope (ship 2 narrations from 2 Qiraat first) ensures:
1. Schemas are architecturally complete and won't require rework when adding narrations from new Qiraat
2. Data fulfillment is manageable - 2 narrations × 15 layers × full validation is achievable in 2 months
3. Quality over quantity - better to ship 2 narrations with 100% accuracy than 6 narrations with 70% accuracy
4. Incremental value delivery - community gets usable MUDMAJ v1.0 quickly, then v2.0, v3.0, etc.
5. Risk mitigation - prove the architecture works before investing heavily in data fulfillment for all 20 narrations

## Research Requirements Framework

### Research Requirement (RR) Structure

Each RR MUST contain:

```markdown
## RR-XXX: [Research Question Title]

**Research Question**: [Clear articulation of what we're investigating]

**Hypothesis**: [What we believe to be true and will test]

**Context**: [Why this question matters, what prior work exists]

**Validation Method**:
- [How we will test this - e.g., "Analyze QS-QIRAAT dataset (6 narrations from 3-4 Qiraat) to validate schema"]
- [What data we will use]
- [What metrics we will measure]

**Success Criteria**:
- [Measurable outcome 1]
- [Measurable outcome 2]

**Data Layer Dependencies**: [Which layers (0-14) this research depends on]

**Qiraat Research Scope**: [Which Qiraat/narrations will be analyzed to validate schemas - minimum 2 Qiraat, ideally 3-4 from QS-QIRAAT]

**Qiraat Delivery Scope**: [Which Qiraat/narrations will be data-fulfilled for MUDMAJ shipment - MUST be Hafs/Warsh only (2 narrations from 2 Qiraat) for Phase 1]

**Schema Requirements**: [Which layer schemas must be defined for this RR - should accommodate full domain (all 10 Qiraat) even if data fulfillment is limited to 2 narrations]

**Dependencies**: [Other RRs that must be complete first]

**Findings**: [To be filled after experimentation - what we learned]
```

### Types of Research Requirements

- **RR-Architectural**: Investigating system design patterns (e.g., "Can layer-based storage reduce redundancy?")
- **RR-Algorithmic**: Testing computational approaches (e.g., "Can rule-based generation match manual tajweed annotation accuracy?")
- **RR-Data**: Exploring data structures (e.g., "What graph model best represents cross-Qiraah relationships?")
- **RR-Schema**: Defining and validating layer schemas (e.g., "What schema constraints ensure Layer 4 word boundary integrity across all Qiraat?")
- **RR-Generative**: Testing layer generation approaches (e.g., "Can Layer 2 paired data be fully generated from Layer 0 character composition for multiple Qiraat?")
- **RR-Performance**: Validating scalability (e.g., "Can character-level indexing support <100ms verse lookup across all narrations?")
- **RR-Domain**: Understanding Quranic scholarship requirements (e.g., "What are variant verse numbering schemes across the 10 Qiraat?")
- **RR-Integration**: Testing community/partner integration approaches (e.g., "Can adapter layer connect QUD to Open Mushaf with <10 LOC?")

## Data Quality Standards

### Quranic Data Sources

All Quranic data MUST be sourced from authenticated references:
- King Fahd Complex editions (Hafs & Warsh manuscripts initially, eventually all 20 canonical narrations)
- Authenticated audio from recognized scholars
- Peer-reviewed Quranic databases (with source attribution) - e.g., QS-QIRAAT v2.0, Tanzil.net

**Phase 1 Source Priorities**:
1. QS-QIRAAT v2.0 (primary source - contains 6 narrations from 3-4 Qiraat for research analysis: Hafs, Warsh, Qalun, Shu'bah, Al-Duri, Al-Susi)
2. King Fahd Complex Hafs edition (validation source for delivery)
3. King Fahd Complex Warsh edition (validation source for delivery)
4. Tanzil.net (cross-validation for character/verse counts)

### Data Validation

Before any data is used in experiments:
- Verify character counts match authoritative sources (Hafs: 323,015 characters)
- Validate verse boundaries across Qiraat (Hafs: 6,236 verses, Warsh: 6,214 verses)
- Cross-check Qiraah variants against scholarly references
- Document any discrepancies found in source data

### Data Processing

- Original source data MUST be preserved immutably
- All transformations MUST be reversible or documented
- Generated data MUST be clearly labeled as derived
- Provide chain of provenance for all processed datasets
- Generated layer data MUST conform to defined schemas
- Schema violations MUST be reported and analyzed (they indicate generation rule errors or schema definition gaps)

## Schema-First Development

### Schema Definition Requirements

For each layer being researched:
1. **Define Schema First**: Before generating layer data, define the schema (structure, types, constraints)
2. **Design for Full Domain**: Schema SHOULD accommodate all 10 Qiraat (20 narrations) even if Phase 1 only fulfills 2 narrations from 2 Qiraat
3. **Document Schema Rationale**: Explain why the schema captures the layer's semantic requirements across all Qiraat
4. **Implement Schema Validation**: Create validators that verify generated data against schema
5. **Test with Authentic Data**: Validate schema against samples from multiple Qiraat (analyze 3-4 Qiraat from QS-QIRAAT for research), fulfill with Hafs/Warsh for delivery
6. **Iterate**: Refine schema based on validation failures and domain expert feedback

### Schema Documentation

Each layer schema MUST document:
- **Structure**: Fields, types, nesting, relationships
- **Constraints**: Required fields, validation rules, cross-field dependencies
- **Invariants**: Properties that MUST hold for all instances (e.g., "sum of verse counts equals 6,236 for Hafs narration")
- **Provenance**: How data in this layer is sourced or generated
- **Dependencies**: Which other layers this schema references (e.g., Layer 7 references Layer 14 for reader/narrator person entities)
- **Qiraah Variants**: How schema handles differences across the 10 Qiraat (e.g., verse count variations, character composition differences, pronunciation rule differences)
- **Narration Variants**: How schema distinguishes between narrations within the same Qiraah (typically >95% shared, differ in specific pronunciation/application details)

Store schemas in: `schemas/layer-XX-name/schema.json` (or appropriate format) with accompanying `README.md` explaining rationale and domain semantics.

## Experimental Code Guidelines

### Code Organization

```
experiments/
├── rr-001-layer-storage/      # One directory per Research Requirement
│   ├── README.md              # Hypothesis, method, findings
│   ├── prototype.py           # Experimental code
│   ├── data/                  # Test data (if small) or data links
│   └── results/               # Output, logs, analysis
│
research-tools/                 # Reusable utilities (higher quality bar)
├── data-loaders/
├── validators/
├── generators/                 # Layer generation utilities
└── analyzers/

schemas/                        # Layer schema definitions
├── layer-00-character-composition/
│   ├── schema.json
│   └── README.md
├── layer-01-symbols-rendering/
│   ├── schema.json
│   └── README.md
└── [...]                       # Schemas for layers 0-14

docs/
├── research-log.md            # Chronological findings log
├── data-layers/               # Documentation per data layer (0-14)
│   ├── layer-00-character-composition.md
│   ├── layer-01-symbols-rendering.md
│   └── [...]
├── qiraat/                    # Qiraat and narrations documentation
│   ├── canonical-qiraat.md    # 10 Qiraat × 2 narrations documentation with Imam/narrator details
│   ├── terminology.md         # Qiraat vs. narration definitions, Imam→student transmission model
│   ├── hierarchy-diagram.md   # Visual showing Qiraah → Narrations hierarchy
│   └── sources.md             # Authenticated sources per Qiraah
├── decisions/                 # Architecture decision records
└── integration/               # Community integration documentation
    ├── itqan-partners.md      # Integration points with ITQAN projects
    ├── adapters/              # Adapter layer designs
    └── contribution-guide.md  # Community contribution guidelines
```

### Code Quality Tiers

**Tier 1 - Experimental Prototypes** (`experiments/` directory):
- Purpose: Test hypotheses quickly
- Standards: Working code, basic comments, document findings
- Acceptable: Hardcoded paths, test data, simple scripts
- Not required: Error handling, edge cases, tests, optimization
- Research Scope: May analyze all available narrations in source datasets (6 narrations from QS-QIRAAT)
- Delivery Scope: Data fulfillment for Hafs/Warsh only (2 narrations from 2 Qiraat) for Phase 1

**Tier 2 - Research Tools** (`research-tools/` directory):
- Purpose: Reusable utilities across experiments
- Standards: Documented functions, input validation, error handling
- Required: Clear interfaces, example usage, basic tests
- Not required: Production performance, comprehensive edge cases
- Scope: Should support Hafs/Warsh minimally, designed for future Qiraat expansion

**Tier 3 - Data Infrastructure** (if building production pipelines - Phase 2-3):
- Purpose: Operational data processing for MUDMAJ releases
- Standards: Production quality - tests, logging, monitoring, error recovery
- Required: Full validation, documentation, performance benchmarks
- This tier may not be needed if project remains research-only through Phase 1

## Governance

### Constitution Authority

This constitution defines the rules of engagement for the QUD research project. All research plans, specifications, and implementations must align with these principles.

### Amendment Process

Constitution amendments require:
1. Documentation of why current principles are insufficient
2. Proposal of specific principle additions/modifications
3. Review of impact on existing research work
4. Version increment following semantic versioning:
   - **MAJOR**: Principle removal or incompatible redefinition
   - **MINOR**: New principle added or materially expanded guidance
   - **PATCH**: Clarifications, wording refinements

### Compliance Verification

All research artifacts (specs, plans, tasks) must include:
- **Constitution Check**: Verification that work aligns with principles
- **Layer Alignment**: Confirm which of the 15 essential layers the work addresses
- **Qiraat Terminology Validation**: Confirm correct use of "Qiraat" (not "recitations/readings") and proper Qiraah/narration distinction
- **Qiraah-Narration Hierarchy Validation**: Confirm understanding that Qiraah = reading method established by Imam, Narration = transmission by student, and that narrations within same Qiraah share >95% commonality
- **Research vs. Delivery Scope Validation**: Distinguish what Qiraat are analyzed (research scope: minimum 2 Qiraat, ideally 3-4) vs. data-fulfilled (delivery scope: 2 narrations from 2 Qiraat for Phase 1)
- **Schema Design vs. Data Fulfillment Validation**: Confirm schemas are designed for full domain (all 10 Qiraat) but data is fulfilled phasedly (Hafs/Warsh first)
- **Schema Validation**: For generative work, confirm schema conformance is tested
- **Complexity Justification**: If violating simplicity principles, document why simpler alternatives are insufficient
- **Domain Integrity Verification**: For Quranic data work, confirm source authentication and accuracy validation
- **Phase Alignment**: Confirm work is appropriate for current project phase per charter

### Research Workflow

1. **Specify**: Articulate research question as RR in spec.md, identify layer dependencies, distinguish research vs. delivery Qiraat scope (analyze 2-4 Qiraat, deliver 2 narrations)
2. **Plan**: Design experiment methodology in plan.md, define/reference layer schemas (designed for all 10 Qiraat), confirm phase alignment
3. **Clarify**: Resolve ambiguities before experimentation, especially around Qiraat terminology, Qiraah-narration hierarchy, and scope distinctions
4. **Experiment**: Build prototype, generate/test layer data, validate against schema using available narrations from multiple Qiraat
5. **Document**: Record findings (positive or negative) in research log, note schema generalizability across Qiraat
6. **Decide**: Determine next research question based on findings and phase roadmap
7. **Deliver**: At phase boundaries, produce MUDMAJ releases with data-fulfilled narrations (Hafs/Warsh for v1.0, add 2-3 more for v2.0, etc.)
8. **Integrate**: Engage community, consolidate findings, prepare for next phase expansion

### Community Engagement Gates

**Phase 1 → Phase 2 Transition (Month 2)**:
- RR-001 through RR-003 validated (layer architecture proven with Hafs/Warsh data, schemas tested with 3-4 Qiraat from QS-QIRAAT)
- MUDMAJ v1.0 released with Hafs & Warsh narrations (2 narrations from 2 Qiraat: Asim + Nafi') fully validated
- Contribution channels established (GitHub, documentation, Slack/Discord)
- Initial partner connections made (ITQAN community, advisory board)

**Phase 2 → Phase 3 Transition (Month 4)**:
- MUDMAJ v2.0 operational with 4-5 narrations (completing Asim + Nafi' Qiraat with both narrations each)
- First adapter/wrapper integrated with at least 1 ITQAN project
- Community contribution processes documented
- Schemas refined based on analysis of additional Qiraat

**Phase 3 → Phase 4 Transition (Month 6)**:
- MUDMAJ v3.0 with 6-8 narrations (3-4 Qiraat coverage)
- Active contributor base (developers, scholars) engaged
- Webinars/workshops conducted, visual content published
- Path to complete 20 narrations (all 10 Qiraat) documented

**Version**: 1.4.2 | **Ratified**: 2025-11-03 | **Last Amended**: 2025-11-04
