from yasdt.functions.exponent import Exponent
from yasdt.functions.trigonometric import Sin, Cos
from yasdt.primary import Variable
from yasdt.operators.add import Add
from yasdt.operators.mul import Mul

ar = Add(Sin(Variable(2)), Variable(2))
ar2 = Add(Cos(Variable(2)), Cos(Variable(2)))

ex = Exponent(ar, 2)
expr = Mul(ex, ar2)

dif = ar.diff()

ddif = dif.diff()
print(type(dif))
print(dif)
print()

for a in dif.args:
    print(type(a), '\t', a)
