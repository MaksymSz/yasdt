from yasdt.operators.operator import Operator
from yasdt.primary import Variable, Constant
from yasdt.function import Function
from yasdt.functions.power import Power
from copy import deepcopy


class Add(Operator):
    def __add__(self, other):
        return Add(deepcopy(self), deepcopy(other))

    def __sub__(self, other):
        _a = Add(deepcopy(self), deepcopy(other))
        _a.factor = -1
        return _a

    def __mul__(self, other):
        raise NotImplemented

    def __repr__(self):
        _s = []
        if self.factor < 0:
            return f'{self.args[0]}-{self.args[1]}'

        for arg in self.args:
            if arg.factor >= 0:
                if isinstance(arg, Add):
                    _s.append(f'+({str(arg)})')
                else:
                    _s.append(f'+{str(arg)}')
            else:
                if isinstance(arg, Operator):
                    _s.append(f'-({str(arg)})')
                else:
                    _s.append(str(arg))
        else:
            if '+' == _s[0][0]:
                _s[0] = _s[0][1:]
        return ''.join(_s)

    def eval(self, x):
        return self.factor * sum(arg.eval(x) for arg in self.args)

    def flatten(self):
        if len(self.args) == 1:
            return self.args[0]
        else:
            _args = deepcopy(self.args)
            if self.factor < 0:
                for arg in _args:
                    if isinstance(arg, Constant):
                        arg.value *= self.factor
                    else:
                        arg.factor *= self.factor

            _flatten = Add()
            for arg in _args:
                if isinstance(arg, Add):
                    _flatten.args += arg.flatten().args
                else:
                    _flatten.args.append(arg)
            return _flatten

    def diff(self, simplify=False):
        _args = [arg.diff() for arg in self.args]

        return Add(*_args)

    def simplify(self):
        f_args = self.flatten().args

        _const = 0
        _args = []
        _simple = []
        # print(self)
        for arg in f_args:
            _simple.append(arg.simplify())
        # print(_simple)
        # for i in _simple:
        #     print(f'\t{i}')
        _var_flag = False
        _var_factor = 0

        _class_ctr = {}

        for arg in _simple:
            if isinstance(arg, Constant):
                _const += arg.value
            elif isinstance(arg, Variable):
                _var_flag = True
                _var_factor += arg.factor
            elif not isinstance(arg, Power) and isinstance(arg, Function) and isinstance(arg.arg,
                                                                                         Variable) and 1 == arg.arg.factor:
                _class_ctr.setdefault(arg.__class__, []).append(arg.factor)
            else:
                _args.append(arg)
        if _const != 0:
            _args.append(Constant(_const))
        if _var_flag and _var_factor != 0:
            _args.append(Variable(_var_factor))
        for _c_name, _ctr in _class_ctr.items():
            _ctr = sum(_ctr)
            if _ctr != 0:
                _args.append(_c_name(Variable(1), _ctr))

        # print('------')
        # for i in _args:
        #     print(f'\t{i}')

        if len(_args) == 1:
            return _args[0]
        return Add(*_args)
