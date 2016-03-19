from .NGramFeature import NGramFeature
from nltk.tokenize import wordpunct_tokenize


class UnknownWordsFeature(NGramFeature):

    def __init__(self, model_path):
        super(UnknownWordsFeature, self).__init__(model_path)

    def evaluate(self, sentence):
        tokens = wordpunct_tokenize(sentence)
        count = 0
        for token in tokens:
            if self._model.score(token) == 0:
                count += 1
        return float(count)/float(len(tokens))

