"""
Quran Data Loader

Tier 2 (Reusable Research Tool)

Loads Quranic data from various sources (JSON, CSV) with support for
multiple Qiraat and Narrations.
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Union
from dataclasses import dataclass


@dataclass
class QuranContext:
    """Context information for Quranic data."""

    qiraat: str
    narration: str
    edition: Optional[str] = None
    manuscript: Optional[str] = None

    def __str__(self) -> str:
        return f"{self.qiraat} ({self.narration})"


class QuranLoader:
    """
    Load Quranic data from various sources.

    Supports:
    - JSON format (QS-QIRAAT dataset structure)
    - CSV format (for validation)
    - Multiple Qiraat/Narrations
    """

    def __init__(self, data_dir: Optional[Path] = None):
        """
        Initialize loader.

        Args:
            data_dir: Base directory for data files. If None, uses current directory.
        """
        self.data_dir = Path(data_dir) if data_dir else Path.cwd()

    def load_json(
        self,
        file_path: Union[str, Path],
        context: Optional[QuranContext] = None
    ) -> Dict:
        """
        Load Quranic data from JSON file.

        Args:
            file_path: Path to JSON file (absolute or relative to data_dir)
            context: Optional context information to attach to loaded data

        Returns:
            Dictionary containing loaded data with context metadata

        Raises:
            FileNotFoundError: If file doesn't exist
            json.JSONDecodeError: If JSON is malformed
        """
        path = Path(file_path)
        if not path.is_absolute():
            path = self.data_dir / path

        if not path.exists():
            raise FileNotFoundError(f"Data file not found: {path}")

        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Attach context metadata if provided
        if context:
            data['_context'] = {
                'qiraat': context.qiraat,
                'narration': context.narration,
                'edition': context.edition,
                'manuscript': context.manuscript
            }

        return data

    def load_qiraat_dataset(
        self,
        qiraat: str,
        narration: str,
        edition: Optional[str] = None
    ) -> Dict:
        """
        Load QS-QIRAAT dataset for specific Qiraat and Narration.

        Args:
            qiraat: Qiraat name (e.g., "Asim", "Nafi")
            narration: Narration name (e.g., "Hafs", "Warsh")
            edition: Optional edition identifier

        Returns:
            Dictionary containing Quranic data with context

        Example:
            >>> loader = QuranLoader(data_dir=Path("data"))
            >>> hafs_data = loader.load_qiraat_dataset("Asim", "Hafs")
        """
        context = QuranContext(
            qiraat=qiraat,
            narration=narration,
            edition=edition
        )

        # Expected file naming convention: {qiraat}_{narration}.json
        filename = f"{qiraat.lower()}_{narration.lower()}.json"

        try:
            return self.load_json(filename, context=context)
        except FileNotFoundError:
            # Try alternate naming convention
            filename = f"{narration.lower()}.json"
            return self.load_json(filename, context=context)

    def get_verses(self, data: Dict, surah: int, verse: Optional[int] = None) -> Union[List, Dict]:
        """
        Extract verse(s) from loaded data.

        Args:
            data: Loaded Quran data
            surah: Surah number (1-114)
            verse: Optional verse number. If None, returns all verses in surah.

        Returns:
            Single verse dict if verse specified, otherwise list of verses
        """
        # This is a placeholder - actual implementation depends on QS-QIRAAT schema
        # Will be refined based on actual data structure

        if 'surahs' in data:
            surah_data = next((s for s in data['surahs'] if s['number'] == surah), None)
            if not surah_data:
                raise ValueError(f"Surah {surah} not found")

            if verse is None:
                return surah_data.get('verses', [])
            else:
                verse_data = next((v for v in surah_data['verses'] if v['number'] == verse), None)
                if not verse_data:
                    raise ValueError(f"Verse {surah}:{verse} not found")
                return verse_data

        raise ValueError("Unexpected data format")

    def get_text(self, verse_data: Dict) -> str:
        """
        Extract text from verse data.

        Args:
            verse_data: Verse dictionary

        Returns:
            Verse text string
        """
        # Flexible extraction - try multiple common field names
        for field in ['text', 'verse_text', 'content', 'ayah']:
            if field in verse_data:
                return verse_data[field]

        raise ValueError("No text field found in verse data")
