import kenlm
import numpy
from .NGramFeature import NGramFeature


class StandardDeviationFeature(NGramFeature):

    def __init__(self, model_path):
        super(StandardDeviationFeature, self).__init__(model_path)

    def evaluate(self, sentence):
        full_scores = self._model.full_scores(sentence)

        prob_list = list()

        for i, (prob, length, oov) in enumerate(full_scores):
            list.append(prob)
        st_deviation = numpy.std(prob_list)

        return st_deviation

