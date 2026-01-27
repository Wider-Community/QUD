# SYM: Character Symbols

Schema for symbols that modify base letters in the Quranic text — diacritics, extensions, stop signs, tajweed marks, and tatweel.

## Files

- `schema.json` — Symbol instance schema (lean, 3 fields per record)
- `symbol_catalog.json` — Symbol catalog schema (discriminated union defining ~30 symbol types)
- `models.py` — Pydantic models for both catalog entries and instances
- `hafs_symbols.md` — Full symbol categorization and cardinality analysis from Uthmanic Hafs v2.0

## Schema Overview

SYM is split into two schemas following the project's normalization principles (no redundant storage):

### Symbol catalog (`symbol_catalog.json`)

Reference data for all symbol types, keyed by `symbol_codepoint`. Uses a discriminated union on `category` to constrain valid category/subcategory pairs:

| Category | Subcategories |
|----------|---------------|
| `diacritic` | haraka, tanween_closed, tanween_open, sukun, shadda |
| `extension` | dagger_alef, small_waw, small_yaa, small_high_yaa |
| `stop_sign` | sili, qili, lazim, jaiz, either_of, seen_sakt |
| `tajweed` | maddah, iqlab_above/below, silent_alef/vowel, imala, ishmam_tasheel, small_noon, small_seen |
| `tatweel` | tatweel |

Each entry carries: `symbol_codepoint`, `symbol_name`, `symbol_char`, `unicode_name`, `category`, `subcategory`, `narration_specific`.

### Symbol instance (`schema.json`)

One record per symbol occurrence on a base letter. Three fields only:

- `symbol_id` — UUID primary key
- `character_ref` — FK to CHR (which letter)
- `symbol_codepoint` — FK to catalog (which symbol)

This avoids repeating name, category, and Unicode metadata across ~300,000 instance records.

## Research Findings

Key findings from the Hafs symbol analysis (see `hafs_symbols.md`):

- **Cardinality**: At most 1 diacritic per letter (2 when one is shadda), at most 1 extension, at most 1 stop sign, at most 1 tajweed mark. All category pairs can co-occur.
- **Rare symbols**: Imala (1 occurrence), Ishmam/Tasheel (2), Small Noon (1), Small Seen (3) — these are narration-specific edge cases.
- **Dual-function U+06DC**: Small High Seen serves as both a stop sign (sakt, 5 occurrences) and a tajweed mark (small seen, 3 occurrences). The schema handles this by having `seen_sakt` under stop signs and `small_seen` under tajweed as separate subcategories.

## Design Decisions

### Non-letter symbols excluded

Symbols that don't modify a base letter — Rub El Hizb (U+06DE), Sajdah marks (U+06E9, U+06E4), and aya end markers — are **not** included in this schema. Every SYM record requires a `character_ref` FK to the CHR layer, and these symbols don't attach to a letter.

These belong in either:
- **DIV (Division Structure)** — Rub El Hizb marks structural divisions
- **AYA (Verse Structure)** — Aya end markers delimit verses
- A **separate layer** if non-letter symbols need their own entity model

### Normalized catalog + lean instances

The schema is split into a **symbol catalog** (~30 reference entries) and **symbol instances** (~300,000 records). This follows the project's architectural principle of no redundant storage (`schemas/README.md`). Fields like `symbol_name`, `symbol_char`, `unicode_name`, `category`, and `subcategory` are properties of the symbol *type*, not the instance — repeating them per record would add ~24 MB of redundant data. Instead, each instance carries only `symbol_codepoint` as an FK to the catalog.

Alternatives considered:
- **Denormalized (self-contained records)** — every instance carries all metadata. Simpler to read in isolation, but violates the project's normalization goals and repeats static data across hundreds of thousands of records.
- **Fully normalized with integer FK** — a numeric ID instead of codepoint as the FK. Rejected because `symbol_codepoint` is already a natural key — unique, stable, and human-readable.

### Discriminated union pattern

The catalog uses `oneOf` with a `category` discriminator per the project's schema subtyping guidelines (see `schemas/README.md`). This was chosen over a flat enum because categories have high field overlap. The discriminated union lives in the catalog, not the instance schema — instances don't need category validation since the catalog already constrains valid symbol types.

## UUID Assessment

**Current convention:** `{narration}:s{surah}:v{verse}:w{word}:c{char}:sym{symbol}`

| Check | Status | Notes |
|-------|--------|-------|
| Uniqueness | Pass | Full character path + `sym{n}` suffix prevents collisions |
| Determinism | **Needs ordering convention** | See below |
| Edition ambiguity | **Needs edition in name string** | See below |
| Dependencies | Pass | Chain `symbol → char → word → verse → surah` is sound |
| Cross-narration | Pass | Narration is the first segment |

### Ordering convention needed

The `sym{n}` index requires a stable ordering of symbols on a character. A character carrying symbols from multiple categories (e.g., Fatha + Maddah + Qili) needs a defined rule for which is `sym1`, `sym2`, `sym3`. Without this, two implementations could assign different indices to the same symbols.

Proposed fixed priority:

| Priority | Category |
|----------|----------|
| 1 | diacritic |
| 2 | extension |
| 3 | tajweed |
| 4 | stop_sign |
| 5 | tatweel |

Within the same category (rare — cardinality is 0..1 per category), sort by codepoint ascending.

**Example:**

| Index | Symbol | Category | Priority | UUID name string |
|-------|--------|----------|----------|------------------|
| sym1 | Fatha | diacritic | 1 | `hafs:s2:v255:w4:c1:sym1` |
| sym2 | Maddah | tajweed | 3 | `hafs:s2:v255:w4:c1:sym2` |
| sym3 | Qili | stop_sign | 4 | `hafs:s2:v255:w4:c1:sym3` |

### Edition context missing from UUID

Symbols vary not just by narration but by mushaf type and edition. Stop signs, tajweed notation, and even some diacritics differ across editions (e.g., King Fahd Complex vs Cairo edition). The current name string uses only narration, meaning two editions of Hafs would produce the same UUID for different symbol sets — a collision.

**Proposed fix:**

```
# Current (ambiguous)
{narration}:s{surah}:v{verse}:w{word}:c{char}:sym{symbol}

# Proposed
{narration}:{edition}:s{surah}:v{verse}:w{word}:c{char}:sym{symbol}
```

This change is scoped to SYM only. Base letters and word boundaries are likely narration-level (to be determined in those layers' research), but symbol annotation is edition-dependent. The `character_ref` FK still points to a narration-level CHR entity.

## Cross-Layer Relationships

### SYM boundaries and neighboring layers

SYM stores the **symbols themselves** — what they are and which letter they sit on. It does not store the meaning, rules, or relationships between symbols. The layer boundaries are:

| Layer | Relationship to SYM |
|-------|---------------------|
| **CHR** | SYM → CHR via `character_ref` FK. Each symbol modifies exactly one base letter. |
| **TJW** | TJW references SYM (and CHR) via FKs. Tajweed *rules* live in TJW — they link letters and symbols to describe relationships (e.g., idghaam connecting a noon symbol on one letter to the following letter). SYM only stores the tajweed *mark* as a visual symbol on a character. |
| **SNT** | Stop signs in SYM mark where stops can occur. SNT defines sentence/waqf structure. Future cross-layer mappings may link stop sign symbols to SNT sentence boundaries. |
| **UTH / QSY** | SYM symbols are orthography-dependent. Uthmani text uses symbols (extensions, tajweed marks) that Qiasy text does not. The same word may carry different symbols in UTH vs QSY representations. |
| **DIV / AYA** | Non-letter symbols (Rub Hizb, aya markers) excluded from SYM — these possibly belong in DIV/AYA as structural markers. |

### Why tajweed marks stay in SYM, not TJW

Tajweed marks (maddah, iqlab, small seen, etc.) are **visual symbols attached to a letter** — they have a codepoint, a character ref, and a position in the text. TJW is a higher-level layer that defines tajweed *rules* as relationships between entities. TJW will have FKs pointing to SYM symbols and CHR letters to express rules like "this iqlab mark on letter X triggers a sound change involving letter Y." Moving the marks into TJW would conflate the symbol (data) with the rule (interpretation).

### Layer independence assessment

SYM is correctly scoped. No split or merge recommended:

- **Not too big** — 5 categories with high field overlap, well served by a single discriminated union schema.
- **Not too small** — Merging into CHR would overload CHR with combining mark logic. Symbols have their own cardinality rules, category taxonomy, and edition-level variation that justify a separate layer.
- **Clean boundary** — SYM = "what symbols exist on a letter." CHR = "what letter it is." TJW = "what the symbols mean together."
