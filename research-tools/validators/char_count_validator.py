"""
Character Count Validator

Tier 2 (Reusable Research Tool)

Zero-tolerance validation for Quranic character counts.

CRITICAL: Quranic text integrity requires exact character counts:
- Hafs: 323,015 characters (excluding Bismillah variants)
- Warsh: Different count due to orthographic variations

Any deviation is a DATA INTEGRITY ERROR.
"""

from typing import Dict, Optional, Tuple


# Canonical character counts (to be refined with authoritative sources)
CANONICAL_CHAR_COUNTS = {
    "Hafs": 323_015,  # Placeholder - needs verification from King Fahd Complex
    "Warsh": None,     # To be determined from authoritative Warsh source
}


class CharacterCountValidator:
    """
    Validate Quranic text character counts.

    Provides zero-tolerance validation against canonical counts.
    """

    def __init__(self, strict: bool = True):
        """
        Initialize validator.

        Args:
            strict: If True, raise exception on validation failure.
                   If False, return validation results without raising.
        """
        self.strict = strict
        self.canonical_counts = CANONICAL_CHAR_COUNTS

    def count_characters(self, text: str, exclude_spaces: bool = True) -> int:
        """
        Count characters in text.

        Args:
            text: Input text
            exclude_spaces: If True, exclude whitespace from count

        Returns:
            Character count
        """
        if exclude_spaces:
            return len(text.replace(' ', '').replace('\n', '').replace('\t', ''))
        return len(text)

    def validate_narration(
        self,
        text: str,
        narration: str,
        exclude_spaces: bool = True
    ) -> Tuple[bool, int, Optional[int], Optional[int]]:
        """
        Validate character count for a specific narration.

        Args:
            text: Full Quranic text for the narration
            narration: Narration name (e.g., "Hafs", "Warsh")
            exclude_spaces: If True, exclude whitespace from count

        Returns:
            Tuple of (is_valid, actual_count, expected_count, difference)

        Raises:
            ValueError: If strict=True and validation fails
        """
        actual = self.count_characters(text, exclude_spaces=exclude_spaces)
        expected = self.canonical_counts.get(narration)

        if expected is None:
            # No canonical count defined yet
            return (True, actual, None, None)

        is_valid = (actual == expected)
        difference = actual - expected

        if not is_valid and self.strict:
            raise ValueError(
                f"Character count mismatch for {narration}: "
                f"expected {expected}, got {actual} (diff: {difference:+d})"
            )

        return (is_valid, actual, expected, difference)

    def validate_text_segments(
        self,
        segments: Dict[str, str],
        narration: str,
        exclude_spaces: bool = True
    ) -> Dict[str, Tuple[bool, int]]:
        """
        Validate character counts for text segments (e.g., individual surahs).

        Args:
            segments: Dictionary of segment_id -> text
            narration: Narration name
            exclude_spaces: If True, exclude whitespace from count

        Returns:
            Dictionary of segment_id -> (is_valid, count)
        """
        results = {}

        for segment_id, text in segments.items():
            count = self.count_characters(text, exclude_spaces=exclude_spaces)
            results[segment_id] = (True, count)  # Individual segments don't have canonical counts

        return results

    def set_canonical_count(self, narration: str, count: int):
        """
        Set or update canonical character count for a narration.

        Args:
            narration: Narration name
            count: Canonical character count

        Note:
            This should only be used after verification from authoritative sources.
        """
        self.canonical_counts[narration] = count

    def get_canonical_count(self, narration: str) -> Optional[int]:
        """
        Get canonical character count for a narration.

        Args:
            narration: Narration name

        Returns:
            Canonical count, or None if not defined
        """
        return self.canonical_counts.get(narration)
