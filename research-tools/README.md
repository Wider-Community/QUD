# QUD Research Tools

Reusable research utilities for Quranic data layer research (Tier 2).

This package contains clean, documented, and reusable tools developed during research. Tools are added incrementally as research progresses and requirements evolve, enabling reuse across experiments and data processing pipelines.

## Directory Structure

```
research-tools/
├── analyzers/          # Data analysis and comparison tools
├── data-loaders/       # Data loading and parsing utilities
├── generators/         # Data generation and ID creation
├── orchestration/      # Query routing and context resolution (stubs)
├── provenance/         # Data lineage and audit tracking
└── validators/         # Data validation tools
```

## Tool Summaries

### Analyzers

| Tool | File | Description |
|------|------|-------------|
| **DataComparator** | `data_comparator.py` | Character-level and verse-level diff utilities for comparing Quranic data across versions/narrations. Useful for validating cross-Qiraat variations. |
| **PerformanceAnalyzer** | `performance_metrics.py` | Timing and throughput analysis for layer generation and data processing tasks. Includes context manager for measuring execution. |

### Data Loaders

| Tool | File | Description |
|------|------|-------------|
| **CSVLoader** | `csv_loader.py` | Load Quranic data from CSV files for validation against authoritative sources. |
| **NarrationParser** | `narration_parser.py` | Parse Qiraat-specific data with awareness of the 10 canonical Qiraat and 20 Narrations. Maps between Qiraat and their narrations. |
| **QuranLoader** | `quran_loader.py` | Load Quranic data from JSON/CSV with support for multiple Qiraat and Narrations. Handles QS-QIRAAT dataset structure. |

### Generators

| Tool | File | Description |
|------|------|-------------|
| **LayerGenerator** | `layer_generator.py` | Abstract base class for layer data generators. Provides standard interface for generate/validate/save operations. |
| **SemanticHasher** | `semantic_hasher.py` | Generate SHA-256 semantic hashes for relationship representation and data integrity verification. |
| **UUID Generator** | `uuid_generator.py` | Deterministic UUID v5 generation for all Quranic entities. Provides consistent naming conventions for surahs, verses, words, characters, symbols, pages, lines, juz, hizb, rub, and metadata entities. |

### Orchestration (Stubs)

Stub implementations for future research (RR-014-016):

| Tool | File | Description |
|------|------|-------------|
| **ContextResolver** | `context_resolver.py` | Resolve full context from partial versioning parameters. |
| **QueryRouter** | `query_router.py` | Route queries to appropriate layer data. |
| **VersionSelector** | `version_selector.py` | Select appropriate data version based on Qiraat/Narration context. |

### Provenance

| Tool | File | Description |
|------|------|-------------|
| **ProvenanceTracker** | `provenance_tracker.py` | Track data lineage through transformation pipelines. Maintains audit log of all transformations for research reproducibility. |

### Validators

| Tool | File | Description |
|------|------|-------------|
| **CharacterCountValidator** | `char_count_validator.py` | Zero-tolerance validation for Quranic character counts (Hafs: 323,015 characters). |
| **ContextValidator** | `context_validator.py` | Validate contextual versioning parameters (Qiraat, Narration, Edition, Manuscript combinations). |
| **SchemaValidator** | `schema_validator.py` | Validate layer data against JSON Schema and Pydantic models. |
| **VerseCountValidator** | `verse_validator.py` | Zero-tolerance validation for verse counts by narration (Hafs: 6,236 / Warsh: 6,214 verses). |


## Adding New Tools

When research reveals a need for new reusable functionality:

1. Identify the appropriate category (analyzer, loader, generator, validator, etc.)
2. Create the tool with clear docstrings and type hints
3. Add a summary entry to this README
4. Ensure the tool is importable from the package

All tools should be:
- **Clean**: Well-structured, readable code
- **Documented**: Clear docstrings with usage examples
- **Reusable**: Designed for use across multiple experiments
- **Tested**: Include validation of expected behavior
