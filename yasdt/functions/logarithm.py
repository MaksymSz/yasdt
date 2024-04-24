from yasdt.core import Function
from yasdt.operators.operator import Operator
from yasdt.operators.mul import Div
from yasdt.primary import Variable, Constant
import math


class Logarithm(Function):
    def __init__(self, arg, factor, base):
        super().__init__(arg, factor)
        self.base = base

    def __str__(self):
        f = "" if self.factor == 1 else self.factor
        if math.e == self.base:
            return f'{f}ln({str(self.arg)})'
        return f'{f}log_{self.base}({str(self.arg)})'

    def __eq__(self, other):
        pass

    def diff(self):
        nominator = self.arg.diff()
        denominator = self.arg()
        return Div(nominator, denominator)

    def simplify(self):
        # TODO: complete implementation
        pass

    def is_zero(self):
        pass

    def eval(self, x):
        raise NotImplemented
