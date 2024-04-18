from abc import ABC, abstractmethod
from enum import Enum
from functions.primary import *


class Operator(Enum):
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'


class Function(ABC):
    def __init__(self, arg, factor=1):
        self.arg = arg
        self.factor = factor

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def diff(self):
        pass

    @abstractmethod
    def simplify(self):
        pass

    @abstractmethod
    def is_zero(self):
        pass


class Expression(ABC):
    def __init__(self, operator, arg1, arg2=None):
        self.arg1 = arg1
        self.arg2 = arg2
        self.operator = operator

    def __str__(self):
        a1l = ""
        a1r = ""
        a2l = ""
        a2r = ""
        if isinstance(self.arg1, Expression):
            a1l = "("
            a1r = ")"

        if isinstance(self.arg2, Expression):
            a2l = "("
            a2r = ")"

        return f'{a1l}{str(self.arg1)}{a1r}{self.operator.value}{a2l}{str(self.arg2)}{a2r}'

    def diff(self):
        if self.operator is Operator.ADD:
            return Expression(self.operator, self.arg1.diff(), self.arg2.diff())
        elif self.operator is Operator.MUL:
            arg1_new = Expression(Operator.MUL, self.arg1.diff(), self.arg2)
            arg2_new = Expression(Operator.MUL, self.arg1, self.arg2.diff())

            return Expression(Operator.ADD, arg1_new, arg2_new)
        else:
            raise ArithmeticError("Something goes wrong calling diff")

    def simplify(self):
        self.arg1 = self.arg1.simplify()
        self.arg2 = self.arg2.simplify()
        # print('-----')
        # print(type(self.arg1), self.arg1)
        # print(type(self.arg2), self.arg2)
        if self.operator is Operator.ADD:
            return self._simplify_add()

        # for multiplication
        if self.operator is Operator.MUL:
            return self._simplify_mul()

    def _simplify_add(self):
        if self.arg1.is_zero() and self.arg2.is_zero():
            return Constant(0)
        elif self.arg1.is_zero():
            return self.arg2
        elif self.arg2.is_zero():
            return self.arg1

        if isinstance(self.arg1, Constant) and isinstance(self.arg2, Constant):
            return self.arg1 + self.arg2
        elif isinstance(self.arg1, Variable) and isinstance(self.arg2, Variable):
            return self.arg1 + self.arg2
        elif type(self.arg1) is type(self.arg2):
            arg_new = type(self.arg1)()
            return arg_new

        return self

    def _simplify_mul(self):
        if isinstance(self.arg1, Constant):
            if self.arg1.value == 0:
                return Constant(0)

            if isinstance(self.arg2, Constant):
                return Constant(self.arg1 * self.arg2)
            elif isinstance(self.arg2, Variable):
                self.arg2.factor *= self.arg1.value
                return self.arg2
            elif isinstance(self.arg2, Function):
                self.arg2.factor *= self.arg1.value
                return self.arg2
            else:
                raise ArithmeticError("Something gone wrong in simplify")
        elif isinstance(self.arg1, Variable):
            if isinstance(self.arg2, Constant):
                self.arg1.factor *= self.arg2.value
                return self.arg1
            elif isinstance(self.arg2, Variable):
                self.arg1.factor *= self.arg2.factor
                return self.arg1
            elif isinstance(self.arg2, Function):
                self.arg2 = self.arg2.simplify()
                return self
            else:
                raise ArithmeticError("Something gone wrong in simplify")
        return self
