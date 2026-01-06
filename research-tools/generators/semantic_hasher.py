"""
Semantic Hash Generator

Tier 2 (Reusable Research Tool)

Generates semantic hashes for relationship representation using SHA-256.
"""

import hashlib
from typing import Any, Dict, List


class SemanticHasher:
    """
    Generate semantic hashes for Quranic data relationships.

    Uses SHA-256 for stable, reproducible hashes.
    """

    def __init__(self):
        """Initialize hasher."""
        pass

    def hash_string(self, data: str) -> str:
        """
        Generate SHA-256 hash of string.

        Args:
            data: Input string

        Returns:
            Hex-encoded hash
        """
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def hash_dict(self, data: Dict[str, Any]) -> str:
        """
        Generate SHA-256 hash of dictionary.

        Args:
            data: Input dictionary

        Returns:
            Hex-encoded hash

        Note:
            Dictionary is sorted by keys before hashing to ensure consistency
        """
        import json

        # Sort keys for deterministic hashing
        normalized = json.dumps(data, sort_keys=True, ensure_ascii=False)
        return self.hash_string(normalized)

    def hash_relationship(
        self,
        source_id: str,
        target_id: str,
        relationship_type: str
    ) -> str:
        """
        Generate hash for a relationship between entities.

        Args:
            source_id: Source entity UUID
            target_id: Target entity UUID
            relationship_type: Type of relationship (e.g., "contains", "follows")

        Returns:
            Hex-encoded hash
        """
        relationship_str = f"{source_id}:{relationship_type}:{target_id}"
        return self.hash_string(relationship_str)

    def hash_layer_data(
        self,
        layer_name: str,
        entity_id: str,
        data: Dict[str, Any]
    ) -> str:
        """
        Generate hash for layer data.

        Args:
            layer_name: Layer name (e.g., "layer-00-character-composition")
            entity_id: Entity UUID
            data: Layer-specific data

        Returns:
            Hex-encoded hash
        """
        composite = {
            "layer": layer_name,
            "entity_id": entity_id,
            "data": data
        }
        return self.hash_dict(composite)

    def verify_hash(self, data: str, expected_hash: str) -> bool:
        """
        Verify data against expected hash.

        Args:
            data: Input data
            expected_hash: Expected hash value

        Returns:
            True if hash matches
        """
        actual_hash = self.hash_string(data)
        return actual_hash == expected_hash
