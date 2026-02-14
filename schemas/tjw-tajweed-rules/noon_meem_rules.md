# Noon & Meem Tajweed Rules (Hafs Riwayah)

Analysis of the Noon and Meem rules (Sakinah, Mushaddadah, and huroof Muqatta'ah) in Uthmanic Hafs v2.0 dataset.

**Source:** `data/QS - QIRAAT/Uthmanic Hafs v2.0/hafsData_v2-0.json`

---

## 1. Noon Sakinah and Tanween

### Scope

This section covers the rules applied to Noon Sakinah and Tanween in Hafs ‘an ‘Asim.

**Definitions:**
*   **Noon Sakinah:** A Noon free from any vowel (Fatha, Damma, Kasra) that is fixed in pronunciation and writing, both in continuing and stopping.
*   **Tanween:** An extra Noon Sakinah attached to the end of nouns phonetically but not in writing, and in continuing but not in stopping.

| # | Rule | Arabic | Description | Count |
| - | ---- | ------ | ----------- | ----- |
| 1 | Izhaar Halqi | إظهار حلقي | Clear pronunciation without extra ghunnah | 3,627 |
| 2 | Idgham | إدغام | Merging of the Noon/Tanween into the next letter |
| 3 | Iqlab | إقلاب | Transformation of Noon/Tanween into a hidden Meem |
| 4 | Ikhfaa Haqiqi | إخفاء حقيقي | Hiding the Noon/Tanween with nasalization |

### Izhaar Halqi (إظهار حلقي)
إخراج الحرف من مخرجه بلا غنة زائدة (فصل النون/التنوين عن التالي بلا سكت).

**Occurs when followed by:** Throat Letters (ء، هـ، ع، ح، غ، خ)

**Technical Detection:**
*   **Unicode Pattern:** Noon (`U+0646`) with `U+06E1` (Small High Dotless Head of Khah) on top of it, or Aligned Tanween (`U+064B` (Fathatan), `U+064C` (Dammatan), `U+064D` (Kasratan))
*   **Visual:** Small head of Kha (حـ) above Noon; Tanween vowels are aligned (stacked directly).

| Following Letter | Examples |
| ---------------- | -------- |
| ء (Hamza) | وَيَنۡـَٔوۡنَ، مَّنۡ أَعۡرَضَ، وَجَنَّٰتٍ أَلۡفَافً | 
| هـ (Ha) | مِّنۡهُم،  مِنۡ هَاد،  قَوۡمٍ هَاد |
| ع (Ain) |  مِنۡ عَاصِمٖۗ،  شَيۡءٍ عَلِيمٌ |
| ح (Ha) | يَنۡحِتُونَ،  عَزِيزٌ حَكِيم |
| غ (Ghain) | مِنۡ غِسۡلِينٖ،  عَفُوًّا غَفُورًا |
| خ (Kha) |  وَٱلۡمُنۡخَنِقَةُ،  ذَرَّةٍ خَيۡرٗا | 

### Idgham (الإدغام)
Use of merging. Classified into Idgham with Ghunnah (Nasalization) and without Ghunnah.

#### Idgham with Ghunnah (إدغام بغنة)
دمج النون الساكنة أو التنوين في (ي، ن، م، و) مع بقاء الغنة.

**Occurs when followed by:** (ي، ن، م، و)

**Technical Detection:**
*   **Unicode Pattern:** Bare Noon (`U+0646`), or `U+065E` (Fatha with Two Dots), `U+0657` (Inverted Damma), `U+0656` (Subscript Alef) (Sequential Tanween)
*   **Visual:** Noon is bare (no sukoon); Tanween vowels are sequential (offset).

| Following Letter | Type | Examples |
| ---------------- | ---- | -------- |
| ي (Ya) | Deficient (Naqis) | مَن يَقُولُ،   يَوۡمَئِذٖ يَتَذَكَّرُ | 
| و (Waw) | Deficient (Naqis) |  مِن وَلِيّ،  يَوۡمَئِذٖ وَاجِفَة |
| م (Meem) | Complete (Kamil) | مِّن مَّآءٖ مَّهِين، َا مَلِكٗا نُّقَٰتِل | 
| ن (Noon) | Complete (Kamil) | إِن نَّفَعَتِ،  يَوۡمَئِذٖ نَّاعِمَةٞ | 

#### Idgham without Ghunnah (إدغام بغير غنة)
دمج النون الساكنة أو التنوين تماماً في (ل، ر) بلا غنة.

**Occurs when followed by:** (ل، ر)

**Technical Detection:**
*   **Unicode Pattern:** Bare Noon (`U+0646`), or `U+065E` (Fatha with Two Dots), `U+0657` (Inverted Damma), `U+0656` (Subscript Alef) (Sequential Tanween) + `U+0651` (Shadda) on next letter.

| Following Letter | Examples |
| ---------------- | -------- |
| ل (Lam) |  مِن لَّدُنكَ،  هُدٗى لِّلۡمُتَّقِينَ | 
| ر (Ra) |  مِّن رَّبِّهِمۡۖ،  غَفُورٞ رَّحِيم | 

#### Exceptions
**Izhaar Mutlaq (الإظهار المطلق):**
If the Noon Sakinah and the Idgham letter (Yaa or Waw) meet in the **same word**, Idgham is forbidden to preserve the meaning.
*   **Examples:** الدنيا (Ad-Dunya), بنيان (Bunyan), قنوان (Qinwan), صنوان (Sinwan).

### Iqlab (إقلاب)
قلب النون الساكنة أو التنوين ميماً مخفاة عند الباء بغنة.

**Occurs when followed by:** (ب)

**Technical Detection:**
*   **Unicode Pattern:** Specific combinations involving the small Meem (`U+06E2` (Small High Meem Isolated) or `U+06ED` (Small Low Meem)).

| Type | Unicode Combination | Visual | Examples |
| ---- | ------------------- | ------ | -------- |
| **Noon** | `U+0646` + `U+06E2` (Small High Meem Isolated) | Small High Meem above Noon |مِنۢ بَعۡد،  مِنۢ بَعۡضٖۗ |
| **Tanween Fatha** | `U+064E` (Fatha) + `U+06E2` (Small High Meem Isolated) | Single Fatha + Small High Meem | سميعاً بصيرا |
| **Tanween Damma** | `U+064F` (Damma) + `U+06E2` (Small High Meem Isolated) | Single Damma + Small High Meem | سَمِيعُۢ بَصِيرٞ |
| **Tanween Kasra** | `U+0650` (Kasra) + `U+06ED` (Small Low Meem) | Single Kasra + Small Low Meem | يَوۡمَئِذِۭ بِجَهَنَّمَ |

### Ikhfaa Haqiqi (إخفاء حقيقي)
ستر النون الساكنة أو التنوين عند مخرج التالي بغنة.

**Occurs when followed by:** The remaining 15 letters (ت، ث، ج، د، ذ، ز، س، ش، ص، ض، ط، ظ، ف، ق، ك).

**Technical Detection:**
*   **Unicode Pattern:** Bare Noon (`U+0646`), or `U+065E` (Fatha with Two Dots), `U+0657` (Inverted Damma), `U+0656` (Subscript Alef) (Sequential Tanween).
*   **Visual:** Noon is bare; Tanween vowels are sequential.

| Following Letter | Examples |
| ---------------- | -------- |
| ت (Ta) | فَمَن تَطَوَّع، فَمَن تَابَ |
| ث (Tha) | مِن ثَمَرَةٖ،  فَمَن ثَقُلَتۡ | 
| ج (Jeem) | فَأَنجَيۡنَٰهُم،  إِن جَآءَكُم |
| د (Dal) | أَندَادٗا،  مِن دُونِ | 
| ذ (Thal) |  مُنذِرُونَ، َ وَمِن ذُرِّيَّتِيۖ | 
| ز (Zay) | أُنزِلَ، فَإِن زَلَلۡتُم |
| س (Seen) | نَنسَخۡ، ۡ مِن سُوٓء | 
| ش (Sheen) |  مَّنشُور،  فَمَن شَآء |
| ص (Sad) | بَقَرَةٞ صَفۡرَآءُ، مَنصُورًا |
| ض (Dad) | مَّنضُودٖ،  مَّن ضَلَّ | 
| ط (Ta) |  مَنطِقَ، اْ مِن طَيِّبَٰتِ | 
| ظ (Zha) | تَنظُرُونَ، هُم مِّن ظَهِيرٖ | 
| ف (Fa) |  أَنفُسِهِمۡ، ْ مَن فَعَلَ | 
| ق (Qaf) |  مُنقَلِبُونَ،  مِن قَرۡيَةٍ | 
| ك (Kaf) | ٱلۡمُنكَرِ، مَن كَانَ | 

#### Special Case: Sakt (السكت المانع)
A brief pause (Sakt) that prevents Idgham despite the conditions being met.

**Example:**
*   **وقيل من راق** (Al-Qiyamah: 27) | وَقِيلَ مَنۡۜ رَاقٖ |
    *   Noon is followed by Ra (usually Idgham), but the Sakt sign `U+06DC` (Small High Seen) or specific narration rules require a pause, preserving the clear Noon.

### Impact of Waqf (Stopping) on Rules

In computational Tajweed, **Waqf** (stopping) changes the state of the letter and often cancels the rule if it depends on the following word.

| Condition | Effect of Stopping | Outcome (Rule Change) |
| --- | --- | --- |
| **Idgham / Iqlab / Ikhfaa** (End of Word) | The connection to the next letter is broken. | **Rule Removed.** The Noon reverts to **Izhaar** (Clear Noon with Sukoon). <br> *Example:* Stop on `من` in `وَقِيلَ مَنۡۜ رَاقٖ` -> Pronounce `Mn`. |
| **Tanween Damma / Kasra** | The Tanween sound is dropped. | **Rule Removed.** The letter becomes Sakin (Silent). <br> *Example:* `عليمٌ` -> `Aleem`. |
| **Tanween Fatha** | The Tanween is substituted with Alif. | **Madd Added (Madd 'Iwad).** <br> *Example:* `عليماً` -> `Aleemaa`. |

### Tanween Fatha at Stop (أحكام تنوين الفتح عند الوقف)

| Rule | Description | Condition | Unicode Pattern | Visual Detection | Performance | Stop Effect | Examples |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Madd 'Iwad (General)** | Substituting Tanween Fatha with an Alif upon stopping | End of Accusative Noun | `U+064B` (Fathatan), `U+0627` | Two Fathas followed generally by Alif | Prolong the letter for 2 counts instead of Tanween | Tanween turns into prolonged Alif | عليماً، حكيماً |
| **Exception: Ta Marbuta** | Turning Ta Marbuta into Ha upon stopping | End of Feminine Word | `U+0629`, `U+064B` (Fathatan) | Ta Marbuta with Tanween | Pronounce Ta as clear silent Ha | Delete Tanween and turn Ta into Ha | جنةً -> `jannah` |
| **Exception: Ism Maqsur** | Deleting Tanween and keeping Alif Maqsur | Nouns ending in (ى) | `U+0649`, `U+064B` (Fathatan) | Alif Maqsura (ى) with Tanween | Prolong Alif for 2 counts (Natural Madd) | Delete Tanween and keep the Madd | هدىً، طوىً |
| **Appendix: Noon Tawkid** | Noon of emphasis written as Tanween Fatha | Surah Yusuf & Al-Alaq | `U+0646`, `U+064B` (Fathatan) (visually) | Noon attached to verb written as Tanween | Treated like Accusative Nouns | Substitute Noon with Alif prolonged for 2 counts |  وَلَيَكُونٗا،   لَنَسۡفَعَۢا |

---

## 2. Meem Sakinah Rules

### Scope

This section covers the rules applied to Meem Sakinah (a Meem with no vowel) in Hafs ‘an ‘Asim.

**Definitions:**
*   **Meem Sakinah:** A Meem (`م`) free from any vowel (Fatha, Damma, Kasra) that is fixed in pronunciation and writing.
*   **The Three Rules:** Ikhfaa Shafawi, Idgham Shafawi (Mithlayn Sagheer), and Izhaar Shafawi.

| # | Rule | Arabic | Description |
| - | ---- | ------ | ----------- |
| 1 | Ikhfaa Shafawi | إخفاء شفوي | Hiding the Meem when followed by Baa |
| 2 | Idgham Shafawi | إدغام شفوي | Merging the Meem when followed by another Meem |
| 3 | Izhaar Shafawi | إظهار شفوي | Clear pronunciation when followed by any other letter |

### Ikhfaa Shafawi (إخفاء شفوي)
ستر الميم عند ملاقاتها للباء مع الغنة.

**Occurs when followed by:** (ب)

**Technical Detection:**
*   **Unicode Pattern:** `U+0645` (Bare Meem) followed by `ب`.
*   **Visual:** Meem is bare (no sukoon sign).

| Following Letter | Examples |
| ---------------- | -------- |
| ب (Baa) | تَرۡمِيهِم بِحِجَارَةٖ،  يَعۡتَصِم بِٱللَّهِ |

### Idgham Shafawi (إدغام شفوي)
Also called Idgham Mithlayn Sagheer (إدغام مثلين صغير). Merging the Meem Sakinah into a following Meem.

**Occurs when followed by:** (م)

**Technical Detection:**
*   **Unicode Pattern:** `U+0645` (Bare Meem) followed by `م` with `U+0651` (Shadda).
*   **Visual:** Meem is bare, following Meem has Shadda.

| Following Letter | Examples |        
| ---------------- | -------- |        
| م (Meem) |  لَهُم مَّا يَشَآءُونَ،   نَ فِي قُلُوبِهِم مَّرَضٞ |     

### Izhaar Shafawi (إظهار شفوي)
نطق الميم واضحة دون غنة زائدة.

**Occurs when followed by:** All letters except (ب) and (م).

**Technical Detection:**
*   **Unicode Pattern:** `U+06E1` (Small High Dotless Head of Khah) on the Meem (`U+0645`).
*   **Visual:** Small head of Kha (حـ) above Meem.

| Following Letter | Examples | Note |
| ---------------- | -------- | ---- |
| و (Waw) |  يَسۡتَهۡزِئُ بِهِمۡ وَيَمُدُّهُمۡ | **Izhaar Shadid:** Be careful not to hide Meem here. |
| ف (Fa) | بِذَنۢبِهِمۡ فَسَوَّىٰهَا | **Izhaar Shadid:** Be careful not to hide Meem here. |
| Others |  أَنۡعَمۡتَ، لَعَلَّكُمۡ تَتَّقُونَ | Standard clear pronunciation. |

### Impact of Waqf (Stopping) on Rules

| Rule | Effect of Stopping | Outcome (Rule Change) | Examples |
| --- | --- | --- | --- |
| **Ikhfaa Shafawi** (Meem-Baa) | Connection to 'Baa' is broken. | **Rule Removed.** Meem becomes clearly pronounced (Izhaar) with Sukoon. | `تَرۡمِيهِم بِحِجَارَةٖ`-> `tarmeehem` |
| **Idgham Shafawi** (Meem-Meem) | Connection to second 'Meem' is broken. | **Rule Removed.** First Meem becomes clearly pronounced (Izhaar) with Sukoon. | `لَهُم مَّا يَشَآءُونَ` -> `lahum`   |
| **Izhaar Shafawi** | No change in status. | **Remains Izhaar.** Meem is pronounced clearly with Sukoon. | `هُمْ فِيهَا` -> `hum` |

---

## 3. Noon and Meem Mushaddadah

### Scope

This section covers the rules applied to Noon and Meem with Shadda (Ghunnah Mushaddadah) in Hafs ‘an ‘Asim.

**Definitions:**
*   **Ghunnah:** A nasal sound emitted from the nose (Khayshum). It is an intrinsic characteristic of the Noon and Meem.
*   **Mushaddadah:** Emphasized (doubled) letter, marked with a Shadda (`ّ`).
*   **Level of Ghunnah:** The strongest level of Ghunnah (Akmal Ma Takoon) occurs in the Mushaddadah.

| # | Rule | Arabic | Description |
| - | ---- | ------ | ----------- |
| 1 | Noon Mushaddadah | النون المشددة | Emphasized Noon with prolonged Ghunnah |
| 2 | Meem Mushaddadah | الميم المشددة | Emphasized Meem with prolonged Ghunnah |
| 3 | Shadda 'Aridah | الشدة العارضة | Temporary emphasis due to Idgham (merging) |

### Noon Mushaddadah (النون المشددة)
نون مضاعفة أصلية تخرج بغنة مشبعة (أكمل ما تكون).

**Technical Detection:**
*   **Unicode Pattern:** `U+0646` (Noon) + `U+0651` (Shadda).
*   **Location:** Middle or end of the word.

| Feature | Description |
| --- | --- |
| **How to Identify** | Presence of Shadda mark above the Noon. |
| **Performance** | Press the tongue tip against the gums with prolonged Ghunnah (approx. 2 counts). |
| **Effect of Stop** | The Ghunnah remains fixed (Nabr) even when stopping. |
| **Examples** | إِنَّآ،  ٱلنَّاسِ،  ٱلۡجَنَّةَ |

### Meem Mushaddadah (الميم المشددة)
ميم مضاعفة أصلية تخرج بغنة مشبعة (أكمل ما تكون).

**Technical Detection:**
*   **Unicode Pattern:** `U+0645` (Meem) + `U+0651` (Shadda).
*   **Location:** Middle or end of the word.

| Feature | Description |
| --- | --- |
| **How to Identify** | Presence of Shadda mark above the Meem. |
| **Performance** | Complete closure of lips with prolonged Ghunnah (approx. 2 counts). |
| **Effect of Stop** | The Ghunnah remains fixed (Nabr) even when stopping. |
| **Examples** | حَمَّالَةَ،  ثُمَّ، عَمَّا |

### Shadda 'Aridah (الشدة العارضة)
علامة ضبط لإدغام سابق وليست أصلية في الكلمة.

**Technical Detection:**
*   **Unicode Pattern:** `U+0651` (Shadda) on a letter at the start of a word.
*   **Context:** Preceded by a letter causing Idgham (e.g., Noon Sakinah or Tanween merging into it).

| Feature | Description |
| --- | --- |
| **How to Identify** | Shadda at the very beginning of the word. |
| **Comparison** | Distinct from original Shadda which is part of the root/word structure. |
| **Performance** | Treated as emphasized (Mushaddad) only when connecting (Wasl). |
| **Effect of Start** | If starting from this word, the Shadda is ignored/removed. |
| **Effect of Stop (Preceding Word)** | If stopping on the previous word, the connection is broken. | **Rule Removed.** This word must be started without Shadda. |
| **Examples** | مِن مَّالٍ، مِن نُّطْفَةٍ |

---

## 4. Huroof Muqatta'at (Disjoint Letters)

### Scope

This section covers the rules applied to the Disjoint Letters (Huroof Muqatta'at) appearing at the beginning of 29 Surahs in Hafs ‘an ‘Asim. Specifically focusing on the interaction between the ending of one letter and the beginning of the next (e.g., Noon of "Seen" meeting Meem of "Meem").

**Definitions:**
*   **Huroof Muqatta'at:** Unique letter combinations at the start of certain Surahs. Pronounced by spelling out their names (e.g., Alif, Lam, Meem).
*   **Target Letters:** Letters ending in Noon or Meem that interact with what follows:
    *   **Lam (لام):** Ends in Meem.
    *   **Seen (سين):** Ends in Noon.
    *   **Meem (ميم):** Begins with Meem.
    *   **Ain (عين):** Contains a Yaa Leen and ends in Noon.
    *   **Noon (نون):** Ends in Noon.

| # | Rule | Arabic | Description |
| - | ---- | ------ | ----------- |
| 1 | Idgham of Meem (Lam) | إدغام الميم (ل) | Merging the Meem of "Lam" into the Meem of "Meem" |
| 2 | Idgham of Noon (Seen) | إدغام النون (س) | Merging the Noon of "Seen" into the Meem of "Meem" |
| 3 | Ikhfaa of Noon (Seen) | إخفاء النون (س) | Hiding the Noon of "Seen" before Qaf |
| 4 | Madd and Ikhfaa (Ain) | مد وإخفاء (ع) | Lengthening the Yaa of "Ain" and hiding its Noon |
| 5 | Izhaar (Narration) | إظهار الرواية | Exceptions where Noon is pronounced clearly despite Idgham rule |

### Idgham of Meem (Lam) (إدغام الميم في الميم)
إدغام ميم "لام" في ميم "ميم".

**Occurs in:** Alif-Lam-Meem (الم), Alif-Lam-Meem-Sad (المص), Alif-Lam-Meem-Ra (المر).

**Technical Detection:**
*   **Unicode Pattern:** `U+0644` (Lam) + `U+0653` (Maddah Above) followed by `U+0645` (Meem) + `U+0651` (Shadda).
*   **Example:** الم (2:1)
    *   Pronunciation: Alif Laaam-Meem.
    *   Mechanism: The Meem at the end of "Laam" meets the Meem at the start of "Meem" = Idgham Shafawi (Mithlayn).

### Idgham of Noon (Seen) (إدغام النون في الميم)
إدغام نون "سين" في ميم "ميم".

**Occurs in:** Ta-Seen-Meem (طسم).

**Technical Detection:**
*   **Unicode Pattern:** `U+0633` (Seen) + `U+0653` (Maddah Above) followed by `U+0645` (Meem) + `U+0651` (Shadda).
*   **Example:** طسم (26:1)
    *   Pronunciation: Taa Seem-Meem.
    *   Mechanism: The Noon at the end of "Seen" meets the Meem at the start of "Meem" = Idgham with Ghunnah.

### Ikhfaa of Noon (Seen) (إخفاء النون عند القاف)
إخفاء نون "سين" عند القاف.

**Occurs in:** Ain-Seen-Qaf (عسق).

**Technical Detection:**
*   **Unicode Pattern:** `U+0633` (Seen) + `U+0653` (Maddah Above) followed by `U+0642` (Qaf).
*   **Example:** عسق (42:2)
    *   Pronunciation: 'Aiiin Seee(ng) Qaaaf.
    *   Mechanism: The Noon at the end of "Seen" meets Qaf = Ikhfaa Haqiqi.

### Madd and Ikhfaa (Ain) (مد وإخفاء عين)
مد لين العين مع إخفاء نونها.

**Occurs in:** Kaf-Ha-Ya-Ain-Sad (كهيعص), Ain-Seen-Qaf (عسق).

**Technical Detection:**
*   **Unicode Pattern:** `U+0639` (Ain) + `U+0653` (Maddah Above).
*   **Example:** كهيعص (19:1)
    *   Pronunciation: ...'Aiiin Saaad.
    *   Mechanism:
        1.  **Madd Leen:** The Yaa inside "Ain" is lengthened 4 or 6 counts (6 is preferred).
        2.  **Ikhfaa:** The Noon at the end of "Ain" meets Sad or Seen = Ikhfaa Haqiqi.

### Izhaar (Narration Exceptions) (إظهار الرواية)
إظهار نون "نون" أو "سين" وصلاً (Exceptions in Hafs).

**Occurs in:** Ya-Seen (يس), Noon (ن).

**Technical Detection:**
*   **Unicode Pattern:** `U+0646` (Noon) or `U+0633` (Seen) followed by `U+0648` (Waw).
*   **Marking:** Presence of `U+06E1` (Small High Dotless Head of Khah) on the Noon/Seen instead of being bare.

| Surah | Ayah | Letters | Rule | Mechanism |
| ----- | ---- | ------- | ---- | --------- |
| **Ya-Seen (36)** | 1-2 | يس وَالْقُرْآنِ | Izhaar Mutlaq (Narration) | Pronounce "Seen" clearly despite connecting to Waw. |
| **Al-Qalam (68)** | 1 | ن وَالْقَلَمِ | Izhaar Mutlaq (Narration) | Pronounce "Noon" clearly despite connecting to Waw. |

### Impact of Waqf (Stopping) on Rules

| Rule | Context | Effect of Stopping (Hypothetical/Test) |
| --- | --- | --- |
| **Idgham (Between Letters)** | e.g., Lam-Meem in `الم` | **Rule Removed.** The first letter (Lam) is pronounced with clear Meem (Izhaar) and Madd Lazim (6 counts). |
| **Ikhfaa (Between Letters)** | e.g., Seen-Qaf in `عسق` | **Rule Removed.** The first letter (Seen) is pronounced with clear Noon (Izhaar) and Madd Lazim (6 counts). |
| **End of Letter Group** | e.g., End of `الم` | **Fixed Sukoon.** The final letter follows the standard pause rule (Madd Lazim 6 counts + Sukoon). |
