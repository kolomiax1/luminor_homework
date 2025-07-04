from abc import ABC, abstractmethod
from typing import Optional

from plugins.error_handlers import ErrorHandlerPlugin
from plugins.validators import ValidatorPlugin


class LoaderPlugin(ABC):
    """
    Abstract base class for data ingestion.
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
        """Initialize connection to the destination system."""
        pass

    @abstractmethod
    def disconnect(self):
        """Close the connection to the destination system."""
        pass

    @abstractmethod
    def load(self, data):
        """Ingest data to the destination system."""
        pass
