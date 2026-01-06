"""
Provenance Tracker

Tier 2 (Reusable Research Tool)

Tracks data provenance through transformation pipeline.
Maintains audit log of all data transformations for research reproducibility.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field, asdict
from enum import Enum


class TransformationType(Enum):
    """Types of data transformations."""
    LOAD = "load"
    PARSE = "parse"
    VALIDATE = "validate"
    TRANSFORM = "transform"
    GENERATE = "generate"
    MERGE = "merge"
    EXPORT = "export"


@dataclass
class SourceTag:
    """Tag identifying data source."""

    source_type: str  # e.g., "King Fahd Complex", "QS-QIRAAT", "Tarteel.ai"
    qiraat: str
    narration: str
    edition: Optional[str] = None
    manuscript: Optional[str] = None
    version: Optional[str] = None
    url: Optional[str] = None
    retrieved_at: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {k: v for k, v in asdict(self).items() if v is not None}


@dataclass
class TransformationRecord:
    """Record of a single transformation."""

    timestamp: str
    transformation_type: str
    operation: str
    input_data: str  # Description or hash of input
    output_data: str  # Description or hash of output
    parameters: Dict[str, Any] = field(default_factory=dict)
    tool_name: Optional[str] = None
    tool_version: Optional[str] = None
    success: bool = True
    error_message: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {k: v for k, v in asdict(self).items() if v is not None}


class ProvenanceTracker:
    """
    Track data provenance and transformation history.

    Maintains audit log of all data transformations for research reproducibility.
    """

    def __init__(self, log_file: Optional[Path] = None):
        """
        Initialize tracker.

        Args:
            log_file: Optional path to audit log file
        """
        self.log_file = log_file
        self.transformations: List[TransformationRecord] = []
        self.source_tags: Dict[str, SourceTag] = {}

    def register_source(
        self,
        data_id: str,
        source_tag: SourceTag
    ):
        """
        Register a data source.

        Args:
            data_id: Unique identifier for this data
            source_tag: Source tag with metadata
        """
        self.source_tags[data_id] = source_tag

    def record_transformation(
        self,
        transformation_type: TransformationType,
        operation: str,
        input_data: str,
        output_data: str,
        parameters: Optional[Dict[str, Any]] = None,
        tool_name: Optional[str] = None,
        tool_version: Optional[str] = None,
        success: bool = True,
        error_message: Optional[str] = None
    ) -> TransformationRecord:
        """
        Record a data transformation.

        Args:
            transformation_type: Type of transformation
            operation: Specific operation performed
            input_data: Description or hash of input
            output_data: Description or hash of output
            parameters: Optional transformation parameters
            tool_name: Tool that performed transformation
            tool_version: Tool version
            success: Whether transformation succeeded
            error_message: Error message if failed

        Returns:
            TransformationRecord
        """
        record = TransformationRecord(
            timestamp=datetime.utcnow().isoformat(),
            transformation_type=transformation_type.value,
            operation=operation,
            input_data=input_data,
            output_data=output_data,
            parameters=parameters or {},
            tool_name=tool_name,
            tool_version=tool_version,
            success=success,
            error_message=error_message
        )

        self.transformations.append(record)

        # Auto-save if log file specified
        if self.log_file:
            self._append_to_log(record)

        return record

    def get_lineage(self, data_id: str) -> Dict[str, Any]:
        """
        Get complete lineage for a data artifact.

        Args:
            data_id: Data identifier

        Returns:
            Dictionary with source and transformation history
        """
        lineage = {
            "data_id": data_id,
            "source": self.source_tags.get(data_id, {})
        }

        if isinstance(lineage["source"], SourceTag):
            lineage["source"] = lineage["source"].to_dict()

        # Find all transformations involving this data
        relevant_transformations = [
            t.to_dict() for t in self.transformations
            if data_id in t.input_data or data_id in t.output_data
        ]

        lineage["transformations"] = relevant_transformations
        lineage["transformation_count"] = len(relevant_transformations)

        return lineage

    def export_audit_log(self, output_path: Path) -> Path:
        """
        Export complete audit log to file.

        Args:
            output_path: Path to output file

        Returns:
            Path to exported file
        """
        audit_log = {
            "generated_at": datetime.utcnow().isoformat(),
            "source_count": len(self.source_tags),
            "transformation_count": len(self.transformations),
            "sources": {
                data_id: tag.to_dict() if isinstance(tag, SourceTag) else tag
                for data_id, tag in self.source_tags.items()
            },
            "transformations": [t.to_dict() for t in self.transformations]
        }

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(audit_log, f, ensure_ascii=False, indent=2)

        return output_path

    def _append_to_log(self, record: TransformationRecord):
        """Append transformation record to log file."""
        if not self.log_file:
            return

        self.log_file.parent.mkdir(parents=True, exist_ok=True)

        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(record.to_dict(), ensure_ascii=False) + '\n')

    def validate_integrity(self) -> Dict[str, Any]:
        """
        Validate integrity of transformation chain.

        Returns:
            Validation results
        """
        issues = []

        # Check for failed transformations
        failed = [t for t in self.transformations if not t.success]
        if failed:
            issues.append(f"{len(failed)} failed transformations found")

        # Check for orphaned data (transformations without source tags)
        # This is a simplified check - real implementation would be more sophisticated

        return {
            "is_valid": len(issues) == 0,
            "issues": issues,
            "total_transformations": len(self.transformations),
            "failed_transformations": len(failed),
            "registered_sources": len(self.source_tags)
        }
