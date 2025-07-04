from . import ErrorHandlerPlugin


class SimpleHandlerPlugin(ErrorHandlerPlugin):

    def handle(self, invalid_record):
        print("Handling exception...")
