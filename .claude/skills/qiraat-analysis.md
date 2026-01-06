# Qiraat Comparative Analysis Skill

You are an expert in the 10 canonical Qiraat (القراءات العشر) and their narrations, with deep knowledge of textual variants, verse boundary differences, and scholarly traditions.

## Qiraat Taxonomy (Critical Knowledge)

### 10 Canonical Qiraat with 20 Primary Narrations

| # | Qiraah (Imam) | Death (AH) | City | Narration 1 | Narration 2 |
|---|---------------|------------|------|-------------|-------------|
| 1 | **Nafi'** (نافع) | 169 | Medina | **Warsh** (ورش) | **Qalun** (قالون) |
| 2 | **Ibn Kathir** (ابن كثير) | 120 | Mecca | Al-Bazzi (البزي) | Qunbul (قنبل) |
| 3 | **Abu Amr** (أبو عمرو) | 154 | Basra | **Al-Duri** (الدوري) | **Al-Susi** (السوسي) |
| 4 | **Ibn Amir** (ابن عامر) | 118 | Damascus | Hisham (هشام) | Ibn Dhakwan (ابن ذكوان) |
| 5 | **Asim** (عاصم) | 127 | Kufa | **Hafs** (حفص) | **Shu'bah** (شعبة) |
| 6 | **Hamzah** (حمزة) | 156 | Kufa | Khalaf (خلف) | Khallad (خلاد) |
| 7 | **Al-Kisa'i** (الكسائي) | 189 | Kufa | Al-Duri (الدوري) | Abul-Harith (أبو الحارث) |
| 8 | **Abu Ja'far** (أبو جعفر) | 130 | Medina | Ibn Wardan (ابن وردان) | Ibn Jammaz (ابن جماز) |
| 9 | **Ya'qub** (يعقوب) | 205 | Basra | Ruways (رويس) | Rawh (روح) |
| 10 | **Khalaf** (خلف) | 229 | Baghdad | Ishaq (إسحاق) | Idris (إدريس) |

**Bold narrations**: Available in QS-QIRAAT dataset

## Qiraah-Narration Hierarchy (CRITICAL)

```
Imam (القارئ) → Establishes Qiraah with pronunciation/application rules
    ↓
Student (الراوي) → Transmits Qiraah with minor variations → Creates Narration (رواية)
    ↓
Result: Narrations within same Qiraah share >95% commonality
```

**Example**:
- **Nafi'** (Imam) established **Nafi's Qiraah**
  - **Warsh** (student) narrated it → **Warsh 'an Nafi'** (ورش عن نافع)
  - **Qalun** (student) narrated it → **Qalun 'an Nafi'** (قالون عن نافع)
- Result: Warsh and Qalun differ slightly but share Nafi's core pronunciation rules

## Known Verse Count Variations

| Narration | Qiraah | Verse Count | Notes |
|-----------|--------|-------------|-------|
| **Hafs** | Asim | **6,236** | Most widely used (>90% of Muslims) |
| **Shu'bah** | Asim | 6,236 | Same as Hafs (same Qiraah) |
| **Warsh** | Nafi' | **6,214** | 22 fewer verses than Hafs |
| **Qalun** | Nafi' | 6,214 | Same as Warsh (same Qiraah) |
| **Al-Susi** | Abu Amr | 6,204 | Fewest verses |
| **Al-Duri** | Abu Amr or Al-Kisa'i | Varies | Depends on Qiraah |

**CRITICAL INSIGHT**: Verse count differences are NOT errors—they reflect different verse boundary decisions in the transmission chain. The SAME content is divided differently.

## Verse Boundary Variation Examples

### Example: Surah Al-Baqarah

**Hafs**: Verse 285 = "آمَنَ الرَّسُولُ بِمَا أُنزِلَ إِلَيْهِ مِن رَّبِّهِ وَالْمُؤْمِنُونَ..."
**Warsh**: Verse 285 splits differently, creating different numbering downstream

**Impact**: By end of Quran, Warsh has 6,214 verses vs Hafs 6,236 (22 verse difference)

## Types of Qiraah Differences

### 1. Pronunciation Differences (أداء)
- Different vowels (فتحة، ضمة، كسرة)
- Hamza treatment variations
- Madd (elongation) duration differences
- **Example**: "مَالِكِ" (Hafs) vs "مَلِكِ" (Warsh) in Al-Fatiha

### 2. Word Choice Differences (اختلافات لفظية)
- Different but synonymous words
- **Example**: "تَعْلَمُونَ" vs "يَعْلَمُونَ" (different pronouns)

### 3. Verse Boundary Differences (حدود الآيات)
- Same content, different verse divisions
- Results in different verse counts
- **Example**: Hafs 6,236 vs Warsh 6,214

### 4. Orthographic Differences (رسم)
- Uthmani script variations between Qiraat
- **Example**: "الصلوة" (Uthmani) may differ slightly across Qiraat

## Comparative Analysis Workflow

### Step 1: Identify Variant Points

Use ErQuran (erquran.org) to identify where narrations differ:
- 3,744+ documented variants across 10 canonical Qiraat
- Word/phrase level variant tracking
- Metadata: variant type, sources, transmitters

### Step 2: Classify Variant Type

```python
class VariantType(Enum):
    PRONUNCIATION = "pronunciation"  # Vowel/hamza differences
    WORD_CHOICE = "word_choice"       # Different words
    VERSE_BOUNDARY = "verse_boundary" # Different verse splits
    ORTHOGRAPHY = "orthography"       # Script differences
```

### Step 3: Map Cross-Qiraah Equivalents

Use UUID-based EntityMapping:

```python
class CrossQiraahMapping(BaseModel):
    """Map equivalent entities across Qiraat."""
    canonical_id: UUID  # Canonical verse/word identity
    hafs_entity_id: UUID
    warsh_entity_id: UUID | None
    qalun_entity_id: UUID | None
    variant_type: VariantType
    description: str  # Describe the difference
```

**Example: Verse Mapping**

```python
# Hafs verse 2:285 maps to Warsh verses 2:285 + 2:286 (split differently)
mapping = CrossQiraahMapping(
    canonical_id=uuid4(),  # Canonical identity for "this content"
    hafs_entity_id="hafs-verse-2-285-uuid",
    warsh_entity_id="warsh-verse-2-285-uuid",  # First part
    variant_type=VariantType.VERSE_BOUNDARY,
    description="Hafs verse 2:285 splits into 2 verses in Warsh"
)
```

## Phase 1 Focus: Hafs vs Warsh

**Strategic Choice**: Hafs and Warsh are from **2 DIFFERENT Qiraat**:
- **Hafs** from **Asim's Qiraah** (Kufa tradition)
- **Warsh** from **Nafi's Qiraah** (Medina tradition)

**Why This Matters**:
- Tests cross-Qiraah compatibility (not just intra-Qiraah)
- Validates schemas work across different scholarly traditions
- Demonstrates verse boundary variation handling (6,236 vs 6,214)

**Alternative (Rejected)**: Hafs + Shu'bah would be 2 narrations from SAME Qiraah (Asim), limiting validation scope

## Available Resources by Qiraah

### Hafs (حفص عن عاصم)
- ✅ QS-QIRAAT: Full text + metadata
- ✅ QUL: Morphology (77,429 words), syntax (11,000 words), tajweed, audio
- ✅ MASAQ: 131,000+ morphological + 123,000+ syntactic entries
- ✅ Corpus.quran.com: Morphology + syntax treebank
- **Status**: Most comprehensive resources available

### Warsh (ورش عن نافع)
- ✅ QS-QIRAAT: Full text + metadata
- ❌ QUL: NO morphology/syntax (Hafs only)
- ❌ MASAQ: NO (Hafs only)
- ⚠️ ErQuran: Variant identification (where Warsh differs from Hafs)
- **Status**: Text available, morphology/syntax require manual annotation

### Other Narrations (Qalun, Shu'bah, Al-Duri, Al-Susi)
- ✅ QS-QIRAAT: Text + metadata (4 additional narrations)
- ❌ QUL: NO morphology/syntax
- ⚠️ ErQuran: Variant documentation
- **Status**: Available for Phase 2-3 research, limited to text only

## Cross-Qiraah Query Patterns

### Query 1: Find Variant Words Between Hafs and Warsh

```sql
SELECT 
    h.word_text AS hafs_word,
    w.word_text AS warsh_word,
    h.surah_number,
    h.verse_number
FROM hafs_words h
JOIN canonical_word_mapping m ON h.word_id = m.hafs_word_id
JOIN warsh_words w ON m.warsh_word_id = w.word_id
WHERE h.word_text != w.word_text;
```

### Query 2: Find Verse Boundary Differences

```sql
SELECT 
    hafs_verse_count,
    warsh_verse_count,
    hafs_verse_count - warsh_verse_count AS difference
FROM (
    SELECT COUNT(*) AS hafs_verse_count FROM hafs_verses
), (
    SELECT COUNT(*) AS warsh_verse_count FROM warsh_verses
);
-- Expected: hafs_verse_count=6236, warsh_verse_count=6214, difference=22
```

### Query 3: Character-Level Diff

```python
def diff_hafs_warsh_verse(hafs_text, warsh_text):
    """Character-level diff between Hafs and Warsh for same canonical verse."""
    import difflib
    
    diff = difflib.unified_diff(
        hafs_text.split(),
        warsh_text.split(),
        lineterm=''
    )
    
    return list(diff)
```

## Scholarly Terminology (Use Correctly)

✅ **CORRECT**:
- "Qiraat" (القراءات) - plural, authenticated reading traditions
- "Qiraah" (قراءة) - singular, one reading tradition
- "Narration" (رواية، Riwayah) - transmission by student
- "Hafs and Warsh are from different Qiraat" (Asim vs Nafi')
- "The 10 canonical Qiraat with 20 narrations"

❌ **INCORRECT**:
- "Recitations" (imprecise, lacks theological grounding)
- "Readings" (too generic)
- "Variants" (implies error; Qiraat are equally valid)
- "Hafs and Warsh ARE Qiraat" (they are narrations, not Qiraat themselves)

## When to Use This Skill

Invoke this skill when:
- Analyzing Qiraah-specific verse boundary differences (RR-012)
- Mapping Hafs ↔ Warsh equivalents
- Designing Context schema with qiraah_narration parameter (RR-014)
- Validating cross-Qiraah queries (RR-009, RR-016)
- Explaining why Hafs has 6,236 verses but Warsh has 6,214
- Determining which resources are available per Qiraah
- Planning Phase 2-3 expansion to additional narrations

## Current Task Context

You are working on QUD Phase 1 with Hafs (6,236 verses, 323,015 chars) and Warsh (6,214 verses) from 2 different Qiraat (Asim and Nafi'). Your schemas must accommodate verse boundary variations and support eventual expansion to all 10 Qiraat (20 narrations).
