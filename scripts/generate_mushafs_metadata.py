#!/usr/bin/env python3
"""
Generate mushafs-metadata.json from QS-QIRAAT datasets.

Outputs:
- verse_counts: surah_no -> {riwaya: count}
- word_counts: "surah:verse" -> {riwaya: count, or 0 if missing}
"""

import json
from pathlib import Path
from datetime import date
from collections import defaultdict

# Project paths
SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR.parent / "data" / "QS - QIRAAT"
OUTPUT_FILE = SCRIPT_DIR.parent / "data" / "mushafs-metadata.json"

# Riwaya folder mappings
RIWAYAT = {
    "douri": "Uthmanic Douri v2.0",
    "hafs": "Uthmanic Hafs v2.0",
    "qaloun": "Uthmanic Qaloun v2.1",
    "shuba": "Uthmanic Shuba v2.0",
    "sousi": "Uthmanic Sousi v2.0",
    "warsh": "Uthmanic Warsh v2.1",
}


def find_json_file(riwaya_folder: str) -> Path:
    """Find the JSON data file in a riwaya folder."""
    folder = DATA_DIR / riwaya_folder
    for subfolder in folder.iterdir():
        if "data" in subfolder.name.lower():
            for f in subfolder.iterdir():
                if f.suffix == ".json":
                    return f
    raise FileNotFoundError(f"No JSON file found in {folder}")


def clean_aya_text(text: str) -> str:
    """Remove trailing NBSP + aya marker glyph."""
    if len(text) >= 2 and text[-2] == "\xa0":
        return text[:-2]
    return text


def count_words(text: str) -> int:
    """Count words in cleaned aya text."""
    cleaned = clean_aya_text(text)
    words = cleaned.split()
    return len(words)


def load_riwaya_data(riwaya_key: str) -> list[dict]:
    """Load JSON data for a riwaya."""
    json_file = find_json_file(RIWAYAT[riwaya_key])
    with open(json_file, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    print("Generating mushafs-metadata.json...")

    # Collect all surah names (from any riwaya, they should be the same)
    surah_names = {}

    # verse_counts[surah_no][riwaya] = count
    verse_counts = defaultdict(dict)

    # word_counts["surah:verse"][riwaya] = count
    word_counts = defaultdict(dict)

    # Track all surah:verse combinations across all riwayat
    all_verses = set()

    for riwaya_key in RIWAYAT:
        print(f"  Processing {riwaya_key}...")
        data = load_riwaya_data(riwaya_key)

        # Group by surah
        surah_verses = defaultdict(dict)  # surah_no -> {aya_no: aya_text}

        for item in data:
            sura_no = item["sura_no"]
            aya_no = item["aya_no"]
            aya_text = item["aya_text"]

            # Store surah names (once)
            if sura_no not in surah_names:
                surah_names[sura_no] = {
                    "name_ar": item["sura_name_ar"],
                    "name_en": item["sura_name_en"],
                }

            # Store verse (overwrite if duplicate due to page splits)
            # We want the full verse, so concatenate if split across pages
            if aya_no in surah_verses[sura_no]:
                # Concatenate text (remove trailing marker from first part)
                existing = clean_aya_text(surah_verses[sura_no][aya_no])
                new_part = clean_aya_text(aya_text)
                surah_verses[sura_no][aya_no] = existing + " " + new_part
            else:
                surah_verses[sura_no][aya_no] = aya_text

            all_verses.add(f"{sura_no}:{aya_no}")

        # Calculate counts
        for sura_no, verses in surah_verses.items():
            verse_counts[str(sura_no)][riwaya_key] = len(verses)

            for aya_no, aya_text in verses.items():
                key = f"{sura_no}:{aya_no}"
                word_counts[key][riwaya_key] = count_words(aya_text)

    # Fill in 0 for missing verses in any riwaya
    for verse_key in all_verses:
        for riwaya_key in RIWAYAT:
            if riwaya_key not in word_counts[verse_key]:
                word_counts[verse_key][riwaya_key] = 0

    # Sort keys properly
    def sort_verse_key(key):
        sura, aya = key.split(":")
        return (int(sura), int(aya))

    sorted_word_counts = {
        k: word_counts[k] for k in sorted(word_counts.keys(), key=sort_verse_key)
    }
    sorted_verse_counts = {
        k: verse_counts[k] for k in sorted(verse_counts.keys(), key=int)
    }

    # Build output
    output = {
        "metadata": {
            "generated": str(date.today()),
            "source": "QS - QIRAAT datasets",
            "riwayat": list(RIWAYAT.keys()),
        },
        "surah_names": {str(k): v for k, v in sorted(surah_names.items())},
        "verse_counts": sorted_verse_counts,
        "word_counts": sorted_word_counts,
    }

    # Write output
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"Done! Output: {OUTPUT_FILE}")
    print(f"  - {len(sorted_verse_counts)} surahs")
    print(f"  - {len(sorted_word_counts)} verse entries")


if __name__ == "__main__":
    main()
