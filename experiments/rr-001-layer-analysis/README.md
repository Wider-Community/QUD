# RR-001: Layer Separation Analysis

**Research Requirement**: RR-001
**Status**: In Progress
**Started**: 2025-11-05
**Priority**: P1 (First Hypothesis)

## Research Goal

Identify which of the Quranic data layers (currently 17 identified layers) are currently mixed in the QS-QIRAAT dataset.

## Hypothesis

**Primary Hypothesis**: The QS-QIRAAT dataset conflates multiple distinct layers into a single flat data structure, and this conflation can be identified and quantified through schema analysis.

**Sub-Hypotheses**:
1. Single QS-QIRAAT fields contain data from multiple QUD layers
2. The conflation can be mapped systematically (field → layer mapping)
3. Some QUD layers are entirely missing from QS-QIRAAT
4. Cross-Qiraat comparison reveals layer-specific vs shared concerns

## Independent Validation Criteria

Manual mapping of each QS-QIRAAT field to the layer taxonomy (currently 17 identified layers) must produce:
1. ✓ A complete mapping table (no unmapped fields)
2. ✓ A layer conflation matrix (which layers mixed in which fields)
3. ✓ A gap analysis (which layers absent from QS-QIRAAT)
4. ✓ Cross-Qiraat variance report (Hafs vs Warsh field differences)

**Validation Success**: If manual analysis produces consistent, unambiguous mappings with clear evidence of layer conflation.

**Validation Failure**: If fields cannot be mapped to layers, or no conflation is evident.

## Data Layer Dependencies

Requires understanding of all identified layers (currently 17) to perform mapping analysis.

**NOTE**: The exact number of layers is under investigation per 2025-11-04 update. Current analysis uses 17 as working count.

## QS-QIRAAT Schema

The dataset contains **11 fields** per verse record:

1. `id` - Unique verse identifier
2. `jozz` - Juz number (1-30)
3. `page` - Mushaf page number
4. `sura_no` - Surah number (1-114)
5. `sura_name_en` - Surah name (English)
6. `sura_name_ar` - Surah name (Arabic)
7. `line_start` - Starting line on page
8. `line_end` - Ending line on page
9. `aya_no` - Verse number within surah
10. `aya_text` - Full verse text (Arabic)
11. `aya_text_emlaey` - Simplified text (modern orthography)

## QUD Layer Taxonomy (17 Layers)

Reference layers for mapping analysis:

**Character Layers (0-2)**:
- Layer 0: Character Composition
- Layer 1: Character Symbols
- Layer 2: Character Paired Data

**Structural Layers (3-8)**:
- Layer 3: Word Structure
- Layer 4: Sentence Structure
- Layer 5: Verse Structure
- Layer 6: Surah Structure
- Layer 7: Division Structure
- Layer 8: Chapter Structure

**Variant Layers (9-10)**:
- Layer 9: Qiraat/Manuscript
- Layer 10: Edition Variants

**Layout Layers (11-12)**:
- Layer 11: Page Layout
- Layer 12: Line Layout

**Meta Layers (13-14)**:
- Layer 13: Orthographic Systems
- Layer 14: Readers/Narrators

**Additional Layers (15-16)** (identified but not yet fully specified):
- Layer 15: TBD
- Layer 16: TBD

## Methodology

### Phase 1: Field Analysis
1. Extract complete QS-QIRAAT schema
2. Document data types, constraints, relationships
3. Identify field semantics and purposes

### Phase 2: Layer Mapping
1. For each QS-QIRAAT field, identify which QUD layer(s) it represents
2. Assign confidence scores (1.0 = certain, 0.5 = probable, 0.0 = uncertain)
3. Document reasoning for each mapping

### Phase 3: Conflation Analysis
1. Identify fields that conflate multiple layers
2. Build NxN conflation matrix
3. Quantify degree of conflation

### Phase 4: Gap Analysis
1. Identify QUD layers not present in QS-QIRAAT
2. Document missing data concerns
3. Assess impact on layer separation feasibility

### Phase 5: Cross-Qiraat Validation (Hafs vs Warsh)
1. Compare field values between Hafs and Warsh datasets
2. Identify Qiraat-specific vs shared fields
3. Document verse count differences (6,236 vs 6,214)

## Expected Outcomes

### If Hypothesis Confirmed:
- Clear evidence of layer conflation in QS-QIRAAT fields
- Systematic mapping table produced
- Gap analysis identifies missing layers
- Proceed to RR-002 (Schema Design) with confidence

### If Hypothesis Refuted:
- QS-QIRAAT already separates layers cleanly
- No conflation evident in field analysis
- Re-evaluate layer taxonomy
- Adjust research direction

## Code Quality

**Tier 1 - Experimental Code**: All code in this experiment is experimental research code. It is acceptable to have:
- Quick prototypes
- Hardcoded values
- Minimal error handling
- Code duplication
- No tests

Mark all experimental code with `# EXPERIMENTAL:` comments.

## Deliverables

### Required Outputs:
1. `results/mapping_table.csv` - Field → Layer mapping with confidence scores
2. `results/conflation_matrix.csv` - NxN matrix of layer conflation
3. `results/gap_analysis.md` - Missing layers report
4. `results/narration_variance.md` - Hafs vs Warsh comparison
5. `results/visualizations/` - Heatmaps and diagrams
6. `results/analysis.md` - Final analysis and findings

### Success Criteria:
- All 11 QS-QIRAAT fields mapped to layers
- Conflation quantified with evidence
- Gap analysis complete
- Hypothesis outcome clearly stated (confirmed/refuted)

## References

- Spec: `/specs/001-quranic-layer-architecture/spec.md`
- Data Model: `/specs/001-quranic-layer-architecture/data-model.md`
- QS-QIRAAT Dataset: [Source TBD]

## Research Log

### 2025-11-05: Experiment Setup
- Created experiment directory structure
- Documented hypothesis and methodology
- Prepared for data gathering phase

---

**Next Step**: Gather QS-QIRAAT Hafs and Warsh datasets (T035-T036)
