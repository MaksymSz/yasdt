from yasdt.core import Function
from yasdt.operators.operator import Operator
from yasdt.operators.mul import Mul
from yasdt.primary import Variable, Constant
import math


class Exponent(Function):
    def __repr__(self):
        f = "-" if self.factor == -1 else str(self.factor)
        f = "" if f == '1' else f
        if isinstance(self.arg, Operator):
            return f'{f}e^{"{"}{str(self.arg)}{"}"}'
        return f'{f}e^{str(self.arg)}'

    def __eq__(self, other):
        return self.arg is other.arg

    def diff(self):
        if isinstance(self.arg, Constant):
            return Constant(0)
        elif isinstance(self.arg, Variable):
            _result = Exponent(self.arg)
            _result.factor = self.factor * self.arg.factor
            return _result
        else:
            return Mul(self.arg.diff(), self)

    def simplify(self):
        arg = self.arg.simplify()
        # if isinstance(arg, Constant):
        #     return Constant(math.exp(arg.value))
        return Exponent(arg, factor=self.factor)

    def is_zero(self):
        return False

    def eval(self, x):
        return self.factor*math.exp(self.arg.eval(x))
