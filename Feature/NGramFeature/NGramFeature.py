from ..Feature import Feature
from abc import ABCMeta
import kenlm


class NGramFeature(Feature, metaclass=ABCMeta):

    _model = None

    def __init__(self, file_path):
        super(Feature, self).__init__()
        if not self._model:
            self.load_model(file_path)

    @classmethod
    def load_model(cls, file_path):
        cls._model = kenlm.Model(file_path)
