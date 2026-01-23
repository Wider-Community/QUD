# Layer Schema Development Procedure

For each layer, complete the following 4 subtasks in order.

---

## 1. Research & Schema Revision

- Read `schemas/README.md` and related documentation
- Reference `schemas/json-schema-guide.md` for JSON Schema syntax and validation patterns
- Review current `schema.json` for the layer
- Research Quran datasets (`data/QS - QIRAAT`), QUD slides, demo videos, etc. for relevant data patterns
- Modify schema based on findings
- Assess layer boundaries:
  - Is this layer too divided? (should merge with another layer)
  - Is this layer too big? (needs splitting into sub-layers)

---

## 2. Pydantic Models

- Reference `schemas/pydantic-guide.md` for Pydantic patterns and validation
- Create `schemas/<layer>/models.py`
- Implement Pydantic model(s) matching the JSON schema
- Ensure type hints and validation rules align with schema constraints

---

## 3. UUID Assessment

- Review the layer's UUID generator function in `research-tools/generators/uuid_generator.py` and UUID table in `schemas/README.md`
- Check for uniqueness - no collisions across contexts
- Check for ambiguity - naming convention is clear and deterministic
- Check that it handles all dependencies and variants across different contexts/layers
- Identify if revisions are needed

**Note:** UUID assessment may reveal issues requiring changes to the schema. If so, loop back to subtask 1 to revise the schema before proceeding.

---

## 4. Layer Documentation

Create `schemas/<layer>/README.md` for the layer documenting:

- Research findings summary
- Schema decisions and rationale
- Uncertainties and edge cases
- Cross-layer mapping considerations for future work
- How this layer varies by context and affects other layers
- Tasks and work items for next sprint regarding layer refinements and cross-layer-mappings (`schemas/cross-layer-mappings/entity-mapping-schema.json`)
- Layer independence assessment (split/merge recommendations)
- Alternatives considered and consequences
- UUID assessment findings

Update if needed:
- `schemas/README.md`
- `schemas/base_layers/base_layers_v1.json`
