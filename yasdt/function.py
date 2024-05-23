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
    def __repr__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    # def __add__(self, other):
    #     if isinstance(other, self.__class__) and self.arg == other.arg:
    #         _f = self.factor + other.factor
    #         return self.__class__(deepcopy(self.arg), _f)
    #     else:
    #         return Add(deepcopy(self), deepcopy(other))
    #
    # def __sub__(self, other):
    #     if isinstance(other, self.__class__) and self.arg == other.arg:
    #         _f = self.factor - other.factor
    #         return self.__class__(deepcopy(self.arg), _f)
    #     else:
    #         _add = Add(deepcopy(self), deepcopy(other))
    #         _add.factor = -1
    #         return _add
    #
    # def __mul__(self, other):
    #     return Mul(deepcopy(self), deepcopy(other))

    @abstractmethod
    def diff(self, simplify=False):
        pass

    @abstractmethod
    def simplify(self):
        pass

    @abstractmethod
    def is_zero(self):
        pass

    @abstractmethod
    def eval(self, x):
        pass
