class Variable:
    def __init__(self, factor=1):
        self.factor = factor

    def __repr__(self):
        if -1 == self.factor:
            return '-x'
        elif 1 == self.factor:
            return 'x'
        else:
            return f'{self.factor}x'

        # return f'{"-" if -1 == self.factor else "" if 1 == self.factor else ""}x'

    def __add__(self, other):
        return Variable(self.factor + other.factor)

    def __sub__(self, other):
        return Variable(self.factor - other.factor)

    def __mul__(self, other):
        factor = self.factor * other.factor
        if factor == 0:
            return Constant(0)
        return Variable(factor)

    def diff(self):
        return Constant(self.factor)

    def simplify(self):
        return Constant(0) if self.factor == 0 else Variable(self.factor)

    def is_zero(self):
        return self.factor == 0

    def eval(self, x):
        return self.factor * x


class Constant:
    def __init__(self, value):
        self.value = value
        self.__factor = 1 if value >= 0 else -1

    def __repr__(self):
        return str(self.value)

    def __add__(self, other):
        return Constant(self.value + other.value)

    def __sub__(self, other):
        return Constant(self.value - other.value)

    def __mul__(self, other):
        return Constant(self.value * other.value)

    @property
    def factor(self):
        return self.__factor

    @factor.setter
    def factor(self, value):
        self.value *= value
        self.__factor = value

    def diff(self):
        return Constant(0)

    def simplify(self):
        return self

    def is_zero(self):
        return self.value == 0

    def eval(self, x):
        return self.value
