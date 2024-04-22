from calc.test.CalcListener import CalcListener
from calc.test.CalcParser import CalcParser
from yasdt.operators.add import Add
from yasdt.operators.mul import Mul
from yasdt.primary import Constant


class ExprTestListener(CalcListener):
    def __init__(self):
        self.stack = []

    # Expr rule
    def enterExpr(self, ctx: CalcParser.ExprContext):
        pass

    def exitExpr(self, ctx: CalcParser.ExprContext):
        if ctx.getChildCount() == 3 and ctx.getChild(1).getText() == '+':
            right = self.stack.pop()
            left = self.stack.pop()

            self.stack.append(Add(right, left))
        if ctx.getChildCount() == 1:
            child = self.stack.pop()
            self.stack.append(child)

    # Term rule
    def enterTerm(self, ctx: CalcParser.TermContext):
        pass

    def exitTerm(self, ctx: CalcParser.TermContext):
        pass

    # Factor rule
    def enterFactor(self, ctx: CalcParser.FactorContext):
        pass

    def exitFactor(self, ctx: CalcParser.FactorContext):
        if ctx.getChildCount() == 1:
            child = int(ctx.getText())
            self.stack.append(Constant(child))

    def getValue(self):
        return self.stack.pop()
