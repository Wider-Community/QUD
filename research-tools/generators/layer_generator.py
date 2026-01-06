"""
Layer Generator Framework

Tier 2 (Reusable Research Tool)

Base framework for generating layer data.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List, Optional
from dataclasses import dataclass


@dataclass
class LayerMetadata:
    """Metadata for a generated layer."""

    layer_name: str
    layer_number: int
    qiraat: str
    narration: str
    edition: Optional[str]
    generated_at: str  # ISO format timestamp
    entity_count: int
    dependencies: List[str]  # List of layer names this depends on


class LayerGenerator(ABC):
    """
    Abstract base class for layer generators.

    Each layer implements this interface to generate its data.
    """

    def __init__(
        self,
        layer_name: str,
        layer_number: int,
        output_dir: Optional[Path] = None
    ):
        """
        Initialize generator.

        Args:
            layer_name: Layer name (e.g., "character-composition")
            layer_number: Layer number (e.g., 0)
            output_dir: Output directory for generated data
        """
        self.layer_name = layer_name
        self.layer_number = layer_number
        self.output_dir = Path(output_dir) if output_dir else Path.cwd() / "output"
        self.metadata: Optional[LayerMetadata] = None

    @abstractmethod
    def generate(
        self,
        source_data: Any,
        context: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        Generate layer data from source.

        Args:
            source_data: Input data (format depends on layer)
            context: Context dict with qiraat, narration, edition

        Returns:
            Generated layer data dictionary
        """
        pass

    @abstractmethod
    def validate(self, layer_data: Dict[str, Any]) -> bool:
        """
        Validate generated layer data.

        Args:
            layer_data: Generated data to validate

        Returns:
            True if valid

        Raises:
            ValueError: If validation fails
        """
        pass

    @abstractmethod
    def get_dependencies(self) -> List[str]:
        """
        Get list of layer dependencies.

        Returns:
            List of layer names this layer depends on (empty if no dependencies)
        """
        pass

    def save(self, layer_data: Dict[str, Any], filename: Optional[str] = None) -> Path:
        """
        Save generated layer data to file.

        Args:
            layer_data: Generated data
            filename: Optional custom filename (default: {layer_name}.json)

        Returns:
            Path to saved file
        """
        import json
        from datetime import datetime

        if filename is None:
            filename = f"layer-{self.layer_number:02d}-{self.layer_name}.json"

        output_path = self.output_dir / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Add metadata
        output_data = {
            "metadata": {
                "layer_name": self.layer_name,
                "layer_number": self.layer_number,
                "generated_at": datetime.utcnow().isoformat(),
                "entity_count": len(layer_data.get("entities", []))
            },
            "data": layer_data
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)

        return output_path
