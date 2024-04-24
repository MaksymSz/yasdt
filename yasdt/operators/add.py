from yasdt.operators.operator import Operator
from yasdt.primary import Constant


class Add(Operator):
    def __str__(self):
        _s = []

        for arg in self.args:
            _s.append(f'+{str(arg)}' if arg.factor >= 0 else f'-({str(arg)})')
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
            _flatten = Add()
            for arg in self.args:
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
        for arg in f_args:
            _simple.append(arg.simplify())

        for arg in _simple:
            if isinstance(arg, Constant):
                _const += arg.value
            else:
                _args.append(arg)
        if _const != 0:
            _args.append(Constant(_const))
        if len(_args) == 1:
            return _args[0]
        return Add(*_args)
