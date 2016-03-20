from ..Feature import Feature
from nltk.tokenize  import wordpunct_tokenize

class WeirdPunctuationFeature(Feature):

    WEIRD_PUNCT = ('*', '~', '[', ']', '^', '<', '>')

    def evaluate(self, sentence):
        tokens = wordpunct_tokenize(sentence)

        count = 0
        for token in tokens:
            if token in self.WEIRD_PUNCT:
                count += 1

        return float(count)/float(len(tokens))
