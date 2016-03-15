from .SyntaxFeature import SyntaxFeature


class GenderIncoherenceFeature(SyntaxFeature):

    def __init__(self, address):
        super(GenderIncoherenceFeature, self).__init__(address)

    def evaluate(self, sentence):
        return 2
