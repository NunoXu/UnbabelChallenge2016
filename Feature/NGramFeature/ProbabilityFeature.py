import kenlm
import numpy
import math
from .NGramFeature import NGramFeature


class Probability(NGramFeature):

    def __init__(self, model_path):
        super(Probability, self).__init__(model_path)

    def evaluate(self, sentence):
        return math.pow(10, self._model.score(sentence))

