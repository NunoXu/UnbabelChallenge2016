import re
import codecs


def clean_wiki_corpus(old_file_path, new_file_path):

    with open(new_file_path, mode='w') as writee:

        with open(old_file_path, mode='r', encoding='latin-1') as corpus:
            keep_killing = False
            for line in corpus:
                if re.search(r"<doc.*>", line) or re.search(r"</doc.*>", line):
                    writee.write('\n')
                elif re.search(r"ENDOFARTICLE\.", line):
                    keep_killing = False
                    writee.write(line)
                elif keep_killing:
                    writee.write('\n')
                elif re.search(r" Fuentes \.", line)\
                        or re.search(r" Referencias \.", line)\
                        or re.search(r" Bibliografía\ \.", line)\
                        or re.search(r" Enlaces externos \.", line)\
                        or re.search(r" Véase también \.", line)\
                        or re.search(r" Referencias y enlaces externos \.", line)\
                        or re.search(r" Galería \.", line)\
                        or re.search(r" Referencias y enlaces externos \.", line):

                    keep_killing = True
                    writee.write('\n')
                else:
                    writee.write(line)



