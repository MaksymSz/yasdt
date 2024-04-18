from functions import function
from functions import primary
from basic import Expression, Operator
from functions.polynomial import Polynomial

e1 = Expression(Operator.MUL, function.Sin(primary.Variable(1)), function.Cos(primary.Variable(1)))
e2 = Expression(Operator.MUL, function.Sin(primary.Constant(0)), primary.Variable(3))

s1 = Expression(Operator.ADD, e1, e2)

print(s1)
