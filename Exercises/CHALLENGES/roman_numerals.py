"""
Need to write an algorithm to determine best way to replace numbers with roman numerals

if not a key in the dict, 
then 1100 % 10 = 0
110 % 10 = 0
11 % 10 = 1
1 % 10 = 1 
"""
class RomanNumeral:

    ROMAN_MAP = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]


    def __init__(self, digit):
        self.digit = digit

    def to_roman(self):
        return self._recursive_converter(self.digit)
    
    def _recursive_converter(self, number):
        if number == 0:
            return ""
        for value, numeral in self.ROMAN_MAP:
            if number >= value:
                return numeral + self._recursive_converter(number-value)
