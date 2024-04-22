from yasdt.function import Function
from yasdt.operators.operator import Operator
from yasdt.primary import Constant


class Power(Function):
    def __init__(self, arg, factor=1, powarg=1):
        super().__init__(arg, factor)
        self.powarg = powarg

    def __str__(self):
        f = "-" if self.factor == -1 else str(self.factor)
        f = "" if f == '1' else f

        if isinstance(self.arg, Operator):
            return f'{f}{"("}{str(self.arg)}{")"}^{self.powarg}'
        return f'{f}{str(self.arg)}^{self.powarg}'

    def __eq__(self, other):
        raise NotImplemented

    def diff(self):
        if 0 == self.powarg and self.arg.is_zero():
            raise ArithmeticError("Operation 0/0 not defined")
        arg = self.arg.diff()
        factor = self.factor * self.powarg
        if 1 == factor:
            return arg
        elif 0 == factor:
            return Constant(0)
        return Power(arg, factor=factor, powarg=self.powarg - 1)

    def simplify(self):
        arg = self.arg.simplify()
        if 0 == self.factor:
            return Constant(0)
        elif 0 == self.powarg:
            return Constant(1)
        elif 1 == self.powarg:
            return self.arg
        return Power(arg, factor=self.factor)

    def is_zero(self):
        raise NotImplemented
