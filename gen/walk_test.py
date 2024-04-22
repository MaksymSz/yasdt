from antlr4 import *
from gen.ExpressionGrammarLexer import ExpressionGrammarLexer
from gen.ExpressionGrammarParser import ExpressionGrammarParser
from gen.ExpressionListener import ExpressionListener

input_text = "2^2 + x^2 + pow((2x + 2), 2) + pow(2x + 2, 2)"
lexer = ExpressionGrammarLexer(InputStream(input_text))
stream = CommonTokenStream(lexer)
parser = ExpressionGrammarParser(stream)

tree = parser.expr()

# print(tree.toStringTree(recog=parser))

walker = ParseTreeWalker()
listener = ExpressionListener()
walker.walk(listener, tree)
exp = listener.stack.pop()
print(input_text)
print(exp)
