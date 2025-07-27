import re

class Octal:
    
    def __init__(self, octal):
        self.octal = octal

    @property
    def octal(self):
        return self._octal

    @octal.setter
    def octal(self, number):
        if self._validate_octal(number):
            self._octal = str(number)
        else:
            self._octal = '0' # default to 0 if not valid to pass tests

    def to_decimal(self):
        return sum(
            int(digit) * 8 ** n for n, digit in enumerate(reversed(self._octal))
        )
    def _validate_octal(self, number):
        return bool(re.match(r'^[0-7]+$', str(number)))
