# Qiraat Verse Count & Word Count Analysis

Analysis of verse and word count variations across six Quranic riwayat (transmission traditions).

## Data Source

- **Dataset:** QS-QIRAAT (Uthmanic script datasets)
- **Generated from:** `data/mushafs-metadata.json`
- **Analysis date:** 2026-01-21

### Riwayat Analyzed

| Riwaya | Qari (Reader) | Version |
|--------|---------------|---------|
| Hafs | Asim | v2.0 |
| Shuba | Asim | v2.0 |
| Qaloun | Nafi | v2.1 |
| Warsh | Nafi | v2.1 |
| Douri | Abu Amr | v2.0 |
| Sousi | Abu Amr | v2.0 |

---

## 1. Surah-Level Verse Count Analysis

### Summary

| Metric | Count | Percentage |
|--------|-------|------------|
| Full agreement (all 6 riwayat same) | 62 surahs | 54.4% |
| Disagreement (at least 2 differ) | 52 surahs | 45.6% |

### Coalition Patterns

The riwayat cluster into three main groups based on verse numbering:

```
┌─────────────────────────────────────────────────────────┐
│  Kufan School       │  Medinan School     │  Basran    │
│  (Asim)             │  (Nafi)             │  (Abu Amr) │
│  hafs + shuba       │  qaloun + warsh     │  douri     │
│                     │                     │  sousi     │
└─────────────────────────────────────────────────────────┘
```

| Pattern | Frequency |
|---------|-----------|
| **Hafs+Shuba** vs Douri+Qaloun+Sousi+Warsh | 40 surahs |
| **Qaloun+Warsh** vs Douri+Hafs+Shuba+Sousi | 9 surahs |
| **Douri+Sousi** vs Hafs+Qaloun+Shuba+Warsh | 2 surahs |
| 3-way split | 1 surah (Hud) |

### Pairwise Agreement Matrix

Number of surahs (out of 114) where two riwayat agree on verse count:

|          | douri | hafs | qaloun | shuba | sousi | warsh |
|----------|:-----:|:----:|:------:|:-----:|:-----:|:-----:|
| **douri**| 114 | 71 | 102 | 71 | **114** | 102 |
| **hafs** | 71 | 114 | 64 | **114** | 71 | 64 |
| **qaloun**| 102 | 64 | 114 | 64 | 102 | **114** |
| **shuba**| 71 | **114** | 64 | 114 | 71 | 64 |
| **sousi**| **114** | 71 | 102 | 71 | 114 | 102 |
| **warsh**| 102 | 64 | **114** | 64 | 102 | 114 |

### Perfect Pairs

These pairs **always agree** on verse count (same Qari's two transmitters):

- **Douri = Sousi** (both from Abu Amr)
- **Hafs = Shuba** (both from Asim)
- **Qaloun = Warsh** (both from Nafi)

### Total Verses Per Riwaya

| Riwaya | Total Verses |
|--------|-------------|
| Hafs | 6,236 |
| Shuba | 6,236 |
| Douri | 6,217 |
| Sousi | 6,217 |
| Qaloun | 6,214 |
| Warsh | 6,214 |

---

## 2. Verse-Level Word Count Analysis

### Summary

| Metric | Count |
|--------|-------|
| Total verse entries | 6,263 |
| Verses existing in ALL riwayat | 6,187 |
| Verses missing in at least one riwaya | 76 |

Among 6,187 common verses:

| Agreement | Verses | Percentage |
|-----------|--------|------------|
| All 6 agree on word count | 3,196 | 51.7% |
| At least 2 differ | 2,991 | 48.3% |

### Pairwise Agreement Matrix

Percentage of common verses where two riwayat have identical word count:

|          | douri | hafs | qaloun | shuba | sousi | warsh |
|----------|:-----:|:----:|:------:|:-----:|:-----:|:-----:|
| **douri**| 100% | 55.5% | 91.2% | 55.5% | **100%** | 91.3% |
| **hafs** | 55.5% | 100% | 54.6% | **100%** | 55.5% | 54.6% |
| **qaloun**| 91.2% | 54.6% | 100% | 54.6% | 91.2% | **96%** |
| **shuba**| 55.5% | **100%** | 54.6% | 100% | 55.5% | 54.6% |
| **sousi**| **100%** | 55.5% | 91.2% | 55.5% | 100% | 91.3% |
| **warsh**| 91.3% | 54.6% | **96%** | 54.6% | 91.3% | 100% |

### Coalition Patterns (Word Differences)

| Pattern | Verses |
|---------|--------|
| **Hafs+Shuba** vs Douri+Qaloun+Sousi+Warsh | 2,331 |
| **Qaloun+Warsh** vs Douri+Hafs+Shuba+Sousi | 159 |
| 3-way: Douri+Sousi vs Hafs+Shuba vs Qaloun+Warsh | 130 |
| **Douri+Sousi** vs Hafs+Qaloun+Shuba+Warsh | 124 |
| Qaloun vs Hafs+Shuba vs Douri+Sousi+Warsh | 62 |

### Difference Magnitude Distribution

| Word Difference | Verses |
|-----------------|--------|
| ±1 word | 702 |
| ±2 words | 354 |
| ±3 words | 274 |
| ±4 words | 228 |
| ±5-10 words | 666 |
| ±11-20 words | 505 |
| ±21-50 words | 198 |
| ±51+ words | 64 |

### Largest Word Count Differences

| Verse | Difference | Explanation |
|-------|------------|-------------|
| 2:281 | ±114 words | Verse boundary shift |
| 2:282 | ±96 words | Verse boundary shift |
| 73:18 | ±73 words | Qaloun+Warsh differ |
| 2:102 | ±62 words | Hafs+Shuba differ |
| 2:195 | ±60 words | Verse boundary shift |

### Total Words Per Riwaya

| Riwaya | Total Words |
|--------|-------------|
| Warsh | 77,860 |
| Douri | 77,858 |
| Sousi | 77,858 |
| Qaloun | 77,853 |
| Hafs | 77,630 |
| Shuba | 77,630 |

**Range:** 230 words (0.30% difference)

---

## 3. Key Findings

1. **Three transmission schools** emerge clearly from the data:
   - Kufan (Hafs+Shuba from Asim)
   - Medinan (Qaloun+Warsh from Nafi)
   - Basran (Douri+Sousi from Abu Amr)

2. **Transmitters of the same Qari always agree** on verse count (100% agreement within pairs)

3. **Large per-verse word differences** (up to ±114 words) are due to **verse boundary placement**, not actual textual differences

4. **Total content is nearly identical**: All six riwayat contain approximately 77,700-77,900 words (within 0.3%)

5. **Hafs+Shuba vs others** is the dominant pattern of disagreement, appearing in:
   - 40 surahs (verse count)
   - 2,331 verses (word count)
