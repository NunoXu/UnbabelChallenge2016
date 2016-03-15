import kenlm
import numpy
from .NGramFeature import NGramFeature


class Probability(NGramFeature):

    def __init__(self, model_path):
        NGramFeature.__init__(model_path)

    def evaluate(self, sentence):
        return self._model.score(sentence)

