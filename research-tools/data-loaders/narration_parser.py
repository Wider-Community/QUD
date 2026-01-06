"""
Narration Parser

Tier 2 (Reusable Research Tool)

Parses Qiraat-specific data with awareness of canonical narrations.
Handles the mapping between 10 Qiraat and 20 Narrations.
"""

from typing import Dict, List, Optional, Set
from dataclasses import dataclass


# Canonical Qiraat and their narrations (10 Qiraat, 20 Narrations)
CANONICAL_QIRAAT: Dict[str, List[str]] = {
    "Nafi": ["Warsh", "Qalun"],
    "Ibn Kathir": ["Al-Bazzi", "Qunbul"],
    "Abu Amr": ["Ad-Duri", "As-Susi"],
    "Ibn Amir": ["Hisham", "Ibn Dhakwan"],
    "Asim": ["Hafs", "Shu'bah"],
    "Hamzah": ["Khalaf", "Khallad"],
    "Al-Kisai": ["Abu al-Harith", "Ad-Duri"],
    "Abu Jafar": ["Ibn Wardan", "Ibn Jammaz"],
    "Yaqub": ["Ruways", "Rawh"],
    "Khalaf": ["Ishaq", "Idris"]
}


@dataclass
class NarrationInfo:
    """Information about a specific narration."""

    qiraat: str
    narration: str
    is_canonical: bool
    narration_index: int  # Which narration of this Qiraat (1 or 2)

    def __str__(self) -> str:
        return f"{self.qiraat} - {self.narration}"


class NarrationParser:
    """
    Parse and validate Qiraat/Narration information.

    Provides utilities for:
    - Validating canonical Qiraat and Narrations
    - Mapping between Qiraat and Narrations
    - Identifying narration-specific data
    """

    def __init__(self):
        """Initialize parser with canonical Qiraat data."""
        self.qiraat_map = CANONICAL_QIRAAT

        # Build reverse mapping: narration -> qiraat
        self.narration_to_qiraat = {}
        for qiraat, narrations in CANONICAL_QIRAAT.items():
            for narration in narrations:
                self.narration_to_qiraat[narration] = qiraat

    def is_canonical_qiraat(self, qiraat: str) -> bool:
        """Check if a Qiraat is one of the 10 canonical readings."""
        return qiraat in self.qiraat_map

    def is_canonical_narration(self, narration: str) -> bool:
        """Check if a Narration is one of the 20 canonical transmissions."""
        return narration in self.narration_to_qiraat

    def get_qiraat_for_narration(self, narration: str) -> Optional[str]:
        """
        Get the Qiraat for a given Narration.

        Args:
            narration: Narration name

        Returns:
            Qiraat name, or None if not canonical
        """
        return self.narration_to_qiraat.get(narration)

    def get_narrations_for_qiraat(self, qiraat: str) -> Optional[List[str]]:
        """
        Get all Narrations for a given Qiraat.

        Args:
            qiraat: Qiraat name

        Returns:
            List of Narration names, or None if not canonical
        """
        return self.qiraat_map.get(qiraat)

    def get_narration_info(self, qiraat: str, narration: str) -> NarrationInfo:
        """
        Get detailed information about a Qiraat/Narration pair.

        Args:
            qiraat: Qiraat name
            narration: Narration name

        Returns:
            NarrationInfo object

        Raises:
            ValueError: If combination is invalid
        """
        if not self.is_canonical_qiraat(qiraat):
            raise ValueError(f"Non-canonical Qiraat: {qiraat}")

        if not self.is_canonical_narration(narration):
            raise ValueError(f"Non-canonical Narration: {narration}")

        expected_qiraat = self.get_qiraat_for_narration(narration)
        if expected_qiraat != qiraat:
            raise ValueError(
                f"Invalid combination: {narration} belongs to {expected_qiraat}, not {qiraat}"
            )

        narrations = self.get_narrations_for_qiraat(qiraat)
        narration_index = narrations.index(narration) + 1

        return NarrationInfo(
            qiraat=qiraat,
            narration=narration,
            is_canonical=True,
            narration_index=narration_index
        )

    def get_all_canonical_pairs(self) -> List[tuple[str, str]]:
        """
        Get all 20 canonical (Qiraat, Narration) pairs.

        Returns:
            List of tuples (qiraat, narration)
        """
        pairs = []
        for qiraat, narrations in self.qiraat_map.items():
            for narration in narrations:
                pairs.append((qiraat, narration))
        return pairs

    def get_phase1_narrations(self) -> List[tuple[str, str]]:
        """
        Get Phase 1 focus narrations: Hafs and Warsh.

        Returns:
            List of tuples: [("Asim", "Hafs"), ("Nafi", "Warsh")]
        """
        return [
            ("Asim", "Hafs"),
            ("Nafi", "Warsh")
        ]

    def validate_context(self, qiraat: str, narration: str) -> bool:
        """
        Validate a Qiraat/Narration context.

        Args:
            qiraat: Qiraat name
            narration: Narration name

        Returns:
            True if valid combination, False otherwise
        """
        try:
            self.get_narration_info(qiraat, narration)
            return True
        except ValueError:
            return False
