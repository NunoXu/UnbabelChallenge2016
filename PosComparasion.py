from nltk import bigrams
from nltk import trigrams
import nltk
import matplotlib.pyplot as plt



def make_tokens(file_name):
    tokens_1 = []
    with open(file_name) as file_1:
        for i, line in enumerate(file_1):
            tok_list = ['<s>'] + line.split(" ")
            tok_list.append('</s>')
            tokens_1 += tok_list
    return tokens_1


def compare_pos(file_name_1, file_name_2):

    tokens_1 = make_tokens(file_name_1)
    tokens_2 = make_tokens(file_name_2)

    tri_tokens_1  = trigrams(tokens_1)
    tri_tokens_2  = trigrams(tokens_2)

    dist_1 = nltk.FreqDist(tri_tokens_1)
    dist_2 = nltk.FreqDist(tri_tokens_2)

    diff_1 = dist_1 - dist_2
    diff_2 = dist_2 - dist_1

    with open("common_pos_mt.txt", "w") as file:
        for word, freq in diff_1.most_common(20):
            line = str(word) + " " + str(freq) + '\n'
            print(line)
            file.write(line)

    with open("common_pos_hmn.txt", "w") as file:
        for word, freq in diff_2.most_common(20):
            line = str(word) + " " + str(freq) + '\n'
            print(line)
            file.write(line)


    """
    x = []
    y = []
    for i, (token, f) in enumerate(dist.items()):
        x.append(token[0])
        y.append(token[1])
        if i >= 6:
            break
    plt.bar(y, x)

    plt.show()
    """


if __name__ == '__main__':
    compare_pos('mt_pos_corpus.txt', 'hmn_pos_corpus.txt')