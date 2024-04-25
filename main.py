from testt import parse
import json
from functools import reduce
from yasdt.functions.power import Power
from yasdt.functions.trigonometric import Cos
from yasdt.primary import Variable

# with open('tests.json') as f:
#     tests = json.load(f)
#
# for i, input_text in enumerate(tests):
#     print(f'-----  {i}  -----')
#     expr = parse(input_text['input'])
#     print(f'expr: \t{expr}')
#
#     simp = expr.simplify()
#     # print(f'simp: \t{simp}')
#     dif = simp.diff()
#     # print(f'dif: \t{dif}')
#
#     dif_simp = dif.simplify()
#     print(f'difs: \t{dif_simp}')
#     print(f'res: \t{input_text["result"]}')

# input_text = '(x + 2x) * sin(-4x + e^3) + cos(x * x)'
input_text = '3x^2 - 5x'

expr = parse(input_text)

print(f'expr: \t{expr}')
#
# a = expr.args[0]
# print(type(a), a)

simp = expr.simplify()
print(f'simp: \t{simp}')
# print(type(simp))
dif = simp.diff()
# print(f'dif: \t{dif}')
#
#
dif_simp = dif.simplify()
print(f'difs: \t{dif_simp}')
