from yasdt.core import Function
from yasdt.operators.operator import Operator
from yasdt.operators.mul import Mul
from yasdt.primary import Variable, Constant


class Exponent(Function):
    def __str__(self):
        if isinstance(self.arg, Operator):
            return f'{self.factor}e^{"{"}{str(self.arg)}{"}"}'
        return f'{self.factor}e^{str(self.arg)}'

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
        pass

    def is_zero(self):
        return self.arg.is_zero()
