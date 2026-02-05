# SYM: Character Symbols

Schema for symbols that modify base letters in the Quranic text — diacritics, extensions, tajweed marks, and tatweel.

## Files

- `schema.json` — Symbol instance schema (lean, 3 fields per record)
- `symbol_catalog.json` — Symbol catalog schema (discriminated union defining ~24 symbol types)
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

- **Cardinality**: At most 1 diacritic per letter (2 when one is shadda), at most 1 extension, at most 1 tajweed mark. All category pairs can co-occur.
- **Rare symbols**: Imala (1 occurrence), Ishmam/Tasheel (2), Small Noon (1), Small Seen (3) — these are narration-specific edge cases.

## Design Decisions

### Non-letter symbols excluded

Symbols that don't modify a base letter are **not** included in this schema. Every SYM record requires a `character_ref` FK to the CHR layer, and these symbols don't attach to a letter:

- **Stop signs** — While Unicode places these as combining marks, they semantically belong at word/sentence level. A stop sign indicates where a reader *may* or *must* pause — this is a property of the recitation flow between words, not a modification of a single letter.
- **Rub El Hizb** (U+06DE) — Marks structural divisions
- **Sajdah marks** (U+06E9, U+06E4) — Verse-level prostration indicators
- **Aya end markers** — Delimit verses

These belong in:
- **SNT (Sentence Structure)** — Stop signs define waqf/pause structure at sentence level
- **DIV (Division Structure)** — Rub El Hizb marks structural divisions
- **AYA (Verse Structure)** — Aya end markers and sajdah marks

### Normalized catalog + lean instances

The schema is split into a **symbol catalog** (~24 reference entries) and **symbol instances** (~300,000 records). This follows the project's architectural principle of no redundant storage (`schemas/README.md`). Fields like `symbol_name`, `symbol_char`, `unicode_name`, `category`, and `subcategory` are properties of the symbol *type*, not the instance — repeating them per record would add ~24 MB of redundant data. Instead, each instance carries only `symbol_codepoint` as an FK to the catalog.

Alternatives considered:
- **Denormalized (self-contained records)** — every instance carries all metadata. Simpler to read in isolation, but violates the project's normalization goals and repeats static data across hundreds of thousands of records.
- **Fully normalized with integer FK** — a numeric ID instead of codepoint as the FK. Rejected because `symbol_codepoint` is already a natural key — unique, stable, and human-readable.

### Discriminated union pattern

The catalog uses `oneOf` with a `category` discriminator per the project's schema subtyping guidelines (see `schemas/README.md`). This was chosen over a flat enum because categories have high field overlap. The discriminated union lives in the catalog, not the instance schema — instances don't need category validation since the catalog already constrains valid symbol types.

## UUID Assessment

**Convention:** `{narration}:{edition}:s{surah}:v{verse}:w{word}:c{char}:sym.{slot}`

| Check | Status | Notes |
|-------|--------|-------|
| Uniqueness | Pass | Full character path + `sym.{slot}` suffix prevents collisions |
| Determinism | Pass | Category names are deterministic — no ordering needed |
| Edition context | Pass | Edition segment handles edition-level symbol variation |
| Dependencies | Pass | Chain `symbol → char → word → verse → surah` is sound |
| Cross-narration | Pass | Narration is the first segment |

### Category-based slots

Since each category has cardinality 0..1 per character, we use category names directly as slots instead of numeric indices. This eliminates the need for an ordering convention — the slot name is inherently deterministic.

| Slot | Category | Cardinality |
|------|----------|-------------|
| `sym.diacritic` | diacritic (haraka, tanween, sukun) | 0..1 |
| `sym.shadda` | diacritic (shadda only) | 0..1 |
| `sym.extension` | extension | 0..1 |
| `sym.tajweed` | tajweed | 0..1 |
| `sym.tatweel` | tatweel | 0..1 |


### Edition context in UUID

Symbols vary not just by narration but by mushaf type and edition. Tajweed notation and even some diacritics differ across editions (e.g., King Fahd Complex vs Cairo edition). The edition segment in the UUID prevents collisions between different editions of the same narration.

This change is scoped to SYM only. Base letters and word boundaries are likely narration-level (to be determined in those layers' research), but symbol annotation is edition-dependent. The `character_ref` FK still points to a narration-level CHR entity.

## Cross-Layer Relationships

### SYM boundaries and neighboring layers

SYM stores the **symbols themselves** — what they are and which letter they sit on. It does not store the meaning, rules, or relationships between symbols. The layer boundaries are:

| Layer | Relationship to SYM |
|-------|---------------------|
| **CHR** | SYM → CHR via `character_ref` FK. Each symbol modifies exactly one base letter. |
| **TJW** | TJW references SYM (and CHR) via FKs. Tajweed *rules* live in TJW — they link letters and symbols to describe relationships (e.g., idghaam connecting a noon symbol on one letter to the following letter). SYM only stores the tajweed *mark* as a visual symbol on a character. |
| **SNT** | Stop signs belong in SNT, not SYM — they define waqf/pause structure at word/sentence level, not letter-level modifications. SNT owns stop sign data and their semantic relationships to recitation flow. |
| **UTH / QSY** | SYM symbols are orthography-dependent. Uthmani text uses symbols (extensions, tajweed marks) that Qiasy text does not. The same word may carry different symbols in UTH vs QSY representations. |
| **DIV / AYA** | Non-letter symbols (Rub Hizb, aya markers, sajdah marks) excluded from SYM — these belong in DIV/AYA as structural markers. |

### Why tajweed marks stay in SYM, not TJW

Tajweed marks (maddah, iqlab, small seen, etc.) are **visual symbols attached to a letter** — they have a codepoint, a character ref, and a position in the text. TJW is a higher-level layer that defines tajweed *rules* as relationships between entities. TJW will have FKs pointing to SYM symbols and CHR letters to express rules like "this iqlab mark on letter X triggers a sound change involving letter Y." Moving the marks into TJW would conflate the symbol (data) with the rule (interpretation).

### Layer independence assessment

SYM is correctly scoped. No split or merge recommended:

- **Not too big** — 4 categories with high field overlap, well served by a single discriminated union schema.
- **Not too small** — Merging into CHR would overload CHR with combining mark logic. Symbols have their own cardinality rules, category taxonomy, and edition-level variation that justify a separate layer.
- **Clean boundary** — SYM = "what symbols exist on a letter." CHR = "what letter it is." TJW = "what the symbols mean together."
