# Generated from C:/Users/Maksym/PycharmProjects/yasdt/grammars/Calc.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,33,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,3,1,17,8,1,1,2,1,2,1,2,1,2,1,2,3,2,24,8,2,1,3,1,3,1,3,1,
        3,1,3,3,3,31,8,3,1,3,0,0,4,0,2,4,6,0,0,31,0,8,1,0,0,0,2,16,1,0,0,
        0,4,23,1,0,0,0,6,30,1,0,0,0,8,9,3,2,1,0,9,10,5,1,0,0,10,1,1,0,0,
        0,11,17,3,4,2,0,12,13,3,4,2,0,13,14,5,2,0,0,14,15,3,2,1,0,15,17,
        1,0,0,0,16,11,1,0,0,0,16,12,1,0,0,0,17,3,1,0,0,0,18,24,3,6,3,0,19,
        20,3,6,3,0,20,21,5,3,0,0,21,22,3,4,2,0,22,24,1,0,0,0,23,18,1,0,0,
        0,23,19,1,0,0,0,24,5,1,0,0,0,25,26,5,4,0,0,26,27,3,2,1,0,27,28,5,
        5,0,0,28,31,1,0,0,0,29,31,5,6,0,0,30,25,1,0,0,0,30,29,1,0,0,0,31,
        7,1,0,0,0,3,16,23,30
    ]

class CalcParser ( Parser ):

    grammarFileName = "Calc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'a'", "'+'", "'*'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "ADD", "MUL", "LPAREN", 
                      "RPAREN", "NUMBER", "WS" ]

    RULE_st = 0
    RULE_expr = 1
    RULE_term = 2
    RULE_factor = 3

    ruleNames =  [ "st", "expr", "term", "factor" ]

    EOF = Token.EOF
    T__0=1
    ADD=2
    MUL=3
    LPAREN=4
    RPAREN=5
    NUMBER=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_st

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSt" ):
                listener.enterSt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSt" ):
                listener.exitSt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSt" ):
                return visitor.visitSt(self)
            else:
                return visitor.visitChildren(self)




    def st(self):

        localctx = CalcParser.StContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_st)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expr()
            self.state = 9
            self.match(CalcParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(CalcParser.TermContext,0)


        def ADD(self):
            return self.getToken(CalcParser.ADD, 0)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = CalcParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 16
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 12
                self.term()
                self.state = 13
                self.match(CalcParser.ADD)
                self.state = 14
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(CalcParser.FactorContext,0)


        def MUL(self):
            return self.getToken(CalcParser.MUL, 0)

        def term(self):
            return self.getTypedRuleContext(CalcParser.TermContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = CalcParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        try:
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.factor()
                self.state = 20
                self.match(CalcParser.MUL)
                self.state = 21
                self.term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(CalcParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(CalcParser.RPAREN, 0)

        def NUMBER(self):
            return self.getToken(CalcParser.NUMBER, 0)

        def getRuleIndex(self):
            return CalcParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = CalcParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(CalcParser.LPAREN)
                self.state = 26
                self.expr()
                self.state = 27
                self.match(CalcParser.RPAREN)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.match(CalcParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





