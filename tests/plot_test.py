from yasdt import parse
from yasdt.utils import plot

raw_expressions = ['2+3', 'x+x*x', 'sin(x) + cos(x + 3.14/2)', 'e^{sin(2x) + ln(x+3)}']

parsed = [parse(e) for e in raw_expressions]
plot(parsed, -2, 2, True)
