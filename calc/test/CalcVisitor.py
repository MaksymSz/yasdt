# Generated from C:/Users/Maksym/PycharmProjects/yasdt/grammars/Calc.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalcParser import CalcParser
else:
    from CalcParser import CalcParser

# This class defines a complete generic visitor for a parse tree produced by CalcParser.

class CalcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalcParser#st.
    def visitSt(self, ctx:CalcParser.StContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#expr.
    def visitExpr(self, ctx:CalcParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#term.
    def visitTerm(self, ctx:CalcParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#factor.
    def visitFactor(self, ctx:CalcParser.FactorContext):
        return self.visitChildren(ctx)



del CalcParser