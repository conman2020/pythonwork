"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...
    def __init__(self,path):
        new_file= open(path)
        self.words =self.parse(new_file)
        print(f"{len(self.words)} words read")
    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)
class SpecialWordFinder(WordFinder):


    def parse(self,dict_file):
        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]


