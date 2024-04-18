from functions import elementary
from functions import primary
from basic import Expression, Operator

e1 = Expression(Operator.MUL, elementary.Sin(primary.Variable(1)), elementary.Cos(primary.Variable(2)))
e2 = Expression(Operator.MUL, elementary.Sin(primary.Constant(0)), primary.Variable(3))


s1 = Expression(Operator.ADD, e1, e2)

print(s1)
s1_diff = s1.diff()

print(s1_diff)
print(s1_diff.simplify())
