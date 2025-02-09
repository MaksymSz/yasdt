import math

from yasdt.function import Function
from yasdt.operators.operator import Operator
from yasdt.primary import Constant, Variable
from copy import deepcopy


class Power(Function):

    def __init__(self, arg, factor=1, powarg=1):
        super().__init__(arg, factor)
        self.powarg = powarg

    def __repr__(self):
        f = "-" if self.factor == -1 else str(self.factor)
        f = "" if f == '1' else f

        if isinstance(self.arg, Operator):
            return f'{f}{"("}{str(self.arg)}{")"}^{self.powarg}'
        return f'{f}{str(self.arg)}^{self.powarg}'

    def __eq__(self, other):
        raise NotImplemented

    def diff(self, simplify=False):
        if 0 == self.powarg and self.arg.is_zero():
            raise ArithmeticError("Operation 0/0 not defined")
        if not isinstance(self.arg, Variable):
            arg = self.arg.diff()
        else:
            arg = deepcopy(self.arg)

        if isinstance(arg, Variable):
            if self.powarg > 1 and self.powarg != 2:
                return Power(arg, self.factor * self.powarg, self.powarg - 1)
            elif 2 == self.powarg:
                return Variable(self.factor * 2)
            elif 1 == self.powarg:
                return Constant(self.factor)

        factor = self.factor * self.powarg
        if 1 == factor:
            return arg
        elif 0 == factor or isinstance(arg, Constant):
            return Constant(factor)
        return Power(arg, factor=factor, powarg=self.powarg - 1).simplify() if simplify else Power(arg, factor=factor, powarg=self.powarg - 1)

    def simplify(self):
        arg = self.arg.simplify()
        if 0 == self.factor:
            return Constant(0)
        elif 0 == self.powarg:
            return Constant(1)
        elif 1 == self.powarg:
            arg.factor *= self.factor
            return deepcopy(arg)
        return Power(arg, factor=self.factor, powarg=self.powarg)

    def is_zero(self):
        return False

    def eval(self, x):
        return self.factor*math.pow(self.arg.eval(x), self.powarg)
