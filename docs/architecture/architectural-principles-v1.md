# QUD Architectural Principles (v1.0)

**Date**: 2025-11-09
**Status**: ESTABLISHED - Based on Layer 5 Interview Findings
**Authority**: Derived from user requirements and Quranic data structure analysis

---

## Core Principles

### 1. Version-Per-Context Model 🌍

**Principle**: Each Qiraah/Narration represents a complete, independent content version, not just different numbering of the same content.

**Why**:
- 99.9% of Quranic text is identical across Qiraat
- 0.1% variations are divinely revealed (Prophet Muhammad ﷺ taught all versions)
- Variations include: word presence/absence (e.g., "من"), character differences, diacritics
- Cannot have single "truth" version - all versions are authoritative

**Implementation**:
```
Each layer exists in multiple versions:
- Characters_Hafs
- Characters_Warsh
- Characters_Qalun
- [etc.]

OR

Single table with version context:
- Characters { id, char, context: "hafs", ... }
```

**Implications**:
- Storage: More data (each version stored separately or with context field)
- Queries: Must specify context ("give me words in Hafs context")
- Mappings: Need cross-version canonical mappings (Hafs Ayah 2:255 ↔ Warsh Ayah 2:254)

---

### 2. 2D Flat Representation (No Deep Nesting) 📊

**Principle**: Nested relationships between layers must be representable as flat/2D structures in the base representation. Avoid deep hierarchical nesting.

**Why**:
- An Ayah doesn't "contain" words as nested data because: **Which version of words?** Hafs? Warsh? Edition A? Edition B?
- Same content may have different words across contexts
- Nesting creates ambiguity about which version is nested
- Flat structures with mappings make versioning explicit

**Implementation**:

❌ **WRONG (Nested)**:
```json
{
  "ayah": {
    "number": 1,
    "words": [
      {
        "text": "بسم",
        "characters": ["ب", "س", "م"]
      }
    ]
  }
}
```

✅ **CORRECT (Flat with Mappings)**:
```json
Ayah:        { ayah_id: 1, number: 1, context: "hafs" }
Word:        { word_id: 1, text: "بسم", context: "hafs" }
Character:   { char_id: 1, letter: "ب", context: "hafs" }

Ayah_Word_Mapping:  { ayah_id: 1, word_id: 1, position: 1, context: "hafs" }
Word_Char_Mapping:  { word_id: 1, char_id: 1, position: 1, context: "hafs" }
```

**Implications**:
- More tables (entity tables + mapping tables)
- Explicit context in mappings
- Easier to query across contexts
- Can expand to higher dimensions in "expanded versions" but keep base 2D

---

### 3. Multi-Relational Graph (Not Linear Hierarchy) 🕸️

**Principle**: Quranic data layers form a multi-relational graph where each layer can relate to MULTIPLE other layers, not a simple linear parent-child hierarchy.

**Why**:
- Character relates to: Word (contains), Ayah (character range), Line (positioned on)
- Word relates to: Character (contains), Ayah (belongs to), Page (positioned on)
- Ayah relates to: Word (contains), Surah (belongs to), Division (spans?), Juz (organized by), Page (spans), Line (spans)
- Linear hierarchy oversimplifies reality

**Implementation**:

❌ **WRONG (Linear Hierarchy)**:
```
Character → Word → Sentence → Ayah → Surah → Division → Quran
(Simple tree structure)
```

✅ **CORRECT (Multi-Relational Graph)**:
```
Character ←→ Word [contains]
Character ←→ Ayah [character range]
Character ←→ Line [positioned on]

Word ←→ Character [contains]
Word ←→ Ayah [belongs to]
Word ←→ Page [positioned on]

Ayah ←→ Word [contains]
Ayah ←→ Surah [belongs to]
Ayah ←→ Division [organized by/spans?]
Ayah ←→ Juz [organized by - different from Division!]
Ayah ←→ Page [positioned on/spans]
Ayah ←→ Line [positioned on/spans]

[Many more relationships...]
```

**Implications**:
- Map relationships as graph, not tree
- Some layers relate horizontally (siblings), not vertically (parent/child)
- Multiple valid "views" of the data (organizational, positional, structural)
- More complex but more accurate to Quranic reality

---

### 4. Mapping Layers Have Depth 🔗

**Principle**: Mapping layers are not simple foreign key joins. They are full layers with enough depth to "imitate the original layer" and handle all variations across contexts.

**Why**:
- Simple join: `ayah_id → word_id` cannot handle:
  - Word merging across Qiraat
  - Word removal/addition across Qiraat
  - Positional variations
  - Context-specific mappings
- Need rich mapping structure to accommodate maximum variation

**Implementation**:

❌ **WRONG (Simple Join)**:
```sql
Ayah_Word_Mapping:
  ayah_id, word_id
```

✅ **CORRECT (Full Mapping Layer)**:
```sql
Ayah_Word_Mapping:
  mapping_id (UUID)
  ayah_id (UUID)
  word_id (UUID)
  position (integer - word position in ayah)
  context (string - "hafs" / "warsh" / etc.)
  version (semver - for schema evolution)
  cardinality (1:1, 1:N, N:1, N:M)
  semantic_hash (for equivalence queries)
  provenance (source of mapping)
  created_at, updated_at
  [... more fields as needed]
```

**Implications**:
- Mapping layers are first-class entities (not afterthoughts)
- Mapping layers have their own schemas, UUIDs, versions
- Maximum mapping layer size = largest variation across all contexts
- Example: Words Mapping Layer must accommodate max words across all Quraat

---

### 5. Base Layers → Expanded Layers via Big Mapping Table 🗺️

**Principle**: Each Base Layer (conceptual) expands into one or more Expanded Layers (data representations). This expansion is systematically defined in a "big mapping table."

**Why**:
- Base Layer = abstract concept ("Division")
- Expanded Layers = concrete data representations ("Division Number", "Division Quarter")
- Need systematic way to map base → expanded for all layers
- Enables consistent expansion pattern across all layers

**Implementation**:

```
Base Layer: Division Structure
  ↓ (expands to)
Expanded Layer 1: Division Number (integer 1-30, global, never resets)
Expanded Layer 2: Division Quarter (ordinal 1-4, resets per division)

Base Layer: Ayah Structure
  ↓ (expands to)
Expanded Layer 1: Canonical Ayah ID (UUID, universal across Qiraat)
Expanded Layer 2: Surah-Relative Ayah Number (integer, resets per Surah)
Expanded Layer 3: Sequential Ayah Number (integer 1-6236 for Hafs, continuous)

[Pattern repeats for all layers]
```

**Big Mapping Table Schema** (TBD):
```
BaseLayer_ExpandedLayer_Mapping:
  base_layer_name (e.g., "Division Structure")
  expanded_layer_name (e.g., "Division Number")
  data_type (integer, ordinal, UUID, string, etc.)
  value_range (e.g., "1-30")
  reset_behavior (global, resets_per_parent, resets_per_context)
  required (boolean)
  [... more metadata]
```

**Implications**:
- All base→expanded mappings in one place (single source of truth)
- Systematic approach to layer expansion
- Easier to validate completeness ("did we expand all base layers?")
- Schema generation can be automated from this mapping

---

### 6. Divine Authority & Scholarly Convention 📖

**Principle**: Distinguish between divinely revealed elements (immutable across all interpretations) and scholarly conventions (may vary).

**Divinely Revealed**:
- ✅ Verse boundaries (where each Ayah starts/ends)
- ✅ Text variations across Qiraat (all taught by Prophet Muhammad ﷺ)
- ✅ Surah structure (114 Surahs)

**Scholarly Convention**:
- 📚 Division system (Juz, Hizb, Rub - for recitation scheduling)
- 📚 Page layout (Mushaf formatting)
- 📚 Line breaks
- 📚 Tajweed annotation styles
- 📚 Geographic traditions (Medina, Kufa, etc.)

**NOT Data Layers** (Content/Metadata):
- Tajweed schools (content attached to character layer)
- Geographic origin (content attached to various layers)
- Historical context (content/metadata)

**Implications**:
- Divine elements: Zero tolerance for errors, 100% validation required
- Scholarly elements: Document conventions, allow variations
- Content/metadata: Store as fields on layers, not separate layers
- Clear labeling of authority source for each layer

---

### 7. Surah-Relative Numbering (No Global Ayah Numbering in Mushaf) 🔢

**Principle**: Ayah numbering is ALWAYS relative to its parent Surah. There is no such thing as "Mushaf Ayah numbering."

**Why**:
- Quranic citation convention: "Surah 2, Ayah 255" (not "Ayah #294 of the Quran")
- Surah-relative numbering is the canonical reference system
- When mapping Ayah ↔ Mushaf on numbering level → use Surah-relative number

**Clarifications**:
- ✅ Ayah numbering: Surah-relative (1-286 for Surah 2 in Hafs)
- ✅ Mushaf numbering: Page numbering (Page 1-604)
- ❌ "Mushaf Ayah numbering": Does NOT exist

**May Exist** (to be confirmed):
- Sequential Ayah Number (1-6236 for Hafs, continuous across whole Quran)
- Used for: Quick lookup, indexing, iteration
- NOT for: Citation, scholarly reference

**Implications**:
- Ayah entity has: `surah_id` + `ayah_number_in_surah` (required)
- Ayah entity may have: `sequential_ayah_number` (optional, computed)
- Page Layout layer has: `page_number` (1-604)
- No confusion between Ayah numbering systems

---

### 8. Context Determines Content 🎯

**Principle**: The process is: (1) Establish context (Qiraah/Narration), (2) Get numbering scheme for that context, (3) Get content for that numbering.

**Why**:
- Cannot ask "what is Ayat al-Kursi?" without context
- Must ask "what is Ayah 2:255 in Hafs context?" → retrieve Hafs-specific content
- Different contexts may number same semantic content differently

**Process Flow**:
```
1. User specifies context: "Hafs an Asim"
2. System uses Hafs numbering scheme: Ayah 2:255
3. System retrieves Hafs content for 2:255
4. System returns: Hafs-specific text, words, characters

NOT:
1. User asks for "Ayat al-Kursi" (universal)
2. System finds canonical content
3. System shows "this is 2:255 in Hafs, 2:254 in Warsh"
```

**Implications**:
- All queries are context-aware
- Default context must be specified (e.g., Hafs as most common)
- Cross-context queries are explicit ("compare Hafs vs Warsh")
- Canonical mappings for cross-context identity (canonical_ayah_id)

---

### 9. Separation of Content and Structure 🏗️

**Principle**: Structural/organizational layers are separate from content/metadata attachments.

**Structural Layers** (Full Data Layers):
- Character, Word, Ayah, Surah, Division, Juz, Page, Line, Mushaf, etc.
- Have their own tables, UUIDs, expanded layers, mappings
- Subject to this architectural framework

**Content/Metadata** (Fields on Layers):
- Tajweed rules (field on Character layer)
- Geographic origin (field on various layers)
- Historical context (metadata)
- Scholarly commentary (external content)
- NOT separate layers, just attributes/annotations

**Implementation**:
```
Character Layer:
  character_id (UUID)
  character_letter (string)
  context (string - Qiraah/Narration)
  tajweed_mark (string - field, not separate layer)
  diacritic (string - field or separate layer? TBD)
  [...]

NOT:
TajweedSchool Layer:
  [This would be wrong - Tajweed is content, not structure]
```

**Implications**:
- Focus layer definitions on structural/organizational elements
- Attach content/metadata as fields where appropriate
- Don't over-layer: Not everything needs to be a separate layer

---

### 10. Multi-Version Storage Strategy (TBD) 💾

**Principle**: How to store multiple versions (Hafs, Warsh, Qalun, etc.) is still being determined.

**Option A: Separate Tables per Version**:
```
Characters_Hafs
Characters_Warsh
Characters_Qalun
Words_Hafs
Words_Warsh
Words_Qalun
[...]
```
Pros: Clear separation, optimized per version
Cons: Schema duplication, harder to add new versions

**Option B: Single Table with Context Field**:
```
Characters { id, letter, context: "hafs", ... }
Words { id, text, context: "warsh", ... }
[...]
```
Pros: Unified schema, easy to add versions
Cons: Larger tables, context filtering on every query

**Option C: Hybrid**:
```
Characters { id, letter, base_version, ... }
Character_Variants { id, char_id, context: "warsh", variant_letter, ... }
```
Pros: Normalized, efficient for common data
Cons: More complex queries, join overhead

**Decision Required**:
- Evaluate performance implications
- Consider query patterns
- Balance storage vs query efficiency
- May vary by layer (e.g., Characters separate, Pages unified)

---

## Validation Requirements

### Divine Content (100% Accuracy Required) ✅

- Verse boundaries
- Character counts (323,015 for Hafs - or document authoritative count)
- Verse counts (6,236 Hafs, 6,214 Warsh)
- Text content variations

### Scholarly Content (Document Conventions) 📚

- Division system (Juz/Hizb/Rub)
- Page layouts
- Line breaks
- Tajweed annotation styles

### Cross-Version Consistency 🔄

- Canonical mappings (Hafs Ayah ↔ Warsh Ayah)
- Total layer counts across versions
- Structural invariants (e.g., all versions have 114 Surahs)

---

## Design Patterns

### Pattern 1: Entity + Expanded Layers + Mappings

Every base layer follows this pattern:
```
1. Base Layer (conceptual)
   ↓
2. Expanded Layers (data representations)
   - Layer 1: Primary identifier (UUID)
   - Layer 2: Numbering (integer, ordinal, etc.)
   - Layer 3+: Additional dimensions
   ↓
3. Mappings to Other Layers
   - Mapping Layer A (to parent)
   - Mapping Layer B (to children)
   - Mapping Layer C (to siblings)
   Each mapping has its own expanded structure
```

### Pattern 2: Context-Aware Versioning

Every entity that varies by Qiraah:
```
Entity:
  entity_id (UUID - unique per version)
  canonical_id (UUID - same across versions)
  context (string - which Qiraah/Narration)
  version (semver - schema version)
  [... entity-specific fields]

Cross-Version Mapping:
  canonical_id → [entity_id_hafs, entity_id_warsh, entity_id_qalun, ...]
```

### Pattern 3: Reset Behavior

Numbering fields that reset:
```
Field:
  number (integer)
  parent_id (UUID - what triggers reset)
  reset_behavior (enum: global, resets_per_parent, resets_per_context)

Example:
  Division Quarter:
    number: 1-4
    parent_id: division_id
    reset_behavior: resets_per_parent (each new Division → reset to 1)
```

---

## Anti-Patterns (Avoid These) 🚫

### ❌ Anti-Pattern 1: Nested Data Structures
```json
// DON'T DO THIS:
{
  "ayah": {
    "words": [
      { "characters": ["ب", "س", "م"] }
    ]
  }
}
```
**Why**: Which version of words? Which context? Ambiguous.

### ❌ Anti-Pattern 2: Single Truth Model
```json
// DON'T DO THIS:
{
  "ayah_universal": {
    "content": "...",  // What content? Hafs? Warsh?
    "number_in_hafs": 255,
    "number_in_warsh": 254
  }
}
```
**Why**: No single universal content - each version is independent.

### ❌ Anti-Pattern 3: Simple Foreign Key Mappings
```sql
-- DON'T DO THIS:
Ayah_Word_Mapping (ayah_id, word_id)
```
**Why**: Cannot handle positional info, context, cardinality variations.

### ❌ Anti-Pattern 4: Linear Hierarchy Assumption
```python
# DON'T DO THIS:
def get_parent(layer):
    hierarchy = [Character, Word, Ayah, Surah, Division, Quran]
    return hierarchy[hierarchy.index(layer) + 1]
```
**Why**: Layers have multiple relationships, not single parent.

---

## Open Questions (To Be Resolved) ❓

1. **Complete Layer Taxonomy**: How many total layers? What comes before Character? After Quran?

2. **Storage Strategy**: Separate tables per version, or single table with context field?

3. **Big Mapping Table Structure**: What's the schema for base→expanded layer mappings?

4. **Division vs Juz**: Are these the same layer or different? What's the relationship?

5. **Sequential Ayah Number**: Does this exist as a real layer or just computed index?

6. **Canonical ID Format**: UUID or composite (surah:verse) for canonical_ayah_id?

7. **Character-Level Variations**: What types of character differences exist beyond word-level?

8. **Pre-Character Layers**: What structural layers exist before individual characters?

9. **Post-Quran Layers**: What organizational layers exist beyond the whole Quran?

10. **22 Verse Differences**: What are the specific Surahs where Hafs and Warsh differ in verse count?

---

## References

- Interview Session: 2025-11-09
- Checkpoint Document: `/docs/architecture/interview-checkpoint-2025-11-09.md`
- Interview Guide: `/docs/architecture/layer-definition-interview-guide.md`
- Resume Instructions: `/docs/architecture/RESUME-INTERVIEW-HERE.md`

---

**Status**: v1.0 - Established principles based on initial findings. Will evolve as more layers are defined.

**Next Update**: After completing Layer 5 (Ayah) definition and discovering complete layer taxonomy.
