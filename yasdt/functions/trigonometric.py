from yasdt.operators.mul import Mul
from yasdt.primary import Constant
import math
from yasdt.function import Function


class Sin(Function):
    def __eq__(self, other):
        pass

    def __str__(self):
        return f'{self.factor if self.factor != 1 else ""}sin({str(self.arg)})'

    def diff(self):
        return Mul(self.arg.diff(), Cos(self.arg))

    def simplify(self):
        if self.factor == 0:
            return Constant(0)

        self.arg = self.arg.simplify()
        if isinstance(self.arg, Constant):
            return Constant(math.sin(self.arg.value))
        return self

    def is_zero(self):
        pass


class Cos(Function):
    def __eq__(self, other):
        pass

    def __str__(self):
        if self.factor == 1:
            f = ""
        elif self.factor < 0:
            f = "-" if self.factor == -1 else str(self.factor)
            return f'({f}cos({str(self.arg)}))'
        else:
            f = str(self.factor)
        return f'{f}cos({str(self.arg)})'

    def diff(self):
        return Mul(self.arg.diff(), Sin(self.arg, -1))

    def simplify(self):
        if self.factor == 0:
            return Constant(0)

        self.arg = self.arg.simplify()
        if isinstance(self.arg, Constant):
            return Constant(math.cos(self.arg.value))
        return self

    def is_zero(self):
        pass


class Power(Function):
    def __init__(self, arg, pow_):
        super().__init__(arg)
        self.pow_ = pow_

    def __str__(self):
        pass

    def __eq__(self, other):
        pass

    def diff(self):
        pass

    def simplify(self):
        pass

    def is_zero(self):
        pass

