# Research Context & Prior Work

**Research Topic**: Quranic Data Layer Architecture
**Date**: 2025-11-03
**Related Spec**: [spec.md](./spec.md)

## Purpose

This document consolidates prior work, domain knowledge, and technical best practices relevant to the Quranic Data Layer Architecture research. It resolves all "NEEDS CLARIFICATION" items identified during planning and provides research foundation for RR-001, RR-002, and RR-003.

## Domain Background

### Quranic Data Complexity

The Quranic text presents unique data modeling challenges:

1. **Multiple Recitation Systems**: The 10 canonical narrations (القراءات العشر) with 20 narrations represent authentic variations in pronunciation, word choice, and verse boundaries - not errors or alternatives
2. **Layered Semantics**: Quranic data inherently consists of multiple semantic layers (characters, words, verses, chapters, page layout, orthographic systems) that are often conflated in digital representations
3. **Sacred Text Integrity**: Zero tolerance for errors requires rigorous validation against authoritative sources
4. **Scholarly Tradition**: 1400+ years of Islamic scholarship provides authoritative metadata (tajweed rules, narration chains, Makki/Madani classification) that must be preserved

### Existing Digital Quranic Data Projects

**Prior Work Analysis**:

1. **Tanzil.net**:
   - Provides simple text format (one verse per line)
   - Single narration focus (primarily Hafs)
   - Minimal layer separation (conflates text layers)
   - Strength: Verified accuracy, wide adoption
   - Limitation: Flat structure limits advanced queries

2. **Quran.com**:
   - Rich web interface with multiple narrations
   - Translation and tafsir integration
   - Strength: User-facing features, multimedia
   - Limitation: API focused on consumption, not data architecture research

3. **QS-QIRAAT Dataset** (our primary source):
   - 7 narrations from King Fahd Complex
   - Multiple format exports (JSON, CSV, XML, SQL, XLSX)
   - Strength: Authoritative source, multiple narrations, rich metadata
   - **Identified Problem**: Conflates multiple layers in flat schema (motivation for our research)

4. **Digital Khatt Project**:
   - Focuses on Arabic typography and rendering
   - Relevant for Layer 2 (character rendering)
   - Strength: Detailed rendering rules
   - Limitation: Not narration-specific

### Gap Identified

**No existing project systematically separates Quranic data into semantic layers with formal schemas enabling generative architecture.** This research explores whether such separation is feasible and beneficial.

---

## CRITICAL RESOURCE: QUL (Quranic Universal Library) at qul.tarteel.ai

### Overview

**CRITICAL FINDING**: The Quranic Universal Library (QUL) at **qul.tarteel.ai** is the **MOST COMPREHENSIVE hub for Quranic NLP resources** available for download. This platform provides curated, open-source digital Quran resources that can save months of data sourcing, formatting, and validation work.

**Website**: https://qul.tarteel.ai
**GitHub**: https://github.com/TarteelAI/quranic-universal-library
**Download Formats**: SQLite, JSON
**License**: Open source (attribution required)
**Status**: No API - download-only platform with active community contributions

**COMPREHENSIVE CATALOG**: A detailed 24-section catalog of all QUL resources has been compiled and saved to:
- **File**: `/Users/mac/Work/ITQAN Community/QUD/QUL_Tarteel_NLP_Resources_Catalog.md`
- **Size**: 920 lines covering morphology, syntax, tajweed, audio, translations, and more

### CRITICAL LIMITATION: Hafs-Only Coverage

**VALIDATED FINDING**: ALL QUL linguistic resources (morphology, syntax, POS tagging, tajweed) are based on the **Hafs 'an 'Asim narration ONLY**.

**Evidence**:
- **MASAQ dataset explicitly states**: "Ḥafṣ 'an 'Āṣim reading tradition"
- Corpus.quran.com (Dr. Kais Dukes) uses standard Uthmani text (Hafs)
- 21 Hafs-specific Quran scripts in QUL catalog
- 50+ Hafs audio reciters (no Warsh/other Qiraat audio catalog found)
- 3 Hafs-specific fonts (QPC Hafs, Digital Khatt)
- Zero Warsh, Qalun, Shu'bah, or other Qiraat morphology/syntax resources found

**Implication for QUD Research**:
- QUL is **PERFECT for Hafs narration validation** (Phase 1 delivery includes Hafs)
- QUL is **INSUFFICIENT for cross-Qiraah research** (Warsh, Qalun, etc. need external sources)
- Multi-Qiraat morphological analysis is a **SIGNIFICANT RESEARCH GAP** in the field

### Available Resources (Summary)

#### 1. Morphological Analysis (77,429 words)

**QUL Morphology Collection**:
- Word Lemma (normalized lexical forms)
- Word Root (Arabic root forms)
- Word Stem
- Complete morphological analysis
- **Format**: SQLite database + JSON
- **Source**: Based on corpus.quran.com by Dr. Kais Dukes

**Quranic Arabic Corpus (corpus.quran.com v0.4)**:
- **File**: quranic-corpus-morphology-0.4.txt (tab-separated)
- **Columns**: LOCATION (chapter:verse:word:morpheme), FORM (Buckwalter), TAG (POS), FEATURES (pipe-delimited)
- **Coverage**: All 77,430 words with POS tags, lemmas, roots, gender, case, number, person, tense, voice, mood
- **License**: GNU GPL (no modifications allowed)
- **Access**: Free download with email verification

**MASAQ Dataset (Mendeley)**:
- **Entries**: 131,000+ morphological + 123,000+ syntactic
- **Columns**: 20 columns per row
- **Formats**: TXT, CSV, XLSX, XML, JSON (most flexible)
- **License**: CC-BY 4.0 (most permissive)
- **Standard**: 1924 Cairo edition by Al-Azhar
- **Methodology**: Traditional i'rab

#### 2. Syntactic Analysis

**Quranic Arabic Dependency Treebank (QADT)**:
- **Gold Standard**: 11,000 words annotated (14% complete)
- **Total Coverage**: 77,430 words (morphology complete)
- **Framework**: Hybrid dependency/phrase structure grammar
- **Methodology**: Traditional Arabic grammar (i'rab)
- **Documentation**: Dr. Kais Dukes PhD thesis chapters 3, 5, 6

#### 3. Part-of-Speech Tagging

- **Tags**: N (noun), V (verb), P (particle), PN (proper noun), ADJ, DET, PRON, T (time)
- **Extended**: Verb forms I-X, attributes, verbal features (active/passive, perfect/imperfect)
- **Coverage**: All 77,430 words
- **Format**: Embedded in morphology file (TAG column)

#### 4. Tajweed Resources

**21 Tajweed Rule Categories**:
- Hamza rules (ham_wasl, laam_shamsiyah)
- Elongation/Madd (madda_normal, madda_permissible, madda_necessary, madda_obligatory_mottasel, madda_obligatory_monfasel, madd_al_tamkeen)
- Assimilation/Idgham (idgham_ghunnah, idgham_wo_ghunnah, idgham_shafawi)
- Concealment/Clarity (ikhafa, ikhafa_shafawi, izhar, izhar_shafawi)
- Other (ghunnah, qalaqah, iqlab, tafkheem/heavy, tarqeeq/light, slnt/silent)

**Tool**: https://qul.tarteel.ai/tajweed_words/ (character-indexed word-level annotation)
**Status**: Auto-annotated (may contain errors, community verification ongoing)
**Scripts**: QPC Hafs with colored tajweed marks, Uthmani tajweed variants

#### 5. Quran Text & Scripts (26 resources)

**Unicode Formats**:
- Uthmani (القرآن الكريم بالرسم العثماني)
- Indopak
- Madani
- Simplified/Modern Arabic

**Image Formats**: Page-by-page PNG/SVG with tajweed colors
**Specialized**: Word-by-word layouts, ayah-segmented text

#### 6. Audio Recitations (152 total)

- **90 Unsegmented**: Complete surah/Quran recordings
- **62 Segmented**: Ayah-by-ayah and surah-by-surah with timestamps
- **Reciters**: 50+ in Hafs tradition (Abdul Basit, Mishari al-Afasy, Al-Husary, etc.)
- **Format**: MP3 audio + JSON timestamp data
- **Timestamp Granularity**: Ayah-by-ayah, surah-by-surah, word-by-word (some)

#### 7. Translations & Tafsir

- **193 Full Quran translations** (43+ languages)
- **15 Word-by-word translations** (interlinear format)
- **114 Tafsir resources** (32 mukhtasar/concise + 82 detailed)
- **Format**: SQLite, JSON

#### 8. Metadata & Structural Resources

- **Quran Metadata**: Surah (114), Ayah (6,236 for Hafs), Juz (30), Hizb (60), Rub (240), Manzil (7)
- **Mushaf Layouts**: 26 layouts (21 production-ready, 5 WIP)
- **Surah Information**: 7 languages with revelation context, themes, topics

#### 9. Semantic & Conceptual Resources

- **Topics and Concepts**: 2,512 entries (ontology/knowledge graph)
- **Mutashabihat**: 5,277 similar ayah phrases by meaning/context/wording
- **Similar Ayahs**: 4,001 comparative ayah alignments
- **Ayah Themes**: 1,049 thematic tags

#### 10. Transliteration (9 resources)

- 8 Ayah-by-ayah transliterations (various schemes)
- 1 Word-by-word transliteration
- Latin script representation for non-Arabic readers

### Why QUL Matters for QUD Research

**✅ MASSIVE VALUE FOR HAFS VALIDATION**:
1. **Layer 3 (Word Structure)**: 77,429 morphologically analyzed words provide ground truth
2. **Layer 4 (Sentence Structure)**: 11,000 gold-standard syntax annotations (partial but authoritative)
3. **Layer 1 (Symbols/Rendering)**: 21 tajweed rule categories for character symbol generation validation
4. **Layer 5 (Verse Structure)**: 6,236 Hafs verses with metadata for boundary validation
5. **Layer 11-12 (Page/Line Layout)**: 26 Mushaf layouts provide page/line organization data
6. **Cross-Validation**: Multiple independent sources (Corpus, MASAQ, QUL) enable triangulation

**⚠️ LIMITATIONS FOR MULTI-QIRAAT RESEARCH**:
1. **No Warsh morphology** - cannot validate Layer 3 word structure differences for Warsh
2. **No cross-Qiraah alignment** - cannot map Hafs morphology to Warsh equivalents
3. **No variant annotations** - textual variants (Qira'at) not marked in morphology/syntax
4. **Hafs-centric schemas** - schemas may not generalize to other narrations without modification

**STRATEGIC DECISION**:
- **Phase 1 (Hafs + Warsh)**: Use QUL extensively for Hafs, use QS-QIRAAT for Warsh (text only, no morphology)
- **Phase 2-3 (Expand)**: Manually extend QUL-style morphology/syntax to other narrations OR wait for community contributions
- **Research Contribution**: QUD could contribute morphologically analyzed Warsh data back to QUL community

### External Multi-Qiraat Resources (NOT in QUL)

Since QUL is Hafs-only, these external resources provide multi-Qiraat coverage:

#### 1. Encyclopedia of Variant Readings (ErQuran)

**URL**: https://erquran.org/
**Creator**: Professor Shady Nasser (Harvard University)
**Release**: 2022
**License**: Open access

**Features**:
- **3,744+ total variants** for 10 canonical Qiraat (al-Shāṭibiyya + al-Durra)
- Canonical AND non-canonical variant readings
- Detailed metadata: variant type, sources, transmitters, status, audio attachments
- Searchable/filterable database
- Word/phrase level variant tracking

**Format**: Web interface (JavaScript-based, may require scraping for bulk data)
**Coverage**: 10 canonical Qiraat + non-canonical readings

#### 2. nquran.com

**URL**: http://nquran.com
**Type**: Comparative Qiraat viewer (Arabic)

**Features**:
- Color-coded Arabic script highlighting differences
- 10 canonical readings with 2 transmissions each (20 narrations)
- Verse-by-verse comparison
- URL-editable verse selection

**Format**: Web interface (no bulk download documented)

#### 3. Corpus Coranicum

**URL**: https://corpuscoranicum.de/
**Institution**: Berlin-Brandenburg Academy of Sciences

**Features**:
- Variant readings tab for 7 main canonical readings
- Transliterated variants
- Manuscript images for each verse
- Historical and textual criticism focus

**Format**: Web interface
**Coverage**: 7 main canonical Qiraat

#### 4. Bridges Foundation Translation

**Platform**: iOS and Android app (free)
**Creator**: Fadel Soliman
**Release**: 2020

**Features**:
- Words with canonical variants in red font
- Tap for explanatory footnotes showing different readings
- 415 variant words (30% alter meaning)
- 10 Qiraat coverage in English translation

**Format**: Mobile app (not downloadable dataset)

#### 5. QS-QIRAAT Dataset (Our Primary Source)

**Advantage over QUL**: Contains 6 narrations (Hafs, Warsh, Qalun, Shu'bah, Al-Duri, Al-Susi) from 3-4 Qiraat
**Limitation vs QUL**: No morphology, syntax, or tajweed annotations - just text + metadata

### Recommended Research Workflow

**For Hafs Narration (Phase 1)**:
1. ✅ Use QUL/Corpus for morphology validation (77,429 words)
2. ✅ Use MASAQ for syntax validation (131,000+ entries, multiple formats)
3. ✅ Use QUL tajweed for Layer 1 symbol generation validation (21 rule categories)
4. ✅ Use QUL audio for audio-text alignment research (62 segmented narrations)
5. ✅ Cross-validate with QS-QIRAAT Hafs text (character/verse counts)

**For Warsh Narration (Phase 1)**:
1. ⚠️ Use QS-QIRAAT Warsh text as primary source (no morphology available)
2. ⚠️ Manually annotate sample morphology OR defer morphology validation to Phase 2-3
3. ⚠️ Use ErQuran for variant word identification (where Warsh differs from Hafs)
4. ⚠️ Rely on internal consistency validation (schema conformance, character counts)

**For Cross-Qiraah Validation (Phase 2-3)**:
1. Use ErQuran for systematic variant cataloging (3,744+ variants)
2. Use nquran.com for visual comparison and variant verification
3. Use Corpus Coranicum for academic rigor and manuscript evidence
4. Consider manual morphological annotation project for non-Hafs Qiraat

### Data Quality & Licensing

| Resource | License | Commercial Use | Modification | Attribution |
|----------|---------|----------------|--------------|-------------|
| QUL Resources | Open Source | ✓ | ✓ | Required |
| Corpus.quran.com | GNU GPL | ✓ | ✗ (prohibited) | Required + Link |
| MASAQ Dataset | CC-BY 4.0 | ✓ | ✓ | Required |
| ErQuran | Open Access | ✓ | ? (TBD) | Likely required |

**Data Quality Notes**:
- **Corpus v0.4** (2011): Lemmas need standardization, some feminine marking errors, syntax only 14% complete
- **QUL Tajweed**: Auto-annotated, may contain errors, community verification ongoing
- **MASAQ v2** (2024): Most recent, most complete morphological/syntactic dataset

### Key Contributors to QUL Ecosystem

- **Dr. Kais Dukes**: Original digitized Quran morphology (PhD, University of Leeds)
- **Mustafa Jibaly**: Improved morphology data
- **Tanzil.net**: Verified Quran text (3-step verification process)
- **ReciteQuran.com**: Tajweed narrations and images
- **King Fahd Glorious Qur'an Printing Complex**: Authoritative editions

### Download Access

**QUL Platform**: https://qul.tarteel.ai/resources (SQLite, JSON downloads)
**Corpus Quran**: https://corpus.quran.com/download/ (TXT/TSV, email verification)
**MASAQ Dataset**: https://data.mendeley.com/datasets/9yvrzxktmr/2 (TXT, CSV, XLSX, XML, JSON - free, no registration)
**QUL GitHub**: https://github.com/TarteelAI/quranic-universal-library (code + dev database)

**Community Support**: Discord at https://discord.gg/HAcGh8mfmj

### Research Gap Identified

**CRITICAL OPPORTUNITY**: Creating morphologically and syntactically annotated resources for non-Hafs Qiraat (Warsh, Qalun, etc.) would be a **VALUABLE CONTRIBUTION TO THE FIELD**. No ready-made multi-Qiraat morphological dataset exists. This represents a potential PhD-level research contribution.

**QUD Phase 2-3 Potential**: If QUD successfully validates layered architecture for Hafs + Warsh (Phase 1), extending QUL-style morphology to Warsh and contributing back to the community could be a major deliverable.

---

## Technical Research

### 1. JSON Schema + Pydantic Dual Approach

**Decision**: Use JSON Schema for formal specification + Pydantic for Python implementation

**Rationale**:
- **JSON Schema**: Language-agnostic, formal specification, enables documentation generation, validation tooling mature
- **Pydantic**: Python-native type hints, runtime validation, IDE autocomplete, excellent FastAPI integration (if needed later)
- **Dual Benefit**: JSON Schema documents the "what", Pydantic implements the "how" with type safety

**Best Practices**:
- Keep schemas DRY: Define reusable components (`$defs` in JSON Schema, base models in Pydantic)
- Version schemas: Include schema version in `$id` field
- Document constraints: Use `description` fields liberally in JSON Schema
- Validate early: Run schema validation on small samples before full dataset processing
- Generate Pydantic from JSON Schema OR maintain manually: Decision depends on complexity (manual for research flexibility)

**Alternatives Considered**:
- Protocol Buffers: Rejected - binary format, less human-readable, overkill for research
- Avro: Rejected - similar to Protobuf, less Python ecosystem support
- Custom DSL: Rejected - premature abstraction before patterns clear

### 2. NLP for Arabic/Quranic Text Processing

**Decision**: Use NLTK as primary NLP library with domain-specific extensions

**Rationale**:
- **NLTK**: Well-documented, educational-friendly (good for research), tokenization and text processing utilities
- **Arabic Support**: NLTK has Arabic corpus and basic tools
- **Domain Extensions Needed**: Quranic text requires custom tokenizers (Uthmanic script differs from standard Arabic)

**Best Practices for Quranic NLP**:
- **Character Normalization**: Be aware of Unicode normalization forms (NFC vs NFD) - Uthmanic script uses specific codepoints
- **Diacritic Handling**: Separate diacritics (tashkeel, tajweed marks) from base letters algorithmically
- **Word Boundaries**: Whitespace in Quranic text may be non-breaking spaces or zero-width joiners
- **Grapheme Clusters**: Arabic combines multiple codepoints (base + diacritics) into single visual units

**Alternatives Considered**:
- spaCy: Rejected - heavier framework, overkill for research, less educational transparency
- Stanza (Stanford NLP): Rejected - requires models we don't need (NER, POS tagging beyond scope)
- PyArabic: Considered - lightweight Arabic utilities, may supplement NLTK for specific tasks

**Research Tasks**:
- Experiment with NLTK Arabic tokenizer on QS-QIRAAT `aya_text` field
- Build custom tokenizer if NLTK inadequate for Uthmanic script
- Document Unicode handling decisions (NFC vs NFD) in ADR

### 3. Jupyter Notebooks for Research Documentation

**Decision**: Use Jupyter notebooks for exploratory analysis with inline documentation

**Rationale**:
- **Interactive**: Run code iteratively, inspect intermediate results
- **Documentation**: Markdown cells explain methodology inline with code
- **Visualization**: Inline plots for layer relationship diagrams, conflation matrices
- **Reproducibility**: Notebooks capture exact analysis steps

**Best Practices**:
- **Narrative Structure**: Treat notebook as lab notebook - chronological exploration with explanations
- **Modular Code**: Extract reusable functions to `.py` modules, import into notebooks (avoid 1000-line notebooks)
- **Clear Outputs**: Always show head/tail of datasets, summarize large outputs
- **Version Control**: Commit notebooks with outputs cleared (use nbstripout or manual clear) to reduce diff noise
- **Naming**: Use numbered prefixes for sequence (01-data-loading.ipynb, 02-schema-analysis.ipynb)

**Alternatives Considered**:
- Plain Python scripts: Rejected - less exploratory, harder to document inline
- Observable notebooks: Rejected - JavaScript-focused, less suitable for Python NLP work
- Google Colab: Considered for collaboration but local Jupyter preferred for data privacy

### 4. SQLite for Sample Database

**Decision**: Use SQLite for demonstrating layered architecture query capabilities

**Rationale**:
- **Embedded**: No server setup, single file database
- **SQL Support**: Enables JOIN queries across layers to demonstrate query benefits
- **Python Integration**: `sqlite3` standard library, no external dependencies
- **Portability**: Database file can be shared for demo purposes

**Schema Design for SQLite**:
- One table per layer (e.g., `layer_00_qiraat`, `layer_06_verses`, `layer_11_pages`)
- Foreign keys to represent cross-layer relationships (e.g., verse → sura)
- Indexes on common query fields (e.g., verse_id, sura_id, narration_id)
- JSON fields for complex structures (SQLite supports JSON functions since 3.9.0)

**Best Practices**:
- **Normalization**: Leverage layer separation to normalize redundant data (page numbers not repeated per verse)
- **Read-Only**: For research demo, database is read-only (no need for transaction complexity)
- **Views**: Create SQL views for common cross-layer queries

**Alternatives Considered**:
- PostgreSQL: Rejected - overkill for research, requires server
- MongoDB: Rejected - document model less suitable for demonstrating relational layer queries
- DuckDB: Considered - columnar analytics database, may be useful for performance analysis later

### 5. Visualization Libraries

**Decision**: Use matplotlib for static plots, plotly for interactive visualizations

**Rationale**:
- **Matplotlib**: Standard Python plotting, good for paper-ready static plots (conflation matrix heatmaps)
- **Plotly**: Interactive plots embeddable in Jupyter (layer dependency graphs, cross-narration diff exploration)
- **Seaborn**: Wrapper on matplotlib for statistical visualizations (may use for correlation analysis)

**Visualization Needs**:
1. **Conflation Matrix**: Heatmap showing which layers mixed in QS-QIRAAT fields
2. **Layer Dependency Graph**: Directed graph showing layer generation dependencies (Layer 0→1→3)
3. **Cross-Recitation Differences**: Comparative visualizations (Hafs vs Warsh character diffs)
4. **Schema Coverage**: Bar charts showing field coverage per layer

**Best Practices**:
- Export high-DPI figures for documentation (300 DPI)
- Use colorblind-friendly palettes
- Label axes clearly with units
- Include data sources in captions

## Research Questions Refinement

Based on prior work and technical research, we refine the research questions:

### RR-001 Clarifications

**Question**: What specific data layers are currently mixed together in the QS-QIRAAT dataset?

**Approach**:
1. Load QS-QIRAAT JSON for one narration (Hafs)
2. Inspect schema: field names, data types, sample values
3. Map each field to QUD layer taxonomy using domain knowledge
4. Create conflation matrix: NxN matrix where cell (i,j) indicates if layers i and j are mixed in same field
5. Repeat for other 6 narrations to identify narration-specific vs shared fields

**Unknowns Resolved**:
- Data format: JSON primary (clarified in spec)
- Validation approach: Automated character/verse count checks (clarified in spec)

### RR-002 Clarifications

**Question**: Can we define formal schemas for each of the 14 essential layers?

**Approach**:
1. For each layer 0-13, define JSON Schema based on:
   - QS-QIRAAT fields mapped to this layer (from RR-001)
   - Domain knowledge of what layer represents
   - Generation rules (what dependencies this layer has)
2. Create corresponding Pydantic models
3. Test schema against sample data
4. Document schema rationale in per-layer README

**Unknowns Resolved**:
- Schema format: JSON Schema + Pydantic dual approach (clarified in planning)
- Validation tolerance: Best-effort, document failures (clarified in spec)

### RR-003 Clarifications

**Question**: Can a simulation demonstrate layer separation and generation?

**Approach**:
1. Build Python prototype that:
   - Loads QS-QIRAAT JSON
   - Transforms to 14-layer format per RR-002 schemas
   - Validates using Pydantic models
   - Generates SQLite database
   - Runs sample cross-narration queries
2. Document in Jupyter notebook with inline analysis
3. Create visualization of results

**Unknowns Resolved**:
- Technology stack: Python + NLTK + Jupyter + Pydantic + SQLite (clarified in planning)
- Validation process: Automated validation during cycles, scholarly review at end (clarified in spec)

## Risks & Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| NLTK inadequate for Uthmanic script | May need custom tokenizer | Budget time for custom development, research PyArabic alternatives |
| QS-QIRAAT data quality issues | Validation failures | Document all discrepancies, escalate to scholarly review |
| Schema complexity grows beyond manageable | Hard to maintain 14+ schemas | Start simple, iterate based on RR-001 findings |
| Character count mismatches | Validation failure | Research Unicode normalization deeply, document in ADR |
| SQLite performance inadequate for full dataset | Can't demonstrate queries | Use subset of data for demo (e.g., first 3 suras), document limitation |

## Next Steps

With research context established:
1. ✅ Research complete - no more NEEDS CLARIFICATION items
2. → Proceed to Phase 1: Design data-model.md and experiment-design.md
3. → Begin RR-001 experimentation with clear methodology
