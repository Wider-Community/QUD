"""
CSV Data Loader

Tier 2 (Reusable Research Tool)

Loads Quranic data from CSV format for validation purposes.
"""

import csv
from pathlib import Path
from typing import Dict, List, Optional, Union


class CSVLoader:
    """
    Load Quranic data from CSV files.

    Primarily used for validation against authoritative sources.
    """

    def __init__(self, data_dir: Optional[Path] = None):
        """
        Initialize loader.

        Args:
            data_dir: Base directory for CSV files. If None, uses current directory.
        """
        self.data_dir = Path(data_dir) if data_dir else Path.cwd()

    def load_csv(
        self,
        file_path: Union[str, Path],
        encoding: str = 'utf-8'
    ) -> List[Dict[str, str]]:
        """
        Load CSV file and return as list of dictionaries.

        Args:
            file_path: Path to CSV file (absolute or relative to data_dir)
            encoding: File encoding (default: utf-8)

        Returns:
            List of dictionaries, one per row

        Raises:
            FileNotFoundError: If file doesn't exist
        """
        path = Path(file_path)
        if not path.is_absolute():
            path = self.data_dir / path

        if not path.exists():
            raise FileNotFoundError(f"CSV file not found: {path}")

        with open(path, 'r', encoding=encoding) as f:
            reader = csv.DictReader(f)
            return list(reader)

    def load_layer_data(
        self,
        file_path: Union[str, Path],
        layer_name: str
    ) -> List[Dict[str, str]]:
        """
        Load CSV data for a specific layer.

        Args:
            file_path: Path to CSV file
            layer_name: Name of the layer (for metadata)

        Returns:
            List of dictionaries with layer metadata attached
        """
        data = self.load_csv(file_path)

        # Attach layer metadata to each row
        for row in data:
            row['_layer'] = layer_name

        return data

    def validate_required_columns(
        self,
        data: List[Dict[str, str]],
        required_columns: List[str]
    ) -> bool:
        """
        Validate that all required columns are present.

        Args:
            data: Loaded CSV data
            required_columns: List of required column names

        Returns:
            True if all required columns present

        Raises:
            ValueError: If required columns are missing
        """
        if not data:
            raise ValueError("Empty dataset")

        actual_columns = set(data[0].keys())
        required_set = set(required_columns)

        missing = required_set - actual_columns
        if missing:
            raise ValueError(f"Missing required columns: {missing}")

        return True
