import kenlm
import numpy
from . import NGramFeature


class Probability(NGramFeature.NGramFeature):

    def __init__(self, model_path):
        super(Probability, self).__init__(model_path)

    def evaluate(self, sentence):
        return self._model.score(sentence)

