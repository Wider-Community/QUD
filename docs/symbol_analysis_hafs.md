# Uthmanic Hafs Symbol Categorization

Functional categorization of all unique symbols in the Uthmanic Hafs v2.0 aya text.

**Source:** `data/QS - QIRAAT/Uthmanic Hafs v2.0/UthmanicHafs_v2-0 data/hafsData_v2-0.json`

---

## Summary

| Category | Symbol Count | Total Occurrences |
|----------|--------------|-------------------|
| Letters | 36 | 325,387 |
| Diacritics | 9 | 272,025 |
| Extensions | 7 | 18,620 |
| Stop Symbols (Waqf) | 5 | 4,272 |
| Tajweed Symbols | 11 | 6,874 |
| Other Symbols | 4 | 7,183 |
| Aya End Markers | 286 | 6,236 |

---

## 1. Letters

Base Arabic letters used in Quranic text.

| Symbol | Unicode | Name | Count |
|--------|---------|------|-------|
| ء | `U+0621` | ARABIC LETTER HAMZA | 2,783 |
| أ | `U+0623` | ARABIC LETTER ALEF WITH HAMZA ABOVE | 9,177 |
| ؤ | `U+0624` | ARABIC LETTER WAW WITH HAMZA ABOVE | 705 |
| إ | `U+0625` | ARABIC LETTER ALEF WITH HAMZA BELOW | 5,088 |
| ئ | `U+0626` | ARABIC LETTER YEH WITH HAMZA ABOVE | 908 |
| ا | `U+0627` | ARABIC LETTER ALEF | 24,907 |
| ب | `U+0628` | ARABIC LETTER BEH | 11,491 |
| ة | `U+0629` | ARABIC LETTER TEH MARBUTA | 2,344 |
| ت | `U+062A` | ARABIC LETTER TEH | 10,520 |
| ث | `U+062B` | ARABIC LETTER THEH | 1,414 |
| ج | `U+062C` | ARABIC LETTER JEEM | 3,317 |
| ح | `U+062D` | ARABIC LETTER HAH | 4,140 |
| خ | `U+062E` | ARABIC LETTER KHAH | 2,497 |
| د | `U+062F` | ARABIC LETTER DAL | 5,991 |
| ذ | `U+0630` | ARABIC LETTER THAL | 4,932 |
| ر | `U+0631` | ARABIC LETTER REH | 12,403 |
| ز | `U+0632` | ARABIC LETTER ZAIN | 1,599 |
| س | `U+0633` | ARABIC LETTER SEEN | 6,010 |
| ش | `U+0634` | ARABIC LETTER SHEEN | 2,124 |
| ص | `U+0635` | ARABIC LETTER SAD | 2,074 |
| ض | `U+0636` | ARABIC LETTER DAD | 1,686 |
| ط | `U+0637` | ARABIC LETTER TAH | 1,273 |
| ظ | `U+0638` | ARABIC LETTER ZAH | 853 |
| ع | `U+0639` | ARABIC LETTER AIN | 9,405 |
| غ | `U+063A` | ARABIC LETTER GHAIN | 1,221 |
| ف | `U+0641` | ARABIC LETTER FEH | 8,747 |
| ق | `U+0642` | ARABIC LETTER QAF | 7,034 |
| ك | `U+0643` | ARABIC LETTER KAF | 10,497 |
| ل | `U+0644` | ARABIC LETTER LAM | 38,102 |
| م | `U+0645` | ARABIC LETTER MEEM | 26,735 |
| ن | `U+0646` | ARABIC LETTER NOON | 27,268 |
| ه | `U+0647` | ARABIC LETTER HEH | 14,850 |
| و | `U+0648` | ARABIC LETTER WAW | 24,971 |
| ى | `U+0649` | ARABIC LETTER ALEF MAKSURA | 2,913 |
| ي | `U+064A` | ARABIC LETTER YEH | 21,925 |
| ٱ | `U+0671` | ARABIC LETTER ALEF WASLA | 13,483 |

**Total:** 36 letters

---

## 2. Diacritics

### Haraka (Short Vowels)

| Symbol | Unicode | Name | Count | Examples |
|--------|---------|------|-------|----------|
| َ | `U+064E` | Fatha (a) | 122,777 | 1:1, 1:2 |
| ُ | `U+064F` | Damma (u) | 37,454 | 1:2, 1:5 |
| ِ | `U+0650` | Kasra (i) | 46,069 | 1:1, 1:2 |

### Tanween (Nunation)

| Symbol | Unicode | Name | Count | Examples |
|--------|---------|------|-------|----------|
| ً | `U+064B` | Fathatan (an) | 734 | 2:35, 2:59 |
| ٌ | `U+064C` | Dammatan (un) | 578 | 2:6, 2:7 |
| ٍ | `U+064D` | Kasratan (in) | 599 | 2:29, 2:36 |

### Sukun (Vowelless Markers)

| Symbol | Unicode | Name | Count | Examples |
|--------|---------|------|-------|----------|
| ْ | `U+0652` | Sukun (standard) | 3,988 | 2:5, 2:6 |
| ۡ | `U+06E1` | Small High Dotless Head of Khah (Uthmanic sukun) | 37,148 | 1:1, 1:2 |

### Shadda (Gemination)

| Symbol | Unicode | Name | Count | Examples |
|--------|---------|------|-------|----------|
| ّ | `U+0651` | Shadda | 22,678 | 1:1, 1:2 |

---

## 3. Extensions

*Marks indicating implied/silent letters or vowel prolongation.*

| Symbol | Unicode | Name | Function | Count | Examples |
|--------|---------|------|----------|-------|----------|
| ٰ | `U+0670` | Superscript Alef | Dagger Alef / Alef Khanjariyyah - represents long /aː/ | 9,726 | 1:1, 1:2 |
| ۥ | `U+06E5` | Small Waw | Indicates silent/implied waw | 1,256 | 2:17, 2:37 |
| ۦ | `U+06E6` | Small Yeh | Indicates silent/implied yeh | 957 | 2:22, 2:23 |
| ۧ | `U+06E7` | Small High Yeh | Indicates shortened yeh | 38 | 2:61, 2:124 |
| ٖ | `U+0656` | Subscript Alef | Short /i/ vowel in specific orthography | 1,935 | 2:17, 2:19 |
| ٗ | `U+0657` | Inverted Damma | Special prolongation marker | 2,901 | 2:2, 2:5 |
| ٞ | `U+065E` | Fatha with Two Dots | Tanween continuation variant | 1,807 | 2:7, 2:10 |

---

## 4. Stop Symbols (Waqf)

*Marks indicating where/how to pause during recitation.*

| Symbol | Unicode | Name | Meaning | Count | Examples |
|--------|---------|------|---------|-------|----------|
| ۖ | `U+06D6` | Small High Sad-Lam-Ya | صلى - Stop is preferred (الوقف أولى) | 1,651 | 2:5, 2:7 |
| ۗ | `U+06D7` | Small High Qaf-Lam-Ya | قلى - Continue is preferred (الوصل أولى) | 511 | 2:13, 2:61 |
| ۘ | `U+06D8` | Small High Meem Initial | م - Mandatory stop (وقف لازم) | 21 | 2:26, 2:118 |
| ۚ | `U+06DA` | Small High Jeem | ج - Permissible stop (جائز) | 2,083 | 2:19, 2:20 |
| ۛ | `U+06DB` | Small High Three Dots | Interchangeable stops (مُعَانَقَة) | 6 | 2:2, 5:26 |

---

## 5. Tajweed Symbols

*Marks for specific recitation rules.*

### Prolongation (Madd)

| Symbol | Unicode | Name | Rule | Count | Examples |
|--------|---------|------|------|-------|----------|
| ٓ | `U+0653` | Maddah Above | Indicates madd (prolongation) | 5,652 | 1:7, 2:1 |
| ۤ | `U+06E4` | Small High Madda | Extended prolongation | 26 | 7:206, 13:15 |

### Nasalization (Ghunnah) & Assimilation

| Symbol | Unicode | Name | Rule | Count | Examples |
|--------|---------|------|------|-------|----------|
| ۢ | `U+06E2` | Small High Meem Isolated | Ghunnah/nasalization | 510 | 2:10, 2:18 |
| ۭ | `U+06ED` | Small Low Meem | Iqlab (nun → meem before ba) | 99 | 2:41, 2:99 |
| ۨ | `U+06E8` | Small High Noon | Special noon pronunciation | 1 | 21:88 |

### Special Pronunciation

| Symbol | Unicode | Name | Rule | Count | Examples |
|--------|---------|------|------|-------|----------|
| ۜ | `U+06DC` | Small High Seen | Saktah (brief pause without breath) | 8 | 2:245, 7:69 |
| ۠ | `U+06E0` | Small High Rectangular Zero | Letter written but not pronounced | 66 | 2:258, 3:81 |
| ۪ | `U+06EA` | Empty Centre Low Stop | Imalah (vowel inclination) | 1 | 11:41 |
| ۬ | `U+06EC` | Rounded High Stop | Special pronunciation rule | 2 | 12:11, 41:44 |

### Combining Hamza

| Symbol | Unicode | Name | Use | Count | Examples |
|--------|---------|------|-----|-------|----------|
| ٔ | `U+0654` | Hamza Above | On non-standard carriers (tatweel, etc.) | 495 | 2:31, 2:33 |
| ٕ | `U+0655` | Hamza Below | On yeh (no precomposed form exists) | 14 | 10:15, 16:90 |

---

## 6. Other Symbols

*Structural and ornamental marks.*

| Symbol | Unicode | Name | Function | Count | Examples |
|--------|---------|------|----------|-------|----------|
| ۞ | `U+06DE` | Rub El Hizb | Marks 1/4 of a Hizb (60 total in Quran) | 199 | 2:26, 2:44 |
| ۩ | `U+06E9` | Place of Sajdah | Prostration marker (14 in Quran) | 15 | 7:206, 13:15 |
| ـ | `U+0640` | Tatweel (Kashida) | Elongation for typography/hamza carrier | 535 | 2:31, 2:33 |
| (space) | `U+00A0` | Non-breaking Space | Word separation | 6,434 | - |

---

## 7. Aya End Markers

*Arabic Presentation Forms ligatures (U+FC00–U+FD1D) repurposed as verse-end number glyphs.*

- **Unique glyphs:** 286
- **Total occurrences:** 6,236

These appear at the end of each aya to mark verse boundaries. In this font system, ligature characters serve as stylized aya numerals rather than their original ligature purpose.

**Examples:**
- `ﰀ` (U+FC00) — Aya 1
- `ﰁ` (U+FC01) — Aya 2
- `ﰆ` (U+FC06) — Aya 7
