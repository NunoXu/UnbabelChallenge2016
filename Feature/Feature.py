from abc import ABCMeta, abstractmethod


class Feature(metaclass=ABCMeta):

    @abstractmethod
    def evaluate(self, sentence):
        pass

