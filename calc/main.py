from antlr4 import *
from calc.test.CalcLexer import CalcLexer
from calc.test.CalcParser import CalcParser
from calc.ExprTestListener import ExprTestListener

input_text = "2+2"
lexer = CalcLexer(InputStream(input_text))
stream = CommonTokenStream(lexer)
parser = CalcParser(stream)

tree = parser.expr()

# print(tree.toStringTree(recog=parser))

walker = ParseTreeWalker()
listener = ExprTestListener()
walker.walk(listener, tree)
exp = listener.stack.pop()
print(exp)
print(exp.eval(0))

for a in exp.args:
    print(type(a))
