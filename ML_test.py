from Feature.NGramFeature import ProbabilityFeature
from Feature.NGramFeature import StandardDeviationFeature

PATH = "corpus.arpa"
stdF = StandardDeviationFeature.StandardDeviationFeature(PATH)
pF = ProbabilityFeature.Probability(PATH)

