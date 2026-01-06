# Contextual Versioning System

**Status**: Design Phase
**Last Updated**: 2025-11-05

## Overview

The Contextual Versioning System enables tracking Quranic data variations across:
- **Qiraat** (10 canonical readings)
- **Narrations** (20 canonical transmission paths)
- **Editions** (e.g., King Fahd Complex, Dar Al-Maarifah)
- **Manuscripts** (historical sources)

## Core Principles

1. **Version is Context**: Every piece of data has explicit context (Qiraat, Narration, Edition)
2. **No Default Version**: All data tagged with explicit version context
3. **Variation Tracking**: Capture differences between versions at all layers
4. **Bidirectional Mapping**: Navigate from any version to any other version

## Context Schema

Each data entity includes:
```json
{
  "context": {
    "qiraat": "Asim",
    "narration": "Hafs",
    "edition": "King Fahd Complex",
    "manuscript": null
  }
}
```

## Design Status

This document will be refined during Phase 1 (Setup) based on:
- RR-008: Context schema design
- RR-009: Mudghaj representation
- RR-010: Cross-version mapping

## References

- See `specs/001-quranic-layer-architecture/spec.md` Section 5.4
- See `schemas/context-schema/` for formal definitions
