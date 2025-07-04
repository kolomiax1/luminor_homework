from . import LoaderPlugin


class S3Loader(LoaderPlugin):

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.disconnect()

    def connect(self) -> None:
        print("Connecting...")

    def disconnect(self) -> None:
        print("Disconnecting...")

    def load(self, data):

        try:
            print("Uploading to S3...")
        except Exception as e:
            if hasattr(self, "error_handler"):
                self.error_handler.handle(e)
