"""
UUID Generator

Tier 2 (Reusable Research Tool)

Generates UUIDs for cross-layer entity mapping.

Supports:
- v4 (random) for unique entity IDs
- v5 (name-based) for deterministic IDs from content
"""

import uuid
from typing import Optional


# Namespace UUIDs for different entity types
NAMESPACE_CHARACTER = uuid.UUID('6ba7b810-9dad-11d1-80b4-00c04fd430c8')  # DNS namespace placeholder
NAMESPACE_WORD = uuid.UUID('6ba7b811-9dad-11d1-80b4-00c04fd430c8')
NAMESPACE_VERSE = uuid.UUID('6ba7b812-9dad-11d1-80b4-00c04fd430c8')
NAMESPACE_SURAH = uuid.UUID('6ba7b813-9dad-11d1-80b4-00c04fd430c8')


class UUIDGenerator:
    """
    Generate UUIDs for Quranic entities.

    Provides both random (v4) and deterministic (v5) UUID generation.
    """

    def __init__(self):
        """Initialize UUID generator."""
        pass

    def generate_v4(self) -> str:
        """
        Generate random UUID (v4).

        Returns:
            UUID string

        Use case: Unique IDs for entities without content-based identity
        """
        return str(uuid.uuid4())

    def generate_v5(
        self,
        name: str,
        namespace: Optional[uuid.UUID] = None
    ) -> str:
        """
        Generate deterministic UUID (v5) from name.

        Args:
            name: Input name/content
            namespace: UUID namespace (default: DNS namespace)

        Returns:
            UUID string

        Use case: Deterministic IDs based on content (e.g., verse text generates same UUID)
        """
        if namespace is None:
            namespace = uuid.NAMESPACE_DNS

        return str(uuid.uuid5(namespace, name))

    def generate_character_uuid(
        self,
        character: str,
        position: int,
        context: Optional[str] = None
    ) -> str:
        """
        Generate UUID for a character entity.

        Args:
            character: Character
            position: Position in text (global index)
            context: Optional context string (e.g., "Hafs-1:1")

        Returns:
            UUID string
        """
        name = f"char:{character}:pos:{position}"
        if context:
            name += f":ctx:{context}"

        return self.generate_v5(name, namespace=NAMESPACE_CHARACTER)

    def generate_word_uuid(
        self,
        word: str,
        surah: int,
        verse: int,
        word_index: int,
        context: Optional[str] = None
    ) -> str:
        """
        Generate UUID for a word entity.

        Args:
            word: Word text
            surah: Surah number
            verse: Verse number
            word_index: Word index within verse
            context: Optional context string (e.g., "Hafs")

        Returns:
            UUID string
        """
        name = f"word:{word}:ref:{surah}:{verse}:{word_index}"
        if context:
            name += f":ctx:{context}"

        return self.generate_v5(name, namespace=NAMESPACE_WORD)

    def generate_verse_uuid(
        self,
        surah: int,
        verse: int,
        context: Optional[str] = None
    ) -> str:
        """
        Generate UUID for a verse entity.

        Args:
            surah: Surah number
            verse: Verse number
            context: Optional context string (e.g., "Hafs")

        Returns:
            UUID string
        """
        name = f"verse:{surah}:{verse}"
        if context:
            name += f":ctx:{context}"

        return self.generate_v5(name, namespace=NAMESPACE_VERSE)

    def generate_surah_uuid(
        self,
        surah: int,
        context: Optional[str] = None
    ) -> str:
        """
        Generate UUID for a surah entity.

        Args:
            surah: Surah number
            context: Optional context string (e.g., "Hafs")

        Returns:
            UUID string
        """
        name = f"surah:{surah}"
        if context:
            name += f":ctx:{context}"

        return self.generate_v5(name, namespace=NAMESPACE_SURAH)
