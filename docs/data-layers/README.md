# Quranic Data Layers Documentation

This directory contains detailed documentation for each of the 15 essential Quranic data layers (0-14).

## Layer Overview

The QUD architecture separates Quranic data into distinct semantic layers:

| Layer | Name | Type | Description |
|-------|------|------|-------------|
| 0 | Character Composition | Generative Base | Base letters and phonetic metadata |
| 1 | Character Symbols | Generative | Visual representation rules |
| 2 | Character Paired Data | Generative | Diacritics, tajweed marks |
| 3 | Word Structure | Generative | Word boundaries, morphology |
| 4 | Sentence Structure | Generative | Grammar, waqf/ibtida |
| 5 | Verse Structure | Organizational | Verse boundaries, numbering |
| 6 | Surah Structure | Organizational | Surah metadata, boundaries |
| 7 | Division Structure | Organizational | Juz, hizb, rub divisions |
| 8 | Chapter Structure | Organizational | Sura metadata |
| 9 | Qiraah Manuscript | Recitation-Specific | Complete text per riwayah |
| 10 | Edition Variants | Manuscript | Publisher-specific formatting |
| 11 | Page Layout | Manuscript | Page numbers, breaks |
| 12 | Line Layout | Manuscript | Line numbers, breaks |
| 13 | Orthographic Systems | Presentation | Uthmanic vs Standard script |
| 14 | Readers & Narrators | Metadata | Biographical, isnad chains |

## Layer Categories

- **Generative Layers** (0-4): Can be algorithmically generated from base data + rules
- **Organizational Layers** (5-8): Define structure and hierarchy
- **Recitation-Specific Layers** (9): Vary across the 10 canonical Qiraat
- **Manuscript Layers** (10-12): Publisher and edition-specific
- **Presentation Layers** (13): Different orthographic representations
- **Metadata Layers** (14): Scholarly and biographical information

## Documentation Status

Each layer should have its own markdown file (layer-00-character-composition.md, etc.) containing:
- Semantic definition
- Schema specification reference
- Generation rules (if generative)
- Dependencies on other layers
- Cross-Qiraah considerations
- Examples

## Research Notes

The exact number and boundaries of these layers are under investigation as part of RR-001 and RR-002. This structure represents current understanding and may be refined based on research findings.
