"""
Performance Metrics Analyzer

Tier 2 (Reusable Research Tool)

Analyzes performance metrics for layer generation and data processing.
"""

import time
from typing import Any, Callable, Dict, List, Optional
from dataclasses import dataclass, field
from contextlib import contextmanager


@dataclass
class PerformanceMetrics:
    """Performance metrics for a task."""

    task_name: str
    duration_seconds: float
    memory_mb: Optional[float] = None
    entity_count: Optional[int] = None
    entities_per_second: Optional[float] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __str__(self) -> str:
        lines = [
            f"Task: {self.task_name}",
            f"Duration: {self.duration_seconds:.3f}s"
        ]

        if self.entity_count:
            lines.append(f"Entities: {self.entity_count:,}")

        if self.entities_per_second:
            lines.append(f"Rate: {self.entities_per_second:.1f} entities/s")

        if self.memory_mb:
            lines.append(f"Memory: {self.memory_mb:.2f} MB")

        return " | ".join(lines)


class PerformanceAnalyzer:
    """
    Analyze and track performance metrics.

    Provides utilities for timing, memory tracking, and throughput analysis.
    """

    def __init__(self):
        """Initialize analyzer."""
        self.metrics_history: List[PerformanceMetrics] = []

    @contextmanager
    def measure(
        self,
        task_name: str,
        entity_count: Optional[int] = None
    ):
        """
        Context manager for measuring task performance.

        Args:
            task_name: Name of task being measured
            entity_count: Optional entity count for throughput calculation

        Yields:
            None

        Example:
            >>> analyzer = PerformanceAnalyzer()
            >>> with analyzer.measure("generate_characters", entity_count=323015):
            ...     # perform task
            ...     pass
        """
        start_time = time.time()

        try:
            yield
        finally:
            duration = time.time() - start_time

            entities_per_second = None
            if entity_count:
                entities_per_second = entity_count / duration if duration > 0 else 0

            metrics = PerformanceMetrics(
                task_name=task_name,
                duration_seconds=duration,
                entity_count=entity_count,
                entities_per_second=entities_per_second
            )

            self.metrics_history.append(metrics)

    def measure_function(
        self,
        func: Callable,
        *args,
        task_name: Optional[str] = None,
        **kwargs
    ) -> tuple[Any, PerformanceMetrics]:
        """
        Measure function execution.

        Args:
            func: Function to measure
            *args: Positional arguments for function
            task_name: Optional task name (default: function name)
            **kwargs: Keyword arguments for function

        Returns:
            Tuple of (function_result, metrics)
        """
        task_name = task_name or func.__name__

        start_time = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start_time

        metrics = PerformanceMetrics(
            task_name=task_name,
            duration_seconds=duration
        )

        self.metrics_history.append(metrics)

        return result, metrics

    def get_summary(self) -> Dict[str, Any]:
        """
        Get summary statistics of all measured tasks.

        Returns:
            Dictionary with summary statistics
        """
        if not self.metrics_history:
            return {"message": "No metrics recorded"}

        total_duration = sum(m.duration_seconds for m in self.metrics_history)
        total_entities = sum(m.entity_count for m in self.metrics_history if m.entity_count)

        return {
            "total_tasks": len(self.metrics_history),
            "total_duration_seconds": total_duration,
            "total_entities": total_entities,
            "average_duration_seconds": total_duration / len(self.metrics_history),
            "tasks": [
                {
                    "name": m.task_name,
                    "duration": m.duration_seconds,
                    "entities": m.entity_count
                }
                for m in self.metrics_history
            ]
        }

    def print_summary(self):
        """Print summary to console."""
        print("\nPerformance Summary")
        print("=" * 80)

        for metrics in self.metrics_history:
            print(metrics)

        print("=" * 80)

        summary = self.get_summary()
        print(f"Total tasks: {summary['total_tasks']}")
        print(f"Total duration: {summary['total_duration_seconds']:.3f}s")
        print(f"Total entities: {summary.get('total_entities', 'N/A')}")

    def clear(self):
        """Clear metrics history."""
        self.metrics_history.clear()
