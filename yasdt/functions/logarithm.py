from yasdt.core import Function
from yasdt.operators.mul import Mul, Div
from yasdt.primary import Constant
import math


class Logarithm(Function):
    def __init__(self, arg, factor=1, base=math.e):
        super().__init__(arg, factor)
        self.base = base

    def __repr__(self):
        f = "" if self.factor == 1 else self.factor
        if math.e == self.base:
            return f'{f}ln({str(self.arg)})'
        return f'{f}log_{self.base}({str(self.arg)})'

    def __eq__(self, other):
        pass

    def diff(self):
        nominator = self.arg.diff()
        if math.e == self.base:
            denominator = self.arg
        else:
            denominator = Mul(self.arg, Logarithm(Constant(self.base)))
        denominator.factor *= math.log(self.base, math.e)
        return Div(nominator, denominator)

    def simplify(self):
        _arg = self.arg.simplify()
        return Logarithm(_arg, base=self.base)

    def is_zero(self):
        pass

    def eval(self, x):
        return self.factor*math.log(self.arg.eval(x), self.base)
