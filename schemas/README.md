# QUD Quranic Data Layer Schemas

**Version**: 3.0.0
**Date**: 2025-01-23
**Project**: QUD (Layered Universal Big Data for Quranic Studies)

## Overview

This directory contains formal schema definitions for the QUD Quranic data layer architecture. The schemas define 15 base data layers (Layers 0-14) with orthographic sub-layers (12a/12b).

## Architecture Principles

### 1. Flat with Separate Mappings
- **Entity schemas**: Simple FK properties only (no embedded mapping objects)
- **Complex relationships**: Use separate `entity-mapping-schema.json`
- **No redundant storage**: Each relationship stored in ONE place

### 2. Context-Based Versioning
- Each entity belongs to a specific context (Qiraah + Edition)
- Example: `qud_id("hafs", s=2, v=255)` → deterministic UUID
- Cross-context relationships handled via entity-mapping table

### 3. UUID v5 Deterministic IDs
- All IDs generated from naming convention: `{context}:{layer}{number}:...`
- Same input always produces same UUID
- See `research-tools/generators/uuid_generator.py`

## Layer Architecture

### Character & Word Layers

| Code | Folder | Name | Description |
|------|--------|------|-------------|
| CHR | `chr-character-composition` | Character Composition | Base letters, phonetic metadata |
| SYM | `sym-character-symbols` | Character Symbols | Diacritics, tajweed marks |
| TJW | `tjw-tajweed-rules` | Tajweed Rules | Tajweed relationships (idgham, ikhfa) |
| WRD | `wrd-word-structure` | Word Structure | Word boundaries, morphology |
| UTH | `uth-orthographic-uthmani` | Orthographic Uthmani | Traditional Quranic orthography |
| QSY | `qsy-orthographic-qiasy` | Orthographic Qiasy | Modern standard Arabic |

### Structural Layers

| Code | Folder | Name | Description |
|------|--------|------|-------------|
| SNT | `snt-sentence-structure` | Sentence Structure | Grammar, waqf/ibtida rules |
| AYA | `aya-verse-structure` | Verse Structure | Verse boundaries (varies by Qiraah) |
| SUR | `sur-surah-structure` | Surah Structure | 114 chapters |
| QIR | `qir-qiraat-structure` | Qiraat Structure | Narration metadata and rules |
| MSH | `msh-mushaf-structure` | Mushaf Structure | Complete manuscript composition |

### Layout Layers (vary by Edition)

| Code | Folder | Name | Description |
|------|--------|------|-------------|
| DIV | `div-division-structure` | Division Structure | Juz, Hizb, Rub divisions |
| PAG | `pag-page-layout` | Page Layout | Page-level composition |
| LIN | `lin-line-layout` | Line Layout | Line-level composition |

### Metadata Layers

| Code | Folder | Name | Description |
|------|--------|------|-------------|
| EDN | `edn-edition-variants` | Edition Variants | Publisher-specific formatting |
| RDR | `rdr-readers-narrators` | Readers & Narrators | Biographical data |

## Cross-Layer Mappings

**Schema**: `cross-layer-mappings/entity-mapping-schema.json`

Used for complex relationships that don't fit simple FK patterns:

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

1. **No embedded `cross_layer_mappings`** - Removed from all entity schemas
2. **No `canonical_verse_id`** - Each Qiraah is independent, no universal canonical
3. **No `semantic_hash`** - UUID v5 already encodes identity
4. **Simple FK properties** - Direct references only, no redundant arrays

## Directory Structure

```
schemas/
├── README.md                           # This file
├── Base-Data-Layer-Schemas/
│   ├── Initial-Base-Data-Layer.csv
│   └── Initial-Base-Data-Layer.json
├── Expanded-Data-Layers-Schema/
│   └── Initial-Data-Layers-Expanded-Schema.csv
├── cross-layer-mappings/
│   └── entity-mapping-schema.json      # Complex relationship mappings
├── chr-character-composition/
│   └── schema.json                     # CHR: Character Composition
├── sym-character-symbols/
│   └── schema.json                     # SYM: Character Symbols
├── tjw-tajweed-rules/
│   └── schema.json                     # TJW: Tajweed Rules
├── wrd-word-structure/
│   └── schema.json                     # WRD: Word Structure
├── uth-orthographic-uthmani/
│   └── schema.json                     # UTH: Orthographic Uthmani
├── qsy-orthographic-qiasy/
│   └── schema.json                     # QSY: Orthographic Qiasy
├── snt-sentence-structure/
│   └── schema.json                     # SNT: Sentence Structure
├── aya-verse-structure/
│   └── schema.json                     # AYA: Verse Structure
├── sur-surah-structure/
│   └── schema.json                     # SUR: Surah Structure
├── qir-qiraat-structure/
│   └── schema.json                     # QIR: Qiraat Structure
├── msh-mushaf-structure/
│   └── schema.json                     # MSH: Mushaf Structure
├── div-division-structure/
│   └── schema.json                     # DIV: Division Structure
├── pag-page-layout/
│   └── schema.json                     # PAG: Page Layout
├── lin-line-layout/
│   └── schema.json                     # LIN: Line Layout
├── edn-edition-variants/
│   └── schema.json                     # EDN: Edition Variants
└── rdr-readers-narrators/
    └── schema.json                     # RDR: Readers & Narrators
```

## UUID Generation

Use the QUD UUID generator for consistent IDs:

```python
from research_tools.generators.uuid_generator import qud_id, verse_id, word_id

# Generate IDs
verse_id("hafs", 2, 255)              # → deterministic UUID
word_id("hafs", 2, 255, 4)            # → deterministic UUID
qud_id("hafs", s=2, v=255, w=4, c=2)  # → character UUID
qud_id("hafs", p=42, l=7)             # → line UUID
```

## Related Documentation

- **Specification**: `/specs/001-quranic-layer-architecture/spec.md`
- **Architecture Principles**: `/docs/architecture/architectural-principles.md`
- **UUID Generator**: `/research-tools/generators/uuid_generator.py`

## License & Attribution

**Source Data**: King Fahd Quranic Printing Complex Uthmanic Hafs v2.0 dataset

**QUD Schema Architecture**: ITQAN Community, 2025

---

**Last Updated**: 2025-01-23
**Schema Version**: 3.0.0
