# Quran Data Validation Skill

You are an expert in validating Quranic data against authoritative sources with ZERO tolerance for errors in sacred text.

## Validation Principles

1. **Zero Tolerance**: Any discrepancy in Quranic text is unacceptable
2. **Authoritative Sources**: Always cross-reference with King Fahd Complex editions, Tanzil.net, QUL
3. **Character Precision**: Count every character, including diacritics and spaces
4. **Verse Boundaries**: Respect Qiraah-specific verse numbering variations
5. **Provenance Tracking**: Document source of every piece of data

## Known Authoritative Counts

### Hafs 'an Asim Narration
- **Total Verses**: 6,236
- **Total Characters**: 323,015 (with diacritics and spaces)
- **Total Words**: ~77,429
- **Surahs**: 114

### Warsh 'an Nafi' Narration
- **Total Verses**: 6,214 (22 fewer than Hafs)
- **Verse Differences**: Different verse boundaries in some surahs
- **Character Count**: Validate per source (may differ slightly)

### Other Narrations
- **Qalun**: 6,214 verses (same as Warsh for Nafi's Qiraah)
- **Shu'bah**: 6,236 verses (same as Hafs for Asim's Qiraah)
- **Al-Duri**: Varies by Qiraah (Abu Amr or Al-Kisa'i)
- **Al-Susi**: 6,204 verses (from Abu Amr's Qiraah)

## Validation Checklist

### Character Count Validation

```python
def validate_character_count(text, expected_count, narration='hafs'):
    """Validate total character count."""
    actual = len(text)
    match = actual == expected_count
    
    return {
        'narration': narration,
        'expected': expected_count,
        'actual': actual,
        'match': match,
        'difference': actual - expected_count,
        'accuracy': (min(actual, expected_count) / max(actual, expected_count)) * 100
    }

# Example usage
hafs_text = load_hafs_text()  # From QS-QIRAAT
result = validate_character_count(hafs_text, 323015, 'hafs')
assert result['match'], f"Character count mismatch: {result}"
```

### Verse Count Validation

```python
def validate_verse_count(verses, narration='hafs'):
    """Validate verse count per narration."""
    expected_counts = {
        'hafs': 6236,
        'warsh': 6214,
        'qalun': 6214,
        'shubah': 6236,
        'susi': 6204
    }
    
    expected = expected_counts.get(narration.lower())
    actual = len(verses)
    
    return {
        'narration': narration,
        'expected': expected,
        'actual': actual,
        'match': actual == expected if expected else None
    }
```

### Surah Metadata Validation

```python
def validate_surah_metadata(surah_data):
    """Validate surah count and basic metadata."""
    assert len(surah_data) == 114, "Must have exactly 114 surahs"
    
    # Validate Surah 1 (Al-Fatiha)
    assert surah_data[0]['name_ar'] == 'الفاتحة'
    assert surah_data[0]['verses'] == 7
    
    # Validate Surah 114 (An-Nas)
    assert surah_data[113]['name_ar'] == 'الناس'
    assert surah_data[113]['verses'] == 6
    
    return True
```

## Cross-Validation Strategy

### Primary Source: QS-QIRAAT v2.0
- King Fahd Complex Uthmanic Script Dataset
- 6 narrations available: Hafs, Warsh, Qalun, Shu'bah, Al-Duri, Al-Susi
- Formats: JSON, CSV, XML, SQL, XLSX

### Secondary Source: QUL (qul.tarteel.ai)
- **Limitation**: Hafs only for morphology/syntax
- Use for: Morphological validation, tajweed rules, audio timestamps
- 77,429 morphologically analyzed words (Hafs)

### Tertiary Source: Tanzil.net
- Verified Quranic text (3-step verification process)
- Cross-reference for character/verse counts
- Simple text format for quick validation

### Comparative Source: ErQuran (erquran.org)
- 3,744+ textual variants across 10 canonical Qiraat
- Use for: Identifying where Warsh differs from Hafs
- Harvard-backed, academically rigorous

## Validation Workflow

1. **Load Data**: Import from QS-QIRAAT (primary source)
2. **Count Validation**: Verify character/verse counts against known values
3. **Structure Validation**: Check surah metadata (114 surahs, correct names)
4. **Cross-Reference**: Compare with Tanzil.net or QUL (for Hafs)
5. **Variant Analysis**: Use ErQuran to identify expected differences between narrations
6. **Document Discrepancies**: Log ANY deviation for scholarly review
7. **Scholarly Review**: Present findings to domain experts (engineering-mediated)

## Common Validation Errors

### Error 1: Unicode Normalization Mismatch
- **Symptom**: Character count off by small amount
- **Cause**: Different Unicode normalization (NFC vs NFD)
- **Fix**: Document normalization form used, normalize before comparing

### Error 2: Whitespace Handling
- **Symptom**: Character count includes/excludes spaces inconsistently
- **Cause**: Different space handling across sources
- **Fix**: Clarify whether spaces are counted, document decision

### Error 3: Diacritic Inclusion
- **Symptom**: Character count varies significantly
- **Cause**: Some sources strip diacritics
- **Fix**: Always include diacritics for Quranic text validation

### Error 4: Verse Boundary Variations
- **Symptom**: Verse counts don't match between narrations
- **Cause**: This is EXPECTED - different Qiraat have different verse boundaries
- **Fix**: Validate against narration-specific expected counts

## Red Flags (Require Immediate Investigation)

🚨 **Character count differs from authoritative source by >10 characters**
🚨 **Verse count doesn't match ANY known narration pattern**
🚨 **Surah count is not exactly 114**
🚨 **Surah names don't match traditional Arabic names**
🚨 **Invalid Unicode codepoints in Arabic text range**

## Green Lights (Validation Passed)

✅ Character count matches authoritative source exactly
✅ Verse count matches narration-specific expected value
✅ All 114 surahs present with correct metadata
✅ Unicode validation passes (all chars in valid range)
✅ Cross-validation with secondary source confirms accuracy

## When to Use This Skill

Invoke this skill when:
- Loading Quranic data from any source (QS-QIRAAT, QUL, Tanzil)
- Implementing RR-008 (Validate against authoritative sources)
- Debugging character/verse count mismatches
- Designing automated validation scripts
- Preparing data for scholarly review
- Verifying Layer 0 (Character) or Layer 5 (Verse) extraction accuracy

## Current Task Context

You are validating data for the QUD research project. Phase 1 focuses on Hafs (6,236 verses, 323,015 chars) and Warsh (6,214 verses) narrations. All validation must achieve 100% accuracy before proceeding to next research phase.
