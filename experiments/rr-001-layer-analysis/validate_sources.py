#!/usr/bin/env python3
"""
Source Data Validation Script for RR-001

Validates QS-QIRAAT Hafs and Warsh datasets before analysis.

EXPERIMENTAL: Tier 1 research code
"""

import json
import sys
from pathlib import Path

# Add research-tools to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "research-tools"))

from validators.verse_validator import VerseCountValidator
from validators.char_count_validator import CharacterCountValidator


def load_dataset(filepath: Path) -> list:
    """Load JSON dataset."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as e:
        print(f"❌ ERROR: Invalid JSON in {filepath}: {e}")
        return None


def validate_schema(records: list) -> tuple[bool, list]:
    """
    Validate QS-QIRAAT schema (11 required fields).

    Returns:
        (is_valid, errors)
    """
    required_fields = [
        'id', 'jozz', 'page', 'sura_no', 'sura_name_en', 'sura_name_ar',
        'line_start', 'line_end', 'aya_no', 'aya_text', 'aya_text_emlaey'
    ]

    errors = []

    if not records:
        errors.append("Empty dataset")
        return (False, errors)

    # Check first record has all fields
    first_record = records[0]
    missing = [f for f in required_fields if f not in first_record]

    if missing:
        errors.append(f"Missing fields in first record: {missing}")

    # Spot check random records
    for i in [0, len(records) // 2, -1]:
        if i >= len(records):
            continue

        record = records[i]
        missing = [f for f in required_fields if f not in record]
        if missing:
            errors.append(f"Missing fields in record {i}: {missing}")

    return (len(errors) == 0, errors)


def validate_narration(
    records: list,
    narration: str,
    expected_verse_count: int
) -> dict:
    """
    Validate narration dataset.

    Returns validation results dictionary.
    """
    results = {
        "narration": narration,
        "success": True,
        "errors": [],
        "warnings": [],
        "metrics": {}
    }

    if not records:
        results["success"] = False
        results["errors"].append(f"No data found for {narration}")
        return results

    # Schema validation
    schema_valid, schema_errors = validate_schema(records)
    if not schema_valid:
        results["success"] = False
        results["errors"].extend(schema_errors)
        return results

    results["metrics"]["record_count"] = len(records)

    # Verse count validation
    verse_validator = VerseCountValidator(strict=False)
    is_valid, actual, expected, diff = verse_validator.validate_total_verses(
        len(records),
        narration
    )

    results["metrics"]["verse_count"] = {
        "actual": actual,
        "expected": expected,
        "difference": diff,
        "valid": is_valid
    }

    if not is_valid:
        results["success"] = False
        results["errors"].append(
            f"Verse count mismatch: expected {expected}, got {actual} (diff: {diff:+d})"
        )

    # Character count validation (full text only)
    char_validator = CharacterCountValidator(strict=False)
    full_text = " ".join(r['aya_text'] for r in records)
    is_valid, actual, expected, diff = char_validator.validate_narration(
        full_text,
        narration,
        exclude_spaces=True
    )

    results["metrics"]["character_count"] = {
        "actual": actual,
        "expected": expected,
        "difference": diff if diff is not None else "N/A",
        "valid": is_valid
    }

    if expected and not is_valid:
        results["warnings"].append(
            f"Character count mismatch: expected {expected}, got {actual} (diff: {diff:+d})"
        )
        # Note: Don't fail on character count - may not have canonical value yet

    return results


def main():
    """Run validation on Hafs and Warsh datasets."""

    print("=" * 80)
    print("RR-001 Source Data Validation")
    print("=" * 80)
    print()

    data_dir = Path(__file__).parent / "data"

    # Check for complete datasets
    hafs_complete = data_dir / "hafs_complete.json"
    warsh_complete = data_dir / "warsh_complete.json"

    # Fallback to sample datasets
    hafs_file = hafs_complete if hafs_complete.exists() else data_dir / "hafs_sample.json"
    warsh_file = warsh_complete if warsh_complete.exists() else data_dir / "warsh_sample.json"

    if hafs_file == hafs_complete:
        print("✓ Using complete Hafs dataset")
    else:
        print("⚠️  Using SAMPLE Hafs dataset (complete dataset not found)")

    if warsh_file == warsh_complete:
        print("✓ Using complete Warsh dataset")
    else:
        print("⚠️  Using SAMPLE Warsh dataset (complete dataset not found)")

    print()

    # Load datasets
    print("Loading datasets...")
    hafs_data = load_dataset(hafs_file)
    warsh_data = load_dataset(warsh_file)

    if not hafs_data:
        print(f"❌ FATAL: Could not load Hafs dataset from {hafs_file}")
        return 1

    if not warsh_data:
        print(f"❌ FATAL: Could not load Warsh dataset from {warsh_file}")
        return 1

    print(f"✓ Loaded {len(hafs_data)} Hafs records")
    print(f"✓ Loaded {len(warsh_data)} Warsh records")
    print()

    # Validate Hafs
    print("-" * 80)
    print("Validating Hafs Dataset")
    print("-" * 80)
    hafs_results = validate_narration(hafs_data, "Hafs", 6236)

    if hafs_results["success"]:
        print("✅ Hafs validation: PASS")
    else:
        print("❌ Hafs validation: FAIL")

    for error in hafs_results["errors"]:
        print(f"  ❌ ERROR: {error}")

    for warning in hafs_results["warnings"]:
        print(f"  ⚠️  WARNING: {warning}")

    print(f"  Records: {hafs_results['metrics']['record_count']}")
    print(f"  Verses: {hafs_results['metrics']['verse_count']}")
    print(f"  Characters: {hafs_results['metrics']['character_count']}")
    print()

    # Validate Warsh
    print("-" * 80)
    print("Validating Warsh Dataset")
    print("-" * 80)
    warsh_results = validate_narration(warsh_data, "Warsh", 6214)

    if warsh_results["success"]:
        print("✅ Warsh validation: PASS")
    else:
        print("❌ Warsh validation: FAIL")

    for error in warsh_results["errors"]:
        print(f"  ❌ ERROR: {error}")

    for warning in warsh_results["warnings"]:
        print(f"  ⚠️  WARNING: {warning}")

    print(f"  Records: {warsh_results['metrics']['record_count']}")
    print(f"  Verses: {warsh_results['metrics']['verse_count']}")
    print(f"  Characters: {warsh_results['metrics']['character_count']}")
    print()

    # Overall status
    print("=" * 80)
    overall_success = hafs_results["success"] and warsh_results["success"]

    if overall_success:
        print("✅ OVERALL STATUS: PASS - Datasets ready for analysis")
        return 0
    else:
        print("❌ OVERALL STATUS: FAIL - Fix errors before proceeding")
        return 1


if __name__ == "__main__":
    sys.exit(main())
