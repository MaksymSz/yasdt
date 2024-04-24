from yasdt.parser import parse

input_text = '2x * 3 * x'

expr = parse(input_text)
print(expr)
print()
dif = expr.diff()
print(dif)
print(dif.eval(1))
