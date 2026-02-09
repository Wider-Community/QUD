"""SYM: Character Symbols — Pydantic models.

Diacritics, extensions, tajweed marks, and tatweel
for base characters in the Quranic text.

Split into two concerns:
- Symbol catalog: reference data for ~24 symbol types (discriminated union)
- Symbol instance: lean per-character records with FK to catalog

Note: Stop signs are excluded from SYM — they belong at word/sentence level
in SNT (Sentence Structure), not as letter-level modifications.
"""

from __future__ import annotations

from enum import StrEnum, auto
from typing import Annotated, Literal, Union
from uuid import UUID

from pydantic import BaseModel, Field


# ── subcategory enums ────────────────────────────────────────────

class DiacriticSub(StrEnum):
    HARAKA = auto()
    TANWEEN_CLOSED = auto()
    TANWEEN_OPEN = auto()
    SUKUN = auto()
    SHADDA = auto()


class ExtensionSub(StrEnum):
    DAGGER_ALEF = auto()
    SMALL_WAW = auto()
    SMALL_YAA = auto()
    SMALL_HIGH_YAA = auto()


class TajweedSub(StrEnum):
    MADDAH = auto()
    IQLAB_ABOVE = auto()
    IQLAB_BELOW = auto()
    SILENT_ALEF = auto()
    SILENT_VOWEL = auto()
    IMALA = auto()
    ISHMAM_TASHEEL = auto()
    SMALL_NOON = auto()
    SMALL_SEEN = auto()


class TatweelSub(StrEnum):
    TATWEEL = auto()


# ── catalog entry models ────────────────────────────────────────

class _CatalogBase(BaseModel):
    symbol_codepoint: str = Field(
        pattern=r"^U\+[0-9A-F]{4,6}$",
        description="Unicode codepoint — primary key (e.g., U+064E)",
    )
    symbol_name: str = Field(
        description="Human-readable name (e.g., Fatha, Maddah, Dagger Alef)"
    )
    symbol_char: str = Field(
        description="The actual Unicode character"
    )
    unicode_name: str = Field(
        description="Official Unicode character name"
    )
    narration_specific: bool = Field(
        default=False,
        description="Whether this symbol varies by narration",
    )


class DiacriticCatalogEntry(_CatalogBase):
    category: Literal["diacritic"] = "diacritic"
    subcategory: DiacriticSub


class ExtensionCatalogEntry(_CatalogBase):
    category: Literal["extension"] = "extension"
    subcategory: ExtensionSub


class TajweedCatalogEntry(_CatalogBase):
    category: Literal["tajweed"] = "tajweed"
    subcategory: TajweedSub


class TatweelCatalogEntry(_CatalogBase):
    category: Literal["tatweel"] = "tatweel"
    subcategory: TatweelSub


SymbolCatalogEntry = Annotated[
    Union[
        DiacriticCatalogEntry,
        ExtensionCatalogEntry,
        TajweedCatalogEntry,
        TatweelCatalogEntry,
    ],
    Field(discriminator="category"),
]


# ── instance model ──────────────────────────────────────────────

class SymbolInstance(BaseModel):
    symbol_id: UUID = Field(
        description="Unique identifier for this symbol instance (UUID v5)"
    )
    character_ref: UUID = Field(
        description="Foreign key to CHR — the base letter this symbol modifies"
    )
    symbol_codepoint: str = Field(
        pattern=r"^U\+[0-9A-F]{4,6}$",
        description="Unicode codepoint — foreign key to symbol catalog",
    )
