# QIR: Qiraat Structure
A **Metadata Schema** for describing Quranic Qiraat systems and narrations (the Ten Qiraat).

## Overview
The QIR layer defines a reference schema for representing **a single Quranic narration** (e.g., Hafs 'an 'Asim) in a structured, machine-readable format. This layer does **not** contain Quranic text or verse locations; instead, it serves as a foundational reference layer relied upon by other Quranic layers.

**Practical Example:**
- A single record may represent "Hafs 'an 'Asim", including narrator and imam, and general performance rules.

## Responsibilities
The QIR layer is responsible for describing the narration in terms of:
- Narrator
- Imam (primary reciter)
- Tajweed and recitation rules specific to each narration

**Practical Example:**
- `imam` field = "Hafs"
- `narrator` field = "'Asim"
- `qiraah_rules` field contains general rule names like: "Idgham with Ghunnah", "Mandatory Connected Madd"

## Design Scope
- Reference layer only
- Full focus on metadata
- Does not contain text, verse numbering, or Mushaf details
- May include external links to text or audio references if needed, without embedding them in the schema

**Note:** This layer strictly contains metadata and does not embed Quranic text, verse numbers, or Mushaf details.

## Files
- `schema.json` — JSON schema for Qiraat structure
- `models.py` — Optional Pydantic / ORM models
- `README.md` — QIR layer documentation

## Schema Overview
Each QIR record represents **a single narration** and is designed to be used as a **foreign key** by other layers, such as:
- Quranic text layers
- Tajweed rule systems
- Audio and phonetic analysis systems

**Practical Example for Linking:**
- The TXT layer uses `qiraah_id` to reference the narration in QIR
- The TAJ layer uses `qiraah_id` to link Tajweed rules with audio

## Research on Data Nature
Qiraat data is inherently **scholarly, documentary, and based on authoritative sources**, not crowd-sourced or subject to constant change. Core attributes (Imam, narrator) are stable over time, while differences are limited to **how rules are applied**, not the Quranic text itself. Therefore, QIR is designed as a **reference metadata layer**, not a textual layer.

## Detailed Schema Overview
The schema aims to represent **one narration per record**, adhering to normalization and strict value validation.

Key features:
- One-to-one representation per narration
- Reusable across different systems
- Does not contain Quranic text

**Practical Examples of Fields:**
- `qiraah_id`: unique identifier for each narration
- `imam`, `narrator`
- `qiraah_rules`: list of general rules
- `audio_examples`: links to illustrative audio clips
- `source_authority`: book or reference used
- `narrator_lineage`: transmission chain
- `transmission_confidence`: scholarly assessment of narration reliability

## What Can and Cannot Be Included in `qiraah_rules`
The `qiraah_rules` field is intended to represent **categories of rules**, not raw content or detailed data.

**Allowed:**
- Names or types of rules (e.g., types of Madd or Idgham)
- General, abstract descriptions of pronunciation behavior
- High-level identifiers or classifications for performance rules
- Links to audio references or external explanations

**Not allowed:**
- Full texts of verses or surahs
- Verse-by-verse documentation
- Raw audio data
- Timing, waveforms, or phonetic/temporal analysis

**Exceptionally allowed:**
- External links to audio files used **for reference only** (`audio_examples`) without embedding audio or analytical data in the schema

## Representing Scientific Authority (Source)
The scientific authority of a source is represented using multiple integrated fields:
- `source_authority`: scholarly reference or traditional text (string)
- `narrator_lineage`: transmission chain in order, suitable for automated linking
- `transmission_confidence`: scholarly assessment of narration reliability

**Practical Notes:**
- Each narrator or reference can be assigned a **unique ID** to facilitate automatic linking between layers
- Example: `"narrator_id": "n1", "source_authority": "Kitab al-Qiraat al-Kubra"`

## Schema Scoping Rationale
Quranic text, detailed Mushaf data, and precise audio analysis are **intentionally excluded** to avoid overlapping responsibilities. The QIR layer acts as a **legal/reference layer** used by other layers.

Benefits of this scoping:
- Prevents overlap with text, Tajweed, and audio layers
- Maintains a clear, layered architecture
- Ensures long-term maintainability

## Design Rationale
The QIR layer is designed to be:
- **Strict**: no undefined properties (`additionalProperties = false`)
- **Normalized**: reusable across multiple systems
- **Composable**: compatible with RDR, TXT, and TAJ layers

This makes QIR a **foundational layer suitable for long-term use**.

**Schema Version:** 1.0.0  
**Layer Code:** QIR

## Summary of Additions and Updates
This document has been expanded to clarify previously unclear aspects while maintaining its role as the definitive schema documentation.

Updates include:
- Added **practical examples** to illustrate real application of fields
- Added **unique identifiers** for narrations and narrators to facilitate automated linking
- Clarified what **can and cannot** be included in `qiraah_rules`, including audio references
- Explained how **scientific authority and transmission** are represented in a practical, linkable way
- Added **schema scoping rationale** to prevent overlap with other layers

These clarifications aim to improve reviewability, comprehension, and practical application, ensuring design consistency over time.

