# QUD GitHub Project Issues

**Created**: 2025-01-11
**Purpose**: Initial issue set for GitHub Project setup
**Total Issues**: 32 issues

> **Note**: For project setup, field IDs, and CLI commands, see [github-projects-guide.md](github-projects-guide.md)

---

## A. Layer Foundation (المحاذاة والتسمية)

**Epic Summary**: Theoretical alignment and standardization of 50+ data layers

---

### [LF-001] Layer Naming Standards

**System**: QUD-General
**Category**: Layer-Foundation
**Priority**: P1-Critical
**Issue Type**: Research + Design
**Related RRs**: RR-001 (Layer Separation Analysis), RR-002 (Schema Design)

#### Research Questions
- **RQ1**: What criteria define a valid layer? (semantic boundaries, data independence, etc.)
- **RQ2**: What naming convention for layer IDs/codes? (L00, L01... or semantic codes?)

#### Description
Define the criteria and naming conventions for Quranic data layers. This is foundational work that must precede all layer definition activities. Two key outputs:
1. **Criteria**: What makes something a distinct layer vs a sub-layer or attribute?
2. **Convention**: How should layers be named/coded for consistency across 50+ layers?


تسمية الطبقات بشكل معياري - يجب وضع معايير واضحة لتسمية الطبقات قبل البدء في تعريفها. يشمل: معايير تحديد الطبقة + اصطلاحات التسمية.

#### Acceptance Criteria
- [ ] Layer identification criteria document
- [ ] Naming convention specification (ID format, semantic codes)
- [ ] Examples applied to 5+ existing layers
- [ ] Review and approval by architecture team

#### References (Primary)
- `/docs/architecture/architectural-principles-v1.md` - Principle 5: Base→Expanded
- `/schemas/README.md` - Current naming patterns (L00-L15)

#### References (Secondary)
- `/specs/001-quranic-layer-architecture/spec.md` - RR-001, RR-002 requirements
- `/MARQOUM Quranic Manual.md` - Quranic naming standards
- `/docs/architecture/layer-definition-interview-guide.md` - Section 2: Expanded Layer naming conventions

---

### [LF-002] Layer Inventory & Classification

**System**: QUD-General
**Category**: Layer-Foundation
**Priority**: P1-Critical
**Issue Type**: Research
**Related RRs**: RR-001 (Layer Separation Analysis), RR-002 (Schema Design), RR-003 (Layer Simulation)

#### Research Questions
- **RQ1**: What layers currently exist? (complete inventory of all identified layers)
- **RQ2**: What is the folded/unfolded (base/expanded) distinction? How does 17 base → 50+ expanded?

#### Description
Audit and document all currently identified layers with clear classification:
- **Base layers (folded)**: Core conceptual layers (e.g., "Verse Structure")
- **Expanded layers (unfolded)**: Concrete instantiations (e.g., "Verse-Hafs", "Verse-Warsh")

Current state: 17 base layers identified → potentially 50+ expanded layers across all Qiraat.


محاذاة الطبقات بشكل نظري - جرد شامل للطبقات الحالية مع التمييز بين الطبقات الأساسية (المطوية) والموسعة (المفتوحة). التقدير: ١٧ أساسية → ٥٠+ موسعة.

#### Acceptance Criteria
- [ ] Complete inventory of all identified layers (base + expanded)
- [ ] Classification table: base vs expanded with relationships
- [ ] Gap analysis: what layers are missing?
- [ ] Layer dependency map (which layers depend on which)

#### References (Primary)
- `/specs/001-quranic-layer-architecture/spec.md` - Layer Count Status section
- `/docs/architecture/layer-taxonomy-organizational.md` - Organizational layer definitions
- `/schemas/README.md` - Layer 0-15 architecture

#### References (Secondary)
- `/experiments/rr-001-layer-analysis/results/gap_analysis.md` - Missing layers from RR-001
- `/schemas/Base-Data-Layer-Schemas/` - CSV listing of 15 base layers
- `/schemas/Expanded-Data-Layers-Schema/` - CSV listing of 17+ expanded layers

---

### [LF-003] Layer Taxonomy Template

**System**: QUD-General
**Category**: Layer-Foundation
**Priority**: P2-High
**Issue Type**: Design
**Related RRs**: RR-002 (Schema Design)

#### Research Questions
- **RQ1**: What attributes must a layer definition capture? (identifier, name, description, relationships, schema, versioning)
- **RQ2**: How to standardize layer documentation format?

#### Description
Design a standard template for defining new layers. The template should capture all essential layer attributes:
- Layer identifier (number + semantic code)
- Layer name (Arabic and English)
- Layer description and purpose
- Parent/child/sibling relationships
- Schema requirements
- Versioning considerations
- Cross-layer mapping requirements


قالب موحد لتعريف الطبقات - يشمل: المعرف، الاسم، الوصف، العلاقات، المخطط، الإصدارات.

#### Acceptance Criteria
- [ ] Template document created (markdown format)
- [ ] All required attributes defined
- [ ] Template tested on 2-3 existing layers (L05, L06)
- [ ] Template approved and added to docs/

#### References (Primary)
- `/docs/architecture/layer-definition-interview-guide.md` - Output format section
- `/docs/architecture/layer-interview-session-L05-verse.md` - L05 as example

#### References (Secondary)
- `/specs/001-quranic-layer-architecture/data-model.md` - Entity definitions
- `/docs/architecture/layer-taxonomy-organizational.md` - Exemplar layer definitions (Juz, Hizb, Rub, Surah)

---

### [LF-004] Architectural Principles Review

**System**: QUD-General
**Category**: Layer-Foundation
**Priority**: P2-High
**Issue Type**: Review
**Related RRs**: RR-014 (QUD Orchestrator)

#### Research Questions
- **RQ1**: Are the 10 established architectural principles still valid?
- **RQ2**: What changes or additions needed based on new findings?

#### Description
Review and validate the 10 architectural principles established through interviews:
1. Version-Per-Context Model
2. 2D Flat Representation
3. Multi-Relational Graph
4. Mapping Layers Have Depth
5. Base → Expanded via Big Mapping Table
6. Divine Authority vs Scholarly Convention
7. Surah-Relative Numbering
8. Context Determines Content
9. Separation of Content and Structure
10. Multi-Version Storage Strategy (TBD)

Also review the 10 Open Questions and propose answers.


مراجعة معمارية وطرح أي تغيرات مطلوبة في التصميم الأساسي - مراجعة المبادئ العشرة والأسئلة المفتوحة.

#### Acceptance Criteria
- [ ] Each principle reviewed with status (valid/modified/deprecated)
- [ ] Change proposals documented with rationale
- [ ] Open questions addressed or deferred with reasoning
- [ ] ADR created for any significant changes

#### References (Primary)
- `/docs/architecture/architectural-principles-v1.md` - 10 principles + 10 open questions
- `/docs/architecture/interview-checkpoint-2025-11-09.md` - Interview findings

#### References (Secondary)
- `/specs/001-quranic-layer-architecture/spec.md` - QUD Orchestrator section
- `/docs/architecture/contextual-versioning.md` - Version-Per-Context principle details
- `/docs/architecture/qud-orchestrator.md` - Orchestrator architecture elaboration

---

### [LF-005] Layer Interview Process

**System**: QUD-General
**Category**: Layer-Foundation
**Priority**: P2-High
**Issue Type**: Design + Implementation
**Related RRs**: RR-002 (Schema Design)

#### Research Questions
- **RQ1**: Is the 7-section interview guide complete and effective?
- **RQ2**: What's the status of pending layer interviews (L05-L14)?

#### Description
Two-part effort:
1. **Guide Refinement**: Review and improve the 7-section layer interview methodology
2. **Interview Execution**: Resume and complete pending layer interviews

Current status: L05 (Verse Structure) is 20% complete, L06-L14 not started.

Interview sections:
1. Base Layer Definition
2. Expanded Layer Definition
3. Mapping to Other Layers
4. Data Representation
5. Cross-Narration Validation
6. Source Data Mapping
7. Validation Criteria


عملية المقابلات لتعريف الطبقات - تحسين الدليل واستكمال المقابلات المعلقة (L05-L14).

#### Acceptance Criteria
- [ ] Interview guide refinements documented
- [ ] L05 interview completed (currently 20%)
- [ ] Interview schedule for L06-L14 created
- [ ] Process flow documented

#### References (Primary)
- `/docs/architecture/layer-definition-interview-guide.md` - 7-section methodology
- `/docs/architecture/RESUME-INTERVIEW-HERE.md` - Resume instructions
- `/docs/architecture/layer-interview-session-L05-verse.md` - L05 in progress

#### References (Secondary)
- `/docs/architecture/interview-checkpoint-2025-11-09.md` - Progress: 10 questions answered

---

### [LF-006] Layer Numbering Evaluation

**System**: QUD-General
**Category**: Layer-Foundation
**Priority**: P2-High
**Issue Type**: Research
**Related RRs**: RR-001 (Layer Separation Analysis), RR-002 (Schema Design)

#### Research Questions
- **RQ1**: Is the current 0-15 numbering scheme optimal?
- **RQ2**: How to number/code 50+ expanded layers? (e.g., L05 → L05-HAFS, L05-WARSH?)

#### Description
Evaluate the current layer numbering scheme and propose improvements:
- Current: L00-L15 with L12a/L12b variants
- Challenge: 17 base layers → 50+ expanded layers
- Options: Hierarchical numbering, semantic codes, or hybrid

Consider:
- Ordering by dominance (current approach)
- Ordering by category (structural, character, layout)
- Semantic codes instead of numbers

**⚠️ Known Inconsistency**: There is currently a mismatch between:
- **Layer Architecture Table** in `schemas/README.md`: L0=Qiraat (most dominant) → L15=Character Composition (least dominant)
- **Directory Structure** in `schemas/`: `layer-00-character-composition` → `layer-14-readers-narrators` (inverted order)

This inconsistency MUST be resolved as part of this issue.

تقييم نظام ترقيم الطبقات - الترقيم الحالي 0-15 هل هو مناسب؟ كيف نتعامل مع 50+ طبقة موسعة؟

#### Acceptance Criteria
- [ ] Analysis of current numbering pros/cons
- [ ] Evaluation of alternatives
- [ ] Recommendation with rationale
- [ ] Migration plan if renumbering needed

#### References (Primary)
- `/schemas/README.md` - Layer Architecture table (0-15 ordering)
- `/specs/001-quranic-layer-architecture/spec.md` - 17 vs 50+ layers discussion

#### References (Secondary)
- `/docs/architecture/architectural-principles-v1.md` - Open Questions section
- `/docs/architecture/layer-taxonomy-organizational.md` - Current numbering usage in practice

---

### [LF-007] Layer Documentation Standards

**System**: QUD-General
**Category**: Layer-Foundation
**Priority**: P3-Medium
**Issue Type**: Documentation
**Related RRs**: RR-002 (Schema Design)

#### Research Questions
- **RQ1**: What documentation is required per layer? (README, schema, examples, etc.)
- **RQ2**: How should `/docs/data-layers/` be structured?

#### Description
Establish documentation standards for each layer:
- Per-layer documentation requirements
- Directory structure for `/docs/data-layers/`
- Schema documentation requirements
- Example data requirements
- Validation test documentation


معايير توثيق الطبقات - ما التوثيق المطلوب لكل طبقة؟ كيف ننظم مجلد data-layers؟

#### Acceptance Criteria
- [ ] Documentation requirements checklist per layer
- [ ] Directory structure specification
- [ ] Template for layer README
- [ ] 1-2 layers documented as examples

#### References (Primary)
- `/docs/data-layers/README.md` - Current structure
- `/schemas/layer-XX-*/` - Current schema directory pattern
- `/MARQOUM Quranic Manual.md` - Category codes (TF, QS, QN, etc.) and naming conventions

#### References (Secondary)
- `/specs/001-quranic-layer-architecture/spec.md` - RR-002 deliverables
- `/docs/architecture/layer-definition-interview-guide.md` - "Interview Output Format" template (lines 318-372)
- `/.specify/templates/tasks-template.md` - Path conventions for experiments/, research-tools/, schemas/

---

## B. Semantic Hashing (UUID ذات المعنى)

### [SH-001] Define semantic hashing requirements and criteria

**System**: QUD-General
**Category**: Semantic-Hashing
**Priority**: P1-Critical
**Issue Type**: Research
**Related RRs**: RR-011 (UUID-based Cross-Layer Mapping)

#### Research Questions
- **RQ1**: What properties must a semantic hash have to enable cross-layer entity identity?
- **RQ2**: How to balance human-readability with collision-free uniqueness across 50+ layers?
- **Related**: RR-011, RR-012, RR-014 (Orchestrator uses hashes for routing)

#### Description
Define requirements for semantic hashing - a system that generates meaningful, descriptive identifiers (not random UUIDs). The system should:
- Encode layer identity
- Encode entity type
- Encode contextual information (Qiraah, narration, etc.)
- Be human-readable to some degree
- Be unique and collision-free


العمل على صناعة UUID في كل الطبقات ويكون ذا معنى (semantic hashing) - ليس UUID عشوائي بل معرف وصفي يحمل معلومات عن الطبقة والكيان والسياق.

#### Acceptance Criteria
- [ ] Requirements document created
- [ ] Hash structure components identified
- [ ] Uniqueness strategy defined
- [ ] Examples for multiple layer types

#### References (Primary)
- `/docs/architecture/architectural-principles-v1.md` - Principle 4: Mapping Layers Have Depth
- `/specs/001-quranic-layer-architecture/spec.md` - Domain Constraints (UUID Assignment, Semantic Hashing)

#### References (Secondary)
- `/research-tools/generators/semantic_hasher.py` - Current SHA-256 implementation
- `/research-tools/generators/uuid_generator.py` - UUID v4/v5 strategies
- `/docs/architecture/qud-orchestrator.md` - UUID Mapping for bidirectional navigation

---

### [SH-002] Semantic hash structure specification

**System**: QUD-General
**Category**: Semantic-Hashing
**Priority**: P1-Critical
**Issue Type**: Design
**Related RRs**: RR-011 (UUID Cross-Layer Mapping), RR-013 (Orthographic Transformation)

#### Research Questions
- **RQ1**: What information must be encoded in each semantic hash component?
- **RQ2**: How to represent expansion/contraction cases (1:N, N:1, N:M) in hash structure?
- **Related**: RR-011, RR-013, entity-mapping-schema validation

#### Description
Design the structure of semantic hashes. Proposed components:
```
[LAYER_CODE]-[ENTITY_TYPE]-[CONTEXT]-[UNIQUE_SUFFIX]
Example: L05-VERSE-HAFS-001234
```

Determine:
- What information to encode
- Format and length constraints
- Encoding scheme for each component


تصميم بنية المعرف الدلالي - يجب أن يشمل: رمز الطبقة، نوع الكيان، السياق (القراءة/الرواية)، ولاحقة فريدة.

#### Acceptance Criteria
- [ ] Hash structure specification document
- [ ] Component encoding rules
- [ ] Validation rules for hash format
- [ ] Migration strategy from existing UUIDs

#### References (Primary)
- `/schemas/cross-layer-mappings/entity-mapping-schema.json` - semantic_hash field pattern
- `/specs/001-quranic-layer-architecture/spec.md` - Expansion/Contraction Cases with UUID mapping

#### References (Secondary)
- `/docs/architecture/architectural-principles-v1.md` - Principle 4: Mapping Layer depth
- `/research-tools/generators/uuid_generator.py` - Existing UUID encoding strategies
- `/MARQOUM Quranic Manual.md` - Naming format standards that could inform hash structure

---

### [SH-003] Entity naming conventions by layer

**System**: QUD-General
**Category**: Semantic-Hashing
**Priority**: P2-High
**Issue Type**: Design
**Related RRs**: RR-011 (UUID Mapping), RR-013 (Orthographic Transformation for character naming)

#### Research Questions
- **RQ1**: How do entity naming conventions differ across the 5 hierarchical levels (SB, PB, AB, WB, TB)?
- **RQ2**: How to ensure naming consistency while accommodating layer-specific semantics?
- **Related**: RR-011, RR-001 (layer separation findings), MARQOUM standards

#### Description
Define entity naming conventions for each layer type:
- Character entities
- Word entities
- Verse entities
- Surah entities
- etc.

Each layer may have different naming requirements based on its semantics.

MARQOUM provides relevant standards:
- **Category codes**: TF, LI, TR, QS, QC, SS, TJ, QN, QO, SQ, WI, MD, CF, RF
- **Hierarchical levels**: SB (Surah), PB (Page), AB (Ayah), WB (Word), TB (Token)
- **Naming format**: `Category-ResourceName`

اصطلاحات تسمية الكيانات لكل طبقة - كل طبقة قد تحتاج اصطلاحات تسمية مختلفة بناءً على دلالاتها.

#### Acceptance Criteria
- [ ] Naming conventions for character-level entities
- [ ] Naming conventions for word-level entities
- [ ] Naming conventions for verse/surah entities
- [ ] Naming conventions for layout entities

#### References (Primary)
- `/MARQOUM Quranic Manual.md` - Category codes, hierarchical levels, naming format standards

#### References (Secondary)
- `/docs/architecture/layer-definition-interview-guide.md` - Entity naming examples in output format
- `/docs/architecture/layer-taxonomy-organizational.md` - Exemplar layer definitions with naming patterns
- `/schemas/README.md` - Layer 0-15 entity type overview

---

### [SH-004] Semantic hashing guidelines document

**System**: QUD-General
**Category**: Semantic-Hashing
**Priority**: P2-High
**Issue Type**: Documentation
**Related RRs**: RR-011 (UUID Mapping), RR-013 (Orthographic edge cases), RR-014 (Orchestrator usage)

#### Research Questions
- **RQ1**: When should we use semantic hashing vs. v4 random UUIDs?
- **RQ2**: What are common anti-patterns in semantic hash design?
- **Related**: RR-011, RR-013 (expansion/contraction cases), RR-014 (routing)

#### Description
Create comprehensive guidelines document for semantic hashing:
- When to use semantic hashing vs random UUID
- How to generate semantic hashes
- How to parse semantic hashes
- Best practices and anti-patterns


وثيقة إرشادات التجزئة الدلالية - متى نستخدمها، كيف نولدها، كيف نحللها، أفضل الممارسات.

#### Acceptance Criteria
- [ ] Guidelines document created
- [ ] Code examples included
- [ ] Edge cases documented (expansion/contraction, multi-narration, etc.)

#### References (Primary)
- `/research-tools/generators/semantic_hasher.py` - Implementation reference
- `/research-tools/generators/uuid_generator.py` - UUID generation strategies

#### References (Secondary)
- `/specs/001-quranic-layer-architecture/spec.md` - Domain Constraints (Cross-Layer Identity, Bidirectional Mapping)
- `/docs/architecture/architectural-principles-v1.md` - Context-Aware Versioning pattern
- `/schemas/cross-layer-mappings/entity-mapping-schema.json` - semantic_hash field usage

---

## C. Cross-Layer Mapping & Versioning (الربط والنسخ)

### [CLM-001] Identify version variance across narrations

**System**: Mudmaj
**Category**: Cross-Layer-Mapping
**Priority**: P2-High
**Issue Type**: Research
**Related RRs**: RR-001 (Layer Separation Analysis), RR-012 (Multi-Layer Contextual Versioning)

#### Research Questions
- **RQ1**: What specific data variations occur across different Qiraat narrations at each layer?
- **RQ2**: How do these variations affect cross-layer mapping cardinality?
- **Related**: RR-001, RR-012, Domain Constraints in spec.md

#### Description
Research and document how data varies across different Qiraat and narrations:
- Verse count differences (Hafs 6,236 vs Warsh 6,214)
- Character-level variations
- Word boundary differences
- Structural variations

This informs the cross-layer mapping design.


رصد النسخ المختلفة - توثيق كيفية اختلاف البيانات عبر القراءات والروايات المختلفة: اختلافات عدد الآيات، الحروف، حدود الكلمات.

#### Acceptance Criteria
- [ ] Variance report for Hafs vs Warsh
- [ ] List of known differences documented
- [ ] Impact on mapping strategy assessed

#### References (Primary)
- `/experiments/rr-001-layer-analysis/results/narration_variance.md`
- `/specs/001-quranic-layer-architecture/spec.md` (Domain Constraints)
- `/schemas/README.md` - Layer 0-15 context for variance analysis

#### References (Secondary)
- `/experiments/rr-001-layer-analysis/results/conflation_matrix.csv` - Layer conflation data
- `/experiments/rr-001-layer-analysis/results/mapping_table.csv` - Field to layer mappings
- `/docs/architecture/contextual-versioning.md` - Version-per-context model

---

### [CLM-002] EntityMapping schema refinement

**System**: Mudmaj
**Category**: Cross-Layer-Mapping
**Priority**: P2-High
**Issue Type**: Design
**Related RRs**: RR-011 (UUID Cross-Layer Mapping), RR-012 (Contextual Versioning), RR-013 (Orthographic Transformation)

#### Research Questions
- **RQ1**: What cardinality patterns exist in entity mappings across all 16 layers?
- **RQ2**: How should bidirectional mappings handle expansion/contraction cases?
- **Related**: RR-011, RR-012, RR-013, entity-mapping-schema.json

#### Description
Refine the EntityMapping schema to handle:
- 1:1 mappings (simple identity)
- 1:N expansions (1 Uthmani char → 2 Qiasy chars)
- N:1 contractions (2 Warsh verses → 1 Hafs verse)
- N:M complex mappings
- Bidirectional references
- Positional metadata for ordering


تحسين مخطط ربط الكيانات - يجب أن يدعم: ربط ١:١، توسع ١:ن، انكماش ن:١، ربط معقد ن:م، مراجع ثنائية الاتجاه.

#### Acceptance Criteria
- [ ] Updated EntityMapping schema
- [ ] Support for all cardinality types
- [ ] Position metadata for expansion/contraction
- [ ] Bidirectional traversal validated

#### References (Primary)
- `/schemas/cross-layer-mappings/entity-mapping-schema.json`
- `/schemas/README.md` - Layer architecture and cross-layer mapping overview

#### References (Secondary)
- `/specs/001-quranic-layer-architecture/spec.md` - RR-011, RR-013 sections
- `/docs/architecture/mudmaj-storage.md` - Storage implications for mappings
- `/docs/architecture/contextual-versioning.md` - Version context in mappings

---

### [CLM-003] Version naming standards for unlabeled variants

**System**: Mudmaj
**Category**: Cross-Layer-Mapping
**Priority**: P2-High
**Issue Type**: Design
**Related RRs**: RR-011 (UUID Mapping), RR-012 (Contextual Versioning), RR-013 (Orthographic variants)

#### Research Questions
- **RQ1**: What naming standards exist for Quranic text variants?
- **RQ2**: How should we mint names for variants without existing standards?
- **Related**: RR-011, RR-012, RR-013, MARQOUM standards

#### Description
Create standard names for versions/variants that don't have existing naming standards:
- Edition variants without formal names
- Scholarly tradition variations
- Regional conventions
- Custom/derived versions

When no standard exists, we mint new standardized names for linking data.


إذا لم يكن هناك معايير في النسخ يتم صك مسميات معيارية للنسخ في بيانات الربط - إنشاء أسماء موحدة للنسخ التي ليس لها تسمية معيارية.

#### Acceptance Criteria
- [ ] Naming convention for unlabeled variants
- [ ] Registry of minted version names
- [ ] Process for adding new version names

#### References (Primary)
- `/MARQOUM Quranic Manual.md` - Edition naming patterns, Hafs Mushaf editions catalog (qpc-v1, qpc-v2, indopak, etc.)
- `/docs/architecture/contextual-versioning.md` - Version-per-context naming model

#### References (Secondary)
- `/specs/001-quranic-layer-architecture/spec.md` - RR-012 version examples
- `/schemas/README.md` - Layer version metadata
- `/docs/architecture/architectural-principles-v1.md` - Principle 8: Context Determines Content

---

### [CLM-004] Mapping cardinality documentation

**System**: Mudmaj
**Category**: Cross-Layer-Mapping
**Priority**: P3-Medium
**Issue Type**: Documentation
**Related RRs**: RR-011 (UUID Cross-Layer Mapping), RR-012 (Contextual Versioning), RR-013 (Orthographic Transformation)

#### Research Questions
- **RQ1**: When does each cardinality type (1:1, 1:N, N:1, N:M) occur in Quranic data?
- **RQ2**: How should different cardinalities be documented and exemplified?
- **Related**: RR-011, RR-012, RR-013, entity-mapping-schema.json

#### Description
Document the different mapping cardinalities and when each is used:
- 1:1 - Simple identity mapping
- 1:N - Expansion (orthographic, verse split)
- N:1 - Contraction (verse merge)
- N:M - Complex (multiple-to-multiple)

Include examples from real Quranic data.


توثيق أنواع العلاقات في الربط: ١:١، ١:ن، ن:١، ن:م مع أمثلة من البيانات القرآنية الحقيقية.

#### Acceptance Criteria
- [ ] Documentation for each cardinality type
- [ ] Real-world examples for each
- [ ] Diagram showing cardinality relationships

#### References (Primary)
- `/schemas/cross-layer-mappings/entity-mapping-schema.json` - Cardinality types in schema
- `/specs/001-quranic-layer-architecture/spec.md` - Cross-Layer Mapping Entities, Expansion/Contraction Cases

#### References (Secondary)
- `/docs/architecture/mudmaj-storage.md` - Cardinality storage implications
- `/docs/architecture/qud-orchestrator.md` - Cardinality handling in queries
- `/MARQOUM Quranic Manual.md` - Hierarchical levels (SB, PB, AB, WB, TB) affecting cardinality

---

## D. Mujarrad Architecture (معمارية مجرّد)

### [MJ-001] Document current Mujarrad architecture

**System**: Mujarrad
**Category**: Architecture
**Priority**: P1-Critical
**Issue Type**: Research
**Related RRs**: RR-001 (Layer Separation Analysis), RR-002 (Schema Design), RR-014 (QUD Orchestrator)

#### Research Questions
- **RQ1**: What core abstractions does Mujarrad use that map to QUD's 18+ layer architecture?
- **RQ2**: How does Mujarrad's current abstraction model handle the hierarchical layer relationships (L0→L15)?
- **Related**: RR-001, RR-002 (schema alignment), RR-014 (orchestrator integration points)

#### Description
Document the current Mujarrad (مجرّد) architecture:
- Core concepts and abstractions
- How layers are represented
- Integration points
- Current capabilities and limitations

Mujarrad is the data engine built on abstraction.

فهم معمارية تقنية "مجرّد" - توثيق المفاهيم الأساسية، كيفية تمثيل الطبقات، نقاط التكامل، القدرات والقيود الحالية.

#### Acceptance Criteria
- [ ] Architecture overview document
- [ ] Core concepts glossary
- [ ] Integration points identified
- [ ] Limitations documented

#### References (Primary)
- `/docs/architecture/` - Existing architecture documentation
- `/specs/001-quranic-layer-architecture/spec.md` - Layer definitions and RRs

#### References (Secondary)
- `/schemas/README.md` - Layer schema overview
- `/docs/architecture/architectural-principles-v1.md` - Core architectural principles

---

### [MJ-002] Analyze how layers map to Mujarrad concepts

**System**: Mujarrad
**Category**: Architecture
**Priority**: P2-High
**Issue Type**: Research
**Related RRs**: RR-001 (Layer Separation Analysis), RR-002 (Schema Design), RR-011 (UUID Cross-Layer Mapping)

#### Research Questions
- **RQ1**: Which Mujarrad concepts correspond to which QUD layers (L0-L15)?
- **RQ2**: What gaps exist in the mapping, and what adaptations are required?
- **Related**: RR-001 (layer separation), RR-002 (schema alignment), RR-011 (cross-layer mappings)

#### Description
Analyze and document how QUD data layers map to Mujarrad's abstraction model:
- Which Mujarrad concepts correspond to which layers?
- What adaptations are needed?
- Are there gaps in the mapping?

تحليل كيفية تطابق طبقات QUD مع مفاهيم مجرّد - ما هي المفاهيم المقابلة؟ ما التعديلات المطلوبة؟ هل هناك فجوات؟

#### Acceptance Criteria
- [ ] Mapping table: QUD Layer → Mujarrad concept
- [ ] Gap analysis
- [ ] Adaptation recommendations

#### References (Primary)
- `/schemas/README.md` - Complete layer architecture (L0-L15)
- `/specs/001-quranic-layer-architecture/spec.md` - Layer definitions and relationships

#### References (Secondary)
- `/schemas/cross-layer-mappings/entity-mapping-schema.json` - Cross-layer relationship schema
- `/docs/architecture/layer-taxonomy-organizational.md` - Layer categorization

---

### [MJ-003] Propose architectural changes if needed

**System**: Mujarrad
**Category**: Architecture
**Priority**: P2-High
**Issue Type**: Design
**Related RRs**: RR-002 (Schema Design), RR-014 (QUD Orchestrator)

#### Research Questions
- **RQ1**: What architectural changes are required to align Mujarrad with QUD's layered architecture?
- **RQ2**: How do proposed changes impact existing Mujarrad functionality and migration paths?
- **Related**: RR-002 (schema evolution), RR-014 (orchestrator design decisions)

#### Description
Based on MJ-001 and MJ-002 findings, propose any architectural changes needed:
- Changes to layer definitions
- Changes to Mujarrad model
- New abstractions required
- Deprecated concepts

مراجعة معمارية وطرح أي تغيرات مطلوبة في التصميم الأساسي إن وجد.

#### Acceptance Criteria
- [ ] Change proposal document
- [ ] Impact assessment
- [ ] Migration strategy if changes accepted
- [ ] ADR created for significant changes

#### References (Primary)
- `/docs/decisions/` - Architecture Decision Records directory
- `/specs/001-quranic-layer-architecture/spec.md` - RR-002 schema design requirements

#### References (Secondary)
- `/docs/architecture/architectural-principles-v1.md` - Design principles to preserve
- Outputs from MJ-001 and MJ-002

---

### [MJ-004] Mujarrad-QUD integration specification

**System**: Mujarrad
**Category**: Architecture
**Priority**: P2-High
**Issue Type**: Documentation
**Related RRs**: RR-014 (QUD Orchestrator / Context Schema), RR-015 (MUDMAJ Storage Schema), RR-011 (UUID Cross-Layer Mapping)

#### Research Questions
- **RQ1**: What data flow patterns are required between Mujarrad and QUD's multi-layer architecture?
- **RQ2**: How should API contracts handle cross-layer queries and bidirectional navigation?
- **Related**: RR-014 (orchestrator), RR-015 (storage integration), RR-011 (UUID-based navigation)

#### Description
Create specification document for integrating QUD layers with Mujarrad:
- Data flow diagrams
- API contracts
- Error handling
- Performance considerations

مواصفات تكامل مجرّد مع QUD - مخططات تدفق البيانات، عقود API، معالجة الأخطاء.

#### Acceptance Criteria
- [ ] Integration specification document
- [ ] Data flow diagrams
- [ ] API contract definitions

#### References (Primary)
- `/docs/architecture/qud-orchestrator.md` - Orchestrator design (RR-014)
- `/specs/001-quranic-layer-architecture/spec.md` - Integration requirements

#### References (Secondary)
- `/schemas/cross-layer-mappings/entity-mapping-schema.json` - Cross-layer relationships
- Outputs from MJ-001, MJ-002, MJ-003

---

## E. Mudmaj Database (قاعدة بيانات مدمج)

### [MD-001] Define Mudmaj storage requirements

**System**: Mudmaj
**Category**: Database
**Priority**: P2-High
**Issue Type**: Research
**Related RRs**: RR-015 (MUDMAJ Storage Schema), RR-001 (Layer Separation), RR-002 (Schema Design), RR-011 (UUID Cross-Layer Mapping), RR-012 (Multi-Layer Versioning), RR-014 (QUD Orchestrator)

#### Research Questions
- **RQ1**: What storage format (JSON, SQLite, HDF5, hybrid) best supports 50+ layers × multiple narrations?
- **RQ2**: How to optimize storage for cross-layer and cross-narration query patterns?
- **Related**: RR-015 (storage schema), RR-011 (UUID mapping storage), RR-012 (version tracking)

#### Description
Define the storage requirements for Mudmaj:
- Data volume estimates (50+ layers × multiple narrations)
- Query patterns (cross-layer, cross-narration)
- Performance requirements
- Storage format evaluation (JSON, SQLite, HDF5, hybrid)

تحديد متطلبات تخزين "مدمج" - تقديرات حجم البيانات، أنماط الاستعلام، متطلبات الأداء، تقييم صيغ التخزين.

#### Acceptance Criteria
- [ ] Storage requirements document
- [ ] Volume estimates
- [ ] Query pattern analysis
- [ ] Format recommendation

#### References (Primary)
- `/docs/architecture/mudmaj-storage.md` - Existing Mudmaj storage design
- `/specs/001-quranic-layer-architecture/spec.md` - RR-015 MUDMAJ requirements

#### References (Secondary)
- `/schemas/README.md` - Layer schema overview (volume estimation basis)
- `/research-tools/analyzers/performance_metrics.py` - Performance benchmarking utilities

---

### [MD-002] Mudmaj schema for multi-layer storage

**System**: Mudmaj
**Category**: Database
**Priority**: P2-High
**Issue Type**: Design
**Related RRs**: RR-015 (MUDMAJ Storage Schema), RR-002 (Schema Design), RR-011 (UUID Cross-Layer Mapping), RR-012 (Multi-Layer Versioning)

#### Research Questions
- **RQ1**: How to design a unified schema that stores 18+ layers while maintaining logical separation?
- **RQ2**: What indexing strategy enables efficient cross-layer and cross-narration queries?
- **Related**: RR-015 (storage schema), RR-002 (layer schemas), RR-012 (versioning)

#### Description
Design the Mudmaj database schema that:
- Stores all layers in unified structure
- Maintains layer separation logically
- Enables efficient cross-layer queries
- Supports multiple versions/narrations

تصميم مخطط قاعدة بيانات مدمج - تخزين كل الطبقات بهيكل موحد مع الحفاظ على الفصل المنطقي.

#### Acceptance Criteria
- [ ] Database schema design
- [ ] Support for all layer types
- [ ] Version/narration support
- [ ] Indexing strategy

#### References (Primary)
- `/schemas/mudmaj-schema/` - Mudmaj schema directory
- `/specs/001-quranic-layer-architecture/spec.md` - RR-015 schema requirements
- `/MARQOUM Quranic Manual.md` - Database naming format (`Generic-Specific`), file structure standards

#### References (Secondary)
- `/schemas/cross-layer-mappings/entity-mapping-schema.json` - Cross-layer relationship schema
- `/schemas/README.md` - Layer schema overview

---

### [MD-003] Database prototype (no logic layer)

**System**: Mudmaj
**Category**: Database
**Priority**: P3-Medium
**Issue Type**: Implementation
**Related RRs**: RR-015 (MUDMAJ Storage Schema), RR-003 (Layer Simulation Prototype)

#### Research Questions
- **RQ1**: Does the Mudmaj schema design from MD-002 support efficient CRUD operations at scale?
- **RQ2**: What performance baselines should be established for cross-layer queries?
- **Related**: RR-015 (storage validation), RR-003 (prototype simulation)

#### Description
Create a prototype Mudmaj database with:
- Sample data from Hafs narration
- Basic CRUD operations
- No business logic layer
- Pure data storage and retrieval

Purpose: Test database design without logic complexity.

العمل على تسكين المحتوى بعد الربط في تقنية "مجرد" واختبار قاعدة البيانات "مدمج" واختبار التعامل معها بدون logic.

#### Acceptance Criteria
- [ ] Prototype database created
- [ ] Sample data loaded
- [ ] Basic queries working
- [ ] Performance baseline established

#### References (Primary)
- `/research-tools/data-loaders/quran_loader.py` - Data loading utilities
- `/specs/001-quranic-layer-architecture/spec.md` - RR-003 prototype requirements

#### References (Secondary)
- `/research-tools/validators/` - Schema and data validation tools
- Outputs from MD-001 and MD-002

---

### [MD-004] Mudmaj query validation

**System**: Mudmaj
**Category**: Database
**Priority**: P3-Medium
**Issue Type**: Implementation
**Related RRs**: RR-015 (MUDMAJ Storage Schema), RR-011 (UUID Cross-Layer Mapping), RR-003 (Layer Simulation Prototype)

#### Research Questions
- **RQ1**: Which query patterns (single-layer, cross-layer, cross-narration) meet performance requirements?
- **RQ2**: How does UUID-based cross-layer querying perform compared to direct joins?
- **Related**: RR-015 (storage validation), RR-011 (UUID query patterns), RR-003 (validation)

#### Description
Validate that Mudmaj can handle required query patterns:
- Single-layer queries
- Cross-layer queries
- Cross-narration queries
- Aggregation queries

التحقق من صحة استعلامات مدمج - استعلامات الطبقة الواحدة، عبر الطبقات، عبر الروايات.

#### Acceptance Criteria
- [ ] Query test suite
- [ ] All query patterns validated
- [ ] Performance benchmarks

#### References (Primary)
- `/research-tools/analyzers/performance_metrics.py` - Performance benchmarking
- `/specs/001-quranic-layer-architecture/spec.md` - RR-015 validation requirements

#### References (Secondary)
- `/research-tools/analyzers/data_comparator.py` - Data comparison utilities
- Outputs from MD-003 prototype testing

---

## F. QUD Backend (Backend موحد)

### [QB-001] QUD API initial specification

**System**: QUD-General
**Category**: Backend
**Priority**: P3-Medium
**Issue Type**: Design
**Related RRs**: RR-014 (QUD Orchestrator / Context Schema), RR-011 (UUID Cross-Layer Mapping)

#### Research Questions
- **RQ1**: Should QUD API use REST or GraphQL for multi-layer queries with cross-layer relationships?
- **RQ2**: How should the API expose layer-specific vs cross-layer query capabilities?
- **Related**: RR-014 (orchestrator API design), RR-011 (UUID-based navigation endpoints)

#### Description
Design the initial API specification for QUD backend:
- REST vs GraphQL evaluation
- Endpoint structure
- Authentication/authorization
- Rate limiting

بناء backend عام موحد لQUD للتعامل مع الطبقات - تصميم مواصفات API الأولية.

#### Acceptance Criteria
- [ ] API specification document
- [ ] Technology choice justified
- [ ] Endpoint list defined

#### References (Primary)
- `/docs/architecture/qud-orchestrator.md` - Orchestrator design (RR-014)
- `/specs/001-quranic-layer-architecture/spec.md` - API requirements

#### References (Secondary)
- `/schemas/README.md` - Layer endpoints basis
- Outputs from MJ-004 (Mujarrad-QUD integration spec)

---

### [QB-002] Layer query interface design

**System**: QUD-General
**Category**: Backend
**Priority**: P3-Medium
**Issue Type**: Design
**Related RRs**: RR-014 (QUD Orchestrator), RR-012 (Multi-Layer Versioning), RR-011 (UUID Cross-Layer Mapping)

#### Research Questions
- **RQ1**: How should layer queries specify context (narration, orthography, version)?
- **RQ2**: What query syntax enables efficient cross-layer traversal using UUID mappings?
- **Related**: RR-014 (context parameters), RR-012 (version selection), RR-011 (UUID navigation)

#### Description
Design the interface for querying layers:
- How to specify layer(s) to query
- How to specify context (narration, orthography)
- Response format
- Pagination and filtering

تصميم واجهة استعلام الطبقات - كيفية تحديد الطبقات، السياق، صيغة الاستجابة.

#### Acceptance Criteria
- [ ] Query interface specification
- [ ] Request/response schemas
- [ ] Example queries documented

#### References (Primary)
- `/schemas/cross-layer-mappings/entity-mapping-schema.json` - Cross-layer query basis
- `/specs/001-quranic-layer-architecture/spec.md` - Query requirements

#### References (Secondary)
- `/schemas/README.md` - Layer structure for query design
- Outputs from QB-001 (API specification)

---

## G. AI Research (أبحاث الذكاء الاصطناعي)

### [AI-001] Evaluate FAISS and alternatives for layer vectorization

**System**: AI-Research
**Category**: AI-Research
**Priority**: P3-Medium
**Issue Type**: Research
**Related RRs**: RR-011 (UUID Cross-Layer Mapping), RR-015 (MUDMAJ Storage Schema)

#### Research Questions
- **RQ1**: Which vector database (FAISS, Pinecone, Weaviate, Milvus) best supports Quranic layer embedding at scale?
- **RQ2**: What embedding strategies preserve semantic relationships across 18+ Quranic data layers?
- **Related**: RR-011 (semantic similarity for cross-layer), RR-015 (storage integration)

#### Description
Research vector representation technologies:
- FAISS (Facebook AI Similarity Search)
- Pinecone, Weaviate, Milvus alternatives
- Embedding strategies for Quranic text layers
- Performance and scalability considerations

فهم المشكلة بشكل عميق والبحث عن تقنية مثل FAISS لوضع الطبقات في Vector Representation.

#### Acceptance Criteria
- [ ] Technology evaluation report
- [ ] Embedding strategy proposal
- [ ] Performance estimates
- [ ] Recommendation with justification

#### References (Primary)
- `/specs/001-quranic-layer-architecture/spec.md` - Layer structure for embedding design
- `/schemas/README.md` - 18+ layer architecture overview

#### References (Secondary)
- `/research-tools/analyzers/` - Analysis utilities for performance testing
- External: FAISS documentation, Pinecone, Weaviate, Milvus docs

---

### [AI-002] ETL pipeline design for external Quranic content

**System**: AI-Research
**Category**: AI-Research
**Priority**: P3-Medium
**Issue Type**: Design
**Related RRs**: RR-015 (MUDMAJ Storage Schema), RR-001 (Layer Separation), RR-002 (Schema Design)

#### Research Questions
- **RQ1**: How to design an ETL pipeline that maps external Quranic content (Tafsir, etc.) to QUD layers?
- **RQ2**: What standardization rules ensure external content integrates with existing layer schemas?
- **Related**: RR-015 (Mudmaj integration), RR-001 (layer assignment), RR-002 (schema conformance)

#### Description
Design ETL (Extract, Transform, Load) pipeline for external content:
- Example: Tafsir files
- Extraction from source format
- Analysis and segmentation
- Standardized naming
- Layer-compatible storage
- Linking to Mudmaj

محاكاة بيانات الربط والعمل على تصور للبنية المعمارية - مثال ملف تفسير: كيف يمكن عمل ETL ثم تحليله وتقسيم مادته وتسميتها بشكل معياري ثم تسكينها في قاعدة بيانات بشكل يتوافق مع الطبقات ثم ربط المدخلات الأخيرة مع قاعدة بيانات "مدمج".

#### Acceptance Criteria
- [ ] ETL pipeline design document
- [ ] Data flow diagram
- [ ] Standardization rules
- [ ] Mudmaj integration specification

#### References (Primary)
- `/research-tools/data-loaders/quran_loader.py` - Existing data loading patterns
- `/MARQOUM Quranic Manual.md` - Naming standards for content categorization

#### References (Secondary)
- `/schemas/README.md` - Layer schemas for content mapping
- `/docs/architecture/mudmaj-storage.md` - Mudmaj integration target

---

### [AI-003] Content standardization and layer assignment workflow

**System**: AI-Research
**Category**: AI-Research
**Priority**: P3-Medium
**Issue Type**: Design
**Related RRs**: RR-001 (Layer Separation), RR-002 (Schema Design), RR-011 (UUID Cross-Layer Mapping)

#### Research Questions
- **RQ1**: What classification criteria determine which QUD layer(s) external content maps to?
- **RQ2**: How to automate layer assignment while ensuring schema conformance?
- **Related**: RR-001 (layer definitions), RR-002 (schema validation), RR-011 (UUID assignment)

#### Description
Design the workflow for standardizing external content and assigning it to layers:
- Content analysis algorithms
- Layer classification criteria
- Naming standardization
- Quality validation

تسمية المادة بشكل معياري ثم تسكينها في قاعدة بيانات بشكل يتوافق مع الطبقات.

#### Acceptance Criteria
- [ ] Workflow documentation
- [ ] Classification criteria
- [ ] Validation rules

#### References (Primary)
- `/MARQOUM Quranic Manual.md` - Category codes (TF, LI, TR, QS, QC) for classification
- `/schemas/README.md` - Layer schemas for assignment targets

#### References (Secondary)
- `/research-tools/validators/` - Validation utilities
- Outputs from AI-002 (ETL pipeline integration)

---

## H. Munajjam Integration (ربط منجّم)

### [MN-001] Document Munajjam current capabilities

**System**: Munajjam
**Category**: Integration
**Priority**: P2-High
**Issue Type**: Research
**Related RRs**: RR-001 (Layer Separation), RR-015 (MUDMAJ Storage Schema)

#### Research Questions
- **RQ1**: What are Munajjam's current audio-text synchronization capabilities and accuracy levels?
- **RQ2**: How does Munajjam's verse-level output map to QUD layer architecture?
- **Related**: RR-001 (layer mapping for audio data), RR-015 (storage integration)

#### Description
Document the current capabilities of Munajjam:
- Audio-text synchronization algorithm
- Supported Qiraat (currently Hafs only)
- Verse-level segmentation
- Output format and accuracy

Munajjam (منجّم) is the Quranic data digester for recitations.

منجم: هاضم البيانات القرآنية (التلاوات فقط في الوقت الحالي ويعمل على مزامنة الآية صوتاً مع النص القرآني وفي قراءة واحدة فقط ألا وهي حفص).

#### Acceptance Criteria
- [ ] Capabilities document
- [ ] Algorithm overview
- [ ] Current limitations documented
- [ ] Output format specification

#### References (Primary)
- Munajjam source code/documentation (if available)
- `/specs/001-quranic-layer-architecture/spec.md` - Layer integration context

#### References (Secondary)
- `/schemas/README.md` - Layer structure for audio data mapping
- `/docs/architecture/mudmaj-storage.md` - Storage target for Munajjam output

---

### [MN-002] Word-level segmentation feasibility study

**System**: Munajjam
**Category**: Integration
**Priority**: P3-Medium
**Issue Type**: Research
**Related RRs**: RR-001 (Layer Separation), RR-011 (UUID Cross-Layer Mapping)

#### Research Questions
- **RQ1**: Is word-level audio segmentation technically feasible with acceptable accuracy?
- **RQ2**: How would word-level segments integrate with L11 (Word Structure) layer?
- **Related**: RR-001 (word layer alignment), RR-011 (word-level UUID assignment)

#### Description
Research the feasibility of extending Munajjam to word-level segmentation:
- Current verse-level → word-level enhancement
- Technical requirements
- Accuracy expectations
- Resource requirements

العمل على فهم خوارزمية منجّم وبدء فهم التصور بشكل عام ثم العمل على الجانب البحثي ومحاولة إضافة تقسيم التلاوة على مستوى الكلمة.

#### Acceptance Criteria
- [ ] Feasibility report
- [ ] Technical requirements
- [ ] Accuracy baseline
- [ ] Resource estimate

#### References (Primary)
- Outputs from MN-001 (current capabilities baseline)
- `/schemas/layer-03-word-structure/schema.json` - Word layer schema target

#### References (Secondary)
- `/specs/001-quranic-layer-architecture/spec.md` - Layer granularity requirements
- Academic literature on Arabic speech-to-text alignment

---

### [MN-003] Munajjam-Mudmaj integration specification

**System**: Munajjam
**Category**: Integration
**Priority**: P3-Medium
**Issue Type**: Design
**Related RRs**: RR-015 (MUDMAJ Storage Schema), RR-011 (UUID Cross-Layer Mapping), RR-014 (QUD Orchestrator)

#### Research Questions
- **RQ1**: How should Munajjam audio timestamps map to Mudmaj layer entities (verse, word)?
- **RQ2**: What data flow pattern enables bidirectional navigation between audio and text layers?
- **Related**: RR-015 (storage schema), RR-011 (UUID linking), RR-014 (orchestrator routing)

#### Description
Design the integration between Munajjam and Mudmaj:
- How Munajjam output maps to Mudmaj layers
- Data flow from Munajjam to Mudmaj
- Linking recitation data to text layers

ربط منجم بـ "مدمج" - كيف يتم ربط مخرجات منجم بطبقات مدمج.

#### Acceptance Criteria
- [ ] Integration specification
- [ ] Layer mapping for audio data
- [ ] Data flow diagram

#### References (Primary)
- `/docs/architecture/mudmaj-storage.md` - Mudmaj storage target
- `/schemas/cross-layer-mappings/entity-mapping-schema.json` - Cross-layer mapping patterns

#### References (Secondary)
- Outputs from MN-001 (Munajjam capabilities)
- Outputs from MD-002 (Mudmaj schema)

---

### [MN-004] Munajjam algorithm documentation

**System**: Munajjam
**Category**: Integration
**Priority**: P2-High
**Issue Type**: Documentation
**Related RRs**: RR-001 (Layer Separation)

#### Research Questions
- **RQ1**: What are the key algorithmic steps in Munajjam's audio-text synchronization?
- **RQ2**: What edge cases (pauses, repetitions, variations) must the algorithm handle?
- **Related**: RR-001 (layer-aware algorithm design)

#### Description
Document the Munajjam algorithm in detail:
- Audio processing steps
- Text alignment method
- Synchronization logic
- Edge cases and handling

توثيق خوارزمية منجّم بالتفصيل - خطوات معالجة الصوت، طريقة محاذاة النص، منطق المزامنة.

#### Acceptance Criteria
- [ ] Algorithm documentation
- [ ] Process flow diagram
- [ ] Edge cases documented

#### References (Primary)
- Munajjam source code/documentation
- Outputs from MN-001 (capabilities overview)

#### References (Secondary)
- `/docs/architecture/` - Architecture documentation patterns
- Academic literature on forced alignment algorithms

---

## Quick Reference: Issue Count by Category

| Category | Count | Priority |
|----------|-------|----------|
| Layer Foundation | 7 | P1-P3 |
| Semantic Hashing | 4 | P1-P2 |
| Cross-Layer Mapping | 4 | P2-P3 |
| Mujarrad Architecture | 4 | P1-P2 |
| Mudmaj Database | 4 | P2-P3 |
| QUD Backend | 2 | P3 |
| AI Research | 3 | P3 |
| Munajjam Integration | 4 | P2-P3 |
| **Total** | **32** | |

---

## Issue ID Reference

| ID | Title | System | Priority |
|----|-------|--------|----------|
| LF-001 | Layer Naming Standards | QUD-General | P1 |
| LF-002 | Layer Inventory & Classification | QUD-General | P1 |
| LF-003 | Layer Taxonomy Template | QUD-General | P2 |
| LF-004 | Architectural Principles Review | QUD-General | P2 |
| LF-005 | Layer Interview Process | QUD-General | P2 |
| LF-006 | Layer Numbering Evaluation | QUD-General | P2 |
| LF-007 | Layer Documentation Standards | QUD-General | P3 |
| SH-001 | Semantic Hashing Requirements | QUD-General | P1 |
| SH-002 | Semantic Hash Structure Specification | QUD-General | P1 |
| SH-003 | Entity Naming Conventions | QUD-General | P2 |
| SH-004 | Semantic Hashing Guidelines | QUD-General | P2 |
| CLM-001 | Version Variance Research | Mudmaj | P2 |
| CLM-002 | EntityMapping Schema Refinement | Mudmaj | P2 |
| CLM-003 | Version Naming Standards | Mudmaj | P2 |
| CLM-004 | Mapping Cardinality Documentation | Mudmaj | P3 |
| MJ-001 | Document Mujarrad Architecture | Mujarrad | P1 |
| MJ-002 | Layer-to-Mujarrad Mapping | Mujarrad | P2 |
| MJ-003 | Propose Architectural Changes | Mujarrad | P2 |
| MJ-004 | Mujarrad-QUD Integration Spec | Mujarrad | P2 |
| MD-001 | Mudmaj Storage Requirements | Mudmaj | P2 |
| MD-002 | Multi-Layer Storage Schema | Mudmaj | P2 |
| MD-003 | Database Prototype | Mudmaj | P3 |
| MD-004 | Query Validation | Mudmaj | P3 |
| QB-001 | QUD API Specification | QUD-General | P3 |
| QB-002 | Layer Query Interface Design | QUD-General | P3 |
| AI-001 | FAISS Evaluation | AI-Research | P3 |
| AI-002 | ETL Pipeline Design | AI-Research | P3 |
| AI-003 | Content Standardization Workflow | AI-Research | P3 |
| MN-001 | Munajjam Capabilities | Munajjam | P2 |
| MN-002 | Word-Level Segmentation Feasibility | Munajjam | P3 |
| MN-003 | Munajjam-Mudmaj Integration | Munajjam | P3 |
| MN-004 | Algorithm Documentation | Munajjam | P2 |
