"""
Context Validator

Tier 2 (Reusable Research Tool)

Validates contextual versioning parameters (Qiraat, Narration, Edition, Manuscript).
"""

from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass


@dataclass
class ValidationResult:
    """Result of context validation."""

    is_valid: bool
    errors: List[str]
    warnings: List[str]

    def __bool__(self) -> bool:
        return self.is_valid


class ContextValidator:
    """
    Validate contextual versioning parameters.

    Ensures valid combinations of:
    - Qiraat (10 canonical)
    - Narration (20 canonical)
    - Edition (King Fahd Complex, Dar Al-Maarifah, etc.)
    - Manuscript (optional historical sources)
    """

    # Valid Qiraat-Narration mappings
    VALID_NARRATIONS = {
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

    # Known editions (can be extended)
    KNOWN_EDITIONS = {
        "King Fahd Complex",
        "Dar Al-Maarifah",
        "Al-Azhar",
        "Medina Mushaf"
    }

    def __init__(self, strict: bool = True):
        """
        Initialize validator.

        Args:
            strict: If True, treat warnings as errors
        """
        self.strict = strict

    def validate_qiraat(self, qiraat: str) -> ValidationResult:
        """
        Validate Qiraat parameter.

        Args:
            qiraat: Qiraat name

        Returns:
            ValidationResult
        """
        errors = []
        warnings = []

        if not qiraat:
            errors.append("Qiraat cannot be empty")
        elif qiraat not in self.VALID_NARRATIONS:
            errors.append(f"Unknown Qiraat: {qiraat}")

        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )

    def validate_narration(
        self,
        narration: str,
        qiraat: Optional[str] = None
    ) -> ValidationResult:
        """
        Validate Narration parameter.

        Args:
            narration: Narration name
            qiraat: Optional Qiraat to validate against

        Returns:
            ValidationResult
        """
        errors = []
        warnings = []

        if not narration:
            errors.append("Narration cannot be empty")
            return ValidationResult(is_valid=False, errors=errors, warnings=warnings)

        # Find which Qiraat this narration belongs to
        valid_qiraats = [q for q, narrs in self.VALID_NARRATIONS.items() if narration in narrs]

        if not valid_qiraats:
            errors.append(f"Unknown Narration: {narration}")
        elif qiraat and qiraat not in valid_qiraats:
            errors.append(
                f"Invalid combination: {narration} belongs to {valid_qiraats}, not {qiraat}"
            )

        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )

    def validate_edition(self, edition: Optional[str]) -> ValidationResult:
        """
        Validate Edition parameter.

        Args:
            edition: Edition name (can be None)

        Returns:
            ValidationResult
        """
        errors = []
        warnings = []

        if edition and edition not in self.KNOWN_EDITIONS:
            warnings.append(f"Unknown edition: {edition} (not in known editions list)")

        return ValidationResult(
            is_valid=len(errors) == 0 and (not self.strict or len(warnings) == 0),
            errors=errors,
            warnings=warnings
        )

    def validate_context(
        self,
        qiraat: str,
        narration: str,
        edition: Optional[str] = None,
        manuscript: Optional[str] = None
    ) -> ValidationResult:
        """
        Validate complete context parameters.

        Args:
            qiraat: Qiraat name
            narration: Narration name
            edition: Optional edition name
            manuscript: Optional manuscript identifier

        Returns:
            ValidationResult with aggregated errors/warnings
        """
        all_errors = []
        all_warnings = []

        # Validate Qiraat
        qiraat_result = self.validate_qiraat(qiraat)
        all_errors.extend(qiraat_result.errors)
        all_warnings.extend(qiraat_result.warnings)

        # Validate Narration (with Qiraat cross-check)
        narration_result = self.validate_narration(narration, qiraat=qiraat)
        all_errors.extend(narration_result.errors)
        all_warnings.extend(narration_result.warnings)

        # Validate Edition
        edition_result = self.validate_edition(edition)
        all_errors.extend(edition_result.errors)
        all_warnings.extend(edition_result.warnings)

        # Manuscript validation (placeholder - no specific rules yet)
        if manuscript:
            all_warnings.append(f"Manuscript specified: {manuscript} (not validated)")

        return ValidationResult(
            is_valid=len(all_errors) == 0 and (not self.strict or len(all_warnings) == 0),
            errors=all_errors,
            warnings=all_warnings
        )

    def get_valid_narrations(self, qiraat: str) -> Optional[List[str]]:
        """
        Get valid narrations for a given Qiraat.

        Args:
            qiraat: Qiraat name

        Returns:
            List of valid narrations, or None if Qiraat unknown
        """
        return self.VALID_NARRATIONS.get(qiraat)
