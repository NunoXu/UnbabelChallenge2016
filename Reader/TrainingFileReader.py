def next_sentence(file):
    for line in file:
        yield {'classification': int(line[0]),
               'sentence': line[2:]}
    file.close()
    return False


def load_training_file(file_name):
    return next_sentence(open(file_name, 'r'))
