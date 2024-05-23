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


