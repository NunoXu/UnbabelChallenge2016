def next_sentence(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield {'classification': int(line[0]),
                   'sentence': line[2:]}


def load_training_file(file_name):
    return next_sentence(file_name)
