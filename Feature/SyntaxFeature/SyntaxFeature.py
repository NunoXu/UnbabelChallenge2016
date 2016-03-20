from abc import ABCMeta
from pycorenlp import StanfordCoreNLP
import requests
import json
from..Feature import Feature


class SyntaxFeature(Feature, metaclass=ABCMeta):

    host_address = None
    props = None
    headers = {'Content-Type': 'application/json; charset=UTF-8'}

    def __init__(self, host_address, props_location):
        if not self.host_address:
            self.host_address = host_address
        if not self.props:
            with open(props_location, mode="r") as props_file:
                self.props = {'properties': props_file.read().replace('\n', '').replace(' ', '')}

    def make_call_to_api(self, sentence):
        r = requests.post(self.host_address, params=self.props, headers=self.headers, data=sentence.encode('UTF-8'))

        return json.loads(r.text, strict=False)

    def get_pos_tags(self, json_response):
        pos_sent = []
        for json_sent in json_response['sentences']:
            for token in json_sent['tokens']:
                pos_sent.append(token['pos'])

        return pos_sent
