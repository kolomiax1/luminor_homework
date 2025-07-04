from typing import Generator

from . import ExtractorPlugin


class MongoBatchExtractor(ExtractorPlugin):

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.disconnect()

    def connect(self) -> None:
        print("Connecting...")

    def disconnect(self) -> None:
        print("Disconnecting...")

    def extract(self) -> Generator:

        print("Extracting data...")

        dummy_extracted_data = range(3)

        if hasattr(self, "validator"):
            self.validator.validate(dummy_extracted_data)

        return dummy_extracted_data
