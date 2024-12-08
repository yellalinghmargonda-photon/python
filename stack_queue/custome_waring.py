import  warnings
class CustomwarringsWithDetails(warnings):
    def __init__(self, message, code=None):
        # Initialize the warning with a message and an optional code
        self.message = message
        self.code = code
        super().__init__(message)  # Call the parent constructor to set the warning message

    def __str__(self):
        # Customize the string representation of the warning
        if self.code:
            return f"CustomWarning [{self.code}]: {self.message}"
        else:
            return f"CustomWarning: {self.message}"
