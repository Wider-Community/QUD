# Quranic Data Layer Definition Interview Guide

**Purpose**: Systematically define all Quranic data layers, their expanded representations, and mapping relationships.

**Date**: 2025-11-09
**Status**: WORKING DOCUMENT

---

## Interview Methodology

### Process
1. **One layer at a time** - complete all questions for Layer N before moving to Layer N+1
2. **Base → Expansion → Mappings** - define the conceptual layer, then its data representations, then its relationships
3. **Document examples** - provide concrete Quranic examples for each definition
4. **Validate consistency** - ensure layer definitions align with QS-QIRAAT source data

### Terminology
- **Base Layer (Conceptual)**: The collapsed/abstract concept (e.g., "Division" as a concept)
- **Expanded Layers (Data)**: The actual data representation, often multiple layers (e.g., "Division Number" + "Division Quarter")
- **Mapping Layer**: The relationship between two base layers
- **Expanded Mapping**: The data representation of a relationship, often with reset behavior

---

## VALIDATED EXAMPLE (Reference for All Layers)

### Base Layer: Division Structure
**Conceptual Definition**: Organizational segments of the Quran for recitation scheduling (Juz, Hizb, Rub)

#### Expanded Layers:
1. **Division Number Layer**
   - Data Type: Integer
   - Range: 1-30 (for Juz)
   - Scope: Global (does not reset)
   - Example: Juz 1, Juz 2, ..., Juz 30

2. **Division Quarter/Eighth Layer**
   - Data Type: Ordinal (1st, 2nd, 3rd, 4th)
   - Range: 1-4 quarters OR 1-8 eighths
   - Scope: Resets per Division Number
   - Example: Juz 1 - Quarter 1, Quarter 2, Quarter 3, Quarter 4; Juz 2 - Quarter 1, Quarter 2...
   - Reset Behavior: Each new Juz restarts counting from 1st quarter

---

### Base Layer: Chapter Structure
**Conceptual Definition**: The 114 chapters (Surahs) of the Quran

#### Expanded Layers:
1. **Chapter Number Layer**
   - Data Type: Integer
   - Range: 1-114
   - Scope: Global (does not reset)
   - Example: Surah 1 (Al-Fatiha), Surah 2 (Al-Baqarah), ..., Surah 114 (An-Nas)
   - Note: In this case, base layer = expanded layer (single representation)

---

### Mapping Layer: Chapter-Division Relationship
**Conceptual Definition**: How Divisions are distributed within Chapters

#### Expanded Mapping Layers:
1. **Chapter Number** (from Chapter base layer)
   - Data Type: Integer
   - Range: 1-114
   - Scope: Global

2. **Chapter Division Number**
   - Data Type: Integer
   - Range: Varies per chapter (typically 1-2, but larger chapters have more)
   - Scope: Resets per Chapter
   - Reset Behavior: Each new Chapter restarts division counting from 1
   - Example:
     - Chapter 1, Division 1
     - Chapter 1, Division 2
     - Chapter 2, Division 1
     - Chapter 2, Division 2
     - Chapter 2, Division 3

**Relationship Type**: One Chapter contains multiple Divisions (1:N)

**Data Representation**:
```json
{
  "chapter_number": 2,
  "chapter_division_number": 1,
  "global_division_number": 3,
  "division_quarter": 2
}
```

---

## INTERVIEW QUESTIONS (Apply to Each Layer)

### Section 1: Base Layer Definition

**Q1.1**: What is the **conceptual name** of this base layer?
- Example: "Division Structure", "Chapter Structure", "Verse Structure"

**Q1.2**: What is the **semantic purpose** of this layer in Quranic organization?
- Example: "Organizational segments for recitation scheduling"

**Q1.3**: What is the **source of authority** for this layer's existence?
- Options: Quranic revelation / Scholarly convention / Mushaf layout / Narration-specific
- Example: Division (Juz/Hizb) is scholarly convention; Verse boundaries are from revelation

**Q1.4**: Is this layer **narration-specific** or **universal across all narrations**?
- Example: Chapter structure is universal; Verse boundaries vary between Hafs and Warsh

---

### Section 2: Expanded Layer Definition

**Q2.1**: How many **expanded data layers** does this base layer have?
- Options: 1 (same as base) / 2 / 3 / More
- Example: Division → 2 expanded layers (Number + Quarter)

**Q2.2**: For **each expanded layer**, define:

#### Expanded Layer [N] Name:
**Q2.2a**: What is the specific name of this expanded layer?
- Example: "Division Number Layer", "Division Quarter Layer"

**Q2.2b**: What is the **data type**?
- Options: Integer / Ordinal (1st, 2nd, 3rd) / String / Boolean / Composite
- Example: Division Number = Integer; Division Quarter = Ordinal

**Q2.2c**: What is the **value range**?
- Example: Division Number: 1-30; Division Quarter: 1-4

**Q2.2d**: What is the **scope/reset behavior**?
- Options:
  - Global (never resets, continuous sequence)
  - Resets per parent entity (specify which parent)
  - Resets per context (specify context)
- Example: Division Number = Global; Division Quarter = Resets per Division Number

**Q2.2e**: Does this layer **vary by narration**?
- Yes/No
- If yes, document known variations (e.g., Hafs vs Warsh)

**Q2.2f**: Provide **3-5 concrete examples** from the Quran:
- Example:
  - Juz 1, Quarter 1 (Surah 1:1 - Surah 2:25)
  - Juz 1, Quarter 2 (Surah 2:26 - Surah 2:59)
  - Juz 2, Quarter 1 (resets back to Quarter 1)

---

### Section 3: Mapping to Other Layers

**Q3.1**: Which other base layers does this layer **directly relate to**?
- List all related layers
- Example: Division relates to Chapter, Verse, Page

**Q3.2**: For **each related layer**, define the mapping:

#### Mapping to: [Related Layer Name]

**Q3.2a**: What is the **relationship type**?
- Options:
  - 1:1 (one-to-one)
  - 1:N (one-to-many, e.g., one Chapter contains many Verses)
  - N:1 (many-to-one, e.g., many Verses belong to one Chapter)
  - N:M (many-to-many)

**Q3.2b**: What is the **semantic meaning** of this relationship?
- Example: "A Chapter contains multiple Divisions" or "A Division spans multiple Chapters"

**Q3.2c**: What is the **directionality**?
- Options:
  - Contains (parent → children)
  - Belongs to (child → parent)
  - Spans across (cuts through)
  - Aligns with (parallel)

**Q3.2d**: Is this mapping **expanded into multiple layers**?
- Yes/No
- If yes, proceed to Q3.3

---

**Q3.3**: For **expanded mapping layers**, define:

#### Expanded Mapping Layer [N] Name:

**Q3.3a**: What is the name of this expanded mapping layer?
- Example: "Chapter Division Number"

**Q3.3b**: What is the **data type**?
- Integer / Ordinal / String / Boolean / Composite

**Q3.3c**: What is the **value range**?
- Example: Chapter Division Number: Varies (1-2 for small chapters, 1-4 for large chapters)

**Q3.3d**: What is the **reset behavior**?
- Specify the parent entity that triggers reset
- Example: "Resets at each new Chapter boundary"

**Q3.3e**: Provide **5-10 concrete examples** showing reset behavior:
- Example:
  - Chapter 1, Division 1 → Global Division 1, Quarter 1
  - Chapter 1, Division 2 → Global Division 1, Quarter 3
  - Chapter 2, Division 1 (RESET) → Global Division 1, Quarter 4
  - Chapter 2, Division 2 (continues) → Global Division 2, Quarter 1

**Q3.3f**: Is there a **global reference** that does NOT reset?
- Yes/No
- If yes, what is it called?
- Example: Global Division Number (1-30, never resets) vs Chapter Division Number (resets per chapter)

---

### Section 4: Data Representation

**Q4.1**: What is the **canonical data structure** for this layer?
- Provide JSON schema example

**Q4.2**: What are the **required fields** vs **optional fields**?

**Q4.3**: What are the **constraints and invariants**?
- Example: "Sum of all Chapter Division Numbers per chapter must equal total divisions in that chapter"

**Q4.4**: What is the **storage efficiency** consideration?
- Does this layer create redundancy in flat format?
- Example: In QS-QIRAAT, Division Number repeated for every verse in that division (redundancy)

---

### Section 5: Cross-Narration Validation

**Q5.1**: Does this layer **vary between narrations** (Hafs, Warsh, Qalun, etc.)?
- Yes/No/Partially

**Q5.2**: If yes, document **known variations**:
- Hafs vs Warsh example
- Expected variations for other narrations

**Q5.3**: Are there **controversies or scholarly disagreements** about this layer?
- Example: Verse numbering differs between narrations (6,236 Hafs vs 6,214 Warsh)

**Q5.4**: How should the **UUID system** handle cross-narration identity?
- Does each narration get separate UUIDs?
- Is there a canonical UUID that spans narrations?
- Example: canonical_verse_id for verses that exist across narrations

---

### Section 6: Source Data Mapping

**Q6.1**: Which **QS-QIRAAT fields** map to this layer?
- List all source fields
- Example: Division Number ← `jozz` field in QS-QIRAAT

**Q6.2**: Is this layer **explicitly present** or **implicitly derived**?
- Explicit: Data directly in QS-QIRAAT
- Implicit: Must be computed/extracted from other fields

**Q6.3**: What is the **extraction algorithm** if derived?
- Provide pseudocode or algorithm description

**Q6.4**: What are the **known data quality issues** in source data?
- Example: Missing data, inconsistencies, encoding issues

---

### Section 7: Validation Criteria

**Q7.1**: What are the **authoritative counts** for this layer?
- Example: 30 Juz, 114 Chapters, 6,236 Verses (Hafs)

**Q7.2**: What are the **validation rules**?
- Example: "Every verse must belong to exactly one chapter"

**Q7.3**: What are the **known edge cases**?
- Example: Verse boundaries split mid-page, divisions starting mid-verse

---

## LAYER INTERVIEW SEQUENCE

Process layers in this order (blocking dependencies):

### Phase 1: Foundational Layers (No Dependencies)
1. **Character Composition Layer** (Layer 0)
2. **Character Symbols Layer** (Layer 1)
3. **Character Paired Data Layer** (Layer 2)

### Phase 2: Structural Layers (Depend on Character Layers)
4. **Word Structure Layer** (Layer 3)
5. **Sentence Structure Layer** (Layer 4)
6. **Verse Structure Layer** (Layer 5)
7. **Surah/Chapter Structure Layer** (Layer 6)

### Phase 3: Organizational Layers
8. **Division Structure Layer** (Layer 7) ← EXAMPLE COMPLETED ABOVE
9. **Qiraah/Manuscript Layer** (Layer 9)
10. **Readers and Narrators Layer** (Layer 14)

### Phase 4: Layout Layers
11. **Page Layout Layer** (Layer 11)
12. **Line Layout Layer** (Layer 12)

### Phase 5: Orthographic Layers
13. **Orthographic Systems Layer** (Layer 13)

### Phase 6: Edition Layers
14. **Edition Variants Layer** (Layer 10)

### Phase 7: Higher-Order Organizational Layers (If Exist)
15. **Chapter Structure Layer** (Layer 8) - IF DIFFERENT from Layer 6
16. **Additional Layers** (15-16) - IF THEY EXIST

---

## INTERVIEW OUTPUT FORMAT

For each layer, produce a document in `/docs/data-layers/layer-XX-name.md` with:

```markdown
# Layer [N]: [Name]

## Base Layer Definition
- Conceptual Name: ...
- Semantic Purpose: ...
- Authority Source: ...
- Narration-Specific: Yes/No

## Expanded Layers
### Expanded Layer 1: [Name]
- Data Type: ...
- Value Range: ...
- Scope/Reset: ...
- Examples: ...

### Expanded Layer 2: [Name]
[If applicable]

## Mappings to Other Layers
### Mapping to Layer [M]: [Related Layer Name]
- Relationship Type: ...
- Semantic Meaning: ...
- Directionality: ...

#### Expanded Mapping Layers
[If applicable]

## Data Representation
```json
{
  "example": "data structure"
}
```

## Constraints and Invariants
- ...

## Cross-Narration Considerations
- Variations: ...
- Controversies: ...

## Source Data Mapping
- QS-QIRAAT Fields: ...
- Extraction Algorithm: ...

## Validation Criteria
- Authoritative Counts: ...
- Validation Rules: ...
- Edge Cases: ...
```

---

## NEXT STEPS

1. **Confirm methodology**: Review this interview guide and confirm it captures the required information
2. **Start with Layer 5 (Verse)**: This is most critical for verse numbering controversy
3. **Proceed systematically**: One layer at a time, completing all questions
4. **Cross-reference**: Ensure layer definitions are consistent across all documentation

---

## DECISION RECORD

**Date**: 2025-11-09
**Decision**: Adopt base/expanded layer model for Quranic data architecture
**Rationale**:
- Resolves confusion between conceptual layers and data representations
- Explains reset behavior (e.g., division quarters reset per division)
- Clarifies mapping layers as separate data entities
- Aligns with observed data patterns in QS-QIRAAT

**Status**: APPROVED - Proceed with interviews