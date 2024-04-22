from yasdt import primary
from yasdt.core import Expression, Oper

e1 = Expression(Oper.MUL, elementary.Sin(primary.Variable(1)), elementary.Cos(primary.Variable(2)))
e2 = Expression(Oper.MUL, elementary.Sin(primary.Constant(0)), primary.Variable(3))


s1 = Expression(Oper.ADD, e1, e2)

print(s1)
s1_diff = s1.diff()

print(s1_diff)
print(s1_diff.simplify())


print(sum((i for i in range(5))))