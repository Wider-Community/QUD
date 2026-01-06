# Data Model Specification

**Research Topic**: Quranic Data Layer Architecture
**Date**: 2025-11-03
**Related Spec**: [spec.md](./spec.md)
**Related Research**: [research.md](./research.md)

## Purpose

This document specifies the data models for the Quranic data layers (currently 17 identified layers). Each layer is defined with:

**NOTE (2025-11-04)**: The exact number of data layers is under investigation and subject to refinement. See spec.md for details on layer count uncertainty.
- Semantic purpose and domain meaning
- Key entities and relationships
- Schema structure (fields, types, constraints) **including UUID identifiers**
- Cross-layer mapping specifications (bidirectional UUIDs, expansion/contraction handling)
- Generation rules (how data is derived)
- Validation requirements

## Current State: QS-QIRAAT Mixed Layer Model

### QS-Verse Record (Flat Schema)

**Source**: QS-QIRAAT Dataset v2.0

**Structure**:
```json
{
  "id": "integer - sequential verse ID",
  "jozz": "integer - Juz number (1-30)",
  "page": "integer - Mushaf page number",
  "sura_no": "integer - Surah number (1-114)",
  "sura_name_en": "string - Surah name in English",
  "sura_name_ar": "string - Surah name in Arabic",
  "line_start": "integer - Starting line number on page",
  "line_end": "integer - Ending line number on page",
  "aya_no": "integer - Verse number within surah",
  "aya_text": "string - Complete verse in Uthmanic script",
  "aya_text_emlaey": "string - Complete verse in standard script"
}
```

**Conflation Problem** (identified in RR-001):
- `jozz` → Layer 9 (Division Structure - Juz/Hizb/Rub)
- `page` → Layer 10 (Page Layout)
- `sura_no`, `sura_name_*` → Layer 6 (Surah Structure)
- `line_start`, `line_end` → Layer 11 (Line Layout)
- `aya_no` → Layer 5 (Verse Structure)
- `aya_text` → Conflates Layers 0, 1, 3, 12a (Character Composition + Symbols/Rendering + Words + Uthmani Script)
- `aya_text_emlaey` → Conflates Layers 0, 3, 12b (Character Composition + Words + Qiasy/Standard Script)

**Impact**: Every verse record repeats page/line/sura metadata (redundancy). Cannot independently query character-level vs word-level vs layout concerns.

## Target State: QUD Multi-Layer Separated Model

### Layer 0: Character Composition

**Purpose**: Base letter sequences with phonetic metadata - the atomic units of Quranic text

**Entity**: `Character`

**Fields**:
- `character_id`: UUID - **Unique identifier for this character instance**
- `narration_ref`: foreign key → Layer 7 (Qiraat Structure) - Which narration this character belongs to
- `verse_ref`: foreign key → Layer 5 (Verse)
- `position`: integer - Character position in verse (0-indexed)
- `base_letter`: string - Single Unicode codepoint for base Arabic letter (no diacritics)
- `phonetic_class`: enum - Letter type (consonant, long vowel, hamza, alif, etc.)
- `tajweed_class`: enum - Tajweed classification (e.g., qalqalah, ghunnah, shamsiyyah, qamariyyah)
- `orthography_type`: enum - Uthmani/Qiasy/Imla'i (which writing system this character follows)

**Cross-Layer Mapping** (UUID-based):
- **→ Layer 1**: Each character maps to its rendering symbols (1:N, multiple diacritics/marks per character)
- **→ Layer 2**: Each character may participate in paired data relationships (1:N, e.g., multiple tajweed pairs)
- **→ Layer 3**: Characters aggregate into words (N:1, many characters per word)
- **→ Layer 12**: Each Uthmani character may map to 1+ Qiasy characters (1:N expansion) or N Qiasy → 1 Uthmani (N:1 contraction)
  - Example expansion: 1 Uthmani "ا" → 2 Qiasy "أ" + "ل" (orthographic transformation with position metadata)
  - Requires `position_metadata` field in EntityMapping to track ordering

**Generation**: Extract from QS-QIRAAT `aya_text` by parsing Unicode codepoints and stripping diacritics

**Validation**:
- Total character count for Hafs narration MUST equal 323,015
- Character counts for other narrations documented and validated
- Only valid Arabic Unicode codepoints (U+0600 to U+06FF range)
- Each character has valid UUID and bidirectional mappings to adjacent layers

---

### Layer 1: Character Symbols and Rendering Data

**Purpose**: Diacritical marks, tajweed symbols, and visual rendering rules for each character

**Entity**: `CharacterSymbol`

**Fields**:
- `symbol_id`: UUID - **Unique identifier for this symbol instance**
- `character_ref`: foreign key → Layer 0 (Character) - The base character this symbol modifies
- `symbol_type`: enum - tashkeel/tajweed/hamza/maddah/tanween
- `symbol_codepoint`: string - Unicode for diacritic (e.g., U+064E for fatha)
- `tajweed_rule`: string - Tajweed rule this symbol represents (if applicable)
- `narration_specific`: boolean - Does this vary by narration?
- `positional_form`: enum - isolated/initial/medial/final (rendering context)
- `ligature_context`: array - Characters involved if ligature (e.g., "لا" lam-alif)
- `font_variant`: string - Font-specific rendering rule (e.g., kfgqpc_hafs_uthmanic_script)

**Cross-Layer Mapping** (UUID-based):
- **← Layer 0**: Maps from base character (N:1, multiple symbols per character)
- **→ Layer 2**: Symbols may participate in paired relationships (e.g., sukun + shadda)
- **→ Layer 12**: Rendering rules differ between Uthmani and Qiasy scripts (1:1 or 1:N mappings)

**Generation**:
- **GENERATIVE HYPOTHESIS (RR-003)**: Can be generated from Layer 0 + Layer 7 Qiraah rules
- Extraction from QS-QIRAAT `aya_text` as baseline
- Rule-based generation tested against extracted baseline

**Validation**:
- Generated symbols MUST match QS-QIRAAT symbols >95% accuracy
- Mismatches reviewed by domain expert
- Scholarly review confirms theological accuracy
- Each symbol has valid UUID and bidirectional mapping to Layer 0 character

---

### Layer 2: Character Paired Data

**Purpose**: Relational metadata between characters (tajweed rules requiring context, idgham relationships, etc.)

**Entity**: `CharacterPair`

**Fields**:
- `pair_id`: UUID - **Unique identifier for this pair relationship**
- `character_1_ref`: foreign key → Layer 0 (Character) - First character in relationship
- `character_2_ref`: foreign key → Layer 0 (Character) - Second character in relationship
- `pair_type`: enum - idgham/ikhfa/qalb/izhar/iqlab/madd/etc.
- `tajweed_rule`: string - Specific tajweed rule governing this pair
- `phonetic_transformation`: string - How pronunciation changes due to pairing
- `narration_specific`: boolean - Does this pairing vary by narration?

**Cross-Layer Mapping** (UUID-based):
- **← Layer 0**: Maps from two characters (2:1, pair relates two character UUIDs)
- **← Layer 1**: May reference specific symbols that trigger the pairing rule
- **→ Layer 3**: Paired data influences word-level tajweed analysis

**Generation**: Analyze Layer 0 character sequences using tajweed rule engine

**Validation**:
- Pair relationships must reference valid character UUIDs from Layer 0
- Tajweed rules cross-referenced with scholarly sources
- Each pair has bidirectional mappings to source characters

---

### Layer 3: Word Structure

**Purpose**: Word boundaries and morphological composition

**Entity**: `Word`

**Fields**:
- `word_id`: UUID - **Unique identifier for this word instance**
- `verse_ref`: foreign key → Layer 5 (Verse)
- `word_position`: integer - Word index in verse (0-indexed)
- `character_range`: array - [start_pos, end_pos] referencing Layer 0 character positions
- `character_refs`: array - UUIDs of Layer 0 characters composing this word
- `morphology`: object - Root, pattern, affixes (if analyzed)
- `word_count_contribution`: integer - Usually 1, may be 0 for aya marks
- `word_type`: enum - noun/verb/particle/etc.

**Cross-Layer Mapping** (UUID-based):
- **← Layer 0**: Aggregates multiple character UUIDs (N:1, many characters per word)
- **← Layer 1**: References symbols for complete word rendering
- **← Layer 2**: May incorporate paired data for intra-word tajweed
- **→ Layer 4**: Words aggregate into sentences (N:1, many words per sentence)
- **→ Layer 5**: Words contained within verses

**Generation**: Word segmentation algorithm on Layer 0 characters using whitespace/zero-width delimiters

**Validation**:
- Total word count for Hafs MUST match authoritative sources (expected ~77,429 words)
- Word boundaries match QS-QIRAAT whitespace
- Each word has valid UUID and bidirectional mappings to constituent characters

---

### Layer 4: Sentence Structure

**Purpose**: Grammatical composition, waqf (stopping) rules, ibtida (starting) rules

**Entity**: `Sentence`

**Fields**:
- `sentence_id`: UUID - **Unique identifier for this sentence instance**
- `verse_ref`: foreign key → Layer 5 (Verse)
- `word_range`: array - [start_word, end_word] referencing Layer 3 word positions
- `word_refs`: array - UUIDs of Layer 3 words composing this sentence
- `grammar_type`: enum - nominal/verbal/conditional/interrogative/etc.
- `waqf_rule`: enum - Must stop/permitted stop/continue/not permitted
- `ibtida_rule`: enum - Permitted start/not permitted/etc.
- `sentence_position`: integer - Sentence index within verse

**Cross-Layer Mapping** (UUID-based):
- **← Layer 3**: Aggregates multiple word UUIDs (N:1, many words per sentence)
- **→ Layer 5**: Sentences contained within verses
- May span partial verses or multiple verses depending on grammar

**Generation**: **MISSING from QS-QIRAAT** - Requires external linguistic database or manual encoding

**Validation**:
- Cross-reference with Quranic grammar references (e.g., "الجدول في إعراب القرآن")
- Each sentence has valid UUID and bidirectional mappings to constituent words

**Note**: This layer is OUT OF SCOPE for initial research (RR-001, RR-002, RR-003) due to missing source data

---

### Layer 5: Verse Structure

**Purpose**: Verse enumeration and boundaries - the primary organizational unit of the Quran

**Entity**: `Verse`

**Fields**:
- `verse_id`: UUID - **Unique identifier for this verse instance within a specific narration**
- `canonical_verse_id`: UUID - **CRITICAL: Canonical identity independent of narration** (solves verse numbering controversy)
- `narration_ref`: foreign key → Layer 7 (Qiraat Structure)
- `sura_ref`: foreign key → Layer 6 (Surah)
- `verse_number`: integer - Verse number within surah (position-based, varies by narration)
- `verse_number_alt`: object - Alternative numbering schemes (if differs across narrations)
- `start_character_ref`: foreign key → Layer 0 (first character UUID)
- `end_character_ref`: foreign key → Layer 0 (last character UUID)
- `character_count`: integer - Total characters in this verse
- `word_count`: integer - Total words in this verse

**Cross-Layer Mapping** (UUID-based):
- **← Layers 0-4**: Contains characters, symbols, pairs, words, sentences
- **→ Layer 6**: Contained within surah (N:1, many verses per surah)
- **→ Layers 10-11**: Referenced by page and line layout
- **Cross-Recitation Mapping** (CRITICAL for RR-011, RR-012):
  - `canonical_verse_id` enables mapping 1 Hafs verse ↔ 2 Warsh verses (verse boundary variation)
  - Example: Hafs verse 2:285 may split into Warsh verses 2:285 and 2:286
  - Requires EntityMapping with cardinality 1:N or N:1 and `position_metadata`

**Generation**: Direct extraction from QS-QIRAAT `aya_no` field

**Validation**:
- Total verse count per narration MUST match:
  - Hafs: 6,236 verses
  - Warsh: 6,214 verses
  - Document other narrations
- Verse numbering differences across narrations are CORE REQUIREMENTS
- Each verse has both `verse_id` (Qiraah-specific) and `canonical_verse_id` (cross-Qiraah identity)
- Bidirectional mappings to constituent entities and parent surah

---

### Layer 6: Surah Structure

**Purpose**: Chapter metadata and organization

**Entity**: `Surah`

**Fields**:
- `surah_id`: UUID - **Unique identifier for this surah**
- `surah_number`: integer - Surah number (1-114)
- `surah_name_ar`: string - Arabic name (e.g., "الفاتحة")
- `surah_name_en`: string - English transliteration (e.g., "Al-Fatiha")
- `surah_name_translation`: string - Meaning in English (e.g., "The Opening")
- `revelation_type`: enum - Makki/Madani
- `verse_count`: integer - Total verses in this surah (may vary by narration)
- `verse_count_by_narration`: object - {narration_id: count} for variant counts
- `revelation_order`: integer - Chronological revelation sequence
- `themes`: array - Topical themes (optional enrichment)

**Cross-Layer Mapping** (UUID-based):
- **← Layer 5**: Contains multiple verse UUIDs (1:N, one surah contains many verses)
- **→ Layer 8**: Contained within mushaf organization
- Same metadata across all narrations (except verse_count may differ)

**Generation**: Extract from QS-QIRAAT `sura_no`, `sura_name_*` fields, enrich with external metadata

**Validation**:
- 114 chapters for all narrations
- Verse counts per chapter match authoritative sources
- Makki/Madani classification matches traditional sources
- Each surah has valid UUID and bidirectional mappings to verses

---

### Layer 7: Qiraat Structure

**Purpose**: Foundational metadata for Qiraat systems (القراءات العشر)

**Entity**: `Narration`

**Fields**:
- `narration_id`: UUID - **Unique identifier for this narration**
- `reader_name_ar`: string - Reader (narrator) name in Arabic (e.g., "حفص")
- `reader_name_en`: string - Reader (narrator) name transliterated (e.g., "Hafs")
- `narrator_name_ar`: string - Imam (Qari) name in Arabic (e.g., "عاصم")
- `narrator_name_en`: string - Imam (Qari) transliterated (e.g., "Asim")
- `full_name`: string - Combined narration (e.g., "حفص عن عاصم" / "Hafs 'an 'Asim")
- `qiraah_rules`: object - Tajweed rules specific to this narration
- `canonical_category`: enum - One of 10 canonical Qiraat (العشر) or additional
- `source_authority`: string - Reference to isnad chain/scholarly source

**Cross-Layer Mapping** (UUID-based):
- **→ Layer 0**: Each character instance references its narration
- **→ Layer 1**: Symbol rules vary by narration
- **→ Layer 5**: Verse structure and boundaries may vary by narration
- **→ Layer 8**: Each mushaf instance references its narration

**Generation**: Manual encoding from authenticated scholarly sources (Ibn al-Jazari's "النشر في القراءات العشر")

**Validation**:
- Cross-reference with established Quranic scholarship
- Verify narration names match QS-QIRAAT conventions
- Each narration has valid UUID

---

### Layer 8: Mushaf Structure

**Purpose**: Complete manuscript text for each narration

**Entity**: `Mushaf`

**Fields**:
- `mushaf_id`: UUID - **Unique identifier for this mushaf instance**
- `narration_ref`: foreign key → Layer 7 (Qiraat Structure)
- `edition_ref`: foreign key → Layer 13 (Edition Variants - optional)
- `composition_rules`: object - How layers 0-7 are composed for this mushaf
- `complete_text`: text - Full Quran text in this narration (derived from layers)
- `provenance`: string - Source authority (e.g., "King Fahd Complex Hafs v2.0")
- `total_verses`: integer - Total verse count for this mushaf/narration
- `total_characters`: integer - Total character count

**Cross-Layer Mapping** (UUID-based):
- **← Layer 7**: References narration
- **← Layers 0-6**: Composed from all lower layers specific to narration
- **→ Layers 9-11**: Has organizational and layout structure

**Generation**: Composition of Layers 0-6 specific to narration

**Validation**:
- Character count and verse count match Qiraah-specific requirements
- Each mushaf has valid UUID and references to all constituent layers

---

### Layer 9: Division Structure (Juz, Hizb, Rub)

**Purpose**: Traditional organizational segments for recitation scheduling

**Entity**: `Division`

**Fields**:
- `division_id`: UUID - **Unique identifier for this division**
- `mushaf_ref`: foreign key → Layer 8 (Mushaf)
- `division_type`: enum - juz/hizb/rub/quarter
- `division_number`: integer - Sequential number within type (1-30 for juz, 1-60 for hizb, etc.)
- `start_verse_ref`: foreign key → Layer 5 (Verse UUID)
- `end_verse_ref`: foreign key → Layer 5 (Verse UUID - optional, if known)
- `start_character_position`: integer - Character offset within start verse (for mid-verse divisions)
- `narration_specific`: boolean - Do division boundaries vary by narration?

**Cross-Layer Mapping** (UUID-based):
- **← Layer 8**: Each division belongs to a mushaf
- **→ Layer 5**: References verse boundaries via UUIDs
- Independent of page/line layout (Layers 10-11)

**Generation**: Extract from QS-QIRAAT `jozz` field + aya_text hizb symbols (ﭖ ﭗ ﭘ)

**Validation**:
- 30 Juz for all narrations
- Verify hizb/rub symbols match traditional divisions
- Each division has valid UUID and bidirectional mappings to verses

---

### Layer 10: Page Layout

**Purpose**: Page-level composition and pagination

**Entity**: `Page`

**Fields**:
- `page_id`: UUID - **Unique identifier for this page**
- `mushaf_ref`: foreign key → Layer 8 (Mushaf)
- `page_number`: integer - Page number in mushaf
- `start_verse_ref`: foreign key → Layer 5 (Verse UUID)
- `end_verse_ref`: foreign key → Layer 5 (Verse UUID)
- `start_character_ref`: foreign key → Layer 0 (Character UUID - if page starts mid-verse)
- `end_character_ref`: foreign key → Layer 0 (Character UUID - if page ends mid-verse)
- `line_count`: integer - Lines per page (typically 15)

**Cross-Layer Mapping** (UUID-based):
- **← Layer 8**: Each page belongs to a mushaf
- **→ Layer 5**: Cross-references verse UUIDs
- **→ Layer 11**: Contains line UUIDs (1:N, one page contains many lines)

**Generation**: Extract from QS-QIRAAT `page` field, normalize (currently repeated per verse)

**Validation**:
- Page breaks match QS-QIRAAT page field
- Each page has valid UUID and bidirectional mappings to verses and lines

---

### Layer 11: Line Layout

**Purpose**: Line-level composition and line breaks

**Entity**: `Line`

**Fields**:
- `line_id`: UUID - **Unique identifier for this line**
- `page_ref`: foreign key → Layer 10 (Page UUID)
- `line_number`: integer - Line number on page (1-15 typically)
- `start_verse_ref`: foreign key → Layer 5 (Verse UUID - or character ref for mid-verse breaks)
- `end_verse_ref`: foreign key → Layer 5 (Verse UUID)
- `start_character_ref`: foreign key → Layer 0 (Character UUID - if line starts mid-verse)
- `end_character_ref`: foreign key → Layer 0 (Character UUID - if line ends mid-verse)

**Cross-Layer Mapping** (UUID-based):
- **← Layer 10**: Contained within page (N:1, many lines per page)
- **→ Layer 5**: References verse UUIDs
- **→ Layer 0**: References character UUIDs for mid-verse breaks

**Generation**: Extract from QS-QIRAAT `line_start`, `line_end` fields, normalize

**Validation**:
- Line breaks match QS-QIRAAT line fields
- Each line has valid UUID and bidirectional mappings to page, verses, and characters

---

### Layer 12: Orthographic Systems

**Purpose**: Writing system rules (Uthmani vs Qiasy/Imla'i) - CRITICAL for RR-013 expansion/contraction mapping

#### Layer 12a: Uthmani Script

**Entity**: `UthmanicOrthography`

**Fields**:
- `orthography_id`: UUID - **Unique identifier for this Uthmani text instance**
- `verse_ref`: foreign key → Layer 5 (Verse UUID)
- `uthmanic_text`: string - Rendered text using Rasm Uthmani rules
- `character_refs`: array - UUIDs of Layer 0 characters composing this text
- `symbol_refs`: array - UUIDs of Layer 1 symbols
- `script_rules`: object - Specific Uthmanic orthographic rules applied

**Cross-Layer Mapping** (UUID-based):
- **← Layer 0**: Composes character UUIDs
- **← Layer 1**: Composes symbol UUIDs
- **→ Layer 12b**: Transforms to Qiasy/Imla'i script with expansion/contraction mappings
  - **CRITICAL**: 1 Uthmani character may → 2 Qiasy characters (expansion, e.g., "الصلوة" → "الصلاة")
  - **CRITICAL**: 2 Uthmani characters may → 1 Qiasy character (contraction)
  - Requires EntityMapping with `position_metadata` for character ordering

**Generation**: Composition from Layers 0+1

**Validation**:
- MUST match QS-QIRAAT `aya_text` exactly (byte-for-byte Unicode)
- Each orthography instance has valid UUID and character mappings

#### Layer 12b: Qiasy/Imla'i Script

**Entity**: `QiasyOrthography`

**Fields**:
- `orthography_id`: UUID - **Unique identifier for this Qiasy text instance**
- `verse_ref`: foreign key → Layer 5 (Verse UUID)
- `qiasy_text`: string - Rendered text using modern standard orthography
- `transformation_rules`: object - Uthmani→Qiasy rules applied
- `character_mapping_refs`: array - EntityMapping UUIDs showing Uthmani↔Qiasy character correspondences

**Cross-Layer Mapping** (UUID-based):
- **← Layer 12a**: Derived from Uthmani via transformation rules
  - **Expansion Example**: 1 Uthmani char "و" (UUID-A) → 2 Qiasy chars "و" (UUID-B) + "ة" (UUID-C)
  - EntityMapping: {source: UUID-A, targets: [UUID-B, UUID-C], cardinality: "1:N", position_metadata: {UUID-B: 0, UUID-C: 1}}
- Corresponds to QS-QIRAAT `aya_text_emlaey`

**Generation**: Transform Layer 12a using orthographic rules (e.g., الصلوة → الصلاة)

**Validation**:
- Match QS-QIRAAT `aya_text_emlaey`
- All character mappings have valid UUIDs and position metadata

---

### Layer 13: Edition Variants

**Purpose**: Publisher-specific formatting differences

**Entity**: `Edition`

**Fields**:
- `edition_id`: UUID - **Unique identifier for this edition**
- `publisher`: string - Publishing house (e.g., "King Fahd Complex")
- `edition_name`: string - Specific edition name
- `publication_date`: date
- `formatting_rules`: object - Edition-specific layout preferences
- `narration_ref`: foreign key → Layer 7 (Qiraat Structure - optional if edition-specific)

**Cross-Layer Mapping** (UUID-based):
- **→ Layer 8**: Referenced by mushaf instances (editions determine layout)
- **→ Layers 10-11**: Determines page/line layout specifications

**Generation**: **Implicit in QS-QIRAAT** (assumes King Fahd Complex formatting) - extract when comparing multiple editions

**Validation**:
- Document edition differences when found
- Each edition has valid UUID

---

### Layer 14: Readers and Narrators

**Purpose**: Biographical data for readers and narrators (القراء والرواة)

**Entity**: `Reader`

**Fields**:
- `reader_id`: UUID - **Unique identifier for this reader**
- `name_ar`: string - Arabic name
- `name_en`: string - Transliteration
- `birth_year_hijri`: integer (nullable)
- `death_year_hijri`: integer (nullable)
- `biography`: text - Brief biographical information
- `isnad_chain`: array - Transmission chain to Prophet Muhammad (PBUH)
- `canonical_rank`: enum - One of 10 canonical/additional
- `geographical_origin`: string - Place of origin/school

**Cross-Layer Mapping** (UUID-based):
- **→ Layer 7**: Referenced by narration definitions
- Has narrators (self-referential for narrator biographical data)

**Generation**: **MISSING from QS-QIRAAT** - Requires external scholarly databases (e.g., biographical dictionaries of Quranic readers)

**Validation**:
- Cross-reference with established Islamic scholarship sources
- Each reader has valid UUID

**Note**: OUT OF SCOPE for initial research (RR-001, RR-002, RR-003) due to missing source data

---

## Cross-Layer Relationships (UUID-Based)

```
Layer 7 (Qiraat Structure) ────informs────> Layer 0 (Characters)
                               └───informs────> Layer 1 (Symbols)
                               └───defines────> Layer 5 (Verses)
                               └───defines────> Layer 8 (Mushaf)

Layer 0 (Characters) ───aggregates (N:1)───> Layer 3 (Words)
                     └───maps (1:N)────────> Layer 1 (Symbols)
                     └───maps (1:N)────────> Layer 2 (Pairs)
                     └───maps (1:N or N:1)─> Layer 12 (Orthographic transformation)

Layer 1 (Symbols) ───participates in───> Layer 2 (Pairs)
                  └───composes────────> Layer 12a (Uthmani)

Layer 3 (Words) ───aggregates (N:1)───> Layer 4 (Sentences)
                └───contained in (N:1)─> Layer 5 (Verses)

Layer 5 (Verses) ───contains────> Layers 0-4
                 └───aggregates (N:1)──> Layer 6 (Surahs)
                 └───referenced by─────> Layers 9, 10, 11 (Divisions, Pages, Lines)
                 └───cross-Qiraah──> canonical_verse_id (1:N or N:1 mapping)

Layer 6 (Surahs) ───contains (1:N)───> Layer 5 (Verses)
                 └───contained in────> Layer 8 (Mushaf)

Layers 0+1 ───compose (via UUIDs)───> Layer 12a (Uthmani Script)
Layer 12a ───transforms (with UUID mapping)───> Layer 12b (Qiasy Script)

Layers 0-7 ───compose (via UUIDs)───> Layer 8 (Mushaf)
Layer 8 ───has organizational structure───> Layer 9 (Divisions)
        └───has layout structure──────────> Layers 10-11 (Pages, Lines)

Layer 13 (Editions) ───determines formatting for───> Layers 10-11
Layer 14 (Readers/Narrators) ───referenced by───> Layer 7
```

**UUID Mapping Types**:
- **1:1** - One-to-one (e.g., one symbol to one character in some cases)
- **1:N** - One-to-many expansion (e.g., 1 Uthmani char → 2 Qiasy chars, 1 Hafs verse → 2 Warsh verses)
- **N:1** - Many-to-one aggregation (e.g., many characters per word, many words per verse)
- **N:M** - Many-to-many (e.g., complex orthographic transformations)

All mappings use EntityMapping structure with `position_metadata` for ordering preservation.

## Schema Conformance Requirements

For each layer, generated data MUST:
1. **Type Conformance**: All fields match declared types in JSON Schema / Pydantic model
2. **Constraint Satisfaction**: Required fields present, value ranges respected (e.g., verse_number > 0)
3. **Referential Integrity**: Foreign keys reference existing entities via UUIDs
4. **UUID Validity**: Every entity has a valid UUID field that is:
   - Unique within its layer
   - Properly formatted (UUID v4 or v5)
   - Bidirectionally mapped to related entities in adjacent layers
5. **Cross-Layer Mapping Integrity**: All EntityMapping instances must:
   - Reference valid source and target UUIDs
   - Have correct cardinality labels (1:1, 1:N, N:1, N:M)
   - Include `position_metadata` for expansion/contraction cases
   - Include `semantic_hash` for relationship representation
   - Have bidirectional references (forward and reverse mappings)
6. **Invariant Preservation**: Domain-specific rules hold:
   - Sum of verse counts per chapter equals total verse count per narration
   - Character count matches authoritative sources
   - No orphaned references (e.g., verse without chapter)
   - All cross-Qiraah canonical_verse_id mappings are valid

## Redundancy Reduction Analysis

**QS-QIRAAT Redundancy** (6,236 Hafs verses):
- Page number repeated ~25 times per page (25 verses/page average) = ~249 redundant page entries
- Sura metadata repeated per verse = ~6,236 redundant sura records
- Line layout repeated per verse on same line = ~416 redundant line records (15 verses/line average)

**QUD Normalized Storage**:
- Page: 604 unique records (Hafs mushaf pages)
- Sura: 114 unique records
- Line: ~9,060 unique records (604 pages × 15 lines)

**Estimated Redundancy Reduction**: >40% (hypothesis to validate in RR-003)

## Contextual Versioning Architecture

### The Multi-Layer Versioning Problem

**CRITICAL INSIGHT**: The versioning controversy is NOT limited to verse numbering - it affects ALL data layers (currently 17 identified layers). Each layer can have different content versions determined by a set of contextual parameters.

**Examples of Context-Dependent Layer Versions**:
- **Layer 0 (Character Composition)**: Different character sets for Hafs vs Warsh pronunciation
- **Layer 1 (Symbols/Rendering)**: Different diacritics across scholarly traditions
- **Layer 2 (Character Paired Data)**: Different tajweed pair rules across tajweed schools
- **Layer 5 (Verse Structure)**: Different verse numbering (Hafs 6,236 vs Warsh 6,214)
- **Layer 12 (Orthographic Systems)**: Uthmani vs Qiasy script representations
- **Layers 6-14**: Contextual variations in higher organizational layers

### Context Schema (HYPOTHETICAL - TO BE VALIDATED IN RR-014)

**Entity**: `Context`

**Purpose**: Defines a set of parameters that collectively determine which version of each layer to use.

**Structure** (SAMPLE - actual parameters validated through RR-014 research):

```json
{
  "context_id": "UUID",
  "narration": "hafs | warsh | qaloun | ...",
  "orthographic_system": "uthmani | qiasy | imla'i",
  "edition": "king_fahd_complex | ...",
  "tajweed_school": "al_jazari | ibn_kathir | ...",
  "scholarly_tradition": "...",
  "geographic_origin": "medina | kufa | basra | ...",
  "time_period": "classical | modern",
  "custom_parameters": {}
}
```

**Fields**:
- `context_id`: UUID - Unique identifier for this context configuration
- `narration`: Enum - Which of the 10 canonical Qiraat (القراءات العشر)
- `orthographic_system`: Enum - Script system (Uthmani vs modernized)
- `edition`: String - Publisher/edition identifier
- `tajweed_school`: Enum - Which tajweed tradition (affects Layers 1-2)
- `scholarly_tradition`: String - Broader scholarly tradition context
- `geographic_origin`: Enum - Geographic origin of tradition (may affect Qiraah rules)
- `time_period`: Enum - Historical vs contemporary encoding
- `custom_parameters`: Object - Extensibility for discovered parameters

**Research Questions** (RR-014 MUST RESOLVE):
- Which parameters are mandatory vs optional?
- Valid enumeration values for each parameter?
- Parameter dependencies (e.g., does tajweed_school depend on geographic_origin)?
- Which parameters affect which layers (context inheritance rules)?
- Minimal context set for unambiguous layer version resolution?

**Context Inheritance Rules** (HYPOTHETICAL):
- **Global Parameters** (apply to all layers): `narration`, `edition`
- **Layer-Specific Parameters**:
  - Layers 0-2: Affected by `narration`, `orthographic_system`, `tajweed_school`
  - Layer 5: Affected by `narration` (verse count differences)
  - Layer 12: Determined by `orthographic_system`
  - Layers 11-12: Affected by `edition` (layout variations)

### LayerVersion Entity (HYPOTHETICAL META-SCHEMA - TO BE VALIDATED IN RR-015)

**Entity**: `LayerVersion`

**Purpose**: Metadata about a specific version of a specific layer under a specific context.

**Structure** (SAMPLE - actual schema validated through RR-015 research):

```json
{
  "layer_version_id": "UUID",
  "layer_number": "integer (0-14)",
  "context_parameters": {
    "narration": "hafs",
    "orthographic_system": "uthmani",
    "edition": "king_fahd_complex"
  },
  "version_semver": "1.0.0",
  "entity_count": "integer",
  "parent_version_id": "UUID | null",
  "generation_rules": "reference to rules that generated this version",
  "validation_status": {
    "character_count": 323015,
    "verse_count": 6236,
    "schema_validation": "pass | fail",
    "scholarly_review": "approved | pending | rejected"
  },
  "provenance": {
    "source_dataset": "QS-QIRAAT-v2.0",
    "transformation_pipeline": "...",
    "created_timestamp": "ISO-8601",
    "created_by": "researcher_id"
  },
  "storage_location": "path or URI to actual layer data"
}
```

**Fields**:
- `layer_version_id`: UUID - Unique identifier for this layer version
- `layer_number`: Integer (0-14) - Which layer this version belongs to
- `context_parameters`: Object - Subset of Context parameters relevant to this layer
- `version_semver`: String - Semantic version (1.0.0) for schema evolution tracking
- `entity_count`: Integer - Number of entities in this layer version (e.g., 323,015 characters, 6,236 verses)
- `parent_version_id`: UUID - If derived from another version (version lineage)
- `generation_rules`: String/Reference - Which rules generated this version
- `validation_status`: Object - Validation metrics specific to this layer/context
- `provenance`: Object - Source attribution, transformation tracking
- `storage_location`: String - Where the actual layer data is stored

**Example Instances**:

1. **Layer 0, Hafs Recitation, Uthmani Script**:
```json
{
  "layer_version_id": "550e8400-...",
  "layer_number": 0,
  "context_parameters": {
    "narration": "hafs",
    "orthographic_system": "uthmani"
  },
  "entity_count": 323015,
  "validation_status": {
    "character_count": 323015,
    "schema_validation": "pass"
  }
}
```

2. **Layer 5, Warsh Recitation**:
```json
{
  "layer_version_id": "660e8400-...",
  "layer_number": 5,
  "context_parameters": {
    "narration": "warsh"
  },
  "entity_count": 6214,
  "validation_status": {
    "verse_count": 6214,
    "schema_validation": "pass"
  }
}
```

**Research Questions** (RR-015 MUST RESOLVE):
- Optimal indexing strategy for querying by context_parameters?
- Is parent_version_id lineage tracking useful or over-engineered?
- Granularity of validation_status (per-entity vs per-version)?
- How to handle schema evolution (context_parameters structure changes)?
- Should storage_location be embedded or referenced separately?

## MUDMAJ Storage Organization

### MUDMAJ Architecture

**MUDMAJ (المدمج - "The Merged")**: The underlying database containing all interconnected and interrelated versions of the Quranic dataset with proper layer information.

**Core Principles**:
1. **Multi-Version Storage**: ALL identified layers (currently 17) stored in multiple versions per context
2. **Delta Optimization**: Shared immutable data across contexts, only deltas stored
3. **Cross-Context Mapping**: Canonical identities linking equivalent entities across contexts
4. **Provenance Tracking**: Complete audit trail for all layer versions
5. **Query Efficiency**: Indexed for rapid context-based queries

### Storage Schema (HYPOTHETICAL - TO BE VALIDATED IN RR-015)

**Directory/Table Organization** (SAMPLE - actual structure depends on storage technology choice):

```
MUDMAJ/
├── layer_versions/
│   ├── layer_00_character_composition/
│   │   ├── hafs_uthmani_v1-0-0/           # Version: Hafs + Uthmani
│   │   ├── hafs_qiasy_v1-0-0/             # Version: Hafs + Qiasy
│   │   ├── warsh_uthmani_v1-0-0/          # Version: Warsh + Uthmani
│   │   └── warsh_qiasy_v1-0-0/            # Version: Warsh + Qiasy
│   ├── layer_05_verse_structure/
│   │   ├── hafs_v1-0-0/                   # 6,236 verses
│   │   └── warsh_v1-0-0/                  # 6,214 verses
│   └── [... all layers with context-specific versions]
│
├── cross_layer_mappings/
│   ├── entity_mappings/                   # EntityMapping structures
│   ├── canonical_identities/              # canonical_verse_id, etc.
│   └── semantic_hashes/                   # SHA-256 relationship hashes
│
├── context_metadata/
│   ├── context_definitions/               # Valid Context instances
│   ├── version_registry/                  # LayerVersion catalog
│   ├── resolution_rules/                  # Context resolution algorithms
│   └── parameter_constraints/             # Valid parameter combinations
│
├── provenance/
│   ├── transformation_logs/               # Generation history per version
│   ├── validation_results/                # Character/verse counts per version
│   ├── scholarly_reviews/                 # Expert validation per version
│   └── source_attribution/                # Original dataset references
│
└── delta_storage/                         # HYPOTHETICAL: Shared immutable data
    ├── shared_entities/                   # Entities identical across contexts
    └── context_deltas/                    # Only differences stored
```

**Research Questions** (RR-015 MUST RESOLVE):
- Storage technology: SQL (PostgreSQL), NoSQL (MongoDB), Graph DB (Neo4j), or hybrid?
- Indexing strategy: Which fields to index for context-based queries?
- Delta storage mechanism: How to identify shared vs context-specific data?
- Version naming convention: Deterministic hash vs semantic naming?
- Canonical identities: Stored separately or embedded in entities?
- Provenance granularity: Per-entity, per-version, or per-layer?

### Version Registry

**Purpose**: Catalog of all layer versions and their contexts, enabling the QUD Orchestrator to resolve context → layer version mappings.

**Entity**: `VersionRegistryEntry`

**Structure** (HYPOTHETICAL):

```json
{
  "registry_id": "UUID",
  "layer_number": "integer (0-14)",
  "context_hash": "SHA-256 hash of context_parameters",
  "context_parameters": {
    "narration": "hafs",
    "orthographic_system": "uthmani"
  },
  "layer_version_ref": "UUID reference to LayerVersion entity",
  "priority": "integer - for conflict resolution",
  "active": "boolean - is this version currently in use?",
  "created_timestamp": "ISO-8601"
}
```

**Indexing Requirements**:
- Primary index: `(layer_number, context_hash)` for O(1) lookups
- Secondary index: `layer_version_ref` for reverse lookups
- Filter index: `active = true` for production queries

**Query Pattern Example**:

```
Query: Get Layer 5 (Verse) for context {narration: hafs, edition: king_fahd_complex}

1. Hash context parameters → context_hash
2. Lookup VersionRegistry: WHERE layer_number = 5 AND context_hash = <hash>
3. Retrieve layer_version_ref
4. Query layer_versions/layer_05_verse_structure/<version>/
```

### Delta Storage Strategy (HYPOTHETICAL - TO BE VALIDATED)

**Hypothesis**: Many layer versions share substantial data. Example:
- Layer 6 (Surah metadata) is 99% identical across narrations
- Layer 8 (Chapter structure) is fully identical across orthographic systems
- Layer 11-12 (Page/line layout) varies by edition but shares structure

**Proposed Delta Storage**:
1. **Identify Immutable Entities**: Entities that never change across contexts
2. **Reference Counting**: Track which contexts reference each shared entity
3. **Delta Records**: Store only differences for context-specific versions
4. **Reconstruction**: Generate full layer version by combining base + deltas

**Storage Savings Example** (HYPOTHETICAL - Phase 2-3 Target):

Without delta storage (eventual system with all narrations after Phase 2-3):
- 7 narrations × 17 layers × ~10,000 entities/layer = ~1,190,000 entity records (approximate)

With delta storage:
- Base entities: ~300,000 (immutable shared entities)
- Delta entities: ~750,000 × 20% (only differences) = ~150,000
- **Total**: ~450,000 entity records
- **Savings**: ~57% storage reduction

**NOTE**: Phase 1 (per Constitution VI) validates with Hafs and Warsh only (2 narrations, ~300,000 entities). Phase 2-3 scales to all narrations.

**RR-015 MUST VALIDATE**: Are these savings realistic? What is actual overlap? Phase 1 validates with 2 narrations first.

### Cross-Context Canonical Identities

**Purpose**: Link semantically equivalent entities across different contexts.

**Example**: "Verse 2:255 (Ayat al-Kursi)" is the same verse across:
- Hafs narration (verse 255)
- Warsh narration (verse 254 due to different verse boundaries)
- Uthmani script version
- Qiasy script version

**Entity**: `CanonicalIdentity`

**Structure**:

```json
{
  "canonical_id": "UUID",
  "entity_type": "verse | character | word | surah | ...",
  "canonical_name": "human-readable reference (e.g., 'ayat-al-kursi')",
  "context_instances": [
    {
      "context_id": "UUID",
      "layer_number": 5,
      "entity_uuid": "UUID - verse in Hafs context",
      "positional_id": "2:255"
    },
    {
      "context_id": "UUID",
      "layer_number": 5,
      "entity_uuid": "UUID - same verse in Warsh context",
      "positional_id": "2:254"
    }
  ]
}
```

**Use Case**: Enables queries like:
- "Find Ayat al-Kursi in Warsh narration" (resolves verse numbering controversy)
- "Compare orthographic representations of the same verse"
- "Track verse identity across all contexts"

## Next Steps

- **RR-001**: Validate this model against QS-QIRAAT actual data (mapping exercise)
- **RR-002**: Implement JSON Schema + Pydantic models for each layer with UUID fields and EntityMapping schema
- **RR-003**: Build transformation prototype and measure actual redundancy reduction
- **RR-011**: Implement and validate UUID-based cross-layer mapping system
- **RR-012**: Validate multi-layer contextual versioning (ALL layers can have context-specific versions)
- **RR-013**: Validate character-level UUID mappings for orthographic transformations (Uthmani↔Qiasy expansion/contraction cases)
- **RR-014**: Design and validate QUD Orchestrator (context resolution, query routing, version selection)
- **RR-015**: Design and validate MUDMAJ storage schema (multi-version storage, delta optimization, provenance tracking)
- **RR-016**: Validate context-aware query system (single-context queries, cross-context comparisons, context isolation)
