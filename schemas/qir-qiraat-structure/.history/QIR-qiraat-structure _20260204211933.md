# QIR: Qiraat Structure

Foundational metadata schema for modeling Quranic Qiraat systems and narrations
(القراءات العشر).

## Overview

The QIR layer defines a reference schema for representing a single Quranic narration
(e.g., حفص عن عاصم) in a structured, machine-readable format.

This layer does **not** contain Quranic text or verse positions.
It serves as a foundational reference for other Quranic data layers.

## Responsibilities

The QIR layer is responsible for describing a Qiraah in terms of:

- The narrator (Rawi)
- The Imam (Primary Qari)
- Canonical classification within the Ten Qiraat
- Tajweed and recitation rules specific to the narration

## Design Scope

- Reference layer only
- Metadata-focused
- No text, ayah indexing, or mushaf content

## Files

- `schema.json` — Qiraat structure JSON Schema
- `models.py` — Optional Pydantic / ORM models
- `README.md` — QIR layer documentation

## Schema Overview

Each QIR record represents **one narration** and is designed to be used as a
foreign key reference by other layers such as:

- Quranic text layers
- Tajweed rule engines
- Phonetic and audio analysis systems

## Required Fields

- `narration_id`
- `reader_name_ar`
- `reader_name_en`
- `narrator_name_ar`
- `narrator_name_en`
- `full_name`
- `canonical_category`

## Canonical Classification

The `canonical_category` field identifies the narration’s canonical position
within the Ten Qiraat and supports the following values:

- `nafi`
- `ibn_kathir`
- `abu_amr`
- `ibn_amir`
- `asim`
- `hamzah`
- `al_kisai`
- `abu_jafar`
- `yaqub`
- `khalaf`
- `ten_canonical`
- `additional`

## Design Principles

- **Normalization-first**: No duplication of data across layers
- **Schema-driven**: JSON Schema compatible
- **Strict validation**: `additionalProperties = false`
- **Extensible**: Future-proof for advanced tajweed and phonetic rules

## Intended Usage

The QIR layer acts as a foundational reference for:

- Comparative Qiraat analysis
- Educational platforms
- Tajweed validation systems
- Phonetic and audio research
- Linking Quranic text to its correct narration

---

**Schema Version:** 1.0.0  
**Layer Code:** QIR
