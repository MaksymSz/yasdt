from yasdt.operators.operator import Operator
from yasdt.operators.add import Add
from operator import mul
from functools import reduce
from yasdt.primary import Variable, Constant
from copy import deepcopy
from yasdt.functions.power import Power


class Mul(Operator):
    def __add__(self, other):
        raise NotImplemented

    def __sub__(self, other):
        raise NotImplemented

    def __mul__(self, other):
        return Mul(deepcopy(self), deepcopy(other))

    def __repr__(self):
        _s = []
        for arg in self.args:
            _s += f'({str(arg)})' if isinstance(arg, Operator) else f'{str(arg)}'
            _s.append('*')
        else:
            _s.pop()
        return ''.join(_s)

    def eval(self, x):
        return reduce(mul, [arg.eval(x) for arg in self.args], self.factor)

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
        _flat = self.flatten()
        if not isinstance(_flat, Operator):
            return _flat
        _args = _flat.args
        _difs = [arg.diff() for arg in _args]

        result = []
        for i in range(len(_args)):
            _a = deepcopy(_args)
            _a[i] = _difs[i]
            result.append(Mul(*_a))

        return Add(*result)

    def simplify(self):
        # print(self)
        f_args = self.flatten().args
        _factor = 1
        _args = []
        _flag = 0
        _simple = []
        for arg in f_args:
            _simple.append(arg.simplify())

        for arg in _simple:
            if isinstance(arg, Constant):
                _factor *= arg.value
            elif isinstance(arg, Variable):
                _factor *= arg.factor
                _flag += 1
            else:
                _args.append(arg)

        if _factor == 0:
            return Constant(0)

        if 0 == _flag and len(_args) != 0:
            _args[0].factor *= _factor
        elif 1 == _flag:
            _args.append(Variable(_factor))
        elif _flag > 1:
            _args.append(Power(Variable(1), _factor, _flag))
        else:
            _args.append(Constant(_factor))

        if len(_args) == 1:
            return _args[0]
        return Mul(*_args)


class Div(Operator):
    def __init__(self, *args):
        super().__init__(*args)
        if len(self.args) != 2:
            raise ArithmeticError(f"Provided not valid number of arguments to Div instance: {len(self.args)}")

    def __add__(self, other):
        raise NotImplemented

    def __sub__(self, other):
        raise NotImplemented

    def __mul__(self, other):
        return Div(Mul(deepcopy(self.args[0]), deepcopy(other)), deepcopy(self.args[1]))

    def __repr__(self):
        _s_nom = f'({self.args[0]})' if isinstance(self.args[0], Operator) else f'{self.args[0]}'
        _s_den = f'({self.args[1]})' if isinstance(self.args[1], Operator) else f'{self.args[1]}'

        return f'{_s_nom}/{_s_den}'

    def flatten(self):
        return deepcopy(self)

    def eval(self, x):
        return self.factor * self.args[0].eval(x) / self.args[1].eval(x)

    def diff(self, simplify=False):
        _nom_a = Mul(self.args[0].diff(), deepcopy(self.args[1])).simplify()
        _nom_b = Mul(self.args[0], deepcopy(self.args[1].diff())).simplify()
        # _nom_b.factor *= -1
        _nom = Add(_nom_a, _nom_b)
        _nom.factor = -1

        _den = Mul(self.args[1], self.args[1])
        return Div(_nom, _den)

    def simplify(self):
        _nom = self.args[0].simplify()
        _den = self.args[1].simplify()
        if isinstance(_den, Constant):
            return _nom
        else:
            return Div(_nom, _den)
