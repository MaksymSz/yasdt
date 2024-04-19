from abc import ABC, abstractmethod


class Function(ABC):

    def __init__(self, arg, factor=1):
        """

        :param arg:
        :param factor:
        """
        self.arg = arg
        self.factor = factor

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def diff(self):
        pass

    @abstractmethod
    def simplify(self):
        pass

    @abstractmethod
    def is_zero(self):
        pass

    # @abstractmethod
    # def eval(self, x):
    #     pass
