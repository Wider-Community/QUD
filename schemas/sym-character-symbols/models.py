"""SYM: Character Symbols — Pydantic models.

Diacritics, extensions, stop signs, tajweed marks, and tatweel
for base characters in the Quranic text.

Split into two concerns:
- Symbol catalog: reference data for ~30 symbol types (discriminated union)
- Symbol instance: lean per-character records with FK to catalog
"""

from __future__ import annotations

from enum import Enum
from typing import Annotated, Literal, Union
from uuid import UUID

from pydantic import BaseModel, Field


# ── subcategory enums ────────────────────────────────────────────

class DiacriticSub(str, Enum):
    haraka = "haraka"
    tanween_closed = "tanween_closed"
    tanween_open = "tanween_open"
    sukun = "sukun"
    shadda = "shadda"


class ExtensionSub(str, Enum):
    dagger_alef = "dagger_alef"
    small_waw = "small_waw"
    small_yaa = "small_yaa"
    small_high_yaa = "small_high_yaa"


class StopSignSub(str, Enum):
    sili = "sili"
    qili = "qili"
    lazim = "lazim"
    jaiz = "jaiz"
    either_of = "either_of"
    seen_sakt = "seen_sakt"


class TajweedSub(str, Enum):
    maddah = "maddah"
    iqlab_above = "iqlab_above"
    iqlab_below = "iqlab_below"
    silent_alef = "silent_alef"
    silent_vowel = "silent_vowel"
    imala = "imala"
    ishmam_tasheel = "ishmam_tasheel"
    small_noon = "small_noon"
    small_seen = "small_seen"


class TatweelSub(str, Enum):
    tatweel = "tatweel"


# ── catalog entry models ────────────────────────────────────────

class _CatalogBase(BaseModel):
    symbol_codepoint: str = Field(
        pattern=r"^U\+[0-9A-F]{4,6}$",
        description="Unicode codepoint — primary key (e.g., U+064E)",
    )
    symbol_name: str = Field(
        description="Human-readable name (e.g., Fatha, Sili, Maddah)"
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


class StopSignCatalogEntry(_CatalogBase):
    category: Literal["stop_sign"] = "stop_sign"
    subcategory: StopSignSub


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
        StopSignCatalogEntry,
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
