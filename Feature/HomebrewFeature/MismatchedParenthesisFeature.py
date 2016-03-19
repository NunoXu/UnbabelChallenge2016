import Feature
from nltk.tokenize import wordpunct_tokenize

class MistmatchedParenthesisFeature(Feature):

    possible_puncts = ('(', '[', '"')

    def evaluate(self, sentence):
        tokens = wordpunct_tokenize(sentence)

        stored_puncts = list()

        for i, token in enumerate(tokens):

            if stored_puncts and self.matches_punct(stored_puncts[-1], token):
                stored_puncts = stored_puncts[:-1]
            elif token in self.possible_puncts:
                stored_puncts.append(token)

        if stored_puncts:
            return 1
        else:
            return 0

    def matches_punct(self, stored_token, punct):

        if stored_token == '(':
            return punct == ')'
        elif stored_token == '[':
            return stored_token == ']'
        elif stored_token == '"':
            return stored_token == '"'
        else:
            return False