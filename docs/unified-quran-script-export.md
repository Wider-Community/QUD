# Unified Quran Script Export Library

## Purpose
Export a single, unified Quranic text library supporting **Hafs** and **Warsh** narrations using QUD layered architecture.

## Scope (Per Charter)
- **In**: Hafs & Warsh script data, standardized layers, unified database
- **Out**: Other Qiraat, audio, transliteration

## Export Format

```
QUD-export/
├── hafs/
│   ├── uthmani.json      # Layer 12a - Uthmani script
│   ├── qiasy.json        # Layer 12b - Standard script
│   └── metadata.json     # Verses: 6,236 | Chars: 323,015
├── warsh/
│   ├── uthmani.json
│   ├── qiasy.json
│   └── metadata.json     # Verses: 6,214
├── mappings/
│   ├── canonical-verses.json   # Cross-narration verse IDs
│   └── character-mappings.json # Uthmani↔Qiasy transforms
└── schema-version.json
```

## Key Features

| Feature | Description |
|---------|-------------|
| **Canonical Verse IDs** | UUID-based mapping across narrations (solves verse numbering differences) |
| **Dual Script Support** | Both Uthmani (رسم عثماني) and Qiasy (إملائي) |
| **Layer Separation** | Characters, words, verses cleanly separated |
| **Cross-Narration Queries** | Compare Hafs↔Warsh at any granularity |

## Timeline (Charter Aligned)

| Milestone | Target | Deliverable |
|-----------|--------|-------------|
| M1 | Month 1.5 | Hafs & Warsh datasets validated |
| M2 | Month 3 | Unified export library ready |
| M3 | Month 4 | First adapter for ITQAN integration |

## API Usage (Planned)

```python
from QUD import QuranExport

# Load unified library
quran = QuranExport.load()

# Get verse in both narrations
hafs_verse = quran.hafs.verse(2, 255)
warsh_verse = quran.warsh.verse(2, 255)

# Cross-narration comparison
diff = quran.compare(hafs_verse, warsh_verse)
```

## Risks (From Charter)

- **R2**: Data collection delays → Mitigate with QS-QIRAAT as baseline
- **R4**: Fragmentation → Use MARQOUM standardization guidelines

## Contact
**AI Product Lead**: Omar Hamdy
**Community**: AI Quran Universal Deep Data Community Group

## Documentation

* [Documentation Study of the Quranic Data Layers](https://docs.google.com/spreadsheets/d/1dG2dVAT6gT0ZAaEQMHJ67eqS4cu8kdil/edit?usp=sharing&ouid=102994138952561997115&rtpof=true&sd=true)


## QUD Core Demos

You can find demo videos of the early version of the QUD core on Google Drive.

* [**Demo part 1**](https://drive.google.com/file/d/1hwXCKfWG7Ezap8Zt0TfhRllIOZmd0CTd/view?usp=drive_link)
* [**Demo part 2**](https://drive.google.com/file/d/1sjM7qK2CV7BoaWa9B13E9yDpbbofEZEI/view?usp=drive_link)
* [**Demo part 3**](https://drive.google.com/file/d/1oPv1JvL9_PthSMnbw7YXii28xlNzHT3C/view?usp=drive_link)
* [**Demo part 4**](https://drive.google.com/file/d/1leQT5g5JxkP08w0XtkQ0X7GTrbBUPf_5/view?usp=drive_link)
* [**Demo part 5**](https://drive.google.com/file/d/1vVmY5N5qs_rZGzxsyZnQDsncOgrN-FlP/view?usp=drive_link)
* [**Demo_part 6**](https://drive.google.com/file/d/1qmnZsuGkzrynOVnHqH5YfxrJAWihN6dz/view?usp=drive_link)