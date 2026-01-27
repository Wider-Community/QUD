# QUD Development Guidelines

Auto-generated from all feature plans. Last updated: 2025-11-03

## Active Technologies
- Python 3.11+ (Tier 1 experimental research code) + NLTK, NLP libraries, jsonschema, Pydantic, Jupyter (notebooks), matplotlib/seaborn/plotly (visualization) (001-quranic-layer-architecture)
- SQLite (sample database for demonstrations), JSON files (primary data format), CSV (validation) (001-quranic-layer-architecture)

- Python 3.11+ (Tier 1 experimental research code) (001-quranic-layer-architecture)

## Commands

cd src [ONLY COMMANDS FOR ACTIVE TECHNOLOGIES][ONLY COMMANDS FOR ACTIVE TECHNOLOGIES] pytest [ONLY COMMANDS FOR ACTIVE TECHNOLOGIES][ONLY COMMANDS FOR ACTIVE TECHNOLOGIES] ruff check .

## Code Style

Python 3.11+ (Tier 1 experimental research code): Follow standard conventions

## Schema Verification

After modifying any layer's `schema.json` or `models.py`:

1. **Validate JSON schemas** against metaschema:
   ```bash
   check-jsonschema --check-metaschema schemas/<layer>/schema.json
   ```

2. **Verify Pydantic models match JSON schemas**: Convert Pydantic models to JSON Schema and confirm they produce equivalent output to the hand-written JSON schema:
   ```python
   from schemas.<layer>.models import <Model>
   print(<Model>.model_json_schema())
   ```
   Compare the output against the corresponding `.json` schema file.

3. Confirm compliance with `schemas/README.md`

