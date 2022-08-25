from abc import ABCMeta, abstractmethod


class AbstactGame(metaclass = ABCMeta):

    @property
    @abstractmethod
    def data_report(self):
        """ method to provide report about used data """
        pass

    @property
    @abstractmethod
    def generate_round(self, **kwargs):
        """ method to generate round for game """
        pass