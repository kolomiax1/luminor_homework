from . import ValidatorPlugin


class ModelValidator(ValidatorPlugin):

    def validate(self, data):
        print("Validating data...")
