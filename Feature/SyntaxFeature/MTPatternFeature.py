from .SyntaxFeature import SyntaxFeature


class MTPatternFeature(SyntaxFeature):

    def __init__(self, address, props_location):
        super(MTPatternFeature, self).__init__(address, props_location)

    def evaluate(self, sentence):
        pos_tags = self.get_pos_tags(self.make_call_to_api(sentence))

        tag_String = ""

        desired_tag = 'sp000' + 'da0000' + 'nc0s000'
        #TODO: recortar caracteres desinteressantes de forma a garantir que isto PODE acontecer
        for tag in pos_tags:
            tag_String += str(tag)

        if desired_tag in tag_String:
            return 1
        else:
            return 0




