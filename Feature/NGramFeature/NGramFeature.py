from Feature import Feature
import kenlm


class NGramFeature(Feature):

    _model = None

    def __init__(self, file_path):
        if not self._model:
            self.load_model(file_path)

    @classmethod
    def load_model(cls, file_path):
        cls._model = kenlm.Model(file_path)
