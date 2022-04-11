import random

class WordFinder:
    """Word Finder: finds random words from a dictionary.
    
     >>> dictionary = WordFinder('words.txt')
     235886 lines read

     >>> dictionary.random()

    """

    def __init__(self, path):
        self.path = path
        self.words = self.word_lst()
        print(f'{len(self.words)} lines read')

    def word_lst(self):
        file = open(self.path)
        words = [word[:-1] for word in file]
        return words

    def random(self):
        return random.choice(self.words)


class FunkyWordsFinder(WordFinder):
    """Funky Word Finder: Extends functionality of word finder to work with different file structures
    
    >>> funky_dictionary = FunkyWordsFinder('funkywords.txt')

    >>> funky_dictionary.random()
    
    """

    def __init__(self, path):
        super().__init__(path)
        self.words = [word for word in self.words if '#' not in word and len(word) > 0]
        print(f'{len(self.words)} words total')
