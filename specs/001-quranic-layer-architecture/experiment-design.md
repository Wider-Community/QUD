# Experiment Design

**Research Topic**: Quranic Data Layer Architecture
**Date**: 2025-11-03
**Related Spec**: [spec.md](./spec.md)
**Related Data Model**: [data-model.md](./data-model.md)

## Purpose

This document specifies the experimental methodology for validating the six research hypotheses (RR-001, RR-002, RR-003, RR-011, RR-012, RR-013). Each experiment is designed to be independently executable and validatable.

**Research Track Structure**:
- **RR-001 to RR-003**: Layer architecture separation, schema design, simulation prototype
- **RR-011 to RR-013**: UUID-based cross-layer mapping system validation (verse numbering controversy, orthographic transformations)

## Experiment RR-001: Layer Separation Analysis

### Hypothesis

The QS-QIRAAT dataset conflates at least 6 distinct layers (Layer 5: Verse structure, Layer 6: Surah structure, Layer 7: Qiraah/narration variants, Layer 8: Mushaf structure, Layer 10: Page layout, Layer 11: Line layout) into a single flat data structure, and this conflation can be identified and quantified through schema analysis.

### Experimental Method

**Input Data**:
- QS-QIRAAT Hafs JSON dataset (6,236 verse records)
- All 7 narration JSON datasets for cross-Qiraah comparison

**Procedure**:

1. **Data Loading** (Jupyter notebook: `01-data-loading.ipynb`):
   ```python
   import json
   import pandas as pd

   # Load Hafs dataset
   with open('/path/to/QS-QIRAAT/hafs.json', 'r', encoding='utf-8') as f:
       hafs_data = json.load(f)

   # Convert to DataFrame for analysis
   hafs_df = pd.DataFrame(hafs_data)

   # Inspect schema
   print(hafs_df.dtypes)
   print(hafs_df.head())
   print(hafs_df.describe())
   ```

2. **Field Mapping** (Jupyter notebook: `02-field-layer-mapping.ipynb`):
   - For each field in QS-QIRAAT schema, manually map to QUD layer(s)
   - Document mapping in table format
   - Create conflation matrix: 15×15 matrix where cell (i,j) = 1 if layers i and j mixed in same field (Layers 0-14)

3. **Cross-Qiraah Analysis** (Jupyter notebook: `03-cross-Qiraah-comparison.ipynb`):
   ```python
   # Load Hafs and Warsh narrations (Phase 1 per Constitution VI)
   narrations = ['hafs', 'warsh']  # Phase 1 scope - remaining 5 deferred to Phase 2-3
   data = {}
   for narration in narrations:
       with open(f'/path/to/QS-QIRAAT/{narration}.json', 'r') as f:
           data[narration] = pd.DataFrame(json.load(f))

   # Compare field values across narrations
   # Identify which fields vary (Qiraah-specific) vs identical (shared layers)
   # Document findings that likely generalize to remaining narrations
   ```

4. **Visualization** (Jupyter notebook: `04-conflation-visualization.ipynb`):
   - Heatmap of conflation matrix using seaborn
   - Bar chart showing field count per layer
   - Venn diagram showing layer overlap

**Expected Outputs**:

1. **Mapping Table** (`findings/rr-001-mapping-table.csv`):
   ```csv
   QS_Field,QUD_Layers,Conflation_Type,Notes
   id,N/A,synthetic,"Sequential ID, not semantic layer"
   jozz,9,single,"Layer 9: Division Structure (Juz/Hizb/Rub)"
   page,10,single,"Layer 10: Page Layout"
   sura_no,6,single,"Layer 6: Surah Structure"
   sura_name_en,6,single,"Layer 6: Surah Structure"
   sura_name_ar,6,single,"Layer 6: Surah Structure"
   line_start,11,single,"Layer 11: Line Layout"
   line_end,11,single,"Layer 11: Line Layout"
   aya_no,5,single,"Layer 5: Verse Structure"
   aya_text,"0,1,3,12a",multi,"Conflates Character Composition/Symbols-Rendering/Words/Uthmani Script"
   aya_text_emlaey,"0,3,12b",multi,"Conflates Character Composition/Words/Qiasy Script"
   ```

2. **Conflation Matrix** (`findings/rr-001-conflation-matrix.png`):
   - 15×15 heatmap (Layers 0-14)
   - Bright cells indicate layers mixed in same field

3. **Gap Analysis** (`findings/rr-001-gap-analysis.md`):
   - Which of 15 layers (0-14) completely missing from QS-QIRAAT
   - Expected: Layers 2 (Character Paired Data), 4 (Sentence Structure), 13 (Edition Variants), 14 (Readers/Narrators) implicit/missing

4. **Cross-Qiraah Variance Report** (`findings/rr-001-qiraah-variance.md`):
   - Which fields differ across narrations (indicates Layer 0 Character/Layer 7 Qiraat concerns)
   - Which fields identical (indicates shared higher layers like Layer 6 Surah metadata)

### Success Criteria

- [ ] 100% of QS-QIRAAT fields mapped to QUD layers
- [ ] Conflation matrix produced showing multi-layer fields
- [ ] At least 6 layers identified as mixed (hypothesis validation)
- [ ] Gap analysis identifies missing layers
- [ ] Cross-Qiraah comparison distinguishes Qiraah-specific vs shared fields

### Validation

- Manual review of mapping table by domain expert
- Peer review of conflation matrix logic
- Reproducibility: Another researcher can run notebooks and produce same outputs

---

## Experiment RR-002: Schema Design for Separated Layers

### Hypothesis

A schema-first approach defining Layers 0-14 independently (15 total layers) with UUID-based entity identification and cross-layer mappings will reduce data redundancy by >40%, enable cross-Qiraah queries currently impossible in QS-QIRAAT, and support generative architecture where derivative layers can be computed.

### Experimental Method

**Input Data**:
- RR-001 mapping table (field→layer assignments)
- Data model specification from `data-model.md`
- QS-QIRAAT sample data for schema validation

**Procedure**:

1. **Schema Definition** (directory: `schemas/`):
   - For each layer 0-14 (15 total), create:
     - `schemas/layer-XX-name/schema.json` (JSON Schema formal specification with UUID fields)
     - `schemas/layer-XX-name/models.py` (Pydantic model with UUID validation)
     - `schemas/layer-XX-name/README.md` (domain semantics documentation and cross-layer mapping explanation)
   - Additionally, create `schemas/cross-layer-mappings/`:
     - `entity-mapping-schema.json` (EntityMapping structure definition)
     - `mapping-models.py` (Pydantic model for EntityMapping)

   Example JSON Schema (Layer 5 - Verse):
   ```json
   {
     "$schema": "http://json-schema.org/draft-07/schema#",
     "$id": "https://qud.itqan.community/schemas/layer-05-verse/v1.0.0",
     "title": "Layer 5: Verse Structure",
     "description": "Verse enumeration and boundaries within surahs",
     "type": "object",
     "properties": {
       "verse_id": {
         "type": "string",
         "format": "uuid",
         "description": "Unique verse identifier for this instance within a specific narration"
       },
       "canonical_verse_id": {
         "type": "string",
         "format": "uuid",
         "description": "Canonical identity independent of narration (solves verse numbering controversy)"
       },
       "sura_ref": {
         "type": "string",
         "format": "uuid",
         "description": "Foreign key to Layer 6 Surah"
       },
       "verse_number": {
         "type": "integer",
         "minimum": 1,
         "description": "Verse number within surah (position-based, varies by narration)"
       },
       "narration_ref": {
         "type": "string",
         "format": "uuid",
         "description": "Foreign key to Layer 7 Qiraat (narration)"
       }
     },
     "required": ["verse_id", "canonical_verse_id", "sura_ref", "verse_number", "narration_ref"],
     "additionalProperties": false
   }
   ```

   Corresponding Pydantic model:
   ```python
   from pydantic import BaseModel, UUID4, Field

   class Verse(BaseModel):
       verse_id: UUID4 = Field(..., description="Unique verse identifier")
       canonical_verse_id: UUID4 = Field(..., description="Canonical identity independent of narration")
       sura_ref: UUID4 = Field(..., description="Foreign key to Layer 6 Surah")
       verse_number: int = Field(..., gt=0, description="Verse number within surah")
       narration_ref: UUID4 = Field(..., description="Foreign key to Layer 7 Qiraat (narration)")

       class Config:
           json_schema_extra = {
               "example": {
                   "verse_id": "550e8400-e29b-41d4-a716-446655440000",
                   "sura_ref": "660e8400-e29b-41d4-a716-446655440001",
                   "verse_number": 1,
                   "narration_ref": "770e8400-e29b-41d4-a716-446655440002"
               }
           }
   ```

2. **Transformation Algorithm Design** (`research-tools/transformers/qs_to_qud.py`):
   - Pseudocode/flowchart showing QS-QIRAAT → 15-layer transformation with UUID generation
   - For each QS-Verse record:
     - Generate UUIDs for all entities (verses, characters, surahs, pages, lines, etc.)
     - Extract Layer 5 data (verse structure) from `aya_no` with canonical_verse_id generation
     - Extract Layer 6 data (surah metadata) from `sura_*` fields
     - Parse Layer 0 data (character composition) from `aya_text` by Unicode decomposition with character UUIDs
     - Extract Layer 1 (symbols/rendering) from diacritics in `aya_text`
     - Extract Layer 10 (page), Layer 11 (line) from `page`, `line_*` fields
     - Build EntityMapping instances for cross-layer relationships
     - Normalize: Store unique pages/lines/surahs once (not repeated per verse)

3. **Schema Validation Testing** (Jupyter notebook: `05-schema-validation-test.ipynb`):
   ```python
   from pydantic import ValidationError
   from schemas.layer_06_verse.models import Verse
   import uuid

   # Test schema with sample data
   sample_verse = {
       "verse_id": str(uuid.uuid4()),
       "sura_ref": str(uuid.uuid4()),
       "verse_number": 1,
       "narration_ref": str(uuid.uuid4())
   }

   try:
       verse = Verse(**sample_verse)
       print("✓ Schema validation passed")
   except ValidationError as e:
       print(f"✗ Schema validation failed: {e}")
   ```

4. **Redundancy Analysis** (Jupyter notebook: `06-redundancy-measurement.ipynb`):
   - Transform sample of QS-QIRAAT data (e.g., first 3 suras) to 15-layer format with UUID mappings
   - Measure storage sizes:
     - QS-QIRAAT flat JSON size
     - QUD 15-layer JSON size (sum of all layer files + cross-layer mappings)
   - Calculate redundancy reduction percentage
   - Account for UUID overhead in storage calculations

**Expected Outputs**:

1. **Schema Files** (`schemas/layer-00-character-composition/` through `schemas/layer-14-readers-narrators/` + `schemas/cross-layer-mappings/`):
   - 15 layer directories × 3 files each = 45 files
   - 1 cross-layer-mappings directory × 3 files = 3 files
   - **Total**: 48 files
   - Each with: JSON Schema (formal specification), Pydantic models (Python implementation), README (domain documentation + UUID mapping examples)

2. **Transformation Specification** (`findings/rr-002-transformation-spec.md`):
   - Detailed algorithm for QS-QIRAAT → QUD conversion
   - Pseudocode and flowcharts
   - Edge case handling (e.g., verses spanning multiple lines)

3. **Redundancy Report** (`findings/rr-002-redundancy-analysis.md`):
   - Storage size comparison table
   - Percentage reduction achieved
   - Analysis of where redundancy eliminated (normalized pages/suras/lines)

### Success Criteria

- [ ] 15 layer schemas defined (JSON Schema + Pydantic) with UUID fields
- [ ] Cross-layer mapping schema (EntityMapping) defined
- [ ] All schemas include constraints from data-model.md including UUID validation
- [ ] Transformation algorithm specified for QS-QIRAAT → QUD with UUID generation
- [ ] Schema validation passes for sample data including UUID format validation
- [ ] Redundancy reduction >40% demonstrated on sample dataset (accounting for UUID overhead)
- [ ] Zero information loss: QS-QIRAAT can be reconstructed from 15-layer format
- [ ] All cross-layer relationships documented with EntityMapping examples

### Validation

- Schema completeness: All fields from data-model.md represented
- Pydantic validation: Sample data validates successfully
- Reverse transformation: Generate QS-QIRAAT format from QUD layers, compare byte-for-byte
- Redundancy calculation reviewed for correctness

---

## Experiment RR-003: Layer Simulation Prototype

### Hypothesis

A simulation processing **Hafs (6,236 verses) and Warsh (6,214 verses) = 12,450 total verse records** (Phase 1 per Constitution VI) can successfully separate layers, generate derivative layers via rules, conform to defined schemas with <1% error rate, and enable previously impossible cross-Qiraah queries. Phase 2-3 will scale to remaining narrations (43,652 total records).

### Experimental Method

**Input Data**:
- Hafs and Warsh QS-QIRAAT narration datasets (Phase 1 per Constitution VI)
- RR-002 schemas (JSON Schema + Pydantic models)
- Transformation algorithms from RR-002

**Procedure**:

1. **Prototype Development** (`experiments/rr-003-layer-simulation/prototype.py`):
   ```python
   #!/usr/bin/env python3
   """
   EXPERIMENTAL: Quranic Data Layer Separation Prototype
   Tier 1 research code - validates layer architecture hypothesis
   """

   import json
   from pathlib import Path
   from pydantic import ValidationError
   from schemas import * # Import all layer models
   from research_tools.transformers import qs_to_qud

   def process_narration(narration_name: str, qs_data_path: Path):
       """Transform single narration from QS-QIRAAT to QUD 15-layer format with UUID generation"""

       # Load QS-QIRAAT data
       with open(qs_data_path, 'r', encoding='utf-8') as f:
           qs_data = json.load(f)

       # Transform to 15 layers with UUID mappings
       qud_layers = qs_to_qud.transform(qs_data, narration_name)

       # Validate against schemas (including UUID validation)
       validation_results = validate_all_layers(qud_layers)

       return qud_layers, validation_results

   def validate_all_layers(qud_layers: dict) -> dict:
       """Run Pydantic validation on all 15 layers + cross-layer mappings"""
       results = {}
       for layer_name, layer_data in qud_layers.items():
           try:
               # Validate each record in layer
               validated = [LayerModel(**record) for record in layer_data]
               results[layer_name] = {
                   "status": "pass",
                   "count": len(validated)
               }
           except ValidationError as e:
               results[layer_name] = {
                   "status": "fail",
                   "errors": str(e)
               }
       return results

   if __name__ == "__main__":
       narrations = ['hafs', 'warsh', 'qaloun', 'shuba', 'douri', 'sousi']
       for narration in narrations:
           print(f"Processing {narration}...")
           layers, validation = process_narration(narration, Path(f"data/{narration}.json"))
           print(f"Validation: {validation}")
   ```

2. **Character Count Validation** (`research-tools/validators/char_count_validator.py`):
   ```python
   def validate_character_count(layer1_data: list, expected_count: int, narration: str):
       """Validate Layer 1 character count matches authoritative sources"""
       actual_count = sum(len(verse['characters']) for verse in layer1_data)

       if actual_count == expected_count:
           return {"status": "pass", "count": actual_count}
       else:
           return {
               "status": "fail",
               "expected": expected_count,
               "actual": actual_count,
               "diff": actual_count - expected_count
           }
   ```

3. **Generative Layer Testing** (`experiments/rr-003-layer-simulation/test_generation.py`):
   - Implement Layer 0 → Layer 1 generation (character → symbols/rendering via Qiraah rules)
   - Compare generated Layer 1 against extracted Layer 1 from QS-QIRAAT
   - Measure accuracy percentage

4. **SQLite Database Generation** (`experiments/rr-003-layer-simulation/generate_db.py`):
   ```python
   import sqlite3

   def create_layer_tables(conn):
       """Create one table per layer"""

       # Example: Layer 6 Verses table
       conn.execute("""
           CREATE TABLE layer_06_verses (
               verse_id TEXT PRIMARY KEY,
               sura_ref TEXT NOT NULL,
               verse_number INTEGER NOT NULL,
               narration_ref TEXT NOT NULL,
               FOREIGN KEY (sura_ref) REFERENCES layer_08_chapters(chapter_id),
               FOREIGN KEY (narration_ref) REFERENCES layer_00_qiraat(qiraat_id)
           )
       """)

       # Repeat for all 14 layers...

   def populate_database(conn, qud_layers: dict):
       """Insert QUD layer data into SQLite tables"""
       for layer_name, layer_data in qud_layers.items():
           table_name = f"layer_{layer_name}"
           # Insert records...
   ```

5. **Cross-Qiraah Query Demonstration** (Jupyter notebook: `07-query-capability-demo.ipynb`):
   ```sql
   -- Query 1: Find verses where Hafs and Warsh differ in verse count
   SELECT
       h.sura_ref,
       COUNT(DISTINCT h.verse_number) as hafs_count,
       COUNT(DISTINCT w.verse_number) as warsh_count
   FROM layer_06_verses h
   LEFT JOIN layer_06_verses w ON h.sura_ref = w.sura_ref
   WHERE h.narration_ref = 'hafs_uuid' AND w.narration_ref = 'warsh_uuid'
   GROUP BY h.sura_ref
   HAVING hafs_count != warsh_count;

   -- Query 2: Extract page layout independent of text content
   SELECT page_number, start_verse_ref, end_verse_ref
   FROM layer_11_pages
   WHERE manuscript_ref = 'hafs_manuscript_uuid'
   ORDER BY page_number;

   -- Query 3: Character-level differences between narrations (requires JOIN across layers)
   -- (More complex - involves Layer 1 character comparison)
   ```

**Expected Outputs**:

1. **Simulation Code** (`experiments/rr-003-layer-simulation/`):
   - `prototype.py` - Main transformation script
   - `test_generation.py` - Generative layer testing
   - `generate_db.py` - SQLite database creation
   - `requirements.txt` - Python dependencies

2. **SQLite Database** (`experiments/rr-003-layer-simulation/results/qud_demo.db`):
   - 14 tables (one per layer)
   - Data for at least Hafs narration (6,236 verses)
   - Queryable via SQL

3. **Processing Metrics** (`experiments/rr-003-layer-simulation/results/metrics.json`):
   ```json
   {
     "narrations_processed": 7,
     "total_verses": 43652,
     "processing_time_seconds": 120,
     "memory_usage_mb": 450,
     "schema_validation": {
       "layer_00_qiraat": {"status": "pass", "count": 7},
       "layer_06_verses": {"status": "pass", "count": 43652},
       "layer_01_characters": {"status": "fail", "errors": "..."}
     }
   }
   ```

4. **Validation Report** (`experiments/rr-003-layer-simulation/results/validation_report.md`):
   - Character count verification per narration
   - Verse count verification per narration
   - Schema validation pass/fail summary
   - List of validation failures with root cause analysis

5. **Query Capability Examples** (`experiments/rr-003-layer-simulation/results/query_examples.md`):
   - At least 3 SQL queries impossible/impractical in QS-QIRAAT
   - Execution results showing feasibility
   - Performance notes

6. **Generation Success Analysis** (`experiments/rr-003-layer-simulation/results/generation_analysis.md`):
   - Layer 1 → Layer 3 generation accuracy percentage
   - Sample comparison: generated vs extracted symbols
   - Analysis of generation failures

### Success Criteria

- [ ] All 7 narrations processed through simulation
- [ ] Character count matches authoritative sources:
  - Hafs: 323,015 characters (or document actual count)
  - Other narrations: documented and validated
- [ ] Verse count matches authoritative sources:
  - Hafs: 6,236 verses
  - Warsh: 6,214 verses
  - Others: documented
- [ ] Schema validation executed (best-effort, failures documented)
- [ ] At least 3 cross-Qiraah queries demonstrated in SQLite
- [ ] Generative layer (Layer 1→3) achieves >95% accuracy
- [ ] Processing completes in reasonable time (< 10 minutes for Hafs and Warsh - Phase 1 per Constitution VI)

### Validation

- Automated validators: Run char/verse count checks, capture results
- Scholarly review: End-of-cycle expert reviews generated tajweed symbols
- Reproducibility: Another researcher can run prototype.py and reproduce results
- SQL queries: Execute example queries, verify results

---

## Experiment RR-011: UUID-Based Cross-Layer Mapping System Validation

### Hypothesis

A UUID-based EntityMapping system with semantic hashing can successfully create bidirectional cross-layer mappings for all 15 layers, handle expansion/contraction cases with position metadata, and enable efficient traversal of related entities across layer boundaries.

### Experimental Method

**Input Data**:
- RR-003 simulation output (15-layer QUD format with generated UUIDs)
- Sample verses demonstrating various mapping cardinalities (1:1, 1:N, N:1)

**Procedure**:

1. **EntityMapping Schema Implementation** (`schemas/cross-layer-mappings/entity-mapping-schema.json`):
   ```json
   {
     "mapping_id": "UUID",
     "source_layer": "integer (0-14)",
     "source_entity_id": "UUID",
     "target_layer": "integer (0-14)",
     "target_entity_ids": ["array of UUIDs"],
     "mapping_type": "expansion/contraction/identity/derivation",
     "cardinality": "1:1 | 1:N | N:1 | N:M",
     "position_metadata": "object - ordering for expansion/contraction",
     "mapping_version": "string",
     "semantic_hash": "string - SHA-256",
     "provenance": "object",
     "bidirectional_ref": "UUID"
   }
   ```

2. **Semantic Hash Generator** (`research-tools/semantic-hasher.py`):
   ```python
   import hashlib
   import json

   def generate_semantic_hash(source_uuid: str, target_uuids: list, mapping_type: str) -> str:
       """Generate SHA-256 hash representing relationship semantics"""
       hash_input = {
           "source": source_uuid,
           "targets": sorted(target_uuids),  # Sort for deterministic hashing
           "type": mapping_type
       }
       hash_string = json.dumps(hash_input, sort_keys=True)
       return hashlib.sha256(hash_string.encode()).hexdigest()
   ```

3. **Mapping Creation Test** (Jupyter notebook: `08-uuid-mapping-creation.ipynb`):
   - For sample data (first 3 suras from RR-003), create EntityMappings:
     - Layer 0 → Layer 1 (character → symbols, 1:N)
     - Layer 0 → Layer 3 (characters → word, N:1)
     - Layer 5 → Layer 6 (verses → surah, N:1)
   - Validate all mappings have:
     - Valid UUIDs (source and targets exist in respective layers)
     - Correct cardinality labels
     - Bidirectional references
     - Valid semantic hashes

4. **Bidirectional Traversal Test** (`experiments/rr-011-uuid-mapping/test_traversal.py`):
   ```python
   def traverse_forward(source_uuid: str, mappings: list) -> list:
       """Given source entity UUID, find all target entity UUIDs"""
       results = []
       for mapping in mappings:
           if mapping["source_entity_id"] == source_uuid:
               results.extend(mapping["target_entity_ids"])
       return results

   def traverse_backward(target_uuid: str, mappings: list) -> list:
       """Given target entity UUID, find all source entity UUIDs"""
       results = []
       for mapping in mappings:
           if target_uuid in mapping["target_entity_ids"]:
               results.append(mapping["source_entity_id"])
       return results
   ```

**Expected Outputs**:

1. **EntityMapping File** (`experiments/rr-011-uuid-mapping/results/entity_mappings.json`):
   - All cross-layer mappings for sample data
   - Estimated count: ~10,000 mappings for 3 suras

2. **Validation Report** (`experiments/rr-011-uuid-mapping/results/validation_report.md`):
   - UUID validity check results (100% of UUIDs resolve to entities)
   - Bidirectionality check (all forward mappings have reverse mappings)
   - Semantic hash uniqueness check

3. **Traversal Performance Metrics** (`experiments/rr-011-uuid-mapping/results/traversal_metrics.json`):
   - Query times for forward/backward traversal
   - Memory usage for mapping index

### Success Criteria

- [ ] EntityMapping schema defined with all required fields
- [ ] Semantic hash generator implemented and tested
- [ ] All mappings for sample data have valid UUIDs (100% validation pass)
- [ ] All mappings have bidirectional references
- [ ] Traversal operations complete in <100ms for sample data
- [ ] Semantic hashes are unique per relationship

### Validation

- Manual inspection of sample mappings
- Automated UUID resolution test (all UUIDs must exist in layers)
- Bidirectionality test (verify reverse mappings)

---

## Experiment RR-012: Verse Numbering Controversy Resolution

### Hypothesis

Using canonical_verse_id as a narration-independent identifier enables successful mapping of verses across narrations with different numbering schemes (e.g., Hafs 6,236 verses ↔ Warsh 6,214 verses), resolving the verse numbering controversy through UUID-based identity rather than positional numbering.

### Experimental Method

**Input Data**:
- RR-003 Hafs data (6,236 verses with canonical_verse_id)
- RR-003 Warsh data (6,214 verses with canonical_verse_id)
- Known cases of verse boundary differences (e.g., Surah 2)

**Procedure**:

1. **canonical_verse_id Assignment Strategy**:
   - For verses identical across narrations: assign same canonical_verse_id
   - For split verses (1 Hafs verse → 2 Warsh verses): create 1:N EntityMapping
   - For merged verses (2 Hafs verses → 1 Warsh verse): create N:1 EntityMapping

2. **Cross-Qiraah Mapping Creation** (`experiments/rr-012-verse-numbering/create_mappings.py`):
   ```python
   def map_hafs_to_warsh_verses(hafs_verses: list, warsh_verses: list) -> list:
       """Create canonical_verse_id mappings between Hafs and Warsh"""
       mappings = []

       for hafs_verse in hafs_verses:
           # Find corresponding Warsh verse(s) by text similarity or scholarly mapping
           warsh_matches = find_corresponding_verses(hafs_verse, warsh_verses)

           mapping = {
               "mapping_id": generate_uuid(),
               "source_layer": 5,  # Layer 5: Verse
               "source_entity_id": hafs_verse["verse_id"],
               "target_layer": 5,
               "target_entity_ids": [v["verse_id"] for v in warsh_matches],
               "canonical_verse_id": hafs_verse["canonical_verse_id"],
               "cardinality": f"1:{len(warsh_matches)}"
           }
           mappings.append(mapping)

       return mappings
   ```

3. **Validation Against Scholarly Sources**:
   - Compare generated mappings against known verse boundary differences
   - Document cases where Hafs/Warsh differ
   - Verify canonical_verse_id correctly identifies same semantic content

4. **Cross-Qiraah Query Test** (SQL):
   ```sql
   -- Find all verses where Hafs and Warsh have different numbering but same canonical content
   SELECT
       h.verse_number AS hafs_verse_num,
       w.verse_number AS warsh_verse_num,
       h.canonical_verse_id,
       h.verse_id AS hafs_verse_id,
       w.verse_id AS warsh_verse_id
   FROM layer_05_verses h
   JOIN layer_05_verses w ON h.canonical_verse_id = w.canonical_verse_id
   WHERE h.narration_ref = 'hafs_uuid' AND w.narration_ref = 'warsh_uuid'
     AND h.verse_number != w.verse_number;
   ```

**Expected Outputs**:

1. **Verse Boundary Mapping File** (`experiments/rr-012-verse-numbering/results/hafs_warsh_mappings.json`):
   - All Hafs↔Warsh verse mappings with canonical_verse_id
   - Cases of 1:N and N:1 cardinality documented

2. **Difference Analysis** (`experiments/rr-012-verse-numbering/results/difference_analysis.md`):
   - List of surahs where verse counts differ
   - Specific verses that split or merge
   - Statistical summary (e.g., "22 verses differ in boundary position")

3. **SQL Query Results** (`experiments/rr-012-verse-numbering/results/query_results.md`):
   - Example queries demonstrating cross-Qiraah verse lookup
   - Performance metrics for canonical_verse_id joins

### Success Criteria

- [ ] canonical_verse_id assigned to all verses in both Hafs and Warsh
- [ ] All known verse boundary differences correctly mapped
- [ ] SQL queries using canonical_verse_id successfully retrieve corresponding verses across narrations
- [ ] 100% of Hafs verses map to Warsh verses (either 1:1, 1:N, or via scholarly reference)
- [ ] Verse count differences (6,236 Hafs vs 6,214 Warsh) explained by mappings

### Validation

- Compare against traditional Islamic scholarship on verse numbering systems
- Scholarly review of canonical_verse_id assignments
- Manual verification of sample split/merge cases

---

## Experiment RR-013: Orthographic Transformation Mapping

### Hypothesis

Character-level UUID mappings with position metadata can successfully handle Uthmani↔Qiasy orthographic transformations including expansion cases (1 Uthmani char → 2 Qiasy chars, e.g., "الصلوة" → "الصلاة") and contraction cases (N Uthmani → 1 Qiasy), enabling precise tracking of orthographic variants.

### Experimental Method

**Input Data**:
- RR-003 Layer 0 character data (Uthmani script with UUIDs)
- RR-003 Layer 12b Qiasy orthography data
- Sample verses with known orthographic transformations

**Procedure**:

1. **Transformation Rule Catalog** (`research-tools/orthographic-rules.json`):
   ```json
   {
     "expansion_rules": [
       {"uthmani": "ة", "qiasy": ["ت", "ا"], "description": "Ta marbuta expansion"},
       {"uthmani": "ٰ", "qiasy": ["ا", "ل", "ف"], "description": "Alif khanjariyyah expansion"}
     ],
     "contraction_rules": [
       {"uthmani": ["ا", "ل"], "qiasy": "ا", "description": "Alif-lam contraction"}
     ]
   }
   ```

2. **Character Mapping Creation** (`experiments/rr-013-orthographic/create_char_mappings.py`):
   ```python
   def create_orthographic_mapping(uthmani_char_uuid: str, qiasy_char_uuids: list, position_metadata: dict) -> dict:
       """Create EntityMapping for Uthmani → Qiasy character transformation"""
       return {
           "mapping_id": generate_uuid(),
           "source_layer": 0,  # Layer 0: Character Composition (Uthmani)
           "source_entity_id": uthmani_char_uuid,
           "target_layer": 0,  # Also Layer 0 (Qiasy characters)
           "target_entity_ids": qiasy_char_uuids,
           "mapping_type": "expansion" if len(qiasy_char_uuids) > 1 else "identity",
           "cardinality": f"1:{len(qiasy_char_uuids)}",
           "position_metadata": position_metadata,  # {qiasy_uuid_1: 0, qiasy_uuid_2: 1, ...}
           "semantic_hash": generate_semantic_hash(uthmani_char_uuid, qiasy_char_uuids, "orthographic"),
           "provenance": {"orthography": "uthmani_to_qiasy", "transformation_rule": "..."}
       }
   ```

3. **Expansion Case Test**:
   - Find all instances of Uthmani "ة" (ta marbuta) in sample data
   - Generate mappings to corresponding Qiasy "ت" + "ا"
   - Verify position_metadata preserves ordering

4. **Reconstruction Test**:
   ```python
   def reconstruct_qiasy_from_uthmani(uthmani_text: str, char_mappings: list) -> str:
       """Use character mappings to transform Uthmani → Qiasy"""
       qiasy_chars = []
       for uthmani_char_uuid in uthmani_text_uuids:
           mapping = find_mapping(uthmani_char_uuid, char_mappings)
           qiasy_char_uuids = mapping["target_entity_ids"]
           # Use position_metadata to order characters
           ordered_chars = sort_by_position_metadata(qiasy_char_uuids, mapping["position_metadata"])
           qiasy_chars.extend(ordered_chars)
       return "".join(qiasy_chars)
   ```

**Expected Outputs**:

1. **Character Mapping File** (`experiments/rr-013-orthographic/results/char_mappings.json`):
   - All Uthmani↔Qiasy character mappings for sample data
   - Expansion and contraction cases documented

2. **Transformation Analysis** (`experiments/rr-013-orthographic/results/transformation_analysis.md`):
   - Count of expansion cases (1:N) vs identity cases (1:1)
   - Statistical summary of transformation types
   - Example mappings with position_metadata visualization

3. **Reconstruction Validation** (`experiments/rr-013-orthographic/results/reconstruction_test.md`):
   - Comparison of reconstructed Qiasy text vs QS-QIRAAT `aya_text_emlaey`
   - Character-level diff for any mismatches

### Success Criteria

- [ ] All orthographic transformation rules cataloged
- [ ] Character mappings created for all sample verses
- [ ] All expansion cases (1:N) have position_metadata
- [ ] Reconstructed Qiasy text matches QS-QIRAAT `aya_text_emlaey` >99% accuracy
- [ ] All mappings have valid UUIDs resolving to Layer 0 characters

### Validation

- Compare reconstructed text byte-for-byte with QS-QIRAAT data
- Manual inspection of complex transformation cases
- Scholarly review of transformation rules

---

## Experiment RR-014: QUD Orchestrator Context Resolution Design

**Research Question**: Can we design a QUD Orchestrator component that extracts context parameters from queries, resolves layer versions, and routes queries to appropriate MUDMAJ layer versions?

**Hypothesis**: A context resolution algorithm can map query parameters to specific layer versions with <100ms overhead, handle cross-context queries, and maintain context isolation.

**Dependencies**: RR-002 (schemas), RR-011-013 (UUID mappings)

### Experimental Procedure

#### Step 1: Context Parameter Discovery

1. Analyze QS-QIRAAT dataset to identify actual context parameters:
   - Which narrations are actually present? (Hafs, Warsh, etc.)
   - Which orthographic systems exist? (Uthmani, Qiasy, Imla'i)
   - Which editions? (King Fahd Complex versions)
   - Which scholarly traditions are distinguishable?

2. Research Quranic scholarly literature to identify:
   - Valid tajweed schools and their differences
   - Geographic traditions (Medina, Kufa, Basra, etc.)
   - Historical vs contemporary encoding differences

3. Define minimal context parameters:
   - Which parameters are mandatory for unambiguous layer version resolution?
   - Which are optional with default values?
   - Parameter dependencies (e.g., tajweed_school → geographic_origin)?

**Deliverable**: Context schema with validated parameter set

#### Step 2: Context Inheritance Rules Design

1. Map context parameters to layers:
   - Which parameters affect Layer 0 (Character Composition)?
   - Which affect Layer 5 (Verse Structure)?
   - Which are global vs layer-specific?

2. Design inheritance hierarchy:
   - If user specifies `narration: hafs`, which layers does this affect?
   - If user adds `orthographic_system: uthmani`, does this override or complement?
   - Default parameter values when not specified

3. Implement parameter propagation algorithm:
   ```python
   def resolve_context_for_layer(layer_number, user_context):
       # Apply inheritance rules
       # Merge with defaults
       # Validate parameter combinations
       return resolved_context
   ```

**Deliverable**: Context inheritance specification document

#### Step 3: Context Resolution Algorithm Design

1. Design context extraction from queries:
   - Natural language query parsing (e.g., "Get verse 2:255 in Hafs with Uthmani script")
   - Structured query format (JSON, GraphQL, REST API)
   - Default context when not specified

2. Implement context hash generation:
   ```python
   def hash_context(context_parameters):
       # Sort parameters for deterministic hashing
       # Generate SHA-256 hash
       # Use for version registry lookup
       return context_hash
   ```

3. Design version selection logic:
   - Lookup in VersionRegistry: `(layer_number, context_hash) → layer_version_id`
   - Fallback strategy when exact match not found
   - Priority rules for conflict resolution

**Deliverable**: Context resolution algorithm pseudocode + Python prototype

#### Step 4: Query Routing Design

1. Design query flow:
   ```
   Client Query → Context Extraction → Layer Identification →
   Context Resolution → Version Selection → MUDMAJ Query → Result Assembly
   ```

2. Implement routing logic:
   - Single-context queries: Route to one layer version
   - Cross-context queries: Route to multiple layer versions, assemble results
   - Cross-layer queries within context: Route to multiple layers, join results

3. Design result assembly:
   - How to combine results from multiple layer versions?
   - How to present differences in cross-context comparisons?
   - Format: JSON, GraphQL response, custom DSL?

**Deliverable**: Query routing specification + flow diagrams

#### Step 5: Cross-Context Query Validation

1. Design cross-context query patterns:
   - **Pattern 1**: "Compare verse X in Hafs vs Warsh"
   - **Pattern 2**: "Show verse X in all orthographic systems"
   - **Pattern 3**: "Find differences between contexts A and B for layer L"

2. Implement cross-context query handler:
   ```python
   def execute_cross_context_query(query, contexts_list):
       results = {}
       for context in contexts_list:
           resolved = resolve_context_for_layers(query.layers, context)
           results[context] = query_mudmaj(resolved)
       return compare_results(results)
   ```

3. Design comparison strategies:
   - Character-level diff for text comparisons
   - UUID-based alignment for entity comparisons
   - Canonical identities for cross-context entity matching

**Deliverable**: Cross-context query examples + implementation

#### Step 6: Orchestrator Prototype Implementation

1. Implement core Orchestrator class:
   ```python
   class QUDOrchestrator:
       def __init__(self, version_registry, mudmaj_connector):
           self.registry = version_registry
           self.mudmaj = mudmaj_connector

       def execute_query(self, query, user_context=None):
           # Extract context from query
           # Resolve layer versions
           # Route to MUDMAJ
           # Assemble results
           pass

       def resolve_context(self, layer_number, user_context):
           # Apply inheritance rules
           # Merge with defaults
           # Lookup in registry
           pass
   ```

2. Test with sample queries:
   - Single-context query: "Get Surah Al-Fatiha in Hafs"
   - Cross-context query: "Compare Al-Fatiha Hafs vs Warsh"
   - Cross-layer query: "Get verse text with page layout info"

3. Measure performance:
   - Context resolution time (<100ms target)
   - Query routing overhead
   - Result assembly time

**Deliverable**: Working Python prototype in `experiments/rr-014-orchestrator/`

### Validation

- Context parameter set validated against scholarly sources
- Context resolution produces correct layer versions for test cases
- Cross-context queries return correct comparative results
- Performance targets met (<100ms context resolution)
- Context isolation validated (queries in one context don't return data from another)

---

## Experiment RR-015: MUDMAJ Database Schema Design

**Research Question**: Can we design a MUDMAJ storage schema that organizes multiple layer versions per context, implements efficient delta storage, and optimizes for query performance?

**Hypothesis**: A well-designed storage schema can achieve >40% storage savings through delta optimization while maintaining <100ms query performance for context-based lookups.

**Dependencies**: RR-002 (layer schemas), RR-014 (context schema)

### Experimental Procedure

#### Step 1: Storage Technology Selection

1. Evaluate storage options:
   - **SQL (PostgreSQL)**: Pros: ACID, mature tooling, excellent indexing. Cons: Schema rigidity, joins expensive
   - **NoSQL (MongoDB)**: Pros: Flexible schema, horizontal scaling. Cons: No joins, consistency trade-offs
   - **Graph DB (Neo4j)**: Pros: Relationship queries, perfect for UUID mappings. Cons: Learning curve, specialized
   - **Hybrid**: SQL for metadata, NoSQL for layer data, Graph for mappings

2. Benchmark queries for each technology:
   - Context-based lookup: `Get Layer 5 for context {hafs, uthmani}`
   - Cross-layer join: `Get verse text + page layout`
   - Cross-context comparison: `Compare Layer 5 Hafs vs Warsh`

3. Decision criteria:
   - Query performance (<100ms target)
   - Storage efficiency (delta optimization support)
   - Development velocity (Python library ecosystem)
   - Scalability (can handle 100+ layer versions)

**Deliverable**: Technology selection ADR with benchmark results

#### Step 2: Version Registry Design

1. Design VersionRegistry schema:
   ```sql
   CREATE TABLE version_registry (
       registry_id UUID PRIMARY KEY,
       layer_number INTEGER NOT NULL,
       context_hash VARCHAR(64) NOT NULL,  -- SHA-256 of sorted context params
       context_parameters JSONB NOT NULL,
       layer_version_id UUID NOT NULL REFERENCES layer_versions(id),
       priority INTEGER DEFAULT 0,
       active BOOLEAN DEFAULT TRUE,
       created_timestamp TIMESTAMPTZ NOT NULL,
       UNIQUE (layer_number, context_hash)
   );

   CREATE INDEX idx_layer_context ON version_registry(layer_number, context_hash);
   CREATE INDEX idx_version_ref ON version_registry(layer_version_id);
   ```

2. Implement context hash generator:
   ```python
   def generate_context_hash(context_params):
       sorted_params = sort_dict(context_params)
       json_str = json.dumps(sorted_params, sort_keys=True)
       return hashlib.sha256(json_str.encode()).hexdigest()
   ```

3. Test registry queries:
   - Lookup performance: O(1) for (layer_number, context_hash)
   - Bulk inserts: Can insert all layer versions efficiently
   - Update scenarios: Activating/deactivating versions

**Deliverable**: VersionRegistry schema + implementation

#### Step 3: LayerVersion Metadata Schema

1. Design LayerVersion table:
   ```sql
   CREATE TABLE layer_versions (
       layer_version_id UUID PRIMARY KEY,
       layer_number INTEGER NOT NULL,
       context_parameters JSONB NOT NULL,
       version_semver VARCHAR(20) NOT NULL,
       entity_count INTEGER NOT NULL,
       parent_version_id UUID REFERENCES layer_versions(layer_version_id),
       generation_rules TEXT,
       storage_location TEXT NOT NULL,
       validation_status JSONB,
       provenance JSONB,
       created_timestamp TIMESTAMPTZ NOT NULL
   );

   CREATE INDEX idx_layer_number ON layer_versions(layer_number);
   CREATE INDEX idx_context_params ON layer_versions USING GIN (context_parameters);
   ```

2. Implement version lineage tracking:
   - Query: "Find all versions derived from parent X"
   - Recursive CTE for version tree traversal

3. Design validation_status structure:
   ```json
   {
     "character_count": 323015,
     "verse_count": 6236,
     "schema_validation": "pass",
     "last_validated": "2025-11-04T10:00:00Z",
     "scholarly_review": {
       "status": "approved",
       "reviewer": "scholar_id",
       "date": "2025-11-04"
     }
   }
   ```

**Deliverable**: LayerVersion schema + queries

#### Step 4: Layer Data Storage Design

1. Design layer data organization:
   - **Option A**: One table per layer + version: `layer_05_hafs_v1_0_0`
   - **Option B**: Single table per layer with version_id column: `layer_05_verses(version_id, ...)`
   - **Option C**: Document store with version in document: `{version_id: ..., data: ...}`

2. Evaluate trade-offs:
   - **Option A**: Fastest queries (no filtering), but schema proliferation
   - **Option B**: Single schema, slower queries (must filter by version_id)
   - **Option C**: Most flexible, but requires document store

3. Implement sample layer storage:
   ```python
   # Example: Layer 5 (Verse) storage
   class Layer05Verse(BaseModel):
       entity_id: UUID
       layer_version_id: UUID
       verse_number: int
       canonical_verse_id: UUID
       word_refs: List[UUID]
       # ... other fields
   ```

**Deliverable**: Layer data storage schema + implementation

#### Step 5: Delta Storage Mechanism Design

1. Analyze layer data for shared entities:
   - **Layer 6 (Surah metadata)**: Compare Hafs vs Warsh - measure overlap
   - **Layer 8 (Chapter structure)**: Compare Uthmani vs Qiasy - measure overlap
   - **Layer 11-12 (Page/line layout)**: Compare editions - measure overlap

2. Design delta storage strategy:
   ```
   base_entities/         # Immutable shared entities
   ├── layer_06_surah/
   │   └── surah_001.json  # Al-Fatiha metadata (shared across all contexts)

   version_deltas/        # Context-specific differences
   ├── layer_06_hafs/
   │   └── overrides.json  # Only fields that differ from base
   ```

3. Implement entity deduplication:
   ```python
   def store_layer_version_with_delta(layer_data, base_version_id):
       base_data = load_base_version(base_version_id)
       delta = compute_delta(base_data, layer_data)
       store_delta(delta)
       return delta_storage_ref
   ```

4. Measure storage savings:
   - Without delta: Sum of all layer version sizes
   - With delta: Base + all deltas
   - **Target**: >40% reduction

**Deliverable**: Delta storage implementation + savings analysis

#### Step 6: Cross-Layer Mapping Storage

1. Design EntityMapping table:
   ```sql
   CREATE TABLE entity_mappings (
       mapping_id UUID PRIMARY KEY,
       source_layer INTEGER NOT NULL,
       source_entity_id UUID NOT NULL,
       target_layer INTEGER NOT NULL,
       target_entity_ids UUID[] NOT NULL,
       mapping_type VARCHAR(50) NOT NULL,
       cardinality VARCHAR(10) NOT NULL,
       position_metadata JSONB,
       mapping_version VARCHAR(20),
       semantic_hash VARCHAR(64),
       provenance JSONB,
       bidirectional_ref UUID REFERENCES entity_mappings(mapping_id)
   );

   CREATE INDEX idx_source ON entity_mappings(source_layer, source_entity_id);
   CREATE INDEX idx_target ON entity_mappings(target_layer, target_entity_ids);
   ```

2. Implement bidirectional traversal:
   ```python
   def get_related_entities(entity_id, source_layer, target_layer):
       # Forward mapping
       mapping = query("SELECT * FROM entity_mappings WHERE source_entity_id = ?", entity_id)
       # Reverse mapping
       reverse = query_via_ref(mapping.bidirectional_ref)
       return mapping.target_entity_ids
   ```

3. Test mapping queries:
   - "Find all Layer 0 characters for this Layer 3 word"
   - "Find Layer 5 verses containing this Layer 0 character"
   - Performance: <50ms for cross-layer traversal

**Deliverable**: EntityMapping storage + query implementation

#### Step 7: Provenance and Audit Tracking

1. Design transformation_logs table:
   ```sql
   CREATE TABLE transformation_logs (
       log_id UUID PRIMARY KEY,
       layer_version_id UUID NOT NULL REFERENCES layer_versions(layer_version_id),
       operation VARCHAR(50) NOT NULL,  -- extract, generate, transform
       source_dataset VARCHAR(255),
       transformation_rule_id VARCHAR(255),
       input_count INTEGER,
       output_count INTEGER,
       execution_time_ms INTEGER,
       status VARCHAR(50),
       error_log TEXT,
       created_timestamp TIMESTAMPTZ NOT NULL
   );
   ```

2. Design validation_results table:
   ```sql
   CREATE TABLE validation_results (
       validation_id UUID PRIMARY KEY,
       layer_version_id UUID NOT NULL REFERENCES layer_versions(layer_version_id),
       validation_type VARCHAR(50) NOT NULL,  -- char_count, verse_count, schema
       expected_value JSONB,
       actual_value JSONB,
       status VARCHAR(20) NOT NULL,  -- pass, fail, warning
       error_details TEXT,
       validated_timestamp TIMESTAMPTZ NOT NULL
   );
   ```

3. Implement audit trail queries:
   - "Show transformation history for layer version X"
   - "List all validation failures"
   - "Find all versions derived from source dataset Y"

**Deliverable**: Provenance tracking implementation

### Validation

- Storage technology choice justified with benchmarks
- VersionRegistry lookups achieve <100ms performance
- Delta storage achieves >40% savings (or document actual savings)
- Cross-layer mapping queries execute in <50ms
- Provenance tracking captures complete audit trail
- All schemas validated with sample data

---

## Experiment RR-016: Context-Aware Query System Validation

**Research Question**: Can we validate the complete context-aware query system by executing sample queries requiring context resolution, demonstrating correct version selection, and proving context isolation?

**Hypothesis**: The integrated QUD Orchestrator + MUDMAJ system can correctly route queries to appropriate layer versions, handle cross-context comparisons, and maintain <200ms end-to-end query latency.

**Dependencies**: RR-014 (Orchestrator), RR-015 (MUDMAJ)

### Experimental Procedure

#### Step 1: Single-Context Query Validation

1. Define test queries:
   - **Q1**: "Get Surah Al-Fatiha in Hafs narration"
   - **Q2**: "Get verse 2:255 with Uthmani orthography"
   - **Q3**: "Get page 1 layout from King Fahd Complex edition"

2. Execute queries with Orchestrator:
   ```python
   orchestrator = QUDOrchestrator(version_registry, mudmaj)

   result = orchestrator.execute_query({
       "type": "get_surah",
       "surah_number": 1,
       "context": {
           "narration": "hafs",
           "orthographic_system": "uthmani"
       }
   })
   ```

3. Validate results:
   - Correct layer versions selected?
   - Character counts match expected values?
   - Verse counts match expected values?
   - Query latency <200ms?

**Deliverable**: Single-context query test suite + results

#### Step 2: Cross-Context Query Validation

1. Define cross-context test queries:
   - **Q4**: "Compare Surah Al-Fatiha in Hafs vs Warsh"
   - **Q5**: "Show verse 2:255 in all orthographic systems"
   - **Q6**: "Find verse count differences between Hafs and Warsh"

2. Execute cross-context queries:
   ```python
   result = orchestrator.execute_cross_context_query({
       "type": "compare_surah",
       "surah_number": 1,
       "contexts": [
           {"narration": "hafs"},
           {"narration": "warsh"}
       ]
   })
   ```

3. Validate comparison results:
   - Canonical identities correctly matched?
   - Differences accurately identified?
   - Character-level diffs correct?
   - Verse boundary differences detected?

**Deliverable**: Cross-context query test suite + results

#### Step 3: Cross-Layer Query Validation

1. Define cross-layer test queries:
   - **Q7**: "Get verse text with character composition breakdown"
   - **Q8**: "Get verse with page and line layout information"
   - **Q9**: "Get word with tajweed marks and rendering rules"

2. Execute cross-layer queries:
   ```python
   result = orchestrator.execute_query({
       "type": "get_verse_with_layers",
       "verse_ref": "2:255",
       "layers": [0, 1, 2, 3, 5, 11, 12],  # Multiple layers
       "context": {"narration": "hafs"}
   })
   ```

3. Validate layer joining:
   - UUID references correctly resolved?
   - Cross-layer data correctly assembled?
   - No missing entities?
   - Query latency <200ms?

**Deliverable**: Cross-layer query test suite + results

#### Step 4: Context Isolation Validation

1. Design isolation test cases:
   - **Test 1**: Query Hafs context, verify Warsh data NOT returned
   - **Test 2**: Query Uthmani orthography, verify Qiasy data NOT returned
   - **Test 3**: Query edition A, verify edition B layout NOT returned

2. Execute isolation tests:
   ```python
   hafs_result = orchestrator.execute_query({
       "type": "get_surah",
       "surah_number": 1,
       "context": {"narration": "hafs"}
   })

   # Verify: hafs_result contains ONLY Hafs verse data (6,236 verses)
   # NOT Warsh verse data (6,214 verses)
   assert hafs_result.total_verses == 6236  # Hafs-specific count
   ```

3. Validate negative cases:
   - Query with invalid context → error handling correct?
   - Query with incomplete context → defaults applied correctly?
   - Query with conflicting parameters → conflict resolution correct?

**Deliverable**: Context isolation test suite + results

#### Step 5: Ambiguous Context Handling

1. Define ambiguous context scenarios:
   - **Scenario 1**: User doesn't specify orthography → default to Uthmani?
   - **Scenario 2**: User specifies edition but not narration → error or default?
   - **Scenario 3**: User specifies conflicting parameters → which takes priority?

2. Design resolution strategy:
   ```python
   def resolve_ambiguous_context(user_context):
       defaults = {
           "narration": "hafs",  # Most common
           "orthographic_system": "uthmani",  # Classical default
           "edition": "king_fahd_complex"
       }
       resolved = merge_with_defaults(user_context, defaults)
       validate_parameter_constraints(resolved)
       return resolved
   ```

3. Test ambiguous queries:
   - Query with minimal context
   - Query with partial context
   - Verify correct defaults applied
   - Verify result matches expected context

**Deliverable**: Ambiguous context handling specification + tests

#### Step 6: Performance Benchmarking

1. Define performance test suite:
   - 100 single-context queries (different verses, surahs)
   - 100 cross-context queries (all Hafs vs Warsh comparisons)
   - 100 cross-layer queries (verses with full layer breakdown)

2. Measure latencies:
   - Context resolution time
   - Version lookup time
   - MUDMAJ query time
   - Result assembly time
   - **Total end-to-end time**

3. Performance targets:
   - Context resolution: <100ms
   - Single-context query: <200ms end-to-end
   - Cross-context query: <500ms end-to-end
   - Cross-layer query: <300ms end-to-end

4. Identify bottlenecks:
   - Profiling with Python cProfile
   - Query explain plans (if SQL)
   - Index usage analysis

**Deliverable**: Performance benchmark results + optimization recommendations

### Validation

- Single-context queries return correct layer versions
- Cross-context queries correctly compare across contexts
- Cross-layer queries correctly join multiple layers via UUID references
- Context isolation verified (no data leakage between contexts)
- Ambiguous contexts resolved correctly with documented defaults
- Performance targets met for all query types
- Error handling gracefully manages invalid queries

---

## Research Cycle Structure

Each RR constitutes one research cycle:

1. **RR-001 Cycle** (Duration: ~2-3 days):
   - Execute layer separation analysis
   - Document findings in `findings/rr-001-*.md`
   - Create ADR if architectural decisions made
   - Scholarly review: Expert validates field→layer mapping
   - **Gate**: Mapping table 100% complete before proceeding to RR-002

2. **RR-002 Cycle** (Duration: ~3-5 days):
   - Design schemas based on RR-001 findings with UUID fields
   - Document schemas with README per layer including cross-layer mapping specifications
   - Test schemas on sample data
   - Scholarly review: Expert reviews schema design for domain accuracy
   - **Gate**: All 15 schemas + EntityMapping schema defined and validated before proceeding to RR-003

3. **RR-003 Cycle** (Duration: ~5-7 days):
   - Build prototype using RR-002 schemas with UUID generation
   - Process Hafs and Warsh narrations (Phase 1 per Constitution VI)
   - Generate validation reports
   - Scholarly review: Expert reviews generated data (especially Layer 1 symbols)
   - **Gate**: All validation criteria met or failures documented before proceeding to UUID mapping experiments

4. **RR-011 Cycle** (Duration: ~2-3 days):
   - Implement UUID-based EntityMapping system
   - Create cross-layer mappings for sample data
   - Validate bidirectionality and semantic hashing
   - **Gate**: Mapping system validated before RR-012/013

5. **RR-012 Cycle** (Duration: ~3-4 days):
   - Implement canonical_verse_id strategy
   - Map Hafs↔Warsh verse boundaries
   - Validate against scholarly sources
   - **Gate**: Verse numbering resolution demonstrated

6. **RR-013 Cycle** (Duration: ~3-4 days):
   - Implement orthographic transformation mappings
   - Test Uthmani↔Qiasy character mappings
   - Validate reconstruction accuracy
   - **Gate**: Orthographic transformations validated

## Failure Handling

**Best-Effort Validation Philosophy**: Validation failures do NOT block research progression. Instead:

1. **Document Failure**: Capture exact error, input data, expected vs actual output
2. **Analyze Root Cause**: Is it data quality issue? Schema design issue? Algorithm bug? Unicode handling issue?
3. **Report Impact**: Does this failure invalidate hypothesis? Or is it edge case?
4. **Iterate**: Refine schema/algorithm if needed, or document as known limitation

**Example Failure Scenarios**:
- Character count mismatch by 10 characters → Root cause: Unicode normalization difference → ADR documents NFC vs NFD decision
- Schema validation fails for 5 verses → Root cause: QS-QIRAAT data has unexpected field → Schema refined to accommodate, or verses marked as exceptions
- Generative Layer 3 achieves 85% accuracy (below 95% target) → Hypothesis partially validated, document what cases fail, suggest future research

## Timeline & Milestones

| Milestone | Target Date | Deliverable |
|-----------|-------------|-------------|
| RR-001 Complete | Day 3 | Mapping table, conflation matrix, gap analysis |
| RR-002 Complete | Day 8 | 15 schemas (JSON + Pydantic) + EntityMapping schema, transformation spec, redundancy report |
| RR-003 Complete | Day 15 | Prototype code with UUID generation, SQLite database, validation report, query examples |
| RR-011 Complete | Day 18 | EntityMapping system, bidirectional traversal tests, validation report |
| RR-012 Complete | Day 22 | Hafs↔Warsh verse mappings, canonical_verse_id implementation, cross-Qiraah queries |
| RR-013 Complete | Day 26 | Orthographic transformation mappings, reconstruction tests, accuracy validation |
| Scholarly Review 1 | Day 4 | Expert validates RR-001 mapping |
| Scholarly Review 2 | Day 9 | Expert validates RR-002 schemas |
| Scholarly Review 3 | Day 16 | Expert validates RR-003 generated data |
| Scholarly Review 4 | Day 27 | Expert validates UUID mapping system and verse/orthographic transformations |
| Final Report | Day 30 | Consolidated research log with all 6 RR findings |

## Tools & Environment

- **Python 3.11+**: Primary language
- **Jupyter Lab**: Interactive development environment
- **Libraries**: pandas, NLTK, jsonschema, pydantic, matplotlib, seaborn, plotly, sqlite3
- **Version Control**: Git for all code, schemas, findings
- **Data Location**: `/Users/mac/Work/ITQAN Community/QUD/QS - QIRAAT/`
- **Output Location**: `experiments/rr-00X-*/results/`, `schemas/`, `findings/`

## Success Indicators

Research is successful if:
1. ✅ All 6 hypotheses tested (RR-001 through RR-003, RR-011 through RR-013) (even if results are negative)
2. ✅ Findings documented (positive AND negative results)
3. ✅ 15 layer schemas + EntityMapping schema defined and validated with UUID support
4. ✅ Prototype demonstrates layer separation feasibility (or documents infeasibility)
5. ✅ UUID-based cross-layer mapping system validated for all mapping types
6. ✅ Verse numbering controversy resolution demonstrated via canonical_verse_id
7. ✅ Orthographic transformation mappings validated with >99% reconstruction accuracy
8. ✅ Scholarly review confirms theological accuracy
9. ✅ Research produces actionable insights for next phase (production architecture or pivot)

**Research failure that produces learning is success. The goal is validated knowledge, not perfect code.**
