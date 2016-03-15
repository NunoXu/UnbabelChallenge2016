from abc import ABCMeta
from pycorenlp import StanfordCoreNLP
from..Feature import Feature


class SyntaxFeature(Feature, metaclass=ABCMeta):

    _coreNLPApi = None

    def __init__(self, address):
        if not self._coreNLPApi:
            self._coreNLPApi = StanfordCoreNLP(address)
