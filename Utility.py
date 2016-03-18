# -*- coding: utf-8 -*

import re
import codecs
import requests
import json
from sklearn import svm, cross_validation
from nltk.tokenize import wordpunct_tokenize

from Reader import TrainingFileReader

def tokenize_file(old_file_path, new_file_path):
     with open(new_file_path, mode='w', encoding='latin-1') as writee:
        with open(old_file_path, mode='r', encoding='latin-1') as corpus:
            for line in corpus:
                line_tokens = wordpunct_tokenize(line)
                new_line = ' '.join(line_tokens)
                writee.write(new_line + '\n')


def extract_partial_file(filepath, ratio, new_file_path, other_file_path):
    stored = 0
    ignored = 0
    total = -1

    with open(filepath, mode='r', encoding='latin-1') as read:
        with open(new_file_path, mode='w', encoding='latin-1') as training_set:
            with open(other_file_path, mode='w', encoding='latin-1') as test_set:
                for line in read:
                    if float(stored)/total < ratio:
                        training_set.write(line)
                        stored += 1
                    else:
                        test_set.write(line)
                        ignored += 1
                    total = stored + ignored


def clean_wiki_corpus(old_file_path, new_file_path):

    with open(new_file_path, mode='w') as writee:

        with open(old_file_path, mode='r', encoding='latin-1') as corpus:
            keep_killing = False
            for line in corpus:
                if re.search(r"<doc.*>", line) or re.search(r"</doc.*>", line):
                    pass
                elif re.search(r"ENDOFARTICLE\.", line):
                    keep_killing = False
                elif keep_killing:
                    pass
                elif re.search(r" Fuentes \.", line)\
                        or re.search(r" Referencias \.", line)\
                        or re.search(r" Bibliografía\ \.", line)\
                        or re.search(r" Enlaces externos \.", line)\
                        or re.search(r" Véase también \.", line)\
                        or re.search(r" Referencias y enlaces externos \.", line)\
                        or re.search(r" Galería \.", line)\
                        or re.search(r" Referencias y enlaces externos \.", line):

                    keep_killing = True
                    pass
                elif not line.strip():
                    pass
                else:
                    writee.write(line)


def separate_file_into_two(file_path):

    with open(file_path, mode='r', encoding='latin-1') as file:
        with open("0.txt", mode='w', encoding='latin-1') as zerofile:
            with open("1.txt", mode='w', encoding='latin-1') as onefile:
                for line in file:
                    if line.strip():
                        if line[0] == '0':
                            zerofile.write(line[2:])
                        elif line[0] == '1':
                            onefile.write(line[2:])
                        else:
                            print("Asneira")

    sentences = TrainingFileReader.load_training_file(file_name)
    #sentences = [{u'sentence':u'la biblíoteca'}]
    headers={'Content-Type': 'application/json; charset=UTF-8'}

def tag_corpus(file_name, host_address, props):

    with open("tagged_corpus.txt", "w") as pos_corpus:
        for sentence in sentences:
            props['annotators'] = 'tokenize, ssplit, pos'
            sent = sentence['sentence']
            r = requests.post(host_address, params=props, headers=headers, data=sent.encode('UTF-8'))

            json_response = json.loads(r.text, strict=False)
            for json_sent in json_response['sentences']:
                pos_sent = []
                for token in json_sent['tokens']:
                    pos_sent.append(token['pos'])

                pos_sent = " ".join(pos_sent)
                pos_corpus.write(pos_sent)

if __name__ == '__main__':

    with open("core_nlp_spanish.props", mode="r") as props_file:
        props = {'properties': props_file.read().replace('\n', '').replace(' ', '')}
        print(props)
        tag_corpus("training.txt", host_address="http://146.193.224.53:9000/", props=props)
