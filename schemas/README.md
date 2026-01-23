# QUD Quranic Data Layer Schemas

**Date**: 2025-01-23
**Project**: QUD

## Table of Contents

- [Related Files](#related-files)
- [Overview](#overview)
- [Directory Structure](#directory-structure)
- [Layer Architecture](#layer-architecture)
- [Cross-Layer Mappings](#cross-layer-mappings)
- [Architecture Principles](#architecture-principles)
- [Schema Format](#schema-format)
- [UUID Generation](#uuid-generation)
- [Schema Evolution](#schema-evolution)
- [Research Requirements](#research-requirements)

---

## Related Files

- **Quran Datasets**: `/data/QS - QIRAAT`
- **Specification**: `/specs/001-quranic-layer-architecture/spec.md` - Detailed specifications
- **Architecture Principles**: `/docs/architecture/architectural-principles.md` - 10 Architectural principles
- **Experiment Design**: `/specs/001-quranic-layer-architecture/experiment-design.md` -  RR-002: Schema Design Section
- **Data Model**: `/specs/001-quranic-layer-architecture/data-model.md` - Details for every layer, context layer, MUDMAJ storage
- **Research Tools**: `/research-tools/README.md` - Reusable utilities for data loading, validation, and analysis
- **JSON Schema Guide**: `json-schema-guide.md` - Learn JSON Schema syntax and validation
- **Pydantic Guide**: `pydantic-guide.md` - Python data validation with Pydantic models
- **[IMPORTANT] Data Layers Study**: `/experiments/Quran Data Layers Study.csv` - Arabic layer definitions and analysis

> **Note**: Add new research tools to `/research-tools/` whenever reusable functionality emerges during schema development or data analysis. Tools grow incrementally with research needs.


## Overview

This directory contains formal schema definitions for the QUD Quranic data layer architecture. The schemas define 15 base data layers.

**Phase 1 Scope**: Initial development focuses on **Hafs** and **Warsh** narrations only. Additional narrations will be incorporated as research matures.

## Directory Structure

```
schemas/
├── README.md                           # This file
├── json-schema-guide.md                # JSON Schema syntax guide
├── pydantic-guide.md                   # Pydantic data validation guide
│
├── base_layers/
│   └── base_layers_v1.json             # Summary of all layers (canonical reference)
│
├── cross-layer-mappings/
│   └── entity-mapping-schema.json      # Complex relationship mappings
│
│── Context & Metadata ─────────────────
├── qir-qiraat-structure/
│   └── schema.json                     # QIR: 10 Qiraat, 20 Narrations
├── edn-edition-variants/
│   └── schema.json                     # EDN: Publisher-specific formatting
├── rdr-readers-narrators/
│   └── schema.json                     # RDR: Biographical data
│
│── Mushaf & Layout ────────────────────
├── msh-mushaf-structure/
│   └── schema.json                     # MSH: Complete manuscript instance
├── pag-page-layout/
│   └── schema.json                     # PAG: Page composition
├── lin-line-layout/
│   └── schema.json                     # LIN: Line composition
│
│── Structural Hierarchy ───────────────
├── sur-surah-structure/
│   └── schema.json                     # SUR: 114 chapters
├── div-division-structure/
│   └── schema.json                     # DIV: Juz, Hizb, Rub divisions
├── aya-verse-structure/
│   └── schema.json                     # AYA: Verse boundaries (varies by Qiraah)
├── snt-sentence-structure/
│   └── schema.json                     # SNT: Grammar, waqf/ibtida rules
├── wrd-word-structure/
│   └── schema.json                     # WRD: Word boundaries, morphology
│
│── Character & Orthography ────────────
├── chr-character-composition/
│   └── schema.json                     # CHR: Base letters, phonetic metadata
├── sym-character-symbols/
│   └── schema.json                     # SYM: Diacritics, tajweed marks
├── tjw-tajweed-rules/
│   └── schema.json                     # TJW: Tajweed relationships
├── uth-orthographic-uthmani/
│   └── schema.json                     # UTH: Traditional Quranic orthography
└── qsy-orthographic-qiasy/
    └── schema.json                     # QSY: Modern standard Arabic
```

### base_layers_v1.json

The `base_layers/base_layers_v1.json` file is the **canonical reference** for all QUD layers. It contains:

- **Layer definitions**: Code, name, folder, description for all 16 layers
- **data_status**: Flags for layers missing from QS-QIRAAT dataset

Use this file programmatically to discover layers, validate folder names, or generate documentation.

## Layer Architecture

### Context & Metadata

| Code | Folder | Name | Description |
|------|--------|------|-------------|
| QIR | `qir-qiraat-structure` | Qiraat Structure | 10 Qiraat, 20 Narrations |
| EDN | `edn-edition-variants` | Edition Variants | Publisher-specific formatting |
| RDR | `rdr-readers-narrators` | Readers & Narrators | Biographical data |

### Mushaf & Layout

| Code | Folder | Name | Description |
|------|--------|------|-------------|
| MSH | `msh-mushaf-structure` | Mushaf Structure | Complete manuscript instance |
| PAG | `pag-page-layout` | Page Layout | Page-level composition |
| LIN | `lin-line-layout` | Line Layout | Line-level composition |

### Structural Hierarchy

| Code | Folder | Name | Description |
|------|--------|------|-------------|
| SUR | `sur-surah-structure` | Surah Structure | 114 chapters |
| DIV | `div-division-structure` | Division Structure | Juz, Hizb, Rub divisions |
| AYA | `aya-verse-structure` | Verse Structure | Verse boundaries (varies by Qiraah) |
| SNT | `snt-sentence-structure` | Sentence Structure | Grammar, waqf/ibtida rules |
| WRD | `wrd-word-structure` | Word Structure | Word boundaries, morphology |

### Character & Orthography

| Code | Folder | Name | Description |
|------|--------|------|-------------|
| CHR | `chr-character-composition` | Character Composition | Base letters, phonetic metadata |
| SYM | `sym-character-symbols` | Character Symbols | Diacritics, tajweed marks |
| TJW | `tjw-tajweed-rules` | Tajweed Rules | Tajweed relationships (idgham, ikhfa) |
| UTH | `uth-orthographic-uthmani` | Orthographic Uthmani | Traditional Quranic orthography |
| QSY | `qsy-orthographic-qiasy` | Orthographic Qiasy | Modern standard Arabic |

## Cross-Layer Mappings

**Schema**: `cross-layer-mappings/entity-mapping-schema.json`

Used for complex relationships that don't fit simple FK patterns, such as:

| Use Case | Example |
|----------|---------|
| **Cross-Qiraah verse mapping** | Hafs 2:255 ↔ Warsh 2:254 (verse boundary differs) |
| **Orthographic expansion** | 1 Uthmani char → 2 Qiasy chars |
| **Cross-edition layout** | Same verse on different pages in different editions |

### When to Use Entity Mappings

| Relationship Type | Where to Store |
|-------------------|----------------|
| Simple FK (word → verse) | Direct property on entity |
| 1:N within same context | Direct property (array of refs) |
| Cross-Qiraah (Hafs ↔ Warsh) | `entity-mapping-schema` |
| Cross-edition (Madina ↔ Cairo) | `entity-mapping-schema` |
| N:M complex | `entity-mapping-schema` |

## Architecture Principles

### 1. Flat with Separate Mappings
- **Entity schemas**: Simple FK properties only (no embedded mapping objects)
- **Complex relationships**: Use separate `entity-mapping-schema.json`
- **No redundant storage**: Each relationship stored in ONE place

### 2. Context-Based Versioning
- Each entity belongs to a specific context (Narration and/or Edition)
- Example: `verse_id("hafs", 2, 255)` → deterministic UUID for Hafs verse
- Cross-context relationships handled via entity-mapping table

### 3. UUID v5 Deterministic IDs
- All IDs generated from naming convention (see UUID Generation section below)
- Same input always produces same UUID
- See `research-tools/generators/uuid_generator.py`

### 4. Schema Subtyping Patterns

When a layer has distinct entity types (e.g., SYM has waqf marks, tajweed marks, tashkeel), three approaches:

| Approach | Description | Use When |
|----------|-------------|----------|
| **Enum + Optional Fields** | Single schema, `type` enum, nullable type-specific fields | >70% field overlap, <4 types |
| **Discriminated Union** | Single schema with `oneOf` + discriminator | 40-70% overlap, type-specific validation needed |
| **Separate Sub-Schemas** | Independent schemas per type | <40% overlap, types evolve independently |

**Possible approach per layer:**

| Layer | Possible Approach | Rationale |
|-------|----------|-----------|
| SYM | Discriminated Union | 5+ types (tashkeel, tajweed, waqf, aya_mark, hamza), ~50% field overlap |
| TJW | Discriminated Union | Rule categories (noon, madd, qalqalah) have different parameters |
| DIV | Enum + Optional | High overlap (juz/hizb/rub), only counts differ |
| WRD | Enum + Optional | High overlap, aya_mark is edge case |
| UTH/QSY | Already Split | Orthographies are fundamentally different systems |
| SNT | Discriminated Union | Sentence types (nominal/verbal/conditional) have different grammar rules |

**Discriminated Union Example (SYM):**
```json
{
  "definitions": {
    "base_symbol": { "properties": { "symbol_id": {}, "codepoint": {} } },
    "waqf_symbol": { "allOf": [{"$ref": "#/definitions/base_symbol"}, {"properties": {"waqf_type": {}}}] }
  },
  "oneOf": [
    {"$ref": "#/definitions/tashkeel_symbol"},
    {"$ref": "#/definitions/waqf_symbol"}
  ],
  "discriminator": {"propertyName": "symbol_type"}
}
```

**Decision factors:** different FK relationships, different validation rules, many distinct types with little field overlap.

## Schema Format

All schemas follow JSON Schema Draft 07:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://qud.itqan.community/schemas/xxx-name.json",
  "title": "XXX: Name",
  "type": "object",
  "required": ["entity_id", "parent_ref", ...],
  "properties": {
    "entity_id": {
      "type": "string",
      "format": "uuid",
      "description": "Unique identifier (UUID v5 from naming convention)"
    },
    "parent_ref": {
      "type": "string",
      "format": "uuid",
      "description": "Foreign key to parent layer"
    }
  }
}
```

### Key Design Decisions

1. **No embedded `cross_layer_mappings`** - Use seperate mapping schemas instead
2. **No `canonical_verse_id`** - Each Qiraah is independent, no universal canonical
3. **No `semantic_hash`** - UUID v5 already encodes identity
4. **Simple FK properties** - Direct references only, no redundant arrays

## UUID Generation

> **TENTATIVE**: This naming convention is evolving based on research findings. The goal is to ensure unique, deterministic IDs regardless of context changes, layer mappings, and cross-narration relationships. Expect refinements as we discover edge cases in verse boundaries, orthographic mappings, and edition variations. Parameters of each function are subject to change. 

Use the QUD UUID generator for consistent IDs. See `/research-tools/generators/uuid_generator.py`.

### Generator Functions

#### Context & Metadata

| Function | Parameters | Name String | Example |
|----------|------------|-------------|---------|
| `narration_id` | `name` | `qir:{name}` | `qir:hafs` |
| `edition_id` | `publisher`, `name` | `edn:{publisher}:{name}` | `edn:kfgqpc:hafs_v2` |
| `reader_id` | `name` | `rdr:{name}` | `rdr:hafs` |

#### Mushaf & Layout

| Function | Parameters | Name String | Example |
|----------|------------|-------------|---------|
| `mushaf_id` | `narration`, `edition?` | `msh:{narration}:{edition}` | `msh:hafs:kfgqpc_v2` |
| `page_id` | `narration`, `edition`, `page` | `{narration}:{edition}:p{page}` | `hafs:kfgqpc_v2:p42` |
| `line_id` | `narration`, `edition`, `page`, `line` | `{narration}:{edition}:p{page}:l{line}` | `hafs:kfgqpc_v2:p42:l7` |

#### Structural Hierarchy

| Function | Parameters | Name String | Example |
|----------|------------|-------------|---------|
| `surah_id` | `surah` | `s{surah}` | `s2` → Al-Baqarah (universal) |
| `juz_id` | `narration`, `juz` | `{narration}:j{juz}` | `hafs:j15` |
| `hizb_id` | `narration`, `hizb` | `{narration}:h{hizb}` | `hafs:h30` (global 1-60) |
| `rub_id` | `narration`, `rub` | `{narration}:r{rub}` | `hafs:r120` (global 1-240) |
| `verse_id` | `narration`, `surah`, `verse` | `{narration}:s{surah}:v{verse}` | `hafs:s2:v255` |
| `sentence_id` | `narration`, `surah`, `verse`, `sentence` | `{narration}:s{surah}:v{verse}:snt{sentence}` | `hafs:s2:v255:snt1` |
| `word_id` | `narration`, `surah`, `verse`, `word` | `{narration}:s{surah}:v{verse}:w{word}` | `hafs:s2:v255:w4` |

#### Character-Level

| Function | Parameters | Name String | Example |
|----------|------------|-------------|---------|
| `char_id` | `narration`, `surah`, `verse`, `word`, `char` | `{narration}:s{surah}:v{verse}:w{word}:c{char}` | `hafs:s2:v255:w4:c2` |
| `symbol_id` | `narration`, `surah`, `verse`, `word`, `char`, `symbol` | `{narration}:s{surah}:v{verse}:w{word}:c{char}:sym{symbol}` | `hafs:s2:v255:w4:c2:sym1` |

## Schema Evolution

**Version**: 1.0.0 (Initial release)

Future schema changes will follow semantic versioning:

- **Major version**: Breaking changes to schema structure
- **Minor version**: Backwards-compatible additions (new optional fields)
- **Patch version**: Documentation or constraint clarifications

## Research Requirements

These schemas support the following research objectives:

- **RR-001**: Layer separation analysis of QS-QIRAAT
- **RR-002**: Schema design for separated layers (THIS DELIVERABLE)
- **RR-003**: Layer simulation prototype
- **RR-011**: UUID-based cross-layer mapping implementation
- **RR-012**: Multi-layer contextual versioning validation
- **RR-013**: Orthographic transformation handling

## License & Attribution

**Source Data**: King Fahd Quranic Printing Complex Uthmanic Hafs v2.0 dataset

**QUD Schema Architecture**: ITQAN Community, 2025

---

**Last Updated**: 2025-01-23
