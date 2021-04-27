
class FormulaError(Exception):
    """Exceptions raised for errors in the calculator input

    Atributes:
        value -- user input that caused the error
        message -- a meaningful description of the error

    """
    def __init__(self,value,message):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.value}  >- {self.message}'