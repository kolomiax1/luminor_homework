from abc import ABC, abstractmethod
from typing import Optional

from plugins.error_handlers import ErrorHandlerPlugin
from plugins.validators import ValidatorPlugin


class ExtractorPlugin(ABC):
    """
    Abstract base class for data extraction.
    """

    validator: Optional[ValidatorPlugin]
    error_handler: Optional[ErrorHandlerPlugin]

    def __init__(self, config):
        self.config = config

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        pass

    @abstractmethod
    def connect(self):
        """Initialize connection to the source system."""
        pass

    @abstractmethod
    def disconnect(self):
        """Close the connection to the source system."""
        pass

    @abstractmethod
    def extract(self):
        """Fetch data from the source."""
        pass
