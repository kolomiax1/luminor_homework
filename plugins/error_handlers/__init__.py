from abc import ABC, abstractmethod


class ErrorHandlerPlugin(ABC):
    """Abstract base class for error handling."""

    @abstractmethod
    def handle(self):
        """Handle errors during ETL process."""
        pass
