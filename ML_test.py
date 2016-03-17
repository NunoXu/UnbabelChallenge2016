from Feature.NGramFeature import ProbabilityFeature
from Feature.NGramFeature import StandardDeviationFeature
from Reader import TrainingFileReader
from sklearn import svm, cross_validation
import pickle


PATH = "4.binary"
features = [
    #StandardDeviationFeature.StandardDeviationFeature(PATH),
    ProbabilityFeature.Probability(PATH)
    ]

sentences = TrainingFileReader.load_training_file("training.txt")
counter = 0

training_set = {'features': [],
                'classifications': []}

for sentence in sentences:
    values = []
    for feature in features:
        values.append(feature.evaluate(sentence['sentence']))
    training_set['features'].append(values)
    training_set['classifications'].append(sentence['classification'])


with open('training_data_features.pickle', 'wb') as pickle_file:
    pickle.dump(training_set, pickle_file)


clf = svm.SVC(kernel='linear')
scores = cross_validation.cross_val_score(clf, training_set['features'], training_set['classifications'], cv=10)
print(scores)
"""
clf = svm.SVC()
clf.fit(training_set['features'], training_set['classifications'])
with open('SVC_model.pickle', 'wb') as pickle_file:
    pickle.dump(clf, pickle_file)
"""
