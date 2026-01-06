# Organizational Layers - Complete Taxonomy

**Date**: 2025-11-10
**Status**: VALIDATED with dataset analysis
**Source**: User interview + QS-QIRAAT Hafs v2.0 dataset

---

## Hierarchical Overview

```
Quran (Whole Text)
  ├─ Juz Layer (30 parts)
  │   ├─ Hizb Layer (60 divisions, 2 per Juz)
  │   │   └─ Rub Layer (240 quarters, 4 per Hizb)
  │   │
  │   └─ [Spans across multiple Surahs]
  │
  └─ Surah Layer (114 chapters)
      └─ Ayah Layer (6,236 verses in Hafs, 6,214 in Warsh)
          └─ Word Layer
              └─ Character Layer
                  └─ [Pre-Character Layers - TBD]
```

**KEY INSIGHT**: Juz/Hizb/Rub and Surah/Ayah are **PARALLEL organizational systems**, not nested!

---

## Layer 1: Surah (Chapter) Layer

### **Base Layer Definition**
- **Conceptual Name**: Surah Layer (Chapter Layer)
- **Traditional Arabic**: السورة (As-Surah)
- **Semantic Purpose**: The 114 chapters of the Quran, revealed units with distinct names and themes
- **Authority Source**: Divinely revealed (revelation structure)
- **Universal**: Yes - All Qiraat have same 114 Surahs

### **Expanded Layers**

#### Expanded Layer 1: Surah Number
- **Data Type**: Integer
- **Value Range**: 1-114
- **Reset Behavior**: Global (never resets)
- **Narration Variance**: No (same across all Qiraat)
- **Examples**:
  - Surah 1: Al-Fatiha (The Opening)
  - Surah 2: Al-Baqarah (The Cow)
  - Surah 114: An-Nas (Mankind)

#### Expanded Layer 2: Surah Name (Arabic)
- **Data Type**: String (Arabic)
- **Examples**: الفَاتِحة, البَقَرَة, آل عِمۡرَان
- **Narration Variance**: No (same names across Qiraat)

#### Expanded Layer 3: Surah Name (English/Transliteration)
- **Data Type**: String (Latin script)
- **Examples**: Al-Fātiḥah, Al-Baqarah, Āl-'Imrān
- **Note**: Transliteration conventions may vary

### **Mappings to Other Layers**

#### Mapping to Ayah Layer
- **Relationship Type**: 1:N (one Surah contains many Ayahs)
- **Directionality**: Contains (parent → children)
- **Expanded Mapping Layers**:
  - Surah Number (1-114, global)
  - Ayah-in-Surah Number (resets per Surah, varies by Qiraah)

**Example**:
```
Surah 2 (Al-Baqarah):
  - Hafs: Contains Ayahs 1-286
  - Warsh: Contains Ayahs 1-285 (one fewer)
```

#### Mapping to Juz Layer
- **Relationship Type**: N:M (many-to-many)
- **Directionality**: Spans across
- **Reason**: Long Surahs span multiple Juz; one Juz contains multiple Surahs
- **Examples**:
  - Surah 2 (Al-Baqarah) spans Juz 1, 2, and 3
  - Juz 1 contains Surah 1 (complete) + Surah 2 (partial, Ayahs 1-141)

### **Constraints**
- Total Surah count MUST equal 114
- Surah numbers MUST be sequential 1-114 with no gaps
- Each Ayah MUST belong to exactly one Surah
- Sum of Ayah counts across all Surahs MUST equal total verse count (6,236 for Hafs, 6,214 for Warsh)

---

## Layer 2: Juz Layer (Part/Section)

### **Base Layer Definition**
- **Conceptual Name**: Juz Layer (Part Layer)
- **Traditional Arabic**: الجُزْء (Al-Juz), plural: أَجْزَاء (Ajzā')
- **Semantic Purpose**: 30 equal parts of the Quran for recitation scheduling (one Juz per day of month)
- **Authority Source**: Scholarly convention (not divinely revealed structure)
- **Universal**: Yes - Same 30 Juz structure across all Qiraat

### **Expanded Layers**

#### Expanded Layer 1: Juz Number
- **Data Type**: Integer
- **Value Range**: 1-30
- **Reset Behavior**: Global (never resets)
- **Narration Variance**: No (same 30 Juz across Qiraat)
- **Examples**:
  - Juz 1: Surah 1:1 (Al-Fatiha) to Surah 2:141 (Al-Baqarah)
  - Juz 2: Surah 2:142 to Surah 2:252
  - Juz 30: Surah 78:1 (An-Naba) to Surah 114:6 (An-Nas)

### **Mappings to Other Layers**

#### Mapping to Surah Layer
- **Relationship Type**: N:M (many-to-many)
- **Directionality**: Cuts across
- **Examples from Dataset**:
  - Juz 1: Contains Surah 1 (complete) + part of Surah 2 (Ayahs 1-141)
  - Juz 2: Contains Surah 2 (Ayahs 142-252) only
  - Juz 3: Contains Surah 2 (Ayahs 253-286) + Surah 3 (partial)

#### Mapping to Hizb Layer
- **Relationship Type**: 1:2 (one Juz contains exactly 2 Hizb)
- **Directionality**: Contains (parent → children)
- **Expanded Mapping Layers**:
  - Juz Number (1-30, global)
  - Hizb-in-Juz Number (1-2, resets per Juz)

**Example**:
```
Juz 1:
  └─ Hizb 1 (1st half of Juz 1)
  └─ Hizb 2 (2nd half of Juz 1)

Juz 2:
  └─ Hizb 3 (1st half of Juz 2) ← Global numbering
  └─ Hizb 4 (2nd half of Juz 2)
```

### **Constraints**
- Total Juz count MUST equal 30
- Each Juz MUST contain exactly 2 Hizb
- Juz numbers MUST be sequential 1-30 with no gaps
- Every Ayah MUST belong to exactly one Juz

### **Dataset Validation**
- ✅ Confirmed: 30 unique Juz values in Hafs dataset
- ✅ Juz range: 1-30
- ✅ Verse counts per Juz vary (Juz 1: 148 verses, Juz 2: 111 verses, etc.)

---

## Layer 3: Hizb Layer (Division/Half)

### **Base Layer Definition**
- **Conceptual Name**: Hizb Layer (Division Layer)
- **Traditional Arabic**: الحِزْب (Al-Hizb), plural: أَحْزَاب (Ahzāb)
- **Semantic Purpose**: Divisions of each Juz (2 Hizb per Juz = 60 total) for finer recitation tracking
- **Authority Source**: Scholarly convention
- **Universal**: Yes - Same 60 Hizb structure across Qiraat (boundaries may vary slightly)

### **Expanded Layers**

#### Expanded Layer 1: Hizb Number (Global)
- **Data Type**: Integer
- **Value Range**: 1-60
- **Reset Behavior**: Global (never resets)
- **Calculation**: Hizb Global Number = (Juz Number - 1) × 2 + Hizb-in-Juz Number
- **Examples**:
  - Hizb 1: First half of Juz 1
  - Hizb 2: Second half of Juz 1
  - Hizb 3: First half of Juz 2
  - Hizb 60: Second half of Juz 30

#### Expanded Layer 2: Hizb-in-Juz Number (Local)
- **Data Type**: Ordinal (1st, 2nd)
- **Value Range**: 1-2
- **Reset Behavior**: Resets per Juz
- **Examples**:
  - Juz 1, Hizb 1 (1st Hizb of Juz 1)
  - Juz 1, Hizb 2 (2nd Hizb of Juz 1)
  - Juz 2, Hizb 1 (RESET - 1st Hizb of Juz 2)

### **Mappings to Other Layers**

#### Mapping to Juz Layer
- **Relationship Type**: N:1 (many Hizb belong to one Juz)
- **Directionality**: Belongs to (child → parent)
- **Cardinality**: Exactly 2 Hizb per Juz

#### Mapping to Rub Layer
- **Relationship Type**: 1:4 (one Hizb contains exactly 4 Rub)
- **Directionality**: Contains (parent → children)
- **Expanded Mapping Layers**:
  - Hizb Number (1-60, global)
  - Rub-in-Hizb Number (1-4, resets per Hizb)

### **Constraints**
- Total Hizb count MUST equal 60
- Each Hizb MUST contain exactly 4 Rub
- Each Juz MUST contain exactly 2 Hizb
- Hizb-in-Juz Number MUST be 1 or 2 only

---

## Layer 4: Rub Layer (Quarter/Eighth)

### **Base Layer Definition**
- **Conceptual Name**: Rub Layer (Quarter Layer, also called Thumn/Eighth)
- **Traditional Arabic**: رُبْع الحِزْب (Rub' al-Hizb) = Quarter of Hizb
- **Alternative Names**: Thumn (ثُمْن) = Eighth (of Juz, since 8 Rub = 1 Juz)
- **Semantic Purpose**: Smallest traditional division unit (4 Rub per Hizb = 8 per Juz = 240 total)
- **Authority Source**: Scholarly convention
- **Universal**: Yes - Same 240 Rub structure (boundaries may vary)

### **Expanded Layers**

#### Expanded Layer 1: Rub Number (Global)
- **Data Type**: Integer
- **Value Range**: 1-240
- **Reset Behavior**: Global (never resets)
- **Calculation**: Rub Global = (Hizb Global - 1) × 4 + Rub-in-Hizb Number
- **Examples**:
  - Rub 1: 1st quarter of Hizb 1
  - Rub 4: 4th quarter of Hizb 1
  - Rub 5: 1st quarter of Hizb 2
  - Rub 240: 4th quarter of Hizb 60

#### Expanded Layer 2: Rub-in-Hizb Number (Local)
- **Data Type**: Ordinal (1st, 2nd, 3rd, 4th)
- **Value Range**: 1-4
- **Reset Behavior**: Resets per Hizb
- **Examples**:
  - Hizb 1, Rub 1 (1st quarter)
  - Hizb 1, Rub 2 (2nd quarter)
  - Hizb 1, Rub 3 (3rd quarter)
  - Hizb 1, Rub 4 (4th quarter)
  - Hizb 2, Rub 1 (RESET - 1st quarter of Hizb 2)

#### Expanded Layer 3: Rub-in-Juz Number (Alternative Local)
- **Data Type**: Ordinal (1st through 8th)
- **Value Range**: 1-8
- **Reset Behavior**: Resets per Juz
- **Calculation**: Rub-in-Juz = (Hizb-in-Juz - 1) × 4 + Rub-in-Hizb
- **Note**: Alternative representation (some traditions count Rub as "eighths of Juz" rather than "quarters of Hizb")

### **Mappings to Other Layers**

#### Mapping to Hizb Layer
- **Relationship Type**: N:1 (many Rub belong to one Hizb)
- **Directionality**: Belongs to (child → parent)
- **Cardinality**: Exactly 4 Rub per Hizb

#### Mapping to Ayah Layer
- **Relationship Type**: 1:N (one Rub contains many Ayahs)
- **Directionality**: Contains
- **Boundary Definition**: Rub boundaries marked by special symbol (۞ Rub al-Hizb symbol)
- **Variance**: Rub start/end Ayahs may vary slightly across Qiraat/editions

### **Constraints**
- Total Rub count MUST equal 240
- Each Rub MUST belong to exactly one Hizb
- Each Hizb MUST contain exactly 4 Rub
- Rub-in-Hizb Number MUST be 1, 2, 3, or 4
- Rub-in-Juz Number MUST be 1 through 8

---

## Summary: The Complete Organizational Hierarchy

### **Fixed Counts (Same Across All Qiraat)**:
- **30 Juz** (parts)
- **60 Hizb** (2 per Juz)
- **240 Rub** (4 per Hizb, 8 per Juz)
- **114 Surah** (chapters)

### **Variable Counts (Differ by Qiraah)**:
- **~6,236 Ayah** (verses in Hafs)
- **~6,214 Ayah** (verses in Warsh)
- Variable word counts per Qiraah
- Variable character counts per Qiraah

### **Math Validation**:
```
30 Juz × 2 Hizb/Juz = 60 Hizb ✓
60 Hizb × 4 Rub/Hizb = 240 Rub ✓
```

### **Relationship Map**:
```
Juz (30)
  ├─ Contains → Hizb (60, exactly 2 per Juz)
  │   └─ Contains → Rub (240, exactly 4 per Hizb)
  │       └─ Contains → Ayah (variable count, boundaries marked by ۞)
  │
  └─ Spans across → Surah (114)
      └─ Contains → Ayah (6,236 in Hafs, 6,214 in Warsh)
          └─ Contains → Word (variable)
              └─ Contains → Character (variable)
```

---

## Cross-Qiraah Considerations

### **Universal Elements (Same Across Qiraat)**:
- ✅ 30 Juz structure
- ✅ 60 Hizb structure
- ✅ 240 Rub structure
- ✅ 114 Surah structure

### **Variable Elements (May Differ)**:
- ⚠️ Exact Ayah boundaries for Rub markers (minor variations)
- ⚠️ Ayah counts per Surah (e.g., Surah 2: 286 in Hafs, 285 in Warsh)
- ⚠️ Total Ayah count (6,236 Hafs vs 6,214 Warsh)

### **Modeling Implication**:
- Juz/Hizb/Rub layers: Mostly universal, store once
- Surah-Ayah mapping: Context-specific (Hafs vs Warsh versions)
- Rub-Ayah boundary mapping: May need context-specific versions

---

## Data Representation

### **Juz Entity**:
```json
{
  "juz_id": "uuid-juz-01",
  "juz_number": 1,
  "hizb_count": 2,
  "start_ayah": { "surah": 1, "ayah": 1 },
  "end_ayah": { "surah": 2, "ayah": 141 },
  "context": "universal"
}
```

### **Hizb Entity**:
```json
{
  "hizb_id": "uuid-hizb-01",
  "hizb_number_global": 1,
  "hizb_number_in_juz": 1,
  "juz_ref": "uuid-juz-01",
  "rub_count": 4,
  "context": "universal"
}
```

### **Rub Entity**:
```json
{
  "rub_id": "uuid-rub-01",
  "rub_number_global": 1,
  "rub_number_in_hizb": 1,
  "rub_number_in_juz": 1,
  "hizb_ref": "uuid-hizb-01",
  "start_ayah_ref": "uuid-ayah-...",
  "end_ayah_ref": "uuid-ayah-...",
  "context": "universal"
}
```

### **Surah Entity**:
```json
{
  "surah_id": "uuid-surah-02",
  "surah_number": 2,
  "surah_name_ar": "البَقَرَة",
  "surah_name_en": "Al-Baqarah",
  "ayah_count": 286,
  "context": "hafs",
  "juz_span": [1, 2, 3]
}
```

---

## Dataset Findings (Hafs v2.0)

### **Validated from QS-QIRAAT**:
- ✅ 30 Juz confirmed (field: `jozz`)
- ✅ 6,236 total verses (Hafs)
- ✅ Surah 2 (Al-Baqarah) spans Juz 1, 2, 3
- ✅ Juz 1: 148 verses (Surah 1:1 to Surah 2:141)
- ✅ Juz 2: 111 verses (Surah 2:142 to 2:252)
- ✅ 1,700 verses contain special markers (likely Rub markers ۞)

### **Hizb/Rub Boundaries (Estimated)**:
- Hizb markers likely indicated by special Unicode symbols in `aya_text`
- Need to parse exact boundaries from symbol positions
- Estimated Juz 1 Hizb boundary: around Surah 2:68 (midpoint)

---

## Next Steps

1. **Parse exact Hizb/Rub boundaries** from dataset (find ۞ symbols)
2. **Compare Hafs vs Warsh** Hizb/Rub boundaries (check for variations)
3. **Define Ayah layer** with Surah-Ayah relationships
4. **Map Rub-Ayah boundaries** (which Ayah starts/ends each Rub)
5. **Create cross-reference table** (Juz → Hizb → Rub → Ayah mappings)

---

**Status**: Organizational layers taxonomy complete ✓
**Next**: Define textual/content layers (Ayah, Word, Character, pre-Character)
