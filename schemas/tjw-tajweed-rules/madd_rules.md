# Madd (Hafs Riwayah)

Analysis of madd (vowel prolongation) rules in Uthmanic Hafs v2.0 dataset.

Source:
data/QS - QIRAAT/Uthmanic Hafs v2.0/hafsData_v2-0.json

# Scope

This document covers madd categories in Hafs ‘an ‘Asim:
| # | Rule               | Arabic            | Description                              |
| - | ------------------ | ----------------- | ---------------------------------------- |
| 1 | Madd Tabee‘i       | مد طبيعي          | No hamzah or sukoon after madd letter    |
| 2 | Madd Badal         | مد بدل            | Hamzah precedes madd letter in same word |
| 3 | Madd Muttasil      | مد متصل           | Hamzah follows madd letter in same word  |
| 4 | Madd Munfasil      | مد منفصل          | Hamzah begins next word                  |
| 5 | Madd Lazim         | مد لازم           | Permanent sukoon after madd letter       |
| 6 | Madd ‘Arid         | مد عارض للسكون    | Sukoon due to stop                       |
| 7 | Madd Leen          | مد لين            | Waw/yaa saakin preceded by fatḥa at stop |
| 8 | Madd in Muqatta‘at | مد الحروف المقطعة | Prolongation in disjoint letters         |


# Madd Tabee‘i (مد طبيعي)

Length: 2 harakat

Occurs when a madd letter is not followed by hamzah or sukoon.

| Word    | Ref   |
| ------- | ----- |
| قَالَ   | 2:30  |
| يَقُولُ | 2:8   |
| فِي     | 1:7   |
| نُوحِي  | 7:101 |
# Madd Badal (مد بدل)

Length in Hafs: 2 harakat (fixed)

| Word      | Ref   |
| --------- | ----- |
| آمَنُوا   | 2:9   |
| إِيمَانًا | 2:143 |
| أُوتُوا   | 2:101 |
| ءَامَنَ   | 3:84  |

Note: No extension beyond 2 in Hafs.

# Madd Muttasil (مد متصل)

Length in Hafs: 4–5 harakat

| Word       | Ref  |
| ---------- | ---- |
| جَاءَ      | 2:87 |
| السَّمَاءِ | 2:22 |
| سُوءَ      | 2:49 |
| أُولَٰئِكَ | 2:5  |

Obligatory extension.

# Madd Munfasil (مد منفصل)

Length in Hafs: 4–5 harakat

| Phrase               | Ref   |
| -------------------- | ----- |
| فِي أَنفُسِكُمْ      | 2:235 |
| بِمَا أُنزِلَ        | 2:4   |
| إِنَّا أَعْطَيْنَاكَ | 108:1 |
| قَالُوا آمَنَّا      | 2:136 |

No qasr (2) in standard Hafs performance.

# Madd Lazim (مد لازم)

Length: 6 harakat (mandatory)

Occurs when madd letter is followed by permanent sukoon.

## A) Kalimi Muthaqqal (كلمي مثقل)

Madd letter + shaddah

| Word         | Ref   |
| ------------ | ----- |
| الضَّالِّينَ | 1:7   |
| آلآنَ        | 10:51 |
| الحَاقَّةُ   | 69:1  |
## B) Kalimi Mukhaffaf (كلمي مخفف)

Madd letter + permanent sukoon (no shaddah)

| Word  | Ref   |
| ----- | ----- |
| آلآنَ | 10:51 |

Very rare (only two occurrences in Surah Yunus).

## C) Harfi (in Muqatta‘at)

See section below.

# Madd ‘Arid lil-Sukoon (مد عارض للسكون)

Length: 2 / 4 / 6

Occurs only at stop.

| Word (when stopping) | Ref |
| -------------------- | --- |
| الْعَالَمِينَ        | 1:2 |
| الرَّحِيمِ           | 1:3 |
| نَسْتَعِينُ          | 1:5 |

Temporary sukoon caused by waqf.

# Madd Leen (مد لين)

Pattern:

وْ or يْ

preceded by fatḥa

stop required

Length at stop: 2 / 4 / 6

| Word    | Ref   |
| ------- | ----- |
| خَوْف   | 2:38  |
| بَيْت   | 2:125 |
| قُرَيْش | 106:1 |

No madd in wasl.

# Madd in Muqatta‘at (الحروف المقطعة)

Appears in 29 surahs.

Each letter is pronounced independently.

## Letters with 6 Harakat (Lazim Harfi)

These contain internal madd + permanent sukoon.

| Letter | Example Surah |
| ------ | ------------- |
| ل      | الم (2:1)     |
| م      | الم (2:1)     |
| س      | يس (36:1)     |
| ك      | كهيعص (19:1)  |
| ع      | كهيعص (19:1)  |
| ص      | ص (38:1)      |
| ن      | ن (68:1)      |
| ق      | ق (50:1)      |
All extended 6 harakat.

## Letters with Natural Madd (2 Harakat)
| Letter | Example    |
| ------ | ---------- |
| ح      | حم (40:1)  |
| ي      | يس (36:1)  |
| ط      | طه (20:1)  |
| ه      | طه (20:1)  |
| ر      | الر (10:1) |

Extended 2 harakat only.

# Internal “Munfasil-like” Structures (Within Same Word)

These are structurally internal but phonetically resemble separation.

# Contracted Hamzah Forms
| Word    | Underlying |
| ------- | ---------- |
| آمَنُوا | أَأْمَنُوا |
| أُوتُوا | أُؤْتُوا   |

# Dual Hamzah Structures
| Word            | Ref   |
| --------------- | ----- |
| ءَآلذَّكَرَيْنِ | 6:143 |
| ءَآللَّهُ       | 10:59 |

Contain internal badal + muttasil interaction.

# Alif Wasl Drop (Phonetic Merge)
| Word         | Underlying     |
| ------------ | -------------- |
| لِلرَّحْمٰنِ | لِ + ال + رحمن |
| لِلنَّاسِ    | لِ + ال + ناس  |

Although written as one token, assimilation occurs internally.
##  ملاحظات خاصة برواية حفص
- المد اللازم لا يُقصر أبدًا
- مد البدل ثابت على حركتين
- مد اللين خاص بالوقف فقط
- المد المنفصل لا يُقصر في الأداء المشهور

---



