class Anagram:

    def __init__(self, text):
        self.text = text.lower()
        self._sorted_text = sorted(self.text)

    def match(self, anagrams):
        return [anagram for anagram in anagrams 
                if sorted(anagram.lower()) == self._sorted_text 
                and anagram.lower() != self.text]