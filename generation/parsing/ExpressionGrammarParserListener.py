# Generated from C:/Users/Maksym/PycharmProjects/yasdt/grammar/ExpressionGrammarParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExpressionGrammarParser import ExpressionGrammarParser
else:
    from ExpressionGrammarParser import ExpressionGrammarParser

# This class defines a complete listener for a parse tree produced by ExpressionGrammarParser.
class ExpressionGrammarParserListener(ParseTreeListener):

    # Enter a parse tree produced by ExpressionGrammarParser#expr.
    def enterExpr(self, ctx:ExpressionGrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by ExpressionGrammarParser#expr.
    def exitExpr(self, ctx:ExpressionGrammarParser.ExprContext):
        pass


    # Enter a parse tree produced by ExpressionGrammarParser#term.
    def enterTerm(self, ctx:ExpressionGrammarParser.TermContext):
        pass

    # Exit a parse tree produced by ExpressionGrammarParser#term.
    def exitTerm(self, ctx:ExpressionGrammarParser.TermContext):
        pass


    # Enter a parse tree produced by ExpressionGrammarParser#factor.
    def enterFactor(self, ctx:ExpressionGrammarParser.FactorContext):
        pass

    # Exit a parse tree produced by ExpressionGrammarParser#factor.
    def exitFactor(self, ctx:ExpressionGrammarParser.FactorContext):
        pass


    # Enter a parse tree produced by ExpressionGrammarParser#function.
    def enterFunction(self, ctx:ExpressionGrammarParser.FunctionContext):
        pass

    # Exit a parse tree produced by ExpressionGrammarParser#function.
    def exitFunction(self, ctx:ExpressionGrammarParser.FunctionContext):
        pass


    # Enter a parse tree produced by ExpressionGrammarParser#sinus.
    def enterSinus(self, ctx:ExpressionGrammarParser.SinusContext):
        pass

    # Exit a parse tree produced by ExpressionGrammarParser#sinus.
    def exitSinus(self, ctx:ExpressionGrammarParser.SinusContext):
        pass


    # Enter a parse tree produced by ExpressionGrammarParser#cosinus.
    def enterCosinus(self, ctx:ExpressionGrammarParser.CosinusContext):
        pass

    # Exit a parse tree produced by ExpressionGrammarParser#cosinus.
    def exitCosinus(self, ctx:ExpressionGrammarParser.CosinusContext):
        pass


    # Enter a parse tree produced by ExpressionGrammarParser#tangent.
    def enterTangent(self, ctx:ExpressionGrammarParser.TangentContext):
        pass

    # Exit a parse tree produced by ExpressionGrammarParser#tangent.
    def exitTangent(self, ctx:ExpressionGrammarParser.TangentContext):
        pass


    # Enter a parse tree produced by ExpressionGrammarParser#cotangent.
    def enterCotangent(self, ctx:ExpressionGrammarParser.CotangentContext):
        pass

    # Exit a parse tree produced by ExpressionGrammarParser#cotangent.
    def exitCotangent(self, ctx:ExpressionGrammarParser.CotangentContext):
        pass


    # Enter a parse tree produced by ExpressionGrammarParser#exponential.
    def enterExponential(self, ctx:ExpressionGrammarParser.ExponentialContext):
        pass

    # Exit a parse tree produced by ExpressionGrammarParser#exponential.
    def exitExponential(self, ctx:ExpressionGrammarParser.ExponentialContext):
        pass


    # Enter a parse tree produced by ExpressionGrammarParser#power.
    def enterPower(self, ctx:ExpressionGrammarParser.PowerContext):
        pass

    # Exit a parse tree produced by ExpressionGrammarParser#power.
    def exitPower(self, ctx:ExpressionGrammarParser.PowerContext):
        pass


    # Enter a parse tree produced by ExpressionGrammarParser#logarithm.
    def enterLogarithm(self, ctx:ExpressionGrammarParser.LogarithmContext):
        pass

    # Exit a parse tree produced by ExpressionGrammarParser#logarithm.
    def exitLogarithm(self, ctx:ExpressionGrammarParser.LogarithmContext):
        pass


    # Enter a parse tree produced by ExpressionGrammarParser#variable.
    def enterVariable(self, ctx:ExpressionGrammarParser.VariableContext):
        pass

    # Exit a parse tree produced by ExpressionGrammarParser#variable.
    def exitVariable(self, ctx:ExpressionGrammarParser.VariableContext):
        pass


    # Enter a parse tree produced by ExpressionGrammarParser#constant.
    def enterConstant(self, ctx:ExpressionGrammarParser.ConstantContext):
        pass

    # Exit a parse tree produced by ExpressionGrammarParser#constant.
    def exitConstant(self, ctx:ExpressionGrammarParser.ConstantContext):
        pass



del ExpressionGrammarParser