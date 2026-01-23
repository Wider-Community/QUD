# Pydantic Models Guide

Pydantic is a Python library for **data validation using type hints**. It converts raw data (dicts, JSON) into validated Python objects.

## Why Pydantic?

```python
# Without Pydantic - manual, error-prone
def create_verse(data):
    if "surah" not in data:
        raise ValueError("Missing surah")
    if not isinstance(data["surah"], int):
        raise ValueError("surah must be int")
    if data["surah"] < 1 or data["surah"] > 114:
        raise ValueError("surah out of range")
    # ... repeat for every field

# With Pydantic - automatic validation
from pydantic import BaseModel

class Verse(BaseModel):
    surah: int
    ayah: int
    text: str

verse = Verse(surah=1, ayah=1, text="بسم الله")  # Validated automatically
```

---

## Core Concepts

### 1. Basic Model

```python
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
    active: bool = True  # Default value

# Create instance
p = Person(name="Ahmed", age=30)
print(p.name)      # "Ahmed"
print(p.active)    # True (default)

# From dict
p = Person(**{"name": "Ahmed", "age": 30})

# To dict
p.model_dump()     # {"name": "Ahmed", "age": 30, "active": True}

# To JSON
p.model_dump_json()  # '{"name":"Ahmed","age":30,"active":true}'
```

### 2. Type Coercion

Pydantic automatically converts compatible types:

```python
class Example(BaseModel):
    count: int
    price: float

# These all work - Pydantic converts automatically
Example(count="42", price="3.14")    # count=42, price=3.14
Example(count=42.9, price=10)        # count=42, price=10.0
```

### 3. Validation Errors

```python
from pydantic import ValidationError

class User(BaseModel):
    name: str
    age: int

try:
    User(name="Ahmed", age="not a number")
except ValidationError as e:
    print(e)
    # age
    #   Input should be a valid integer, unable to parse string as an integer
```

---

## Field Types

### 4. Common Types

```python
from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import datetime

class Example(BaseModel):
    # Basic types
    name: str
    count: int
    price: float
    active: bool

    # Optional (can be None)
    nickname: Optional[str] = None

    # Lists
    tags: List[str]
    scores: List[int] = []  # Default empty list

    # Dicts
    metadata: Dict[str, str]

    # Datetime (parses strings automatically)
    created_at: datetime
```

```python
# Usage
Example(
    name="Test",
    count=1,
    price=9.99,
    active=True,
    tags=["a", "b"],
    metadata={"key": "value"},
    created_at="2024-01-15T10:30:00"  # String parsed to datetime
)
```

### 5. Literal and Enum Types

```python
from typing import Literal
from enum import Enum
from pydantic import BaseModel

# Using Literal - fixed string values
class Config(BaseModel):
    mode: Literal["read", "write", "admin"]

Config(mode="read")   # OK
Config(mode="other")  # ValidationError

# Using Enum
class Status(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

class Request(BaseModel):
    status: Status

Request(status="pending")        # OK - converts to Status.PENDING
Request(status=Status.PENDING)   # OK
```

---

## Field Constraints

### 6. Using Field()

```python
from pydantic import BaseModel, Field

class Verse(BaseModel):
    surah: int = Field(ge=1, le=114, description="Surah number")
    ayah: int = Field(ge=1, description="Verse number")
    text: str = Field(min_length=1, description="Arabic text")
    juz: int = Field(default=1, ge=1, le=30)
```

| Constraint | Applies To | Description |
|------------|------------|-------------|
| `ge` | numbers | Greater than or equal (>=) |
| `gt` | numbers | Greater than (>) |
| `le` | numbers | Less than or equal (<=) |
| `lt` | numbers | Less than (<) |
| `multiple_of` | numbers | Must be divisible by |
| `min_length` | str, list | Minimum length |
| `max_length` | str, list | Maximum length |
| `pattern` | str | Regex pattern |
| `default` | any | Default value |
| `description` | any | Documentation |

### 7. String Patterns

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    email: str = Field(pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    username: str = Field(min_length=3, max_length=20, pattern=r'^[a-z0-9_]+$')
```

---

## Nested Models

### 8. Composing Models

```python
from pydantic import BaseModel
from typing import List, Optional

class Word(BaseModel):
    text: str
    position: int
    root: Optional[str] = None

class Verse(BaseModel):
    surah: int
    ayah: int
    text: str
    words: List[Word]  # Nested list of models

# Usage
verse = Verse(
    surah=1,
    ayah=1,
    text="بِسْمِ اللَّهِ",
    words=[
        {"text": "بِسْمِ", "position": 1, "root": "سمو"},
        {"text": "اللَّهِ", "position": 2}
    ]
)

# Access nested data
print(verse.words[0].text)  # "بِسْمِ"
print(verse.words[0].root)  # "سمو"
```

---

## Custom Validators

### 9. Field Validators

```python
from pydantic import BaseModel, field_validator

class Verse(BaseModel):
    surah: int
    ayah: int
    text: str

    @field_validator('text')
    @classmethod
    def text_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError('text cannot be empty or whitespace')
        return v.strip()

    @field_validator('surah')
    @classmethod
    def surah_in_range(cls, v: int) -> int:
        if not 1 <= v <= 114:
            raise ValueError('surah must be between 1 and 114')
        return v
```

### 10. Model Validators (Cross-Field)

```python
from pydantic import BaseModel, model_validator

class DateRange(BaseModel):
    start_date: str
    end_date: str

    @model_validator(mode='after')
    def check_dates(self):
        if self.start_date > self.end_date:
            raise ValueError('start_date must be before end_date')
        return self
```

---

## Computed Fields

### 11. Properties and Computed Fields

```python
from pydantic import BaseModel, computed_field

class Verse(BaseModel):
    surah: int
    ayah: int
    text: str

    @computed_field
    @property
    def reference(self) -> str:
        return f"{self.surah}:{self.ayah}"

    @computed_field
    @property
    def word_count(self) -> int:
        return len(self.text.split())

verse = Verse(surah=1, ayah=1, text="بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ")
print(verse.reference)    # "1:1"
print(verse.word_count)   # 4
print(verse.model_dump()) # includes reference and word_count
```

---

## Configuration

### 12. Model Config

```python
from pydantic import BaseModel, ConfigDict

class Verse(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,    # Strip whitespace from strings
        validate_assignment=True,      # Validate on attribute assignment
        extra='forbid',                # Error on extra fields
        frozen=True,                   # Make immutable (like dataclass frozen)
    )

    surah: int
    ayah: int
    text: str

# With extra='forbid'
Verse(surah=1, ayah=1, text="test", unknown=5)  # ValidationError

# With frozen=True
v = Verse(surah=1, ayah=1, text="test")
v.surah = 2  # Error - frozen
```

| Config Option | Description |
|---------------|-------------|
| `extra='forbid'` | Reject unknown fields |
| `extra='ignore'` | Silently ignore unknown fields |
| `extra='allow'` | Accept and store unknown fields |
| `frozen=True` | Make instances immutable |
| `str_strip_whitespace=True` | Auto-strip string whitespace |
| `validate_assignment=True` | Validate when setting attributes |

---

## JSON Schema Integration

### 13. Generate JSON Schema from Pydantic

```python
from pydantic import BaseModel, Field
from typing import List, Optional
import json

class Word(BaseModel):
    text: str = Field(description="The word text")
    position: int = Field(ge=1, description="Position in verse")

class Verse(BaseModel):
    surah: int = Field(ge=1, le=114)
    ayah: int = Field(ge=1)
    text: str = Field(min_length=1)
    words: Optional[List[Word]] = None

# Generate JSON Schema
schema = Verse.model_json_schema()
print(json.dumps(schema, indent=2))
```

Output:

```json
{
  "properties": {
    "surah": { "maximum": 114, "minimum": 1, "type": "integer" },
    "ayah": { "minimum": 1, "type": "integer" },
    "text": { "minLength": 1, "type": "string" },
    "words": {
      "anyOf": [
        { "items": { "$ref": "#/$defs/Word" }, "type": "array" },
        { "type": "null" }
      ]
    }
  },
  "required": ["surah", "ayah", "text"],
  "$defs": {
    "Word": { ... }
  }
}
```

---

## Complete Example

```python
from pydantic import BaseModel, Field, field_validator, computed_field, ConfigDict
from typing import List, Optional
from enum import Enum

class TajweedRule(str, Enum):
    GHUNNA = "ghunna"
    IDGHAM = "idgham"
    IKHFA = "ikhfa"
    IQLAB = "iqlab"
    QALQALA = "qalqala"

class Word(BaseModel):
    text: str = Field(min_length=1)
    position: int = Field(ge=1)
    root: Optional[str] = None
    tajweed_rules: List[TajweedRule] = []

class Verse(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    surah: int = Field(ge=1, le=114, description="Surah number (1-114)")
    ayah: int = Field(ge=1, description="Verse number")
    text: str = Field(min_length=1, description="Full verse text")
    words: List[Word] = Field(default_factory=list)

    @field_validator('text')
    @classmethod
    def validate_arabic(cls, v: str) -> str:
        # Simple check for Arabic characters
        if not any('\u0600' <= c <= '\u06FF' for c in v):
            raise ValueError('text must contain Arabic characters')
        return v

    @computed_field
    @property
    def reference(self) -> str:
        return f"{self.surah}:{self.ayah}"

    @computed_field
    @property
    def word_count(self) -> int:
        return len(self.words) if self.words else len(self.text.split())


# Usage
verse = Verse(
    surah=1,
    ayah=1,
    text="بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
    words=[
        Word(text="بِسْمِ", position=1, root="سمو"),
        Word(text="اللَّهِ", position=2),
        Word(text="الرَّحْمَٰنِ", position=3, root="رحم"),
        Word(text="الرَّحِيمِ", position=4, root="رحم", tajweed_rules=["ghunna"])
    ]
)

print(verse.reference)     # "1:1"
print(verse.word_count)    # 4
print(verse.model_dump())  # Full dict representation
```

---

## Schema Versioning with Pydantic

### 14. Versioning Strategies

Managing schema evolution is critical for data projects. Here's how to version Pydantic models:

#### Version Metadata in Models

```python
from pydantic import BaseModel, Field
from typing import ClassVar

class PersonV2(BaseModel):
    """Person schema v2.1.0"""

    # Class-level version info (not serialized by default)
    SCHEMA_VERSION: ClassVar[str] = "2.1.0"

    name: str
    age: int = Field(ge=0)
    email: str

    @classmethod
    def schema_version(cls) -> str:
        return cls.SCHEMA_VERSION
```

#### Multiple Schema Versions

```python
from pydantic import BaseModel, Field
from typing import Optional

# v1 schema (legacy)
class PersonV1(BaseModel):
    name: str
    age: int
    address: str  # Deprecated in v2

# v2 schema (current)
class PersonV2(BaseModel):
    name: str
    age: int = Field(ge=0)
    email: str  # New required field

# Migration helper
def migrate_v1_to_v2(v1: PersonV1, email: str) -> PersonV2:
    return PersonV2(
        name=v1.name,
        age=v1.age,
        email=email
    )
```

#### Deprecation with Warnings

```python
from pydantic import BaseModel, Field, field_validator
from typing import Optional
import warnings

class Person(BaseModel):
    name: str
    age: int
    email: str

    # Deprecated field - still accepted but warns
    address: Optional[str] = Field(
        default=None,
        deprecated=True,
        description="DEPRECATED: Will be removed in next major version"
    )

    @field_validator('address')
    @classmethod
    def warn_deprecated(cls, v):
        if v is not None:
            warnings.warn(
                "address is deprecated and will be removed in v3.",
                DeprecationWarning
            )
        return v
```

#### JSON Schema with Version Info

```python
from pydantic import BaseModel, Field

class Person(BaseModel):
    name: str
    age: int = Field(ge=0)
    email: str

    class Config:
        json_schema_extra = {
            "$id": "https://example.com/schemas/v2/person.json",
            "version": "2.1.0"
        }

# Generated schema includes version info
schema = Person.model_json_schema()
# {"$id": "https://example.com/...", "version": "2.1.0", ...}
```

#### Semantic Versioning Rules

| Change Type | Version Bump | Pydantic Action |
|-------------|--------------|-----------------|
| Remove required field | Major | New model class (e.g., `PersonV3`) |
| Add required field | Major | New model class |
| Add optional field | Minor | Add with `default=None` |
| Change validation | Minor | Update `Field()` constraints |
| Fix description | Patch | Update docstring/description |

---

## Pydantic vs JSON Schema

| Feature | JSON Schema | Pydantic |
|---------|-------------|----------|
| Language | JSON (language-agnostic) | Python only |
| Validation | External tools needed | Built-in |
| Type safety | None | Full Python type hints |
| IDE support | Limited | Excellent autocomplete |
| Custom logic | Not possible | Custom validators |
| Computed fields | Not possible | Yes |
| Use case | Data interchange, APIs | Python applications |

**They work together**: Pydantic can generate JSON Schemas, and you can use both in your project.

---

## Installation

```bash
pip install pydantic
```

---

## Resources

- [Pydantic Docs](https://docs.pydantic.dev/)
- [Pydantic V2 Migration Guide](https://docs.pydantic.dev/latest/migration/)
