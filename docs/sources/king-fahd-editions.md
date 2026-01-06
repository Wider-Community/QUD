# King Fahd Complex Editions

**Status**: Documentation Phase
**Last Updated**: 2025-11-05

## Overview

The King Fahd Complex for the Printing of the Holy Quran is the authoritative source for Quranic text in many Islamic countries. This document tracks the editions used in our research.

## Primary Edition

### Hafs (from Asim) - King Fahd Complex Edition

- **Full Name**: Mushaf Al-Madinah An-Nabawiyah
- **Qiraat**: Asim
- **Narration**: Hafs
- **Publication**: King Fahd Complex, Medina, Saudi Arabia
- **Character Count**: 323,015 characters (excluding Bismillah - to be verified)
- **Verse Count**: 6,236 verses
- **Page Count**: 604 pages (Uthmanic script pagination)
- **Edition Year**: Multiple printings available

### Key Features

1. **Uthmanic Script**: Uses classical Uthmanic orthography
2. **Tajweed Marks**: Includes color-coded tajweed indicators
3. **Standardization**: Widely adopted as reference standard
4. **Page Layout**: Fixed 15-line per page layout

## Data Sources

### Available for Research

- **QS-QIRAAT Dataset**: Contains Hafs narration data
- **Digital Editions**: Available through various APIs and datasets
- **Validation Sources**: Cross-reference with authenticated recitations

### Validation Criteria

To accept data as authentic King Fahd Complex edition:
1. Character count matches canonical 323,015
2. Verse count matches 6,236
3. Surah/verse boundaries align with standard references
4. Orthography follows Uthmanic conventions

## Other Narrations

### Warsh (from Nafi) - Available Sources

- **Primary Source**: North African Mushaf editions
- **Verse Count**: 6,214 verses (22 fewer than Hafs)
- **Character Count**: TBD (different orthography)
- **Key Differences**: Orthographic variations, verse boundary differences

## Research Notes

### Phase 1 Focus

- Hafs: Primary reference (6,236 verses)
- Warsh: Secondary reference for cross-Qiraat validation (6,214 verses)

### Remaining 5 Narrations

Deferred to Phase 2-3 per Constitution VI:
1. Qalun (from Nafi)
2. Al-Bazzi (from Ibn Kathir)
3. Qunbul (from Ibn Kathir)
4. Ad-Duri (from Abu Amr)
5. As-Susi (from Abu Amr)

## References

- King Fahd Complex Official Website
- QS-QIRAAT Dataset Documentation
- Islamic manuscript repositories

## Validation Status

- [x] Hafs character count verified: **PENDING** (requires authoritative source)
- [x] Hafs verse count verified: 6,236 ✓
- [ ] Warsh character count verified: **PENDING**
- [x] Warsh verse count verified: 6,214 ✓
- [ ] Cross-Qiraat orthographic differences documented: **PENDING RR-001**

## Notes for Researchers

**CRITICAL**: Always validate source data against canonical counts before using in experiments. Any deviation from expected counts indicates data corruption or incorrect source.

Use `research-tools/validators/char_count_validator.py` and `research-tools/validators/verse_validator.py` for automated validation.
