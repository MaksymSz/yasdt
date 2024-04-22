import math

from gen.ExpressionGrammarListener import ExpressionGrammarListener
from gen.ExpressionGrammarParser import ExpressionGrammarParser
from yasdt.operators.add import Add, Sub
from yasdt.operators.mul import Mul, Div
from yasdt.primary import Variable, Constant
from yasdt.functions.trigonometric import Sin, Cos, Tan, Cot
from yasdt.functions.exponent import Exponent
from yasdt.functions.power import Power
from yasdt.function import Function
from yasdt.functions.logarithm import Logarithm


class ExpressionListener(ExpressionGrammarListener):
    def __init__(self):
        self.stack = []

    def exitExpr(self, ctx: ExpressionGrammarParser.ExprContext):
        if ctx.getChildCount() == 3:
            left = self.stack.pop()
            right = self.stack.pop()
            oper = ctx.getChild(1).getText()

            if '+' == oper:
                self.stack.append(Add(right, left))
            elif '-' == oper:
                self.stack.append(Sub(right, left))
        else:
            pass

    def exitTerm(self, ctx: ExpressionGrammarParser.TermContext):
        if ctx.getChildCount() == 3:
            left = self.stack.pop()
            right = self.stack.pop()
            oper = ctx.getChild(1).getText()

            if '*' == oper:
                self.stack.append(Mul(right, left))
            elif '/' == oper:
                self.stack.append(Div(right, left))
        else:
            pass

    def exitSinus(self, ctx: ExpressionGrammarParser.SinusContext):
        child = self.stack.pop()
        self.stack.append(Sin(child))

    def exitCosinus(self, ctx: ExpressionGrammarParser.CosinusContext):
        child = self.stack.pop()
        self.stack.append(Cos(child))

    def exitTangent(self, ctx: ExpressionGrammarParser.TangentContext):
        child = self.stack.pop()
        self.stack.append(Tan(child))

    def exitCotangent(self, ctx: ExpressionGrammarParser.CotangentContext):
        child = self.stack.pop()
        self.stack.append(Cot(child))

    def exitExponential(self, ctx: ExpressionGrammarParser.ExponentialContext):
        arg = self.stack.pop()
        self.stack.append(Exponent(arg))

    def exitPower(self, ctx: ExpressionGrammarParser.PowerContext):
        arg = self.stack.pop()
        powarg = float(ctx.NUMBER().getText())
        if powarg % 1 == 0:
            powarg = int(powarg)

        if 3 == ctx.getChildCount() and isinstance(arg, Variable):
            f = arg.factor
            arg.factor = 1
            self.stack.append(Power(arg, factor=f, powarg=powarg))
        else:
            self.stack.append(Power(arg, factor=1, powarg=powarg))

    def exitLogarithm(self, ctx: ExpressionGrammarParser.LogarithmContext):
        if ctx.getChild(0).getText() == 'ln':
            base = math.e
        else:
            base = float(ctx.LOGBASE().getText()[1:])
            if base % 1 == 0:
                base = int(base)
        arg = self.stack.pop()
        self.stack.append(Logarithm(arg, factor=1, base=base))

    def exitVariable(self, ctx: ExpressionGrammarParser.VariableContext):
        if ctx.getChildCount() == 2:
            coef = float(ctx.NUMBER().getText())
            if coef % 1 == 0:
                coef = int(coef)
            self.stack.append(Variable(coef))
        else:
            self.stack.append(Variable())

    def exitConstant(self, ctx: ExpressionGrammarParser.ConstantContext):
        coef = float(ctx.NUMBER().getText())
        if coef % 1 == 0:
            coef = int(coef)
        self.stack.append(Constant(coef))
