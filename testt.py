from antlr4 import *
from gen_test.parsing.ExpressionGrammarLexer import ExpressionGrammarLexer
from gen_test.parsing.ExpressionGrammarParser import ExpressionGrammarParser
from gen_test.parsing.ExpressionListener import ExpressionListener

from yasdt.primary import Variable


def parse(exp_to_parse: str):
    lexer = ExpressionGrammarLexer(InputStream(exp_to_parse))
    stream = CommonTokenStream(lexer)
    parser = ExpressionGrammarParser(stream)
    tree = parser.expr()

    walker = ParseTreeWalker()
    listener = ExpressionListener()
    walker.walk(listener, tree)
    return listener.stack.pop()


# # input_text = '(x + 2)^2 + sin(2*e^{tan(x)*cot(4)} + 3*cos(ln(x)/log_2(2))) - 1'
# input_text = '(sin(x))^2'
input_text = '2+2*2'

exp = parse(input_text)
print(exp)
dif = exp.diff()
print('dif: ', dif)
sim = dif.simplify()
print(sim)
print(type(sim))
