# Generated from C:/Users/Maksym/PycharmProjects/yasdt/grammars/ExpressionGrammar.g4 by ANTLR 4.13.1
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
        4,1,23,96,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,0,1,0,3,0,26,8,0,1,1,1,1,
        1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,42,8,2,1,
        3,1,3,1,3,1,3,1,3,1,3,3,3,50,8,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,3,8,81,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,3,9,94,8,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,0,97,
        0,25,1,0,0,0,2,32,1,0,0,0,4,41,1,0,0,0,6,49,1,0,0,0,8,51,1,0,0,0,
        10,56,1,0,0,0,12,61,1,0,0,0,14,66,1,0,0,0,16,80,1,0,0,0,18,93,1,
        0,0,0,20,26,3,2,1,0,21,22,3,2,1,0,22,23,5,11,0,0,23,24,3,0,0,0,24,
        26,1,0,0,0,25,20,1,0,0,0,25,21,1,0,0,0,26,1,1,0,0,0,27,33,3,4,2,
        0,28,29,3,4,2,0,29,30,5,12,0,0,30,31,3,2,1,0,31,33,1,0,0,0,32,27,
        1,0,0,0,32,28,1,0,0,0,33,3,1,0,0,0,34,35,5,13,0,0,35,36,3,0,0,0,
        36,37,5,14,0,0,37,42,1,0,0,0,38,42,5,9,0,0,39,42,5,10,0,0,40,42,
        3,6,3,0,41,34,1,0,0,0,41,38,1,0,0,0,41,39,1,0,0,0,41,40,1,0,0,0,
        42,5,1,0,0,0,43,50,3,8,4,0,44,50,3,10,5,0,45,50,3,12,6,0,46,50,3,
        14,7,0,47,50,3,16,8,0,48,50,3,18,9,0,49,43,1,0,0,0,49,44,1,0,0,0,
        49,45,1,0,0,0,49,46,1,0,0,0,49,47,1,0,0,0,49,48,1,0,0,0,50,7,1,0,
        0,0,51,52,5,1,0,0,52,53,5,13,0,0,53,54,3,0,0,0,54,55,5,14,0,0,55,
        9,1,0,0,0,56,57,5,2,0,0,57,58,5,13,0,0,58,59,3,0,0,0,59,60,5,14,
        0,0,60,11,1,0,0,0,61,62,5,3,0,0,62,63,5,13,0,0,63,64,3,0,0,0,64,
        65,5,14,0,0,65,13,1,0,0,0,66,67,5,4,0,0,67,68,5,13,0,0,68,69,3,0,
        0,0,69,70,5,14,0,0,70,15,1,0,0,0,71,72,5,5,0,0,72,73,5,22,0,0,73,
        81,3,4,2,0,74,75,5,5,0,0,75,76,5,22,0,0,76,77,5,15,0,0,77,78,3,0,
        0,0,78,79,5,16,0,0,79,81,1,0,0,0,80,71,1,0,0,0,80,74,1,0,0,0,81,
        17,1,0,0,0,82,83,5,6,0,0,83,84,5,8,0,0,84,85,5,13,0,0,85,86,3,0,
        0,0,86,87,5,14,0,0,87,94,1,0,0,0,88,89,5,7,0,0,89,90,5,13,0,0,90,
        91,3,0,0,0,91,92,5,14,0,0,92,94,1,0,0,0,93,82,1,0,0,0,93,88,1,0,
        0,0,94,19,1,0,0,0,6,25,32,41,49,80,93
    ]

class ExpressionGrammarParser ( Parser ):

    grammarFileName = "ExpressionGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'sin'", "'cos'", "'tan'", "'cot'", "'e'", 
                     "'log_'", "'ln'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'('", "')'", "'{'", "'}'", 
                     "'+'", "'-'", "'*'", "'/'", "'.'", "'^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "LOGBASE", "VARIABLE", "CONSTANT", "ADD", "MUL", "LPAREN", 
                      "RPAREN", "LBRAC", "RBRAC", "PLUS", "MINUS", "TIMES", 
                      "DIV", "POINT", "POW", "WS" ]

    RULE_expr = 0
    RULE_term = 1
    RULE_factor = 2
    RULE_function = 3
    RULE_sinus = 4
    RULE_cosinus = 5
    RULE_tangent = 6
    RULE_cotangent = 7
    RULE_exponential = 8
    RULE_logarithm = 9

    ruleNames =  [ "expr", "term", "factor", "function", "sinus", "cosinus", 
                   "tangent", "cotangent", "exponential", "logarithm" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    LOGBASE=8
    VARIABLE=9
    CONSTANT=10
    ADD=11
    MUL=12
    LPAREN=13
    RPAREN=14
    LBRAC=15
    RBRAC=16
    PLUS=17
    MINUS=18
    TIMES=19
    DIV=20
    POINT=21
    POW=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.TermContext,0)


        def ADD(self):
            return self.getToken(ExpressionGrammarParser.ADD, 0)

        def expr(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return ExpressionGrammarParser.RULE_expr

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

        localctx = ExpressionGrammarParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.term()
                self.state = 22
                self.match(ExpressionGrammarParser.ADD)
                self.state = 23
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
            return self.getTypedRuleContext(ExpressionGrammarParser.FactorContext,0)


        def MUL(self):
            return self.getToken(ExpressionGrammarParser.MUL, 0)

        def term(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.TermContext,0)


        def getRuleIndex(self):
            return ExpressionGrammarParser.RULE_term

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

        localctx = ExpressionGrammarParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_term)
        try:
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.factor()
                self.state = 29
                self.match(ExpressionGrammarParser.MUL)
                self.state = 30
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
            return self.getToken(ExpressionGrammarParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ExpressionGrammarParser.RPAREN, 0)

        def VARIABLE(self):
            return self.getToken(ExpressionGrammarParser.VARIABLE, 0)

        def CONSTANT(self):
            return self.getToken(ExpressionGrammarParser.CONSTANT, 0)

        def function(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.FunctionContext,0)


        def getRuleIndex(self):
            return ExpressionGrammarParser.RULE_factor

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

        localctx = ExpressionGrammarParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_factor)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(ExpressionGrammarParser.LPAREN)
                self.state = 35
                self.expr()
                self.state = 36
                self.match(ExpressionGrammarParser.RPAREN)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.match(ExpressionGrammarParser.VARIABLE)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.match(ExpressionGrammarParser.CONSTANT)
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 40
                self.function()
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


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sinus(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.SinusContext,0)


        def cosinus(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.CosinusContext,0)


        def tangent(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.TangentContext,0)


        def cotangent(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.CotangentContext,0)


        def exponential(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.ExponentialContext,0)


        def logarithm(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.LogarithmContext,0)


        def getRuleIndex(self):
            return ExpressionGrammarParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = ExpressionGrammarParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.sinus()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.cosinus()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.tangent()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.cotangent()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 47
                self.exponential()
                pass
            elif token in [6, 7]:
                self.enterOuterAlt(localctx, 6)
                self.state = 48
                self.logarithm()
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


    class SinusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ExpressionGrammarParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ExpressionGrammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return ExpressionGrammarParser.RULE_sinus

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinus" ):
                listener.enterSinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinus" ):
                listener.exitSinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinus" ):
                return visitor.visitSinus(self)
            else:
                return visitor.visitChildren(self)




    def sinus(self):

        localctx = ExpressionGrammarParser.SinusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_sinus)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(ExpressionGrammarParser.T__0)
            self.state = 52
            self.match(ExpressionGrammarParser.LPAREN)
            self.state = 53
            self.expr()
            self.state = 54
            self.match(ExpressionGrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CosinusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ExpressionGrammarParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ExpressionGrammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return ExpressionGrammarParser.RULE_cosinus

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCosinus" ):
                listener.enterCosinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCosinus" ):
                listener.exitCosinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCosinus" ):
                return visitor.visitCosinus(self)
            else:
                return visitor.visitChildren(self)




    def cosinus(self):

        localctx = ExpressionGrammarParser.CosinusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_cosinus)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(ExpressionGrammarParser.T__1)
            self.state = 57
            self.match(ExpressionGrammarParser.LPAREN)
            self.state = 58
            self.expr()
            self.state = 59
            self.match(ExpressionGrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TangentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ExpressionGrammarParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ExpressionGrammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return ExpressionGrammarParser.RULE_tangent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTangent" ):
                listener.enterTangent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTangent" ):
                listener.exitTangent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTangent" ):
                return visitor.visitTangent(self)
            else:
                return visitor.visitChildren(self)




    def tangent(self):

        localctx = ExpressionGrammarParser.TangentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tangent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(ExpressionGrammarParser.T__2)
            self.state = 62
            self.match(ExpressionGrammarParser.LPAREN)
            self.state = 63
            self.expr()
            self.state = 64
            self.match(ExpressionGrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CotangentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ExpressionGrammarParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ExpressionGrammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return ExpressionGrammarParser.RULE_cotangent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCotangent" ):
                listener.enterCotangent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCotangent" ):
                listener.exitCotangent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCotangent" ):
                return visitor.visitCotangent(self)
            else:
                return visitor.visitChildren(self)




    def cotangent(self):

        localctx = ExpressionGrammarParser.CotangentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cotangent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ExpressionGrammarParser.T__3)
            self.state = 67
            self.match(ExpressionGrammarParser.LPAREN)
            self.state = 68
            self.expr()
            self.state = 69
            self.match(ExpressionGrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExponentialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POW(self):
            return self.getToken(ExpressionGrammarParser.POW, 0)

        def factor(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.FactorContext,0)


        def LBRAC(self):
            return self.getToken(ExpressionGrammarParser.LBRAC, 0)

        def expr(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.ExprContext,0)


        def RBRAC(self):
            return self.getToken(ExpressionGrammarParser.RBRAC, 0)

        def getRuleIndex(self):
            return ExpressionGrammarParser.RULE_exponential

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExponential" ):
                listener.enterExponential(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponential" ):
                listener.exitExponential(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExponential" ):
                return visitor.visitExponential(self)
            else:
                return visitor.visitChildren(self)




    def exponential(self):

        localctx = ExpressionGrammarParser.ExponentialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_exponential)
        try:
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.match(ExpressionGrammarParser.T__4)
                self.state = 72
                self.match(ExpressionGrammarParser.POW)
                self.state = 73
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.match(ExpressionGrammarParser.T__4)
                self.state = 75
                self.match(ExpressionGrammarParser.POW)
                self.state = 76
                self.match(ExpressionGrammarParser.LBRAC)
                self.state = 77
                self.expr()
                self.state = 78
                self.match(ExpressionGrammarParser.RBRAC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogarithmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOGBASE(self):
            return self.getToken(ExpressionGrammarParser.LOGBASE, 0)

        def LPAREN(self):
            return self.getToken(ExpressionGrammarParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ExpressionGrammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return ExpressionGrammarParser.RULE_logarithm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogarithm" ):
                listener.enterLogarithm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogarithm" ):
                listener.exitLogarithm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogarithm" ):
                return visitor.visitLogarithm(self)
            else:
                return visitor.visitChildren(self)




    def logarithm(self):

        localctx = ExpressionGrammarParser.LogarithmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_logarithm)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.match(ExpressionGrammarParser.T__5)
                self.state = 83
                self.match(ExpressionGrammarParser.LOGBASE)
                self.state = 84
                self.match(ExpressionGrammarParser.LPAREN)
                self.state = 85
                self.expr()
                self.state = 86
                self.match(ExpressionGrammarParser.RPAREN)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.match(ExpressionGrammarParser.T__6)
                self.state = 89
                self.match(ExpressionGrammarParser.LPAREN)
                self.state = 90
                self.expr()
                self.state = 91
                self.match(ExpressionGrammarParser.RPAREN)
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





