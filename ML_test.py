from Feature.NGramFeature import ProbabilityFeature
from Feature.NGramFeature import StandardDeviationFeature

#PATH = "corpus.arpa"
#stdF = StandardDeviationFeature.StandardDeviationFeature(PATH)
#pF = ProbabilityFeature.Probability(PATH)

from Reader import TrainingFileReader

next = TrainingFileReader.load_training_file("training.txt")
counter = 0
for i in next:
    print(i)
    counter += 1

print(counter)


