from ..Feature import Feature
from nltk.tokenize import wordpunct_tokenize
import string


class CapitalizationFeature(Feature):

    def __init__(self):
        super(CapitalizationFeature, self).__init__()

    def evaluate(self, sentence):

        tokens = wordpunct_tokenize(sentence)
        count = 0

        for token in tokens:
            if token not in string.punctuation:
                if self.iswordupper(token):
                    count += 1

        return float(count)/float(len(tokens))

    def iswordupper(self, word):

        is_upper = True
        chars = list(word)
        for char in chars:
            if char.islower():
                is_upper = False
                break

        return is_upper