from yasdt.operators.mul import Mul
from yasdt.primary import Constant
import math
from yasdt.function import Function
from yasdt.operators.mul import Div
from abc import abstractmethod, ABC


class TrigFunc(Function, ABC):
    def __str__(self):
        funcname = self.__class__.__name__.lower()
        if self.factor == 1:
            f = ""
        elif self.factor < 0:
            f = "-" if self.factor == -1 else str(self.factor)
            return f'({f}{funcname}({str(self.arg)}))'
        else:
            f = str(self.factor)
        return f'{f}{funcname}({str(self.arg)})'

    def __eq__(self, other):
        raise NotImplemented


class Sin(TrigFunc):
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


class Cos(TrigFunc):

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


class Tan(TrigFunc):
    def diff(self):
        pass

    def simplify(self):
        pass

    def is_zero(self):
        pass


class Cot(TrigFunc):
    def diff(self):
        pass

    def simplify(self):
        pass

    def is_zero(self):
        pass
