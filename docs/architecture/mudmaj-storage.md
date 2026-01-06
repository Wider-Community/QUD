# MUDMAJ Storage Architecture

**Status**: Design Phase
**Last Updated**: 2025-11-05

## Overview

MUDMAJ (Merged/Combined) is the unified data format that integrates all Quranic data layers into a single navigable structure.

## Core Concept

Instead of storing 17+ separate layer files, MUDMAJ provides:
- **Single Source**: One unified data structure containing all layers
- **Bidirectional Navigation**: UUID-based cross-layer references
- **Context Preservation**: All contextual versioning metadata included
- **Query Efficiency**: Optimized for common access patterns

## Design Goals

1. Support efficient queries across layers (e.g., "show all layer data for verse 1:1")
2. Maintain layer separation logically while integrating physically
3. Enable incremental updates without full regeneration
4. Scale to multiple Qiraat/Narrations

## Storage Format Options (Under Investigation)

- **JSON**: Human-readable, widely supported
- **HDF5**: Efficient for large datasets, supports metadata
- **SQLite**: Queryable, good for relational access patterns
- **Hybrid**: JSON for schemas, binary for data

## Design Status

This document will be refined during RR-004 through RR-007 based on experimental findings.

## References

- See `specs/001-quranic-layer-architecture/data-model.md` for MUDMAJ schema
- See `schemas/mudmaj-schema/` for formal definitions
