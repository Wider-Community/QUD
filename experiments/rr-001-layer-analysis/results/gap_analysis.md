# RR-001: Gap Analysis

**Analysis Date**: 2025-11-05

## Summary

- Total Layers: 17
- Layers Present: 13
- Layers Missing: 4

## Missing Layers

The following QUD layers are NOT represented in QS-QIRAAT:

### Layer 8: Chapter Structure

**Impact**: Chapter structure (hizb, rub, etc.) not tracked
**Mitigation**: Can be derived from verse numbers

### Layer 14: Readers/Narrators

**Impact**: Reader/Narrator metadata not stored with verses
**Mitigation**: Implicit in dataset name (e.g., 'Hafs')

### Layer 15: Layer 15 (TBD)

**Impact**: Extended layers (TBD) not yet specified
**Mitigation**: Layers under investigation

### Layer 16: Layer 16 (TBD)

**Impact**: Extended layers (TBD) not yet specified
**Mitigation**: Layers under investigation

## Layer Coverage

Which fields cover each layer:

### Layer 0: Character Composition [✓ PRESENT]

Covered by fields: aya_text, aya_text_emlaey

### Layer 1: Character Symbols [✓ PRESENT]

Covered by fields: sura_name_ar, aya_text, aya_text_emlaey

### Layer 2: Character Paired Data [✓ PRESENT]

Covered by fields: aya_text

### Layer 3: Word Structure [✓ PRESENT]

Covered by fields: aya_text, aya_text_emlaey

### Layer 4: Sentence Structure [✓ PRESENT]

Covered by fields: aya_text, aya_text_emlaey

### Layer 5: Verse Structure [✓ PRESENT]

Covered by fields: id, aya_no, aya_text, aya_text_emlaey

### Layer 6: Surah Structure [✓ PRESENT]

Covered by fields: sura_no, sura_name_en, sura_name_ar

### Layer 7: Division Structure [✓ PRESENT]

Covered by fields: jozz

### Layer 8: Chapter Structure [✗ MISSING]

Not represented in QS-QIRAAT schema

### Layer 9: Qiraat/Manuscript [✓ PRESENT]

Covered by fields: aya_text

### Layer 10: Edition Variants [✓ PRESENT]

Covered by fields: aya_text, aya_text_emlaey

### Layer 11: Page Layout [✓ PRESENT]

Covered by fields: page

### Layer 12: Line Layout [✓ PRESENT]

Covered by fields: line_start, line_end

### Layer 13: Orthographic Systems [✓ PRESENT]

Covered by fields: aya_text, aya_text_emlaey

### Layer 14: Readers/Narrators [✗ MISSING]

Not represented in QS-QIRAAT schema

### Layer 15: Layer 15 (TBD) [✗ MISSING]

Not represented in QS-QIRAAT schema

### Layer 16: Layer 16 (TBD) [✗ MISSING]

Not represented in QS-QIRAAT schema

## Recommendations

1. **Layer 8 (Chapter Structure)**: Add fields for hizb, rub, manzil
2. **Layer 14 (Readers/Narrators)**: Add explicit narrator metadata
3. **Layers 15-16**: Define these layers before Phase 2

