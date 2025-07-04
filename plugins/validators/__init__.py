from abc import ABC, abstractmethod
from typing import Any, List


class ValidatorPlugin(ABC):
    """Abstract base class for data validation."""

    def __init__(self, model):
        self.model = model

    @abstractmethod
    def validate(self, data: Any) -> tuple[bool, List[str]]:
        """Validate data and return (is_valid, errors)."""
        pass
