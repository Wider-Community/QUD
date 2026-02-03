# PAG Page Layout Generator (Hafs – KFGQPC v2)

**Project**: QUD – Quranic Data Layer  
**Layer**: PAG (Page Layout)  
**Narration**: Hafs  
**Edition**: KFGQPC v2  

---

## Overview

This script generates **PAG (Page Layout)** entities for the **Hafs narration** using the **KFGQPC v2** dataset.  
Each PAG entity represents a single Mushaf page and defines its structural boundaries in terms of verses and characters.

The output is a schema-compliant JSON file designed for direct integration into the QUD PAG layer.

---

## Data Source

The script reads from the following CSV file:
```hafsData_v2-0.csv```

---

## Output

The generated data is written to:
```pag-page-layout.json```


All output is UTF-8 encoded and formatted for readability.

---

## UUID Generation

All identifiers are generated deterministically using UUID v5 functions from:

```research-tools/generators/uuid_generator.py```


The following generators are used:

- `page_id` – Page-level identifier  
- `verse_id` – Start and end verse references  
- `char_id` – Character-level boundary references
- `mushaf_id` - Reference to the Mushaf structure (MSH layer)

This ensures stable IDs across runs and consistent cross-layer references.

---

## Page Grouping Logic

Rows are grouped by the `page` column in the CSV file.

For each page group:

- The **first row** determines the start surah and ayah
- The **last row** determines the end surah and ayah
- Empty page groups are skipped

Each group produces exactly **one PAG entity**.

---

## Page Number Validation

Page numbers are validated before processing.

A page number is considered valid if:

- It is an integer
- It is greater than or equal to 1

Invalid page numbers are skipped to prevent invalid PAG entries.

---

## Surah and Ayah Validation

Surah and ayah values are parsed using safe integer conversion.

- Values that cannot be converted to integers are rejected
- Any page group with invalid start or end surah/ayah values is skipped

This guarantees that all generated UUIDs reference valid Quranic positions.

---

## Arabic Character Counting

Character boundaries are determined by counting **Arabic letters only**.

The counting logic:

- Matches Arabic letters in Unicode range U+0621–U+064A
- Excludes:
  - Spaces
  - Punctuation
  - Quranic symbols
  - Tashkeel (diacritics)

If the input text is not a string, the count safely returns zero.

---

## Safe Character Index Enforcement

The PAG schema requires **positive character indices**.

To ensure schema compliance:

- Character counts are clamped to a minimum value of `1`
- This guarantees that `end_character_ref` is always valid

Character references always start at:
- Word index: `1`
- Character index: `1`

---

## Character Text Source

Arabic character counting uses the following dataset column:

```aya_text_emlaey```


This ensures consistency with the Emlaey orthographic representation used in the Hafs dataset.

---

## PAG Entity Structure

Each generated PAG object includes:

- `page_id` – Deterministic UUID for the page
- `mushaf_ref` – Reference to the Mushaf entity
- `page_number` – Page number from the dataset
- `start_verse_ref` – UUID of the first verse on the page
- `end_verse_ref` – UUID of the last verse on the page
- `start_character_ref` – Start character boundary
- `end_character_ref` – End character boundary
- `line_count` – Fixed value of `15`

All fields conform to the PAG JSON Schema.

---

## Error Handling Strategy

- Invalid rows are skipped silently
- Processing continues even if individual pages fail validation
- No partial or malformed PAG entities are written

This design prioritizes **data integrity over completeness**.

---

## Notes

- Page numbers are assumed to be clean integers in the Hafs dataset
- No page range normalization is required for this version
- UUID generation is fully deterministic and reproducible
- Character-level precision is preserved without relying on word segmentation

---

**Last Updated**: 2026-02-02
