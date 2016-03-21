from Feature.NGramFeature import ProbabilityFeature
from Feature.NGramFeature import StandardDeviationFeature
from Feature.NGramFeature import UnknownWordsFeature
from Feature.HomebrewFeature import CapitalizationFeature
from Feature.HomebrewFeature import MismatchedParenthesisFeature
from Feature.HomebrewFeature import WeirdPunctuationFeature
from Feature.SyntaxFeature import MTPatternFeature
from Reader import TrainingFileReader
from sklearn import svm, cross_validation
import pickle


def write_classifications_to_file(pickle_path, file_path, new_file_path):
    with pickle.load(pickle_path) as classifier:
        with open(new_file_path, mode='w', encoding='latin-1') as writee:
            with open(file_path, mode='r', encoding='latin-1') as test_set:
                for line in test_set:
                    analysis_line = line[2:]
                    classification = classifier.classify(analysis_line) #TODO: XU REPLACE ME FOR SOMETHING GOOD
                    writee.write(str(classification) + line[1:])

PATH = "n_grams/4.binary"
CORE_NLP_HOST_ADDRESS="http://146.193.224.53:9000/"
CORE_NLP_SPANISH_PROPS="core_nlp_spanish.props"
features = [
    StandardDeviationFeature.StandardDeviationFeature(PATH),
    ProbabilityFeature.Probability(PATH),
    UnknownWordsFeature.UnknownWordsFeature(PATH),
    MTPatternFeature.MTPatternFeature(CORE_NLP_HOST_ADDRESS, CORE_NLP_SPANISH_PROPS),
    CapitalizationFeature.CapitalizationFeature(),
    MismatchedParenthesisFeature.MistmatchedParenthesisFeature(),
    WeirdPunctuationFeature.WeirdPunctuationFeature()
    ]

sentences = TrainingFileReader.load_training_file("training.txt")
counter = 0

training_set = {'features': [],
                'classifications': []}

for count, sentence in enumerate(sentences):
    values = []
    for feature in features:
        values.append(feature.evaluate(sentence['sentence']))
    training_set['features'].append(values)
    training_set['classifications'].append(sentence['classification'])

    if count % 100 == 0:
        print("Processed " + str(count) + " sentences.")



with open('training_data_features.pickle', 'wb') as pickle_file:
    pickle.dump(training_set, pickle_file)


clf = svm.SVC()
scores = cross_validation.cross_val_score(clf, training_set['features'], training_set['classifications'], cv=6)
print(scores)
"""
clf = svm.SVC()
clf.fit(training_set['features'], training_set['classifications'])
with open('SVC_model.pickle', 'wb') as pickle_file:
    pickle.dump(clf, pickle_file)
"""
