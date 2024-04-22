from yasdt.operators.operator import Operator
from operator import mul
from functools import reduce
from yasdt.primary import Variable, Constant


class Mul(Operator):
    def __str__(self):
        _s = ""
        for arg in self.args:
            _s += f'{str(arg)}*'
        return _s.removesuffix("*")

    def eval(self, x):
        return reduce(mul, self.args, 1)

    def flatten(self):
        if len(self.args) == 1:
            return self.args[0]
        else:
            _flatten = Mul()
            for arg in self.args:
                if isinstance(arg, Mul):
                    _flatten.args += arg.flatten().args
                else:
                    _flatten.args.append(arg)
            return _flatten

    def diff(self, simplify=False):
        # TODO: add diff of multiplication, not only for 2 args
        # _difs = [arg.diff() for arg in self.args]
        # _args = [self.args[:i] + self.args[i:]]

        pass

    def simplify(self):
        _factor = 1
        _args = []
        _flag = False
        _simple = []
        for arg in self.args:
            _simple.append(arg.simplify())

        for arg in _simple:
            if isinstance(arg, Constant):
                _factor *= arg.value
            elif isinstance(arg, Variable):
                _factor *= arg.factor
                _flag = True
            else:
                _args.append(arg)

        if _flag:
            _args.append(Variable(_factor))
        elif len(_args) == 1:
            _args[0].factor *= _factor
            return _args[0]
        else:
            _args.append(Constant(_factor))
        if _factor == 0:
            return Constant(0)

        return Mul(*_args)


class Div(Operator):
    pass
