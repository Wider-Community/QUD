"""
QUD UUID Generator

Tier 2 (Reusable Research Tool)

Generates deterministic UUIDs (v5) for all Quranic entities using a consistent
naming convention. Each entity type has a dedicated function that enforces
valid parameter combinations.

Naming Conventions:
    Universal:   s{surah}
    Structural:  {narration}:s{surah}:v{verse}:w{word}:c{char}:sym{symbol}
    Layout:      {narration}:{edition}:p{page}:l{line}
    Division:    {narration}:j{juz} | h{hizb} | r{rub}
    Metadata:    qir:{name} | edn:{publisher}:{name} | rdr:{name} | msh:{narration}:{edition}

Examples:
    surah_id(2)                              → Surah 2 (universal)
    verse_id("hafs", 2, 255)                 → Hafs, Surah 2, Verse 255
    word_id("hafs", 2, 255, 4)               → Word 4 in that verse
    char_id("hafs", 2, 255, 4, 2)            → Character 2 in that word
    symbol_id("hafs", 2, 255, 4, 2, 1)       → Symbol 1 on that character
    page_id("hafs", "kfgqpc_v2", 42)         → Page 42 in Hafs King Fahd edition
    line_id("hafs", "kfgqpc_v2", 42, 7)      → Line 7 on that page
    juz_id("hafs", 15)                       → Juz 15
    hizb_id("hafs", 30)                      → Hizb 30 (global, 1-60)
    rub_id("hafs", 120)                      → Rub 120 (global, 1-240)
    narration_id("hafs")                     → Hafs narration metadata
    edition_id("kfgqpc", "hafs_v2")          → King Fahd Hafs v2.0 edition
    reader_id("hafs")                        → Hafs biographical data
    mushaf_id("hafs", "kfgqpc_v2")           → Complete mushaf instance
"""

import uuid
from typing import Optional


# =============================================================================
# NAMESPACE
# =============================================================================

QUD_NAMESPACE = uuid.uuid5(uuid.NAMESPACE_URL, "qud.itqan.community")


# =============================================================================
# VALID COMBINATIONS REGISTRY
# =============================================================================

VALID_PATTERNS = {
    # Universal (same across all narrations)
    "surah":    "s{surah}",

    # Structural hierarchy (narration-specific, as verse boundaries differ)
    "verse":    "{narration}:s{surah}:v{verse}",
    "word":     "{narration}:s{surah}:v{verse}:w{word}",
    "char":     "{narration}:s{surah}:v{verse}:w{word}:c{char}",
    "symbol":   "{narration}:s{surah}:v{verse}:w{word}:c{char}:sym{symbol}",
    "sentence": "{narration}:s{surah}:v{verse}:snt{sentence}",

    # Layout hierarchy (narration + edition specific)
    "page":     "{narration}:{edition}:p{page}",
    "line":     "{narration}:{edition}:p{page}:l{line}",

    # Division hierarchy (global numbering within narration)
    "juz":      "{narration}:j{juz}",
    "hizb":     "{narration}:h{hizb}",       # Global 1-60
    "rub":      "{narration}:r{rub}",        # Global 1-240

    # Metadata entities (fixed registries)
    "narration": "qir:{name}",
    "edition":   "edn:{publisher}:{name}",
    "reader":    "rdr:{name}",
    "mushaf":    "msh:{narration}:{edition}",
    "mushaf_simple": "msh:{narration}",
}

# Known narrations (for validation)
KNOWN_NARRATIONS = {
    "hafs", "warsh", "qalun", "douri", "shuba", "sousi",
    "ibn_kathir", "abu_amr", "ibn_amir", "asim",
    "hamzah", "al_kisai", "abu_jafar", "yaqub", "khalaf",
}


# =============================================================================
# INTERNAL HELPERS
# =============================================================================

def _generate(name: str) -> str:
    """Generate UUID v5 from name string."""
    return str(uuid.uuid5(QUD_NAMESPACE, name))


def _validate_positive(value: int, name: str) -> None:
    """Validate that value is a positive integer."""
    if not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer, got {value}")


def _validate_range(value: int, min_val: int, max_val: int, name: str) -> None:
    """Validate that value is within range."""
    if not isinstance(value, int) or value < min_val or value > max_val:
        raise ValueError(f"{name} must be {min_val}-{max_val}, got {value}")


# =============================================================================
# UNIVERSAL (same across all narrations)
# =============================================================================

def surah_id(surah: int) -> str:
    """
    Generate surah UUID.

    Surahs are universal - Al-Baqarah is Al-Baqarah in every narration.
    Only verse boundaries within surahs vary by narration.

    Args:
        surah: Surah number (1-114)

    Returns:
        Deterministic UUID string
    """
    _validate_range(surah, 1, 114, "surah")
    return _generate(f"s{surah}")


# =============================================================================
# STRUCTURAL HIERARCHY (narration-specific, as verse boundaries differ)
# =============================================================================


def verse_id(narration: str, surah: int, verse: int) -> str:
    """
    Generate verse UUID.

    Args:
        narration: Qiraah narration ("hafs", "warsh", etc.)
        surah: Surah number (1-114)
        verse: Verse number (1-based, max varies by surah)

    Returns:
        Deterministic UUID string
    """
    _validate_range(surah, 1, 114, "surah")
    _validate_positive(verse, "verse")
    return _generate(f"{narration}:s{surah}:v{verse}")


def word_id(narration: str, surah: int, verse: int, word: int) -> str:
    """
    Generate word UUID.

    Args:
        narration: Qiraah narration ("hafs", "warsh", etc.)
        surah: Surah number (1-114)
        verse: Verse number
        word: Word index (1-based within verse)

    Returns:
        Deterministic UUID string
    """
    _validate_range(surah, 1, 114, "surah")
    _validate_positive(verse, "verse")
    _validate_positive(word, "word")
    return _generate(f"{narration}:s{surah}:v{verse}:w{word}")


def char_id(narration: str, surah: int, verse: int, word: int, char: int) -> str:
    """
    Generate character UUID.

    Args:
        narration: Qiraah narration ("hafs", "warsh", etc.)
        surah: Surah number (1-114)
        verse: Verse number
        word: Word index (1-based within verse)
        char: Character index (1-based within word)

    Returns:
        Deterministic UUID string
    """
    _validate_range(surah, 1, 114, "surah")
    _validate_positive(verse, "verse")
    _validate_positive(word, "word")
    _validate_positive(char, "char")
    return _generate(f"{narration}:s{surah}:v{verse}:w{word}:c{char}")


def symbol_id(
    narration: str, surah: int, verse: int, word: int, char: int, symbol: int
) -> str:
    """
    Generate symbol UUID (diacritic/tajweed mark on a character).

    Args:
        narration: Qiraah narration ("hafs", "warsh", etc.)
        surah: Surah number (1-114)
        verse: Verse number
        word: Word index (1-based within verse)
        char: Character index (1-based within word)
        symbol: Symbol index (1-based, multiple symbols per char possible)

    Returns:
        Deterministic UUID string
    """
    _validate_range(surah, 1, 114, "surah")
    _validate_positive(verse, "verse")
    _validate_positive(word, "word")
    _validate_positive(char, "char")
    _validate_positive(symbol, "symbol")
    return _generate(f"{narration}:s{surah}:v{verse}:w{word}:c{char}:sym{symbol}")


def sentence_id(narration: str, surah: int, verse: int, sentence: int) -> str:
    """
    Generate sentence UUID.

    Args:
        narration: Qiraah narration ("hafs", "warsh", etc.)
        surah: Surah number (1-114)
        verse: Verse number
        sentence: Sentence index (1-based within verse)

    Returns:
        Deterministic UUID string
    """
    _validate_range(surah, 1, 114, "surah")
    _validate_positive(verse, "verse")
    _validate_positive(sentence, "sentence")
    return _generate(f"{narration}:s{surah}:v{verse}:snt{sentence}")


# =============================================================================
# LAYOUT HIERARCHY (narration + edition specific)
# =============================================================================

def page_id(narration: str, edition: str, page: int) -> str:
    """
    Generate page UUID.

    Pages depend on both narration (text content) and edition (formatting).
    Page 42 of Hafs Madina ≠ Page 42 of Warsh Madina.

    Args:
        narration: Qiraah narration ("hafs", "warsh", etc.)
        edition: Edition identifier (e.g., "kfgqpc_v2", "madina_v1")
        page: Page number (1-based)

    Returns:
        Deterministic UUID string
    """
    _validate_positive(page, "page")
    return _generate(f"{narration}:{edition}:p{page}")


def line_id(narration: str, edition: str, page: int, line: int) -> str:
    """
    Generate line UUID.

    Args:
        narration: Qiraah narration ("hafs", "warsh", etc.)
        edition: Edition identifier (e.g., "kfgqpc_v2", "madina_v1")
        page: Page number (1-based)
        line: Line number (1-based within page)

    Returns:
        Deterministic UUID string
    """
    _validate_positive(page, "page")
    _validate_positive(line, "line")
    return _generate(f"{narration}:{edition}:p{page}:l{line}")


# =============================================================================
# DIVISION HIERARCHY (global numbering within narration)
# =============================================================================

def juz_id(narration: str, juz: int) -> str:
    """
    Generate juz UUID.

    Args:
        narration: Qiraah narration ("hafs", "warsh", etc.)
        juz: Juz number (1-30)

    Returns:
        Deterministic UUID string
    """
    _validate_range(juz, 1, 30, "juz")
    return _generate(f"{narration}:j{juz}")


def hizb_id(narration: str, hizb: int) -> str:
    """
    Generate hizb UUID.

    Uses global numbering (1-60) rather than nested (juz + hizb within juz).

    Args:
        narration: Qiraah narration ("hafs", "warsh", etc.)
        hizb: Hizb number (1-60, global)

    Returns:
        Deterministic UUID string
    """
    _validate_range(hizb, 1, 60, "hizb")
    return _generate(f"{narration}:h{hizb}")


def rub_id(narration: str, rub: int) -> str:
    """
    Generate rub (quarter) UUID.

    Uses global numbering (1-240) rather than nested.

    Args:
        narration: Qiraah narration ("hafs", "warsh", etc.)
        rub: Rub number (1-240, global)

    Returns:
        Deterministic UUID string
    """
    _validate_range(rub, 1, 240, "rub")
    return _generate(f"{narration}:r{rub}")


# =============================================================================
# METADATA ENTITIES (fixed registries)
# =============================================================================

def narration_id(name: str) -> str:
    """
    Generate narration/qiraah metadata UUID.

    Args:
        name: Narration name ("hafs", "warsh", "qalun", etc.)

    Returns:
        Deterministic UUID string
    """
    return _generate(f"qir:{name}")


def edition_id(publisher: str, name: str) -> str:
    """
    Generate edition UUID.

    Args:
        publisher: Publisher code (e.g., "kfgqpc" for King Fahd Complex)
        name: Edition name (e.g., "hafs_v2")

    Returns:
        Deterministic UUID string
    """
    return _generate(f"edn:{publisher}:{name}")


def reader_id(name: str) -> str:
    """
    Generate reader biographical UUID.

    Args:
        name: Reader name ("hafs", "warsh", "nafi", etc.)

    Returns:
        Deterministic UUID string
    """
    return _generate(f"rdr:{name}")


def mushaf_id(narration: str, edition: Optional[str] = None) -> str:
    """
    Generate mushaf UUID.

    Args:
        narration: Qiraah narration ("hafs", "warsh", etc.)
        edition: Optional edition identifier for edition-specific mushaf

    Returns:
        Deterministic UUID string
    """
    if edition:
        return _generate(f"msh:{narration}:{edition}")
    return _generate(f"msh:{narration}")


# =============================================================================
# NAME INSPECTION (for debugging/logging)
# =============================================================================

def get_verse_name(narration: str, surah: int, verse: int) -> str:
    """Get the name string that produces a verse UUID."""
    return f"{narration}:s{surah}:v{verse}"


def get_word_name(narration: str, surah: int, verse: int, word: int) -> str:
    """Get the name string that produces a word UUID."""
    return f"{narration}:s{surah}:v{verse}:w{word}"


def get_char_name(narration: str, surah: int, verse: int, word: int, char: int) -> str:
    """Get the name string that produces a character UUID."""
    return f"{narration}:s{surah}:v{verse}:w{word}:c{char}"


# =============================================================================
# DEMO
# =============================================================================

if __name__ == "__main__":
    print("=== QUD UUID Generator Demo ===\n")

    print("UNIVERSAL (same across all narrations)")
    print("-" * 50)
    print(f"Surah 2 (Al-Baqarah):  {surah_id(2)}")
    print(f"Surah 114 (An-Nas):    {surah_id(114)}")
    print()

    print("STRUCTURAL HIERARCHY (narration-specific)")
    print("-" * 50)
    print(f"Verse (Hafs 2:255):    {verse_id('hafs', 2, 255)}")
    print(f"Word (2:255 w4):       {word_id('hafs', 2, 255, 4)}")
    print(f"Char (2:255 w4 c2):    {char_id('hafs', 2, 255, 4, 2)}")
    print(f"Symbol (w4 c2 sym1):   {symbol_id('hafs', 2, 255, 4, 2, 1)}")
    print(f"Sentence (2:255 snt1): {sentence_id('hafs', 2, 255, 1)}")
    print()

    print("LAYOUT HIERARCHY (narration + edition)")
    print("-" * 50)
    print(f"Page (hafs kfgqpc p42):    {page_id('hafs', 'kfgqpc_v2', 42)}")
    print(f"Line (hafs kfgqpc p42 l7): {line_id('hafs', 'kfgqpc_v2', 42, 7)}")
    print(f"Page (warsh kfgqpc p42):   {page_id('warsh', 'kfgqpc_v2', 42)}")
    print("(Different narration = different UUID for same page number)")
    print()

    print("DIVISION HIERARCHY")
    print("-" * 50)
    print(f"Juz (j15):             {juz_id('hafs', 15)}")
    print(f"Hizb (h30):            {hizb_id('hafs', 30)}")
    print(f"Rub (r120):            {rub_id('hafs', 120)}")
    print()

    print("METADATA ENTITIES")
    print("-" * 50)
    print(f"Narration (hafs):      {narration_id('hafs')}")
    print(f"Edition (kfgqpc v2):   {edition_id('kfgqpc', 'hafs_v2')}")
    print(f"Reader (hafs):         {reader_id('hafs')}")
    print(f"Mushaf (hafs):         {mushaf_id('hafs')}")
    print(f"Mushaf (hafs+edition): {mushaf_id('hafs', 'kfgqpc_v2')}")
    print()

    print("DETERMINISM CHECK")
    print("-" * 50)
    id1 = verse_id("hafs", 2, 255)
    id2 = verse_id("hafs", 2, 255)
    print(f"verse_id('hafs', 2, 255) x2:")
    print(f"  {id1}")
    print(f"  {id2}")
    print(f"  Match: {id1 == id2}")
    print()

    print("CROSS-NARRATION COMPARISON")
    print("-" * 50)
    print(f"Hafs 2:255:  {verse_id('hafs', 2, 255)}")
    print(f"Warsh 2:255: {verse_id('warsh', 2, 255)}")
    print("(Different UUIDs - verse boundaries may differ by narration)")
