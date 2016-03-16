import re
from nltk.tokenize import wordpunct_tokenize


def tokenize_file(old_file_path, new_file_path):
     with open(new_file_path, mode='w', encoding='latin-1') as writee:
        with open(old_file_path, mode='r', encoding='latin-1') as corpus:
            for line in corpus:
                line_tokens = wordpunct_tokenize(line)
                new_line = ' '.join(line_tokens)
                writee.write(new_line + '\n')


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



