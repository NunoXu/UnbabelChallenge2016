import Feature
from nltk.tokenize import wordpunct_tokenize
import string


class CapitalizationFeature(Feature):


    def evaluate(self, sentence):

        tokens = wordpunct_tokenize(sentence)
        count = 0

        for token in tokens:
            if token not in string.punctuation and token.isupper():
                count += 1

        return float(count)/float(len(tokens))
