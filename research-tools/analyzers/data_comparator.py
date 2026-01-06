"""
Data Comparator

Tier 2 (Reusable Research Tool)

Compare Quranic data at character-level and verse-level.
Useful for validating cross-Qiraat/Narration variations.
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import difflib


@dataclass
class CharacterDiff:
    """Difference at character level."""

    position: int
    char1: str
    char2: str
    context_before: str
    context_after: str


@dataclass
class VerseDiff:
    """Difference at verse level."""

    surah: int
    verse: int
    text1: str
    text2: str
    char_differences: List[CharacterDiff]
    similarity_ratio: float


class DataComparator:
    """
    Compare Quranic data across versions/narrations.

    Provides character-level and verse-level diff utilities.
    """

    def __init__(self, context_window: int = 10):
        """
        Initialize comparator.

        Args:
            context_window: Number of characters to show before/after diff
        """
        self.context_window = context_window

    def compare_strings(self, str1: str, str2: str) -> List[CharacterDiff]:
        """
        Compare two strings at character level.

        Args:
            str1: First string
            str2: Second string

        Returns:
            List of character differences
        """
        differences = []

        # Use difflib for sequence matching
        matcher = difflib.SequenceMatcher(None, str1, str2)

        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag == 'replace':
                # Characters are different
                for pos in range(i1, i2):
                    if pos < len(str1) and pos < len(str2):
                        context_start = max(0, pos - self.context_window)
                        context_end = min(len(str1), pos + self.context_window + 1)

                        diff = CharacterDiff(
                            position=pos,
                            char1=str1[pos],
                            char2=str2[pos] if pos < len(str2) else '',
                            context_before=str1[context_start:pos],
                            context_after=str1[pos + 1:context_end]
                        )
                        differences.append(diff)

            elif tag == 'delete':
                # Character exists in str1 but not str2
                for pos in range(i1, i2):
                    context_start = max(0, pos - self.context_window)
                    context_end = min(len(str1), pos + self.context_window + 1)

                    diff = CharacterDiff(
                        position=pos,
                        char1=str1[pos],
                        char2='',
                        context_before=str1[context_start:pos],
                        context_after=str1[pos + 1:context_end]
                    )
                    differences.append(diff)

            elif tag == 'insert':
                # Character exists in str2 but not str1
                # (represented as position in str2)
                pass  # Handle insertions separately if needed

        return differences

    def compare_verses(
        self,
        verse1_data: Dict[str, str],
        verse2_data: Dict[str, str],
        text_field: str = 'text'
    ) -> VerseDiff:
        """
        Compare two verses.

        Args:
            verse1_data: First verse dictionary
            verse2_data: Second verse dictionary
            text_field: Field name containing verse text

        Returns:
            VerseDiff object
        """
        text1 = verse1_data.get(text_field, '')
        text2 = verse2_data.get(text_field, '')

        char_diffs = self.compare_strings(text1, text2)

        # Calculate similarity ratio
        similarity = difflib.SequenceMatcher(None, text1, text2).ratio()

        return VerseDiff(
            surah=verse1_data.get('surah', 0),
            verse=verse1_data.get('verse', 0),
            text1=text1,
            text2=text2,
            char_differences=char_diffs,
            similarity_ratio=similarity
        )

    def compare_narrations(
        self,
        narration1_verses: List[Dict],
        narration2_verses: List[Dict],
        text_field: str = 'text'
    ) -> List[VerseDiff]:
        """
        Compare all verses between two narrations.

        Args:
            narration1_verses: List of verse dicts from first narration
            narration2_verses: List of verse dicts from second narration
            text_field: Field name containing verse text

        Returns:
            List of VerseDiff objects (only verses with differences)
        """
        differences = []

        # Match verses by surah:verse reference
        verse_map1 = {(v.get('surah'), v.get('verse')): v for v in narration1_verses}
        verse_map2 = {(v.get('surah'), v.get('verse')): v for v in narration2_verses}

        # Find common verses
        common_refs = set(verse_map1.keys()) & set(verse_map2.keys())

        for ref in sorted(common_refs):
            verse1 = verse_map1[ref]
            verse2 = verse_map2[ref]

            verse_diff = self.compare_verses(verse1, verse2, text_field=text_field)

            # Only include if there are actual differences
            if verse_diff.char_differences:
                differences.append(verse_diff)

        return differences

    def get_similarity_ratio(self, str1: str, str2: str) -> float:
        """
        Calculate similarity ratio between two strings.

        Args:
            str1: First string
            str2: Second string

        Returns:
            Similarity ratio (0.0 to 1.0, where 1.0 is identical)
        """
        return difflib.SequenceMatcher(None, str1, str2).ratio()

    def format_diff(self, char_diff: CharacterDiff) -> str:
        """
        Format a character difference for display.

        Args:
            char_diff: CharacterDiff object

        Returns:
            Formatted string
        """
        return (
            f"Position {char_diff.position}: "
            f"'{char_diff.char1}' -> '{char_diff.char2}' "
            f"(context: ...{char_diff.context_before}[{char_diff.char1}]{char_diff.context_after}...)"
        )
