from pymining import itemmining
from nltk.tokenize import wordpunct_tokenize
from Utility import extract_partial_file
"""
with open("/home/valchier/Desktop/training.txt") as file:
    line_tokens_list = list()
    for line in file:
        line_toks = wordpunct_tokenize(line)
        line_tokens_list.append(line_toks[1:])

    relim_input = itemmining.get_relim_input(line_tokens_list)
    report = itemmining.relim(relim_input, min_support=2)

    with open("chaos.txt") as writee:
        for key in report.keys():
            writee.write(str(key) + ' ' + str(report.get(key)) + '\n')
"""
extract_partial_file("/home/valchier/Desktop/training.txt", 0.8, "ourtraining.txt", "ourtest.txt")