# JSON Schema Guide

JSON Schema is a vocabulary that lets you **validate, annotate, and describe JSON data**. Think of it as a contract that defines what valid JSON should look like.

## Core Concepts

### 1. Basic Structure

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.com/my-schema.json",
  "title": "Person",
  "description": "A person record",
  "type": "object"
}
```

| Field | Purpose |
|-------|---------|
| `$schema` | Which JSON Schema version you're using |
| `$id` | Unique identifier for this schema |
| `title` | Human-readable name |
| `description` | What this schema represents |
| `type` | The data type (`string`, `number`, `integer`, `boolean`, `array`, `object`, `null`) |

---

## Data Types

### 2. Primitive Types

```json
{ "type": "string" }                    // "hello"
{ "type": "number" }                    // 3.14
{ "type": "integer" }                   // 42
{ "type": "boolean" }                   // true/false
{ "type": "null" }                      // null
```

### 3. String Constraints

```json
{
  "type": "string",
  "minLength": 1,
  "maxLength": 100,
  "pattern": "^[A-Za-z]+$",
  "format": "email"
}
```

| Constraint | Description |
|------------|-------------|
| `minLength` | Minimum character count |
| `maxLength` | Maximum character count |
| `pattern` | Regular expression the string must match |
| `format` | Built-in formats: `email`, `uri`, `date`, `date-time`, `uuid`, `ipv4`, `ipv6` |

### 4. Number Constraints

```json
{
  "type": "number",
  "minimum": 0,
  "maximum": 100,
  "exclusiveMinimum": 0,
  "exclusiveMaximum": 100,
  "multipleOf": 5
}
```

| Constraint | Description |
|------------|-------------|
| `minimum` | Value >= this number |
| `maximum` | Value <= this number |
| `exclusiveMinimum` | Value > this number |
| `exclusiveMaximum` | Value < this number |
| `multipleOf` | Value must be divisible by this |

---

## Complex Types

### 5. Objects

```json
{
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "age": { "type": "integer" }
  },
  "required": ["name"],
  "additionalProperties": false
}
```

| Constraint | Description |
|------------|-------------|
| `properties` | Define each property and its schema |
| `required` | Array of mandatory field names |
| `additionalProperties` | `false` = no extra fields allowed; or a schema for extra fields |
| `minProperties` | Minimum number of properties |
| `maxProperties` | Maximum number of properties |

### 6. Arrays

```json
{
  "type": "array",
  "items": { "type": "string" },
  "minItems": 1,
  "maxItems": 10,
  "uniqueItems": true
}
```

| Constraint | Description |
|------------|-------------|
| `items` | Schema that all array items must match |
| `minItems` | Minimum array length |
| `maxItems` | Maximum array length |
| `uniqueItems` | `true` = no duplicate values allowed |
| `contains` | At least one item must match this schema |

#### Tuple Validation (Fixed-Position Items)

```json
{
  "type": "array",
  "prefixItems": [
    { "type": "integer" },
    { "type": "string" }
  ],
  "items": false
}
```

This validates arrays like `[1, "hello"]` where position matters.

---

## Value Constraints

### 7. Enums (Fixed Values)

```json
{
  "type": "string",
  "enum": ["red", "green", "blue"]
}
```

Only the listed values are allowed.

### 8. Const (Single Value)

```json
{
  "const": "fixed-value"
}
```

Only this exact value is allowed.

### 9. Default Values

```json
{
  "type": "string",
  "default": "unknown"
}
```

Suggests a default if no value is provided (not enforced, just metadata).

---

## Combining Schemas

### 10. Composition Keywords

```json
// Must match ALL schemas
{
  "allOf": [
    { "type": "object", "properties": { "name": { "type": "string" } } },
    { "required": ["name"] }
  ]
}

// Must match AT LEAST ONE schema
{
  "anyOf": [
    { "type": "string" },
    { "type": "integer" }
  ]
}

// Must match EXACTLY ONE schema
{
  "oneOf": [
    { "type": "string", "maxLength": 5 },
    { "type": "string", "minLength": 10 }
  ]
}

// Must NOT match this schema
{
  "not": { "type": "null" }
}
```

| Keyword | Description |
|---------|-------------|
| `allOf` | Data must be valid against ALL schemas |
| `anyOf` | Data must be valid against AT LEAST ONE schema |
| `oneOf` | Data must be valid against EXACTLY ONE schema |
| `not` | Data must NOT be valid against the schema |

---

## Reusability

### 11. References ($ref)

Reuse definitions to avoid repetition:

```json
{
  "$defs": {
    "address": {
      "type": "object",
      "properties": {
        "street": { "type": "string" },
        "city": { "type": "string" },
        "country": { "type": "string" }
      },
      "required": ["city", "country"]
    }
  },
  "type": "object",
  "properties": {
    "homeAddress": { "$ref": "#/$defs/address" },
    "workAddress": { "$ref": "#/$defs/address" }
  }
}
```

| Reference Type | Example |
|----------------|---------|
| Same file | `{ "$ref": "#/$defs/myDefinition" }` |
| External file | `{ "$ref": "other-schema.json" }` |
| External with path | `{ "$ref": "other-schema.json#/$defs/something" }` |

---

## Schema Versioning

### 12. Versioning Strategies

Schema evolution is critical for data projects. Here are patterns for versioning:

#### Version in `$id`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.com/schemas/v2/person.json",
  "title": "Person",
  "version": "2.1.0"
}
```

| Component | Example | Purpose |
|-----------|---------|---------|
| Path version | `/v2/` | Major version in URL path |
| `version` property | `"2.1.0"` | Semantic version for documentation |

#### Semantic Versioning for Schemas

| Change Type | Version Bump | Example |
|-------------|--------------|---------|
| **Breaking** (remove field, change type) | Major (v1 → v2) | Remove required field |
| **Additive** (new optional field) | Minor (v2.0 → v2.1) | Add `metadata` object |
| **Fix** (description, typo) | Patch (v2.1.0 → v2.1.1) | Fix description text |

#### Backwards-Compatible Changes

Safe changes that don't require major version bump:

```json
{
  "properties": {
    "newField": {
      "type": "string",
      "description": "Added in v2.1 - optional for backwards compatibility"
    }
  }
  // NOT in "required" array = backwards compatible
}
```

#### Deprecation Pattern

```json
{
  "properties": {
    "old_field": {
      "type": "string",
      "deprecated": true,
      "description": "DEPRECATED: Use 'new_field' instead. Will be removed in next major version."
    },
    "new_field": {
      "type": "string",
      "description": "Replacement for old_field"
    }
  }
}
```

---

## Conditional Schemas

### 13. If-Then-Else

```json
{
  "type": "object",
  "properties": {
    "type": { "enum": ["personal", "business"] },
    "companyName": { "type": "string" }
  },
  "if": {
    "properties": { "type": { "const": "business" } }
  },
  "then": {
    "required": ["companyName"]
  },
  "else": {
    "properties": { "companyName": false }
  }
}
```

If `type` is "business", then `companyName` is required.

---

## Complete Example

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://qud.example/verse-schema.json",
  "title": "Quranic Verse",
  "description": "Schema for a single verse entry",
  "type": "object",
  "properties": {
    "surah": {
      "type": "integer",
      "minimum": 1,
      "maximum": 114,
      "description": "Surah number (1-114)"
    },
    "ayah": {
      "type": "integer",
      "minimum": 1,
      "description": "Verse number within the surah"
    },
    "text": {
      "type": "string",
      "minLength": 1,
      "description": "Arabic text of the verse"
    },
    "tags": {
      "type": "array",
      "items": { "type": "string" },
      "uniqueItems": true,
      "description": "Optional categorization tags"
    }
  },
  "required": ["surah", "ayah", "text"],
  "additionalProperties": false
}
```

**Valid JSON for this schema:**

```json
{
  "surah": 1,
  "ayah": 1,
  "text": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
  "tags": ["bismillah", "opening"]
}
```

---

## Why Use JSON Schema?

| Use Case | Benefit |
|----------|---------|
| **Validation** | Automatically check if data is correct before processing |
| **Documentation** | Schema serves as living documentation |
| **Code Generation** | Generate TypeScript types, Python classes, etc. |
| **IDE Support** | Autocomplete and real-time error highlighting |
| **API Contracts** | Define exactly what APIs accept and return |
| **Data Quality** | Catch errors at the boundary, not deep in code |

---

## Validation Tools

### Python

```python
from jsonschema import validate, ValidationError
import json

schema = json.load(open("schema.json"))
data = json.load(open("data.json"))

try:
    validate(instance=data, schema=schema)
    print("Valid!")
except ValidationError as e:
    print(f"Invalid: {e.message}")
```

### Command Line

```bash
# Using ajv-cli (Node.js)
npx ajv-cli validate -s schema.json -d data.json

# Using check-jsonschema (Python)
pip install check-jsonschema
check-jsonschema --schemafile schema.json data.json
```

---

## Resources

- [JSON Schema Official Docs](https://json-schema.org/learn/getting-started-step-by-step)
- [JSON Schema Reference](https://json-schema.org/understanding-json-schema/)
- [Online Validator](https://www.jsonschemavalidator.net/)
