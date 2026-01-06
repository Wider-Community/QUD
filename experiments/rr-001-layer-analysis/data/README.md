# RR-001 Data Sources

## Required Datasets

### 1. QS-QIRAAT Hafs Dataset
- **Narration**: Hafs (from Asim)
- **Expected Verses**: 6,236
- **Format**: JSON
- **Source**: QS-QIRAAT repository or API

### 2. QS-QIRAAT Warsh Dataset
- **Narration**: Warsh (from Nafi)
- **Expected Verses**: 6,214
- **Format**: JSON
- **Source**: QS-QIRAAT repository or API

## QS-QIRAAT Schema

Each verse record contains 11 fields:

```json
{
  "id": "1:1",
  "jozz": 1,
  "page": 1,
  "sura_no": 1,
  "sura_name_en": "Al-Fatihah",
  "sura_name_ar": "الفاتحة",
  "line_start": 1,
  "line_end": 1,
  "aya_no": 1,
  "aya_text": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
  "aya_text_emlaey": "بسم الله الرحمن الرحيم"
}
```

## Data Acquisition

### Option 1: Direct API Access
If QS-QIRAAT provides an API:
```bash
# Example (adjust URL as needed)
curl https://api.qs-qiraat.org/hafs > hafs_complete.json
curl https://api.qs-qiraat.org/warsh > warsh_complete.json
```

### Option 2: Repository Clone
If QS-QIRAAT is in a Git repository:
```bash
git clone https://github.com/QS-QIRAAT/dataset.git qs-qiraat-source
cp qs-qiraat-source/hafs.json hafs_complete.json
cp qs-qiraat-source/warsh.json warsh_complete.json
```

### Option 3: Manual Download
1. Visit QS-QIRAAT website
2. Download Hafs narration dataset
3. Download Warsh narration dataset
4. Place files in this directory as:
   - `hafs_complete.json`
   - `warsh_complete.json`

## Alternative: Sample Data

For initial development/testing, use the sample data files:
- `hafs_sample.json` - First 10 verses of Hafs
- `warsh_sample.json` - First 10 verses of Warsh

## Validation

After obtaining data, run validation:

```bash
cd ../
python validate_sources.py
```

This will verify:
- ✓ Hafs has 6,236 verses
- ✓ Warsh has 6,214 verses
- ✓ Character counts match canonical values
- ✓ Schema is valid (all 11 fields present)

## Data Files

- `hafs_complete.json` - Full Hafs dataset (required for analysis)
- `warsh_complete.json` - Full Warsh dataset (required for analysis)
- `hafs_sample.json` - Sample data for testing
- `warsh_sample.json` - Sample data for testing
- `README.md` - This file

## Status

- [ ] Hafs dataset acquired
- [ ] Warsh dataset acquired
- [ ] Data validated
- [ ] Ready for analysis

## Notes

**CRITICAL**: Do not proceed with analysis until both datasets are validated. Invalid source data will invalidate all research findings.
