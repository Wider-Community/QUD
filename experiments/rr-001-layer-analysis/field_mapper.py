#!/usr/bin/env python3
"""
Field-to-Layer Mapping Analyzer

EXPERIMENTAL: Tier 1 research code

Maps QS-QIRAAT fields to QUD layer taxonomy.
"""

from dataclasses import dataclass
from typing import List, Dict, Tuple
from enum import Enum


class LayerCategory(Enum):
    """Layer categories for organization."""
    CHARACTER = "Character Layers (0-2)"
    STRUCTURAL = "Structural Layers (3-8)"
    VARIANT = "Variant Layers (9-10)"
    LAYOUT = "Layout Layers (11-12)"
    META = "Meta Layers (13-14)"
    EXTENDED = "Extended Layers (15-16)"


@dataclass
class LayerMapping:
    """Mapping of a field to one or more layers."""

    field_name: str
    layer_numbers: List[int]
    layer_names: List[str]
    confidence: float  # 0.0 to 1.0
    reasoning: str
    conflation_detected: bool
    category: LayerCategory


class FieldMapper:
    """
    Analyzes QS-QIRAAT schema and maps fields to QUD layers.

    EXPERIMENTAL: Quick research prototype
    """

    # QUD Layer Taxonomy (17 layers)
    LAYER_TAXONOMY = {
        0: "Character Composition",
        1: "Character Symbols",
        2: "Character Paired Data",
        3: "Word Structure",
        4: "Sentence Structure",
        5: "Verse Structure",
        6: "Surah Structure",
        7: "Division Structure",
        8: "Chapter Structure",
        9: "Qiraat/Manuscript",
        10: "Edition Variants",
        11: "Page Layout",
        12: "Line Layout",
        13: "Orthographic Systems",
        14: "Readers/Narrators",
        15: "Layer 15 (TBD)",
        16: "Layer 16 (TBD)"
    }

    def __init__(self):
        """Initialize mapper."""
        self.mappings: List[LayerMapping] = []

    def analyze_field(
        self,
        field_name: str,
        sample_value: any
    ) -> LayerMapping:
        """
        Analyze a single field and map to layers.

        EXPERIMENTAL: Manual analysis encoded as rules
        """

        # Field: id
        if field_name == "id":
            return LayerMapping(
                field_name="id",
                layer_numbers=[5],
                layer_names=["Verse Structure"],
                confidence=1.0,
                reasoning="Verse identifier (surah:verse) maps directly to Layer 5 (Verse Structure)",
                conflation_detected=False,
                category=LayerCategory.STRUCTURAL
            )

        # Field: jozz
        elif field_name == "jozz":
            return LayerMapping(
                field_name="jozz",
                layer_numbers=[7],
                layer_names=["Division Structure"],
                confidence=1.0,
                reasoning="Juz number maps directly to Layer 7 (Division Structure)",
                conflation_detected=False,
                category=LayerCategory.STRUCTURAL
            )

        # Field: page
        elif field_name == "page":
            return LayerMapping(
                field_name="page",
                layer_numbers=[11],
                layer_names=["Page Layout"],
                confidence=1.0,
                reasoning="Page number maps directly to Layer 11 (Page Layout)",
                conflation_detected=False,
                category=LayerCategory.LAYOUT
            )

        # Field: sura_no
        elif field_name == "sura_no":
            return LayerMapping(
                field_name="sura_no",
                layer_numbers=[6],
                layer_names=["Surah Structure"],
                confidence=1.0,
                reasoning="Surah number maps directly to Layer 6 (Surah Structure)",
                conflation_detected=False,
                category=LayerCategory.STRUCTURAL
            )

        # Field: sura_name_en
        elif field_name == "sura_name_en":
            return LayerMapping(
                field_name="sura_name_en",
                layer_numbers=[6],
                layer_names=["Surah Structure"],
                confidence=1.0,
                reasoning="Surah name (English) maps to Layer 6 (Surah Structure)",
                conflation_detected=False,
                category=LayerCategory.STRUCTURAL
            )

        # Field: sura_name_ar
        elif field_name == "sura_name_ar":
            return LayerMapping(
                field_name="sura_name_ar",
                layer_numbers=[6, 1],
                layer_names=["Surah Structure", "Character Symbols"],
                confidence=0.9,
                reasoning="Surah name (Arabic) primarily maps to Layer 6, but also includes Layer 1 (Character Symbols) due to Arabic text encoding",
                conflation_detected=True,
                category=LayerCategory.STRUCTURAL
            )

        # Field: line_start
        elif field_name == "line_start":
            return LayerMapping(
                field_name="line_start",
                layer_numbers=[12],
                layer_names=["Line Layout"],
                confidence=1.0,
                reasoning="Starting line number maps directly to Layer 12 (Line Layout)",
                conflation_detected=False,
                category=LayerCategory.LAYOUT
            )

        # Field: line_end
        elif field_name == "line_end":
            return LayerMapping(
                field_name="line_end",
                layer_numbers=[12],
                layer_names=["Line Layout"],
                confidence=1.0,
                reasoning="Ending line number maps directly to Layer 12 (Line Layout)",
                conflation_detected=False,
                category=LayerCategory.LAYOUT
            )

        # Field: aya_no
        elif field_name == "aya_no":
            return LayerMapping(
                field_name="aya_no",
                layer_numbers=[5],
                layer_names=["Verse Structure"],
                confidence=1.0,
                reasoning="Verse number within surah maps directly to Layer 5 (Verse Structure)",
                conflation_detected=False,
                category=LayerCategory.STRUCTURAL
            )

        # Field: aya_text
        elif field_name == "aya_text":
            return LayerMapping(
                field_name="aya_text",
                layer_numbers=[0, 1, 2, 3, 4, 5, 9, 10, 13],
                layer_names=[
                    "Character Composition",
                    "Character Symbols",
                    "Character Paired Data",
                    "Word Structure",
                    "Sentence Structure",
                    "Verse Structure",
                    "Qiraat/Manuscript",
                    "Edition Variants",
                    "Orthographic Systems"
                ],
                confidence=1.0,
                reasoning="Full verse text conflates 9 layers: character composition/symbols/paired data, word/sentence/verse structure, qiraat variants, edition differences, and orthography. This is the PRIMARY CONFLATION POINT.",
                conflation_detected=True,
                category=LayerCategory.CHARACTER
            )

        # Field: aya_text_emlaey
        elif field_name == "aya_text_emlaey":
            return LayerMapping(
                field_name="aya_text_emlaey",
                layer_numbers=[0, 1, 3, 4, 5, 10, 13],
                layer_names=[
                    "Character Composition",
                    "Character Symbols",
                    "Word Structure",
                    "Sentence Structure",
                    "Verse Structure",
                    "Edition Variants",
                    "Orthographic Systems"
                ],
                confidence=0.9,
                reasoning="Simplified text (modern orthography) conflates 7 layers: character composition/symbols, word/sentence/verse structure, edition variants, and orthographic normalization. Differs from aya_text by removing diacriticals (Layer 2) but adds orthographic normalization.",
                conflation_detected=True,
                category=LayerCategory.CHARACTER
            )

        # Unknown field
        else:
            return LayerMapping(
                field_name=field_name,
                layer_numbers=[],
                layer_names=[],
                confidence=0.0,
                reasoning=f"Unknown field: {field_name}",
                conflation_detected=False,
                category=LayerCategory.EXTENDED
            )

    def analyze_schema(self, sample_record: Dict) -> List[LayerMapping]:
        """
        Analyze complete QS-QIRAAT schema.

        Args:
            sample_record: Sample verse record with all fields

        Returns:
            List of LayerMapping objects
        """
        self.mappings = []

        for field_name, field_value in sample_record.items():
            mapping = self.analyze_field(field_name, field_value)
            self.mappings.append(mapping)

        return self.mappings

    def get_conflated_fields(self) -> List[LayerMapping]:
        """Get fields that conflate multiple layers."""
        return [m for m in self.mappings if m.conflation_detected]

    def get_layer_coverage(self) -> Dict[int, List[str]]:
        """
        Get which fields cover each layer.

        Returns:
            Dict of layer_number -> list of field names
        """
        coverage = {i: [] for i in range(17)}

        for mapping in self.mappings:
            for layer_num in mapping.layer_numbers:
                coverage[layer_num].append(mapping.field_name)

        return coverage

    def get_missing_layers(self) -> List[Tuple[int, str]]:
        """
        Get layers not represented in QS-QIRAAT schema.

        Returns:
            List of (layer_number, layer_name) tuples
        """
        coverage = self.get_layer_coverage()
        missing = []

        for layer_num in range(17):
            if not coverage[layer_num]:
                missing.append((layer_num, self.LAYER_TAXONOMY[layer_num]))

        return missing

    def print_summary(self):
        """Print analysis summary."""
        print("=" * 80)
        print("FIELD-TO-LAYER MAPPING ANALYSIS")
        print("=" * 80)
        print()

        print(f"Total fields analyzed: {len(self.mappings)}")
        print(f"Fields with conflation: {len(self.get_conflated_fields())}")
        print()

        print("-" * 80)
        print("FIELD MAPPINGS")
        print("-" * 80)

        for mapping in self.mappings:
            status = "⚠️  CONFLATED" if mapping.conflation_detected else "✓ Clean"
            print(f"\n{mapping.field_name} [{status}] (confidence: {mapping.confidence:.1f})")
            print(f"  Layers: {mapping.layer_numbers}")
            print(f"  Names: {mapping.layer_names}")
            print(f"  Reasoning: {mapping.reasoning}")

        print()
        print("-" * 80)
        print("MISSING LAYERS")
        print("-" * 80)

        missing = self.get_missing_layers()
        if missing:
            for layer_num, layer_name in missing:
                print(f"  Layer {layer_num}: {layer_name}")
        else:
            print("  None - all layers represented")

        print()
        print("=" * 80)


def main():
    """Run field mapping analysis."""

    # Sample QS-QIRAAT record
    sample_record = {
        "id": "1:1",
        "jozz": 1,
        "page": 1,
        "sura_no": 1,
        "sura_name_en": "Al-Fatihah",
        "sura_name_ar": "الفاتحة",
        "line_start": 1,
        "line_end": 1,
        "aya_no": 1,
        "aya_text": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
        "aya_text_emlaey": "بسم الله الرحمن الرحيم"
    }

    mapper = FieldMapper()
    mappings = mapper.analyze_schema(sample_record)

    mapper.print_summary()

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
