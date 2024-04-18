from function import Function
from functions.primary import Variable, Constant


class Polynomial(Function):
    def __init__(self, coef):
        super().__init__(1)
        self.coef_ = coef

    def __str__(self):
        s = ""
        for i in range(len(self.coef_), 1, -1):
            if self.coef_[i - 1] == 0:
                continue
            s += f"{self.coef_[i - 1]}x**{i - 1}+"

        if self.coef_[0] != 0:
            s += str(self.coef_[0])
        else:
            s = s.removesuffix("+")
        return s

    def __eq__(self, other):
        return self.coef_ == other.coef_

    def diff(self):
        coefs = [i * self.coef_[i] for i in range(1, len(self.coef_))]
        return Polynomial(coef=coefs)

    # TODO: change coef_ to dictionary or sparse matrix to optimization
    def simplify(self):
        if len(self.coef_) == 0:
            return Constant(self.coef_[0])
        pass

    def is_zero(self):
        return len(self.coef_) == 0 and self.coef_[0] == 0
