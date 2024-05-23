from antlr4 import *
from generation.parsing.ExpressionGrammarLexer import ExpressionGrammarLexer
from generation.parsing.ExpressionGrammarParser import ExpressionGrammarParser
from generation.parsing.ExpressionListener import ExpressionListener


def parse(exp_to_parse: str):
    lexer = ExpressionGrammarLexer(InputStream(exp_to_parse))
    stream = CommonTokenStream(lexer)
    parser = ExpressionGrammarParser(stream)
    tree = parser.expr()

    walker = ParseTreeWalker()
    listener = ExpressionListener()
    walker.walk(listener, tree)
    return listener.stack.pop()


from yasdt.operators.operator import Operator
from yasdt.operators.add import Add
from yasdt.operators.mul import Mul
from yasdt.function import Function
from yasdt.functions.power import Power
from yasdt.functions.exponent import Exponent
from yasdt.functions.logarithm import Logarithm
from yasdt.functions.trigonometric import Sin, Cos, Tan, Cot
from yasdt.primary import Variable, Constant
from copy import deepcopy


def add_operator(o0, o1):
    return Add(deepcopy(o0), deepcopy(o1))


def mul_operator(o0, o1):
    return Mul(deepcopy(o0), deepcopy(o1))


Add.__add__ = add_operator
Mul.__add__ = add_operator
Function.__add__ = add_operator
Power.__add__ = add_operator
Exponent.__add__ = add_operator
Logarithm.__add__ = add_operator
Sin.__add__ = add_operator
Cos.__add__ = add_operator
Tan.__add__ = add_operator
Cot.__add__ = add_operator
Variable.__add__ = add_operator
Constant.__add__ = add_operator

Add.__mul__ = mul_operator
Mul.__mul__ = mul_operator
Function.__mul__ = mul_operator
Power.__mul__ = mul_operator
Exponent.__mul__ = mul_operator
Logarithm.__mul__ = mul_operator
Sin.__mul__ = mul_operator
Cos.__mul__ = mul_operator
Tan.__mul__ = mul_operator
Cot.__mul__ = mul_operator
Variable.__mul__ = mul_operator
Constant.__mul__ = mul_operator

print('operators added kkkkk')
