from abc import ABC, abstractmethod


class Operator(ABC):
    """Abstract class for math operators
    """

    def __init__(self, *args):
        self.args = [arg for arg in args]
        self.factor = 1

    @abstractmethod
    def flatten(self):
        """
        Return flatten version of operator works like:
        Operator(x, Operator(x, x)).flatten() -> Operator(x, x, x)
        Returns Operator
        -------

        """
        pass

    @abstractmethod
    def eval(self, x):
        """Evaluate numeric value of operator for given x"""
        pass

    @abstractmethod
    def diff(self, simplify=False):
        """Proceeds differentiating

        Parameters
        ----------
        simplify
        """
        pass

    @abstractmethod
    def simplify(self):
        pass
