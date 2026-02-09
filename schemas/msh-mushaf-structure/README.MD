# MSH: Mushaf Structure

Schema for representing a Mushaf's Specific text
## Files

- `schema.json` — Mushaf instance schema
- `models.py` — Pydantic models for both catalog entries and instances


## Schema Overview

A mushaf is represented as an Array of words, representation of the Ayahs, Lines,  Surahs and Divisions would be then defined as indices of said array with Pages being an array of lines. 

## Research Findings

Key findings from the Analysis of various Hafs and Warsh as well as Indo-Pak mushafs:

- **The Word Layer is great as an atomic unit of any mushaf/qiraat**: 
    1. All Ayas, lines, surahs and pages start and end with words. 
    2. All diacritics can be tied to either a word or a character in a word.


## Design Decisions


### Mushaf Text is represented as an array of word references

the `complete_text` array is an array of foreign keys to be sequentially populated by words from the Mushaf's Source. All layers higher than that can be done either on the same pass or on additional passes.

### Sajdah symbols  are Defined by word locations

 Sajdah marks (U+06E9, U+06E4) are defined by Indices of the words under which the line is to be drawn. 

## UUID Assessment

*yet to be tackled*


## Cross-Layer Relationships

### Mushaf and the other layers

SYM stores the **symbols themselves** — what they are and which letter they sit on. It does not store the meaning, rules, or relationships between symbols. The layer boundaries are:

| Layer         | Relationship to MSH                                               |
| ------------- | ----------------------------------------------------------------- |
| **WRD**       | N:1 via `complete_text`  Array.  All words are stored in sequence |
| **Line**      | Defined as a subarray of  `complete_text`                         |
| **Ayah**      | Defined as a subarray of  `complete_text`                         |
| QIR           | 1:N As a single Qiraah may have multiple Mushafs                  |
| **DIV / AYA** | Rubs, Hizbs and Ayas are defined per Mushaf                       |

### Layer independence assessment

MSH is correctly scoped. No split or merge recommended:

- **Not too big** — Strictly encapsulates all mushaf Specific information without taking the responsibility of any other layer
- **Not too small** — All information required to textually and structurally recreate a Mushaf are accounted for
