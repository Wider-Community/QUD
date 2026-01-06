# QUD Quranic Data Layer Schemas

**Version**: 2.0.0
**Date**: 2025-11-11
**Project**: QUD (Layered Universal Big Data for Quranic Studies)

## Overview

This directory contains formal schema definitions for the QUD Quranic data layer architecture. The schemas define 16 base data layers (Layers 0-15) with additional sub-layer variations, totaling 18+ identified layers.

**Layer Numbering**: Layers are numbered from **0 (most dominant)** to **15 (least dominant)**. Layer 0 represents the highest-level concern (Qiraat - the complete reading system), while Layer 15 represents the foundational atomic units (Character Composition).

## Purpose

The QUD architecture separates the conflated Quranic data found in existing datasets (like QS-QIRAAT) into distinct, independently queryable layers. This enables:

- **Layer-specific queries**: Query character-level data without page layout concerns
- **Cross-Qiraah analysis**: Compare Hafs vs Warsh at any layer granularity
- **Generative architecture**: Generate derivative layers from source layers + rules
- **Redundancy reduction**: Normalize repeated data across layers
- **UUID-based cross-layer mapping**: Track entity relationships with precision

## Layer Architecture

**Layers are numbered from most dominant (0) to least dominant (15)**

### Qiraat & Narrations System (0-1)

**Most Dominant Layers** - Each Qiraah determines a complete reading tradition, and each has 2 primary narrations

| Layer | Name | Schema File | Description |
|-------|------|-------------|-------------|
| 0 | Qiraat | `layer-00-qiraat/schema.json` | The 10 canonical Quranic readings (القراءات العشر) - Asim, Nafi', etc. |
| 1 | Narrations | `layer-01-narrations/schema.json` | Specific transmissions (الروايات) - e.g., Hafs & Shu'bah from Asim |

### Publication & Layout Layers (2-4)

| Layer | Name | Schema File | Description |
|-------|------|-------------|-------------|
| 2 | Edition Variants | `layer-02-edition-variants/schema.json` | Publisher-specific formatting |
| 3 | Line Layout | `layer-03-line-layout/schema.json` | Line-level composition |
| 4 | Page Layout | `layer-04-page-layout/schema.json` | Page-level composition |

### Quranic Organization Layers (5-9)

| Layer | Name | Schema File | Description |
|-------|------|-------------|-------------|
| 5 | Division Structure | `layer-05-division-structure/schema.json` | Juz, Hizb, Rub divisions |
| 6 | Mushaf Structure | `layer-06-mushaf-structure/schema.json` | Complete manuscript composition |
| 7 | Qiraat Structure | `layer-07-qiraat-structure/schema.json` | Qiraat system metadata and rules |
| 8 | Surah Structure | `layer-08-surah-structure/schema.json` | 114 chapters with metadata |
| 9 | Verse Structure | `layer-09-verse-structure/schema.json` | Verses with canonical_verse_id |

### Linguistic Layers (10-11)

| Layer | Name | Schema File | Description |
|-------|------|-------------|-------------|
| 10 | Sentence Structure | `layer-10-sentence-structure/schema.json` | Grammar, waqf/ibtida rules (MISSING in QS-QIRAAT) |
| 11 | Word Structure | `layer-11-word-structure/schema.json` | Word boundaries, morphology |

### Orthographic Systems (12a-12b)

**Positioned between word and character layers**

| Layer | Name | Schema File | Description |
|-------|------|-------------|-------------|
| 12a | Orthographic - Uthmani | `layer-12a-orthographic-uthmani/schema.json` | Traditional Uthmani script (Rasm Uthmani) |
| 12b | Orthographic - Qiasy | `layer-12b-orthographic-qiasy/schema.json` | Modern standard Arabic script |

### Character-Level Layers (13-15)

**Least Dominant Layers** - Foundational atomic units

| Layer | Name | Schema File | Description |
|-------|------|-------------|-------------|
| 13 | Character Paired Data | `layer-13-character-paired-data/schema.json` | Tajweed relationships (idgham, ikhfa, etc.) |
| 14 | Character Symbols & Rendering | `layer-14-character-symbols-rendering/schema.json` | Diacritics, tajweed symbols, visual rendering |
| 15 | Character Composition | `layer-15-character-composition/schema.json` | Base letter sequences, atomic text units |

### Meta-Layers (16-17, Expanded Version Only)

**HYPOTHETICAL** - System versioning layers

| Layer | Name | Description |
|-------|------|-------------|
| 16 | Context Schema | Context parameters for layer versioning (RR-014) |
| 17 | Layer Version Metadata | Version tracking metadata (RR-015) |

## Cross-Layer Mappings

**EntityMapping Schema**: `cross-layer-mappings/entity-mapping-schema.json`

The EntityMapping schema handles all cross-layer relationships including:
- **1:1 mappings**: Simple one-to-one relationships
- **1:N expansions**: One entity → multiple entities (e.g., 1 Uthmani char → 2 Qiasy chars)
- **N:1 contractions**: Multiple entities → one entity (e.g., 2 Warsh verses → 1 Hafs verse)
- **N:M complex mappings**: Many-to-many relationships

### Critical Use Cases

1. **Orthographic Transformation** (Layer 12a ↔ 12b):
   - Handles expansion: 1 Uthmani character → 2 Qiasy characters
   - Preserves character ordering via `position_metadata`
   - Example: "الصلوة" (Uthmani) → "الصلاة" (Qiasy)

2. **Verse Numbering Variations** (Layer 5 cross-Qiraah):
   - Maps verse boundaries across narrations
   - Uses `canonical_verse_id` for identity
   - Example: Hafs 6,236 verses ↔ Warsh 6,214 verses

3. **Bidirectional Traversal**:
   - All mappings include `bidirectional_ref` for reverse navigation
   - Enables queries in both directions (Layer 0 → Layer 3 and Layer 3 → Layer 0)

## Schema Format

All schemas follow JSON Schema Draft 07 specification with:

- **UUID identifiers**: Every entity has a unique `*_id` UUID field
- **Foreign key references**: UUID-based cross-layer references
- **Validation constraints**: Required fields, value ranges, type checking
- **Cross-layer mappings**: Embedded `cross_layer_mappings` object in each schema
- **Provenance tracking**: Source attribution fields where applicable

### Example Schema Structure

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://qud.itqan.community/schemas/layer-XX-name.json",
  "title": "Layer X: Name",
  "description": "Purpose of this layer",
  "type": "object",
  "required": ["entity_id", ...],
  "properties": {
    "entity_id": {
      "type": "string",
      "format": "uuid",
      "description": "Unique identifier"
    },
    "cross_layer_mappings": {
      "type": "object",
      "properties": {
        "layer_Y_entities": {
          "type": "array",
          "items": { "type": "string", "format": "uuid" }
        }
      }
    }
  }
}
```

## Validation

Each schema is designed for:

1. **Type conformance**: All fields match declared types
2. **Constraint satisfaction**: Required fields present, value ranges respected
3. **Referential integrity**: Foreign keys reference valid UUIDs
4. **UUID validity**: All UUIDs are unique, properly formatted (v4/v5)
5. **Cross-layer integrity**: All EntityMapping instances have valid source/target UUIDs
6. **Invariant preservation**: Domain rules hold (e.g., verse count sums match narration totals)

## Implementation Status

### Phase 1 (Current - Months 1-2)
- ✅ JSON Schemas defined for all 15 base layers + 12a/12b sub-layers
- ✅ EntityMapping schema defined
- ⏳ Pydantic models (next step)
- ⏳ Layer-specific README documentation (next step)
- ⏳ RR-001: Layer mapping analysis of QS-QIRAAT dataset
- ⏳ RR-002: Schema validation with real data transformation
- ⏳ RR-003: Layer simulation prototype with Hafs and Warsh

### Phase 2-3 (Months 2-6)
- ⏳ Extend to additional narrations beyond Hafs and Warsh
- ⏳ Context Schema (Layer 15 - hypothetical)
- ⏳ Layer Version Metadata (Layer 16 - hypothetical)
- ⏳ QUD Orchestrator design (RR-014)
- ⏳ MUDMAJ storage schema (RR-015)

## Data Sources

**Primary**: QS-QIRAAT Dataset v2.0
- 6 narrations from 3-4 Qiraat (Hafs, Warsh, Qalun, Shu'bah, Al-Duri, Al-Susi)
- Phase 1 focuses on Hafs (6,236 verses) and Warsh (6,214 verses)

**Validation**:
- King Fahd Quranic Printing Complex official editions
- Tanzil.net verified datasets

## Schema Evolution

Version: **1.0.0** (Initial release)

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

## Directory Structure

```
schemas/
├── README.md                                    # This file
├── Base-Data-Layer-Schemas/
│   └── Initial-Base-Data-Layer                  # CSV list of 15 base layers
├── Expanded-Data-Layers-Schema/
│   └── Initial-Data-Layers-Expanded-Schema      # CSV list of 17 expanded layers
├── layer-00-character-composition/
│   └── schema.json
├── layer-01-character-symbols-rendering/
│   └── schema.json
├── layer-02-character-paired-data/
│   └── schema.json
├── layer-03-word-structure/
│   └── schema.json
├── layer-04-sentence-structure/
│   └── schema.json
├── layer-05-verse-structure/
│   └── schema.json
├── layer-06-surah-structure/
│   └── schema.json
├── layer-07-qiraat-structure/
│   └── schema.json
├── layer-08-mushaf-structure/
│   └── schema.json
├── layer-09-division-structure/
│   └── schema.json
├── layer-10-page-layout/
│   └── schema.json
├── layer-11-line-layout/
│   └── schema.json
├── layer-12a-orthographic-uthmani/
│   └── schema.json
├── layer-12b-orthographic-qiasy/
│   └── schema.json
├── layer-13-edition-variants/
│   └── schema.json
├── layer-14-readers-narrators/
│   └── schema.json
├── cross-layer-mappings/
│   └── entity-mapping-schema.json
├── context-schema/                              # Hypothetical (RR-014)
└── mudmaj-schema/                               # Hypothetical (RR-015)
```

## Next Steps

1. **Create Pydantic models** for each layer (Python type-safe implementations)
2. **Layer-specific README** for each layer directory with detailed field documentation
3. **Schema validation scripts** to test schemas against sample data
4. **Transformation prototypes** to convert QS-QIRAAT data to QUD format

## Related Documentation

- **Specification**: `/specs/001-quranic-layer-architecture/spec.md`
- **Data Model**: `/specs/001-quranic-layer-architecture/data-model.md`
- **Research Plan**: `/specs/001-quranic-layer-architecture/plan.md`
- **Tasks**: `/specs/001-quranic-layer-architecture/tasks.md`

## License & Attribution

**Source Data**: King Fahd Quranic Printing Complex Uthmanic Hafs v2.0 dataset (© KFGQPC)

**QUD Schema Architecture**: ITQAN Community, 2025

---

**Last Updated**: 2025-11-11
**Schema Version**: 1.0.0
**Status**: RR-002 Deliverable (JSON Schemas Complete)
