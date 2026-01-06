# Authenticated Reciters

**Status**: Documentation Phase
**Last Updated**: 2025-11-05

## Overview

This document tracks authenticated reciters whose recitations serve as validation sources for Quranic data integrity.

## Validation Principle

**Zero-Tolerance Accuracy**: Reciter audio must match canonical text exactly. Any deviation in character count, verse boundaries, or word forms indicates either:
1. Recording error
2. Different Qiraat/Narration
3. Incorrect data source

## Primary Reciters by Narration

### Hafs (from Asim)

#### Sheikh Abdul Basit Abdul Samad
- **Status**: ✓ Authenticated
- **Recording Quality**: High-quality studio recordings
- **Validation**: Matches King Fahd Complex edition
- **Availability**: Widely available, public domain
- **Use Case**: Primary validation source for Hafs

#### Sheikh Mahmoud Khalil Al-Hussary
- **Status**: ✓ Authenticated
- **Recording Quality**: High-quality studio recordings
- **Validation**: Matches King Fahd Complex edition
- **Availability**: Widely available
- **Use Case**: Secondary validation source for Hafs

#### Sheikh Mishari Rashid Alafasy
- **Status**: ✓ Authenticated (modern)
- **Recording Quality**: High-definition digital recordings
- **Validation**: Matches King Fahd Complex edition
- **Availability**: Widely available
- **Use Case**: Modern reference for Hafs

### Warsh (from Nafi)

#### Sheikh Yassin Al-Jazairi
- **Status**: ✓ Authenticated
- **Narration**: Warsh from Nafi
- **Validation**: Matches North African Mushaf editions
- **Use Case**: Primary validation source for Warsh

#### Sheikh Ibrahim Al-Akhdar
- **Status**: ✓ Authenticated
- **Narration**: Warsh from Nafi
- **Validation**: Matches North African editions
- **Use Case**: Secondary validation source for Warsh

## Validation Methodology

### Audio-to-Text Verification

1. **Character Alignment**: Every character in text must align with recited sound
2. **Verse Boundaries**: Reciter pauses must match canonical verse endings
3. **Tajweed Features**: Phonetic features must match Qiraat-specific rules
4. **Word Forms**: Morphological variations must match Narration specifications

### Cross-Reciter Consistency

- Multiple reciters of same Narration must produce identical text
- Deviations indicate either error or different Qiraat
- Use majority consensus for validation

## Data Sources

### Tarteel.ai Resources

- **Available**: Multiple authenticated reciters with aligned text
- **Quality**: Verse-level alignment, high-quality audio
- **Validation Status**: Cross-referenced with canonical sources
- **Use Case**: Potential validation source (pending evaluation)

### Everyayah.com

- **Available**: Multiple reciters by Qiraat/Narration
- **Quality**: Verse-level audio files
- **Validation Status**: Community-validated
- **Use Case**: Secondary validation source

## Research Integration

### Phase 1 Validation Strategy

1. **Primary Source**: King Fahd Complex text (Hafs)
2. **Audio Validation**: Cross-check with Sheikh Abdul Basit
3. **Secondary Validation**: Compare with Sheikh Al-Hussary
4. **Warsh Validation**: Use Sheikh Yassin Al-Jazairi

### Validation Criteria

- Character count must match canonical values
- Verse boundaries must align with audio pauses
- No unexplained character/word variations
- Tajweed features must conform to Qiraat rules

## Remaining Qiraat Reciters

### Deferred to Phase 2-3

Per Constitution VI, the following narrations are deferred:
- Qalun (from Nafi)
- Al-Bazzi (from Ibn Kathir)
- Qunbul (from Ibn Kathir)
- Ad-Duri (from Abu Amr)
- As-Susi (from Abu Amr)

**Action Item**: Document authenticated reciters for these narrations before Phase 2-3 begins.

## References

- Tarteel.ai API documentation
- Everyayah.com reciter catalog
- Islamic Audio Library collections

## Validation Checklist

- [x] Hafs primary reciter identified: Sheikh Abdul Basit ✓
- [x] Hafs secondary reciter identified: Sheikh Al-Hussary ✓
- [x] Warsh primary reciter identified: Sheikh Yassin Al-Jazairi ✓
- [ ] Audio-to-text alignment tool created: **PENDING** (future RR)
- [ ] Automated validation pipeline: **PENDING** (future RR)

## Notes for Researchers

**CRITICAL**: Do not use uncertified recitations for validation. Always verify reciter credentials and cross-check with multiple sources before accepting audio as authoritative.

Use authenticated reciters only for validation, not as primary data source. Canonical text editions remain the source of truth.
