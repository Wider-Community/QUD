# Quran Page-Level Schema (`quran-page.schema.json`)

This schema defines the **page-level structure of a Mushaf (Quran copy)** for digital storage, exchange, and validation. It allows representing the mapping of Quranic pages to ayahs, lines, words, and classical divisions like **juz**, **hizb**, and **rub**.  

It is designed to support structured data processing, pagination, indexing, and reference in Quranic applications.

---

## Schema Overview

- **Schema Version:** Draft 2020-12
- **$id:** `https://example.org/schemas/quran-page.schema.json`
- **Title:** Quran Page-Level Schema
- **Description:** Defines the structure of a Mushaf page, including metadata and page content references.
- **Top-Level Type:** `object`  
- **Required Top-Level Fields:** `metadata`, `pages`  
- **Additional Properties:** Not allowed (strict schema)

---

## Top-Level Properties

### 1. `metadata` (object)

Contains information about the edition, physical Mushaf layout, and versioning.

| Field | Type | Required | Description | Why Used |
|-------|------|----------|-------------|----------|
| `edition` | string | ✅ | Quran textual edition identifier (e.g., `hafs-uthmani`). | Identifies which textual version the page data belongs to. |
| `mushaf` | string | ✅ | Physical layout identifier (e.g., `Madani-15-line`). | Tracks the printed Mushaf layout; affects page breaks and line counts. |
| `version` | string | ✅ | Semantic version of the dataset/schema (e.g., `1.0.0`). | Tracks dataset updates and ensures application compatibility. |

**Constraints:**  
- Strings must be 1–100 characters (edition/mushaf) or 1–32 (version).  
- Allowed characters for edition/mushaf: alphanumeric, underscore `_`, hyphen `-`.  
- Version follows `MAJOR.MINOR.PATCH` semver pattern.

---

### 2. `pages` (array)

An ordered array of **page objects** representing each page in the Mushaf.

- **Type:** `array` of `page` objects  
- **Minimum Items:** 1  
- **Order:** Consumers should preserve order by `pageNumber`.  

Each `page` object provides detailed structural information about that page.

---

## Page Object (`$defs/page`)

### Required Fields

| Field | Type | Description | Why Used |
|-------|------|-------------|----------|
| `pageNumber` | integer (1–604) | Mushaf page number | Primary identifier of the page, ensures order and pagination. |
| `juz` | integer (1–30) or `{start,end}` | The Juz the page belongs to | Captures Quranic divisions. Ranges handle pages spanning multiple Juz. |
| `hizb` | integer (1–60) or `{start,end}` | The Hizb the page belongs to | Helps with recitation tracking and indexing. |
| `rub` | integer (1–240) or `{start,end}` | The Rub the page belongs to | Tracks finer divisions within a Hizb for precise references. |
| `ayahStart` | object `{surah, ayah}` | First ayah on the page | Enables bookmarking, search, and cross-layer linking. |
| `ayahEnd` | object `{surah, ayah}` | Last ayah on the page | Marks the end of the page content; supports navigation and verse ranges. |
| `ayahCount` | integer | Total ayahs on the page | Quick reference for content statistics and validation. |
| `lineCount` | integer (default 15) | Number of text lines on the page | Useful for rendering, layout calculations, and validation. |
| `wordCount` | integer | Total words on the page | Optional metric for text analysis or layout purposes. |

---

### Nested Definitions

#### 1. `intRange` (object)

Represents a **range of integers** for divisions like Juz, Hizb, or Rub:

```json
{ "start": 5, "end": 6 }