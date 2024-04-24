from yasdt.parser import parse

# input_text = '2x - 2x^3*(sin(x) + cos(x*3x))'
input_text = 'log_3(x)'
# input_text = 'x + 3 + x'


expr = parse(input_text)
print(expr)
# print(expr.simplify())
print()
dif = expr.diff()
print(dif)
# print(dif.simplify())
# print(dif.eval(1))
