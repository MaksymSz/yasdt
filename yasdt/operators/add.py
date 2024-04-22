from yasdt.operators.operator import Operator
from yasdt.primary import Constant


class Add(Operator):
    def __str__(self):
        _s = ""
        for arg in self.args:
            _s += f'{str(arg)}+'
        return _s.removesuffix('+')

    def eval(self, x):
        return sum(arg.eval(x) for arg in self.args)

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
        print('=======')
        for a in _args:
            print(a)
        print('=======')

        return Add(*_args)

    def simplify(self):
        _const = 0
        _args = []
        for arg in self.args:
            if isinstance(arg, Constant):
                _const += arg.value
            else:
                _args.append(arg)
        if _const != 0:
            _args.append(Constant(_const))
        if len(_args) == 1:
            return _args[0]
        return Add(*_args)

class Sub(Operator):
    pass