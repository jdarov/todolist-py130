import re

class Scrabble:

    SCORE_MAP = {
        **dict.fromkeys('AEIOULNRST', 1),
        **dict.fromkeys('DG', 2),
        **dict.fromkeys('BCMP', 3),
        **dict.fromkeys('FHVWY', 4),
        **dict.fromkeys('K',5),
        **dict.fromkeys('JX', 8),
        **dict.fromkeys('QZ', 10)
    }

    def __init__(self, word):
        self.word = word

    @property
    def word(self):
        return self._word
    @word.setter
    def word(self, new_word):
        if not new_word:
            self._word = ''
        else:
            self._word = re.sub(r'[\s\\.]', '', new_word).upper()

    @staticmethod
    def _return_score(letter):
        return Scrabble.SCORE_MAP.get(letter, 0)
  
    def score(self):
        return sum(self._return_score(char) for char in self.word)
    
    @classmethod
    def calculate_score(cls, word):
        return cls(word).score()

