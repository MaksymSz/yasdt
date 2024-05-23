from yasdt.operators.mul import Mul
from yasdt.primary import Constant
import math
from yasdt.function import Function
from yasdt.operators.mul import Div
from abc import abstractmethod, ABC
from yasdt.functions.power import Power
from copy import deepcopy


class TrigFunc(Function, ABC):
    def __repr__(self):
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
    def diff(self, simplify=False):
        return Mul(Constant(self.factor), self.arg.diff(), Cos(deepcopy(self.arg))).simplify() if simplify else Mul(
            Constant(self.factor), self.arg.diff(),
            Cos(deepcopy(self.arg)))

    def simplify(self):
        if self.factor == 0:
            return Constant(0)

        _arg = self.arg.simplify()
        # if isinstance(_arg, Constant):
        #     return Constant(math.cos(_arg.value))
        return deepcopy(self)

    def is_zero(self):
        raise NotImplemented

    def eval(self, x):
        return self.factor * math.sin(self.arg.eval(x))


class Cos(TrigFunc):

    def diff(self, simplify=False):
        return Mul(Constant(self.factor), self.arg.diff(), Sin(deepcopy(self.arg), -1)).simplify() if simplify else Mul(
            Constant(self.factor), self.arg.diff(),
            Sin(deepcopy(self.arg), -1))
        # return Mul(Constant(self.factor), Constant(2), Sin(deepcopy(self.arg), -1))

    def simplify(self):
        if self.factor == 0:
            return Constant(0)

        _arg = self.arg.simplify()
        # if isinstance(_arg, Constant):
        #     return Constant(math.cos(_arg.value))
        return deepcopy(self)

    def is_zero(self):
        raise NotImplemented

    def eval(self, x):
        return self.factor * math.cos(self.arg.eval(x))


class Tan(TrigFunc):
    def diff(self):
        _arg = self.arg.diff()
        return Div(Constant(self.factor), Power(Cos(_arg), 1, 2))

    def simplify(self):
        if self.factor == 0:
            return Constant(0)
        _arg = self.arg.simplify()
        return Tan(_arg, factor=self.factor)

    def is_zero(self):
        return self.arg.is_zero()

    def eval(self, x):
        return self.factor * math.tan(self.arg.eval(x))


class Cot(TrigFunc):
    def diff(self):
        _arg = self.arg.diff()
        return Div(Constant(self.factor), Power(Sin(_arg), -1, 2))

    def simplify(self):
        if self.factor == 0:
            return Constant(0)
        _arg = self.arg.simplify()
        return Cot(_arg, factor=self.factor)

    def is_zero(self):
        return self.arg.is_zero()

    def eval(self, x):
        return self.factor / math.tan(self.arg.eval(x))
