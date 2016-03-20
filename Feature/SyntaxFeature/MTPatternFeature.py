from .SyntaxFeature import SyntaxFeature


class MTPatternFeature(SyntaxFeature):

    def __init__(self, address, props_location):
        super(MTPatternFeature, self).__init__(address, props_location)

    def evaluate(self, sentence):
        pos_tags = self.get_pos_tags(self.make_call_to_api(sentence))
        counter = 0
        for tag in pos_tags:
            if tag in ['sp000', 'da0000', 'nc0s000']:
                counter += 1

        if counter > 1:
            return float(counter) / 3.0
        else:
            return 0




