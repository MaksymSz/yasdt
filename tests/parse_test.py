from yasdt import parse
import json

with open('tests.json') as f:
    tests = json.load(f)

for i, input_text in enumerate(tests):
    print(f'-----  {i}  -----')
    expr = parse(input_text['input'])
    print(f'expression: \t{expr}')

    simp = expr.simplify()
    dif = simp.diff()

    dif_simp = dif.simplify()
    print(f'derivative: \t{dif_simp}')
    print(f'expected:    \t{input_text["result"]}')
    # print(f'|{i+1}|{input_text["input"]}|{dif_simp}|')
