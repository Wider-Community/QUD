# RR-001: Cross-Qiraat Variance Report

**Analysis Date**: 2025-11-05
**Scope**: Phase 1 (Hafs vs Warsh only)

## Summary

Comparison of Hafs (from Asim) and Warsh (from Nafi) datasets.

## Verse Count Differences

| Narration | Verse Count | Difference |
|-----------|-------------|------------|
| Hafs      | 6,236       | baseline   |
| Warsh     | 6,214       | -22 verses |

**Analysis**: Warsh has 22 fewer verses than Hafs due to different verse boundary conventions.

## Field Variance Analysis

### Fields Expected to Vary

1. **aya_text**: Primary text varies due to Qiraat differences
2. **aya_text_emlaey**: Simplified text also varies
3. **page/line**: Page/line numbers differ due to different Mushaf layouts

### Fields Expected to be Stable

1. **sura_no**: Surah numbers identical (1-114)
2. **sura_name_en**: English names identical
3. **sura_name_ar**: Arabic names identical
4. **jozz**: Juz divisions identical

## Layer-Specific vs Shared Concerns

### Qiraat-Specific Layers (Vary Between Narrations)
- Layer 0: Character Composition ✓
- Layer 1: Character Symbols ✓
- Layer 2: Character Paired Data ✓
- Layer 9: Qiraat/Manuscript ✓
- Layer 10: Edition Variants ✓
- Layer 13: Orthographic Systems ✓

### Shared Layers (Identical Across Narrations)
- Layer 6: Surah Structure (114 surahs same)
- Layer 7: Division Structure (30 juz same)

### Context-Dependent Layers
- Layer 5: Verse Structure (6,236 vs 6,214 - boundary differences)
- Layer 11: Page Layout (different Mushaf layouts)
- Layer 12: Line Layout (different line breaks)

## Findings That Generalize to Remaining Narrations

Based on Hafs vs Warsh analysis, we predict:

1. **Verse Count**: All 20 narrations likely have slight verse count variations
2. **Character-Level Layers**: All narrations will differ in Layers 0-2
3. **Structural Layers**: Surah/Juz structure stable across all narrations
4. **Layout Layers**: Each narration needs its own page/line mapping

## Recommendations for Phase 2-3

1. Validate verse count for remaining 5 narrations
2. Quantify character-level variations across all 7 narrations
3. Build unified verse mapping across narrations
4. Create Qiraat-aware layer generation pipeline

