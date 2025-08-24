class Helpers:
    def is_number(self, token):
        try:
            float(token)
            return True
        except ValueError:
            return False
        
    def is_variable(self, token):
        return token.isalpha()
    