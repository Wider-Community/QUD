"""
Schema Validator

Tier 2 (Reusable Research Tool)

Validates Quranic layer data against JSON Schema and Pydantic models.
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import jsonschema
from pydantic import BaseModel, ValidationError


class SchemaValidator:
    """
    Validate data against JSON Schema and Pydantic models.
    """

    def __init__(self, schema_dir: Optional[Path] = None):
        """
        Initialize validator.

        Args:
            schema_dir: Directory containing schema files. If None, uses schemas/ in project root.
        """
        self.schema_dir = Path(schema_dir) if schema_dir else Path.cwd() / "schemas"
        self._schema_cache: Dict[str, Dict] = {}

    def load_schema(self, schema_path: Union[str, Path]) -> Dict:
        """
        Load JSON Schema from file.

        Args:
            schema_path: Path to schema file (absolute or relative to schema_dir)

        Returns:
            Schema dictionary

        Raises:
            FileNotFoundError: If schema file doesn't exist
            json.JSONDecodeError: If schema is malformed
        """
        path = Path(schema_path)
        if not path.is_absolute():
            path = self.schema_dir / path

        # Use cache if available
        cache_key = str(path)
        if cache_key in self._schema_cache:
            return self._schema_cache[cache_key]

        if not path.exists():
            raise FileNotFoundError(f"Schema file not found: {path}")

        with open(path, 'r', encoding='utf-8') as f:
            schema = json.load(f)

        self._schema_cache[cache_key] = schema
        return schema

    def validate_json_schema(
        self,
        data: Any,
        schema: Union[Dict, str, Path],
        strict: bool = True
    ) -> tuple[bool, Optional[List[str]]]:
        """
        Validate data against JSON Schema.

        Args:
            data: Data to validate
            schema: Schema dict or path to schema file
            strict: If True, raise exception on validation failure

        Returns:
            Tuple of (is_valid, error_messages)

        Raises:
            jsonschema.ValidationError: If strict=True and validation fails
        """
        # Load schema if path provided
        if isinstance(schema, (str, Path)):
            schema = self.load_schema(schema)

        errors = []

        try:
            jsonschema.validate(instance=data, schema=schema)
            return (True, None)
        except jsonschema.ValidationError as e:
            errors.append(str(e))
            if strict:
                raise
            return (False, errors)
        except jsonschema.SchemaError as e:
            errors.append(f"Schema error: {e}")
            if strict:
                raise
            return (False, errors)

    def validate_pydantic(
        self,
        data: Dict,
        model_class: type[BaseModel],
        strict: bool = True
    ) -> tuple[bool, Optional[BaseModel], Optional[List[str]]]:
        """
        Validate data against Pydantic model.

        Args:
            data: Data dictionary to validate
            model_class: Pydantic model class
            strict: If True, raise exception on validation failure

        Returns:
            Tuple of (is_valid, model_instance, error_messages)

        Raises:
            ValidationError: If strict=True and validation fails
        """
        try:
            instance = model_class(**data)
            return (True, instance, None)
        except ValidationError as e:
            errors = [str(err) for err in e.errors()]
            if strict:
                raise
            return (False, None, errors)

    def validate_layer_data(
        self,
        layer_name: str,
        data: Any,
        schema_filename: str = "schema.json",
        strict: bool = True
    ) -> tuple[bool, Optional[List[str]]]:
        """
        Validate layer data against its schema.

        Args:
            layer_name: Layer name (e.g., "layer-00-character-composition")
            data: Layer data to validate
            schema_filename: Schema filename within layer directory (default: "schema.json")
            strict: If True, raise exception on validation failure

        Returns:
            Tuple of (is_valid, error_messages)
        """
        schema_path = Path(layer_name) / schema_filename
        return self.validate_json_schema(data, schema_path, strict=strict)

    def clear_cache(self):
        """Clear schema cache."""
        self._schema_cache.clear()
