# Generated from C:/Users/Maksym/PycharmProjects/yasdt/grammar/ExpressionGrammarParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExpressionGrammarParser import ExpressionGrammarParser
else:
    from ExpressionGrammarParser import ExpressionGrammarParser

# This class defines a complete generic visitor for a parse tree produced by ExpressionGrammarParser.

class ExpressionGrammarParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExpressionGrammarParser#expr.
    def visitExpr(self, ctx:ExpressionGrammarParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionGrammarParser#term.
    def visitTerm(self, ctx:ExpressionGrammarParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionGrammarParser#factor.
    def visitFactor(self, ctx:ExpressionGrammarParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionGrammarParser#function.
    def visitFunction(self, ctx:ExpressionGrammarParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionGrammarParser#sinus.
    def visitSinus(self, ctx:ExpressionGrammarParser.SinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionGrammarParser#cosinus.
    def visitCosinus(self, ctx:ExpressionGrammarParser.CosinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionGrammarParser#tangent.
    def visitTangent(self, ctx:ExpressionGrammarParser.TangentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionGrammarParser#cotangent.
    def visitCotangent(self, ctx:ExpressionGrammarParser.CotangentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionGrammarParser#exponential.
    def visitExponential(self, ctx:ExpressionGrammarParser.ExponentialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionGrammarParser#power.
    def visitPower(self, ctx:ExpressionGrammarParser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionGrammarParser#logarithm.
    def visitLogarithm(self, ctx:ExpressionGrammarParser.LogarithmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionGrammarParser#variable.
    def visitVariable(self, ctx:ExpressionGrammarParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionGrammarParser#constant.
    def visitConstant(self, ctx:ExpressionGrammarParser.ConstantContext):
        return self.visitChildren(ctx)



del ExpressionGrammarParser