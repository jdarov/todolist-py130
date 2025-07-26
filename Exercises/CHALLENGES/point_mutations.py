"""
C
    input: string as constructor of DNA sequence
    output: hamming distance with the input being another string of DNA sequence

    explicit: 
        create a class that takes a DNA string as initializer
        create a method that determiens hamming distance of an input DNA string compared to classes DNA
    implicit:
        two emptry strings return 0

O 
    see unittest module
D
    strings, regex
    algo:
        create a class with DNA beings stored on instantiation
        create a method that compares an input DNA to stored DNA
            iterate through the characters of both strings
            if characters dont match, increment a count
            only iterate through the length of the shorter of the two input strings

E
"""

class DNA:
    def __init__(self, DNA_strand):
        self._DNA_strand = DNA_strand

    def hamming_distance(self, DNA_strand):
        return sum(this_DNA != other_DNA for this_DNA, other_DNA in zip(self._DNA_strand, DNA_strand))
