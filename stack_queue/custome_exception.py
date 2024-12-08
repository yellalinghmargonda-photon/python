class CustomErrorWithDetails(Exception):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code
        super().__init__(f"Error Code {self.error_code}: {self.message}")