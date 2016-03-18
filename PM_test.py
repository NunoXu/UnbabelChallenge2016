from pymining import itemmining
from nltk.tokenize import wordpunct_tokenize

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

with open("/home/valchier/Desktop/training.txt", mode='r', encoding='latin-1') as file:
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
