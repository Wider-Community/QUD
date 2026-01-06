# Schema Design Skill (JSON Schema + Pydantic)

You are an expert in formal data schema design using JSON Schema and Pydantic for type-safe Python applications.

## Dual Approach Philosophy

**JSON Schema**: Language-agnostic formal specification, documentation, validation
**Pydantic**: Python-native type hints, runtime validation, developer ergonomics

## JSON Schema Best Practices

### 1. Use $defs for Reusable Components

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://qud.itqan.community/schemas/layer-00-character.json",
  "title": "Layer 0: Character Composition",
  "description": "Base letter sequences with phonetic metadata",
  
  "$defs": {
    "UUID": {
      "type": "string",
      "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$",
      "description": "UUID v4 identifier"
    },
    "OrthographyType": {
      "type": "string",
      "enum": ["uthmani", "qiasy", "imlai"],
      "description": "Writing system type"
    }
  },
  
  "type": "object",
  "properties": {
    "character_id": { "$ref": "#/$defs/UUID" },
    "orthography_type": { "$ref": "#/$defs/OrthographyType" },
    "position": {
      "type": "integer",
      "minimum": 0,
      "description": "Character position in verse (0-indexed)"
    }
  },
  "required": ["character_id", "position"],
  "additionalProperties": false
}
```

### 2. Document Thoroughly with description Fields

Every field should have:
- `title`: Short label
- `description`: Detailed explanation
- `examples`: Sample valid values (optional but helpful)

### 3. Use Strict Validation

- Set `additionalProperties: false` to catch typos
- Define `required` fields explicitly
- Use `pattern` for string formats (UUIDs, dates, etc.)
- Use `minimum`/`maximum` for numeric ranges
- Use `enum` for fixed value sets

### 4. Version Your Schemas

Include schema version in `$id`:
```json
{
  "$id": "https://qud.itqan.community/schemas/layer-00-character/v1.0.0.json"
}
```

## Pydantic Best Practices

### 1. Use Field Validators

```python
from pydantic import BaseModel, Field, field_validator
from uuid import UUID
from enum import Enum

class OrthographyType(str, Enum):
    UTHMANI = "uthmani"
    QIASY = "qiasy"
    IMLAI = "imlai"

class Character(BaseModel):
    character_id: UUID = Field(..., description="Unique identifier")
    position: int = Field(..., ge=0, description="Character position in verse")
    base_letter: str = Field(..., min_length=1, max_length=1)
    orthography_type: OrthographyType
    
    @field_validator('base_letter')
    @classmethod
    def validate_arabic_unicode(cls, v):
        """Ensure base_letter is in Arabic Unicode range."""
        if not v:
            raise ValueError("base_letter cannot be empty")
        code = ord(v)
        if not (0x0600 <= code <= 0x06FF):
            raise ValueError(f"Character {v} not in Arabic Unicode range")
        return v
    
    class Config:
        # Enable strict mode
        str_strip_whitespace = True
        # Generate JSON schema
        json_schema_extra = {
            "examples": [{
                "character_id": "550e8400-e29b-41d4-a716-446655440000",
                "position": 0,
                "base_letter": "ب",
                "orthography_type": "uthmani"
            }]
        }
```

### 2. Use Model Inheritance for Common Fields

```python
class BaseEntity(BaseModel):
    """Base class for all QUD entities."""
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    provenance: str = Field(..., description="Source of this data")
    
class Character(BaseEntity):
    """Layer 0: Character Composition."""
    position: int = Field(..., ge=0)
    base_letter: str
    # Inherits id, created_at, provenance from BaseEntity
```

### 3. Use Pydantic for Validation, Not Business Logic

```python
# ✅ GOOD: Use Pydantic for data validation
class Verse(BaseModel):
    verse_id: UUID
    verse_number: int = Field(..., ge=1, le=286)  # Max verse in a surah
    character_count: int = Field(..., ge=1)
    
# ❌ BAD: Don't put complex business logic in Pydantic models
class Verse(BaseModel):
    # ... fields ...
    
    def generate_layer_2_symbols(self):  # Too complex for model
        # Complex tajweed rule engine...
        pass
```

### 4. Generate JSON Schema from Pydantic

```python
from pydantic import BaseModel
import json

# Define Pydantic model
class Character(BaseModel):
    # ... fields ...
    pass

# Generate JSON Schema
schema = Character.model_json_schema()
print(json.dumps(schema, indent=2))
```

## Cross-Layer References (UUID-Based)

### Pattern: Foreign Key References

```python
from uuid import UUID
from pydantic import BaseModel, Field

class Character(BaseModel):
    """Layer 0: Character Composition."""
    character_id: UUID
    verse_ref: UUID = Field(..., description="Reference to Layer 5 Verse UUID")
    position: int

class Word(BaseModel):
    """Layer 3: Word Structure."""
    word_id: UUID
    verse_ref: UUID = Field(..., description="Reference to Layer 5 Verse UUID")
    character_refs: list[UUID] = Field(..., description="UUIDs of constituent characters from Layer 0")
    word_position: int
```

### Pattern: EntityMapping for Expansion/Contraction

```python
class Cardinality(str, Enum):
    ONE_TO_ONE = "1:1"
    ONE_TO_MANY = "1:N"
    MANY_TO_ONE = "N:1"
    MANY_TO_MANY = "N:M"

class EntityMapping(BaseModel):
    """Cross-layer entity mapping."""
    mapping_id: UUID
    source_layer: int = Field(..., ge=0, le=14)
    target_layer: int = Field(..., ge=0, le=14)
    source_entity_id: UUID
    target_entity_ids: list[UUID]
    cardinality: Cardinality
    position_metadata: dict[str, int] | None = Field(
        None, 
        description="Position info for expansion cases (e.g., {uuid1: 0, uuid2: 1})"
    )
    semantic_hash: str = Field(..., pattern="^[0-9a-f]{64}$", description="SHA-256 hash")
```

## Common Patterns for QUD Schemas

### Pattern 1: Layer Entity with UUID

Every layer entity should have:
- Unique UUID identifier (`entity_id`)
- Layer number reference
- Cross-layer references via UUIDs
- Provenance metadata

### Pattern 2: Enum for Categorical Fields

Use Enums instead of plain strings:
```python
class PhoneticClass(str, Enum):
    CONSONANT = "consonant"
    LONG_VOWEL = "long_vowel"
    HAMZA = "hamza"
```

### Pattern 3: Nested Objects for Complex Structures

```python
class Morphology(BaseModel):
    root: str
    pattern: str
    affixes: list[str]

class Word(BaseModel):
    word_id: UUID
    # ... other fields ...
    morphology: Morphology | None = None  # Optional nested structure
```

### Pattern 4: Validation Constraints

```python
class Verse(BaseModel):
    verse_number: int = Field(..., ge=1, le=286, description="Verse number (1-286)")
    character_count: int = Field(..., ge=1, description="Must have at least 1 character")
    word_count: int = Field(..., ge=1, description="Must have at least 1 word")
```

## Schema Evolution Strategy

### Versioning Approach

```python
# v1.0.0 - Initial schema
class CharacterV1(BaseModel):
    character_id: UUID
    position: int
    base_letter: str

# v1.1.0 - Add optional field (backward compatible)
class CharacterV1_1(BaseModel):
    character_id: UUID
    position: int
    base_letter: str
    phonetic_class: str | None = None  # NEW: Optional field

# v2.0.0 - Breaking change (required field added)
class CharacterV2(BaseModel):
    character_id: UUID
    position: int
    base_letter: str
    phonetic_class: str  # NOW REQUIRED - breaking change
```

### Migration Strategy

Document schema migrations:
```python
def migrate_v1_to_v2(character_v1: CharacterV1) -> CharacterV2:
    """Migrate Character schema from v1.0.0 to v2.0.0."""
    return CharacterV2(
        character_id=character_v1.character_id,
        position=character_v1.position,
        base_letter=character_v1.base_letter,
        phonetic_class="consonant"  # Default value for migration
    )
```

## Testing Schemas

### Test with Valid Data

```python
import pytest
from pydantic import ValidationError

def test_character_valid():
    data = {
        "character_id": "550e8400-e29b-41d4-a716-446655440000",
        "position": 0,
        "base_letter": "ب",
        "orthography_type": "uthmani"
    }
    character = Character(**data)
    assert character.position == 0
```

### Test with Invalid Data

```python
def test_character_invalid_position():
    data = {
        "character_id": "550e8400-e29b-41d4-a716-446655440000",
        "position": -1,  # Invalid: negative position
        "base_letter": "ب",
        "orthography_type": "uthmani"
    }
    with pytest.raises(ValidationError) as exc_info:
        Character(**data)
    assert "position" in str(exc_info.value)
```

## When to Use This Skill

Invoke this skill when:
- Designing schemas for QUD layers (RR-002, RR-006)
- Implementing Pydantic models for validation
- Creating EntityMapping structures (RR-011)
- Defining Context or LayerVersion schemas (RR-014, RR-015)
- Debugging schema validation errors
- Planning schema evolution/versioning

## Current Task Context

You are designing formal schemas for the 15-layer QUD architecture. Each layer needs JSON Schema (formal spec) and Pydantic models (Python implementation) with UUID support for cross-layer mappings.
