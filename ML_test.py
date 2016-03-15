from Feature.NGramFeature.ProbabilityFeature import Probability
from Feature.NGramFeature.StandardDeviationFeature import StandardDeviationFeature

PATH = "corpus.arpa"
stdF = StandardDeviationFeature(PATH)
pF = Probability(PATH)

