"""
Verse Count Validator

Tier 2 (Reusable Research Tool)

Zero-tolerance validation for Quranic verse counts.

CRITICAL: Different narrations have different verse counts:
- Hafs: 6,236 verses
- Warsh: 6,214 verses

This is a theological reality, not an error.
"""

from typing import Dict, List, Optional, Tuple


# Canonical verse counts by narration
CANONICAL_VERSE_COUNTS = {
    "Hafs": 6236,
    "Warsh": 6214,
}

# Surah verse counts for Hafs (114 surahs)
HAFS_SURAH_VERSE_COUNTS = {
    1: 7, 2: 286, 3: 200, 4: 176, 5: 120, 6: 165, 7: 206, 8: 75, 9: 129, 10: 109,
    11: 123, 12: 111, 13: 43, 14: 52, 15: 99, 16: 128, 17: 111, 18: 110, 19: 98, 20: 135,
    21: 112, 22: 78, 23: 118, 24: 64, 25: 77, 26: 227, 27: 93, 28: 88, 29: 69, 30: 60,
    31: 34, 32: 30, 33: 73, 34: 54, 35: 45, 36: 83, 37: 182, 38: 88, 39: 75, 40: 85,
    41: 54, 42: 53, 43: 89, 44: 59, 45: 37, 46: 35, 47: 38, 48: 29, 49: 18, 50: 45,
    51: 60, 52: 49, 53: 62, 54: 55, 55: 78, 56: 96, 57: 29, 58: 22, 59: 24, 60: 13,
    61: 14, 62: 11, 63: 11, 64: 18, 65: 12, 66: 12, 67: 30, 68: 52, 69: 52, 70: 44,
    71: 28, 72: 28, 73: 20, 74: 56, 75: 40, 76: 31, 77: 50, 78: 40, 79: 46, 80: 42,
    81: 29, 82: 19, 83: 36, 84: 25, 85: 22, 86: 17, 87: 19, 88: 26, 89: 30, 90: 20,
    91: 15, 92: 21, 93: 11, 94: 8, 95: 8, 96: 19, 97: 5, 98: 8, 99: 8, 100: 11,
    101: 11, 102: 8, 103: 3, 104: 9, 105: 5, 106: 4, 107: 7, 108: 3, 109: 6, 110: 3,
    111: 5, 112: 4, 113: 5, 114: 6
}


class VerseCountValidator:
    """
    Validate Quranic verse counts.

    Provides zero-tolerance validation against canonical verse counts
    for different narrations.
    """

    def __init__(self, strict: bool = True):
        """
        Initialize validator.

        Args:
            strict: If True, raise exception on validation failure.
                   If False, return validation results without raising.
        """
        self.strict = strict
        self.canonical_counts = CANONICAL_VERSE_COUNTS
        self.hafs_surah_counts = HAFS_SURAH_VERSE_COUNTS

    def validate_total_verses(
        self,
        verse_count: int,
        narration: str
    ) -> Tuple[bool, int, Optional[int], Optional[int]]:
        """
        Validate total verse count for a narration.

        Args:
            verse_count: Actual verse count
            narration: Narration name (e.g., "Hafs", "Warsh")

        Returns:
            Tuple of (is_valid, actual_count, expected_count, difference)

        Raises:
            ValueError: If strict=True and validation fails
        """
        expected = self.canonical_counts.get(narration)

        if expected is None:
            # No canonical count defined yet
            return (True, verse_count, None, None)

        is_valid = (verse_count == expected)
        difference = verse_count - expected

        if not is_valid and self.strict:
            raise ValueError(
                f"Verse count mismatch for {narration}: "
                f"expected {expected}, got {verse_count} (diff: {difference:+d})"
            )

        return (is_valid, verse_count, expected, difference)

    def validate_surah_verses(
        self,
        surah_number: int,
        verse_count: int,
        narration: str = "Hafs"
    ) -> Tuple[bool, int, Optional[int], Optional[int]]:
        """
        Validate verse count for a specific surah.

        Args:
            surah_number: Surah number (1-114)
            verse_count: Actual verse count for this surah
            narration: Narration name (default: "Hafs")

        Returns:
            Tuple of (is_valid, actual_count, expected_count, difference)

        Raises:
            ValueError: If surah number invalid or strict=True and validation fails
        """
        if not 1 <= surah_number <= 114:
            raise ValueError(f"Invalid surah number: {surah_number} (must be 1-114)")

        # Currently only have Hafs surah counts
        if narration == "Hafs":
            expected = self.hafs_surah_counts.get(surah_number)
        else:
            expected = None  # Warsh surah counts not yet defined

        if expected is None:
            return (True, verse_count, None, None)

        is_valid = (verse_count == expected)
        difference = verse_count - expected

        if not is_valid and self.strict:
            raise ValueError(
                f"Verse count mismatch for Surah {surah_number} ({narration}): "
                f"expected {expected}, got {verse_count} (diff: {difference:+d})"
            )

        return (is_valid, verse_count, expected, difference)

    def validate_all_surahs(
        self,
        surah_verse_counts: Dict[int, int],
        narration: str = "Hafs"
    ) -> Dict[int, Tuple[bool, int, Optional[int], Optional[int]]]:
        """
        Validate verse counts for all surahs.

        Args:
            surah_verse_counts: Dictionary of surah_number -> verse_count
            narration: Narration name (default: "Hafs")

        Returns:
            Dictionary of surah_number -> (is_valid, actual, expected, difference)
        """
        results = {}

        for surah_num, count in surah_verse_counts.items():
            # Temporarily set strict=False to collect all results
            original_strict = self.strict
            self.strict = False

            results[surah_num] = self.validate_surah_verses(surah_num, count, narration)

            self.strict = original_strict

        return results

    def get_expected_verse_count(self, narration: str) -> Optional[int]:
        """
        Get expected total verse count for a narration.

        Args:
            narration: Narration name

        Returns:
            Expected verse count, or None if not defined
        """
        return self.canonical_counts.get(narration)

    def get_expected_surah_count(self, surah_number: int, narration: str = "Hafs") -> Optional[int]:
        """
        Get expected verse count for a specific surah.

        Args:
            surah_number: Surah number (1-114)
            narration: Narration name (default: "Hafs")

        Returns:
            Expected verse count, or None if not defined
        """
        if narration == "Hafs":
            return self.hafs_surah_counts.get(surah_number)
        return None
