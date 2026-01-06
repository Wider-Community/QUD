# Quickstart Guide: Quranic Layer Architecture Research

**Research Branch**: `001-quranic-layer-architecture`
**Date**: 2025-11-04

## Prerequisites

- Python 3.11 or later
- macOS development environment (or Linux/Windows with Python)
- Git (for cloning and version control)
- 2-4 GB disk space for QS-QIRAAT dataset and generated artifacts

## Installation

### 1. Python Environment Setup

```bash
# Navigate to project root
cd "/Users/mac/Work/ITQAN Community/QUD"

# Create virtual environment
python3.11 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# venv\Scripts\activate   # On Windows

# Upgrade pip
pip install --upgrade pip
```

### 2. Install Dependencies

```bash
# Core dependencies
pip install nltk pydantic jsonschema

# Data processing
pip install pandas numpy

# Visualization
pip install matplotlib seaborn plotly

# Jupyter notebooks
pip install jupyter jupyterlab ipykernel

# Testing (for Tier 2 research-tools)
pip install pytest pytest-cov

# Arabic text processing
pip install pyarabic python-bidi arabic-reshaper

# Optional: Create requirements.txt
pip freeze > requirements.txt
```

### 3. Verify QS-QIRAAT Dataset Access

```bash
# Check that dataset is accessible
ls -la "QS - QIRAAT/Uthmanic Hafs v2.0/UthmanicHafs_v2-0 data/"

# Expected files:
# - hafsData_v2-0.json (primary data source)
# - hafsData_v2-0.csv (validation)
# - read.me (documentation)

# Verify Warsh dataset
ls -la "QS - QIRAAT/Uthmanic Warsh v2.1/UthmanicWarsh_v2-1 data/"
```

## Project Structure Overview

```
QUD/
├── experiments/                  # Research experiments (Tier 1 code)
│   ├── rr-001-layer-separation/  # To be created
│   ├── rr-002-schema-design/     # To be created
│   └── rr-003-layer-simulation/  # To be created
│
├── research-tools/               # Reusable utilities (Tier 2 code)
│   ├── data-loaders/             # To be created
│   ├── validators/               # To be created
│   ├── generators/               # To be created
│   └── analyzers/                # To be created
│
├── schemas/                      # Layer schema definitions
│   ├── layer-00-character-composition/  # To be created
│   ├── layer-01-symbols-rendering/      # To be created
│   └── [layers 02-14]/           # To be created
│
├── docs/                         # Documentation
│   ├── research-log.md           # To be created
│   ├── data-layers/              # Layer documentation
│   └── decisions/                # ADRs
│
├── specs/001-quranic-layer-architecture/  # Current feature specs
│   ├── spec.md                   # Research specification
│   ├── plan.md                   # Implementation plan
│   ├── data-model.md             # Data model (needs correction)
│   ├── experiment-design.md      # Experimental methodology
│   ├── research.md               # Technology research
│   └── quickstart.md             # This file
│
└── QS - QIRAAT/                  # Source datasets
    ├── Uthmanic Hafs v2.0/
    ├── Uthmanic Warsh v2.1/
    └── [other narrations]/
```

## Running Research Experiments

### RR-001: Layer Separation Analysis

**Goal**: Analyze QS-QIRAAT dataset to identify which of the 15 layers are mixed together.

```bash
# Create experiment directory
mkdir -p experiments/rr-001-layer-separation

# Launch Jupyter notebook
jupyter lab

# Create new notebook: experiments/rr-001-layer-separation/analysis.ipynb
```

**Notebook Cells** (sample workflow):

```python
# Cell 1: Load QS-QIRAAT Hafs data
import json
import pandas as pd

# Load Hafs JSON data
with open('QS - QIRAAT/Uthmanic Hafs v2.0/UthmanicHafs_v2-0 data/hafsData_v2-0.json', 'r', encoding='utf-8') as f:
    hafs_data = json.load(f)

print(f"Loaded {len(hafs_data)} verse records")
print("Sample record structure:")
print(json.dumps(hafs_data[0], indent=2, ensure_ascii=False))
```

```python
# Cell 2: Analyze field structure
# Map each QS-QIRAAT field to QUD layers
field_mapping = {
    'id': 'Verse identifier (internal)',
    'jozz': 'Layer 7 - Division Structure',
    'page': 'Layer 11 - Page Layout',
    'sura_no': 'Layer 6 - Surah Structure',
    'sura_name_en': 'Layer 8 - Chapter Structure',
    'sura_name_ar': 'Layer 8 - Chapter Structure',
    'line_start': 'Layer 12 - Line Layout',
    'line_end': 'Layer 12 - Line Layout',
    'aya_no': 'Layer 5 - Verse Structure',
    'aya_text': 'Conflates Layers 0, 1, 2, 3, 13 (Character, Symbols, Paired Data, Words, Orthography)',
    'aya_text_emlaey': 'Conflates Layers 0, 3, 13 (Character, Words, Qiasy Orthography)'
}

for field, layer in field_mapping.items():
    print(f"{field:20s} → {layer}")
```

```python
# Cell 3: Count character occurrences
total_chars = sum(len(verse['aya_text']) for verse in hafs_data)
print(f"Total characters in Hafs: {total_chars}")
print(f"Expected: 323,015 characters")
print(f"Match: {total_chars == 323015}")
```

### RR-002: Schema Design

**Goal**: Define JSON Schema + Pydantic models for each of the 15 layers.

```bash
# Create schema directory for Layer 0
mkdir -p schemas/layer-00-character-composition

# Create schema definition
touch schemas/layer-00-character-composition/schema.json
touch schemas/layer-00-character-composition/models.py
touch schemas/layer-00-character-composition/README.md
```

**Example Pydantic Model** (`schemas/layer-00-character-composition/models.py`):

```python
from pydantic import BaseModel, Field, UUID4
from enum import Enum
from typing import Optional

class PhoneticClass(str, Enum):
    CONSONANT = "consonant"
    LONG_VOWEL = "long_vowel"
    HAMZA = "hamza"
    ALIF = "alif"

class OrthographyType(str, Enum):
    UTHMANI = "uthmani"
    QIASY = "qiasy"
    IMLAI = "imlai"

class Character(BaseModel):
    """Layer 0: Character Composition"""
    character_id: UUID4 = Field(..., description="Unique identifier for this character")
    verse_ref: UUID4 = Field(..., description="Reference to Layer 5 Verse")
    position: int = Field(..., ge=0, description="Character position in verse (0-indexed)")
    base_letter: str = Field(..., min_length=1, max_length=1, description="Unicode codepoint for base letter")
    phonetic_class: PhoneticClass
    orthography_type: OrthographyType
    
    class Config:
        json_schema_extra = {
            "example": {
                "character_id": "550e8400-e29b-41d4-a716-446655440000",
                "verse_ref": "660e8400-e29b-41d4-a716-446655440001",
                "position": 0,
                "base_letter": "ب",
                "phonetic_class": "consonant",
                "orthography_type": "uthmani"
            }
        }
```

### RR-003: Layer Simulation

**Goal**: Build working simulation transforming QS-QIRAAT into 15-layer format.

```bash
# Create simulation directory
mkdir -p experiments/rr-003-layer-simulation

# Create prototype script
touch experiments/rr-003-layer-simulation/prototype.py
```

**Sample Transformation Script**:

```python
# experiments/rr-003-layer-simulation/prototype.py
import json
import uuid
from pathlib import Path

def transform_verse_to_layers(verse_record):
    """
    Transform QS-QIRAAT flat verse record into layered format.
    
    Returns dict with keys: layer_00, layer_01, ..., layer_14
    """
    layers = {}
    
    # Layer 0: Character Composition
    layers['layer_00'] = extract_characters(verse_record['aya_text'])
    
    # Layer 5: Verse Structure
    layers['layer_05'] = {
        'verse_id': str(uuid.uuid4()),
        'verse_number': verse_record['aya_no'],
        'surah_ref': verse_record['sura_no']
    }
    
    # Layer 7: Division Structure
    layers['layer_07'] = {
        'juz_number': verse_record['jozz']
    }
    
    # ... implement other layers
    
    return layers

def extract_characters(aya_text):
    """Extract character entities from aya_text"""
    characters = []
    for pos, char in enumerate(aya_text):
        if char.strip():  # Skip whitespace
            characters.append({
                'character_id': str(uuid.uuid4()),
                'position': pos,
                'base_letter': char,
                'orthography_type': 'uthmani'
            })
    return characters

# Load and transform
with open('QS - QIRAAT/Uthmanic Hafs v2.0/UthmanicHafs_v2-0 data/hafsData_v2-0.json', 'r') as f:
    hafs_data = json.load(f)

# Transform first verse as test
transformed = transform_verse_to_layers(hafs_data[0])
print(json.dumps(transformed, indent=2, ensure_ascii=False))
```

## Validation Tools

### Character Count Validator

```python
# research-tools/validators/char_count_validator.py
def validate_character_count(layer_00_data, expected_count=323015):
    """
    Validate Layer 0 character count against authoritative sources.
    
    Args:
        layer_00_data: List of Character entities
        expected_count: Expected character count for Hafs (323,015)
    
    Returns:
        dict with validation results
    """
    actual_count = len(layer_00_data)
    
    return {
        'expected': expected_count,
        'actual': actual_count,
        'match': actual_count == expected_count,
        'difference': actual_count - expected_count,
        'accuracy': (actual_count / expected_count) * 100
    }
```

### Verse Count Validator

```python
# research-tools/validators/verse_validator.py
def validate_verse_count(layer_05_data, narration='hafs'):
    """
    Validate Layer 5 verse count per narration.
    
    Expected counts:
    - Hafs: 6,236 verses
    - Warsh: 6,214 verses
    """
    expected_counts = {
        'hafs': 6236,
        'warsh': 6214
    }
    
    actual_count = len(layer_05_data)
    expected = expected_counts.get(narration, None)
    
    return {
        'narration': narration,
        'expected': expected,
        'actual': actual_count,
        'match': actual_count == expected if expected else None
    }
```

## Troubleshooting

### Issue: UnicodeDecodeError when loading JSON

**Solution**: Ensure UTF-8 encoding when opening files:

```python
with open('path/to/file.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
```

### Issue: Arabic text displays incorrectly in Jupyter

**Solution**: Install Arabic text support:

```bash
pip install arabic-reshaper python-bidi
```

```python
# In notebook cell
import arabic_reshaper
from bidi.algorithm import get_display

text = "بسم الله الرحمن الرحيم"
reshaped_text = arabic_reshaper.reshape(text)
display_text = get_display(reshaped_text)
print(display_text)
```

### Issue: Import errors for pydantic/jsonschema

**Solution**: Verify virtual environment is activated:

```bash
which python  # Should point to venv/bin/python
pip list | grep pydantic  # Verify pydantic is installed
```

## Next Steps

1. **Review Spec**: Read `spec.md` for complete research requirements
2. **Study Data Model**: Review `data-model.md` (note: needs layer order correction)
3. **Run RR-001**: Start with layer separation analysis
4. **Define Schemas**: Create formal schemas for layers 0-14
5. **Build Prototype**: Implement transformation simulation
6. **Validate Results**: Run validators and document findings
7. **Review Findings**: Update `docs/research-log.md` with results

## Resources

- **QS-QIRAAT Documentation**: `QS - QIRAAT/*/read.me` files per narration
- **Research Spec**: `specs/001-quranic-layer-architecture/spec.md`
- **Constitution**: `.specify/memory/constitution.md` (research principles)
- **NLTK Documentation**: https://www.nltk.org/
- **Pydantic Documentation**: https://docs.pydantic.dev/

## Support

For questions or issues:
1. Check `specs/001-quranic-layer-architecture/` documentation
2. Review constitution principles in `.specify/memory/constitution.md`
3. Consult ITQAN community for domain expertise
4. Document findings in research log (`docs/research-log.md`)

---

**Last Updated**: 2025-11-04
**Research Branch**: `001-quranic-layer-architecture`
