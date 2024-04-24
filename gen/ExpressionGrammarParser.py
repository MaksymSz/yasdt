# Generated from C:/Users/Maksym/PycharmProjects/yasdt/grammar/ExpressionGrammarParser.g4 by ANTLR 4.13.1
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
        4,1,26,139,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,1,0,1,0,3,0,32,8,0,1,1,1,1,1,1,1,1,1,1,3,1,39,8,1,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,3,2,48,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,57,
        8,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,
        1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,88,8,
        8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,112,8,9,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,3,10,125,8,10,1,11,1,11,1,11,3,11,130,
        8,11,1,12,1,12,1,12,1,12,1,12,3,12,137,8,12,1,12,0,0,13,0,2,4,6,
        8,10,12,14,16,18,20,22,24,0,0,143,0,31,1,0,0,0,2,38,1,0,0,0,4,47,
        1,0,0,0,6,56,1,0,0,0,8,58,1,0,0,0,10,63,1,0,0,0,12,68,1,0,0,0,14,
        73,1,0,0,0,16,87,1,0,0,0,18,111,1,0,0,0,20,124,1,0,0,0,22,129,1,
        0,0,0,24,136,1,0,0,0,26,32,3,2,1,0,27,28,3,2,1,0,28,29,5,13,0,0,
        29,30,3,0,0,0,30,32,1,0,0,0,31,26,1,0,0,0,31,27,1,0,0,0,32,1,1,0,
        0,0,33,39,3,4,2,0,34,35,3,4,2,0,35,36,5,14,0,0,36,37,3,2,1,0,37,
        39,1,0,0,0,38,33,1,0,0,0,38,34,1,0,0,0,39,3,1,0,0,0,40,41,5,15,0,
        0,41,42,3,0,0,0,42,43,5,16,0,0,43,48,1,0,0,0,44,48,3,22,11,0,45,
        48,3,24,12,0,46,48,3,6,3,0,47,40,1,0,0,0,47,44,1,0,0,0,47,45,1,0,
        0,0,47,46,1,0,0,0,48,5,1,0,0,0,49,57,3,8,4,0,50,57,3,10,5,0,51,57,
        3,12,6,0,52,57,3,14,7,0,53,57,3,16,8,0,54,57,3,18,9,0,55,57,3,20,
        10,0,56,49,1,0,0,0,56,50,1,0,0,0,56,51,1,0,0,0,56,52,1,0,0,0,56,
        53,1,0,0,0,56,54,1,0,0,0,56,55,1,0,0,0,57,7,1,0,0,0,58,59,5,1,0,
        0,59,60,5,15,0,0,60,61,3,0,0,0,61,62,5,16,0,0,62,9,1,0,0,0,63,64,
        5,2,0,0,64,65,5,15,0,0,65,66,3,0,0,0,66,67,5,16,0,0,67,11,1,0,0,
        0,68,69,5,3,0,0,69,70,5,15,0,0,70,71,3,0,0,0,71,72,5,16,0,0,72,13,
        1,0,0,0,73,74,5,4,0,0,74,75,5,15,0,0,75,76,3,0,0,0,76,77,5,16,0,
        0,77,15,1,0,0,0,78,79,5,5,0,0,79,80,5,24,0,0,80,88,3,4,2,0,81,82,
        5,5,0,0,82,83,5,24,0,0,83,84,5,17,0,0,84,85,3,0,0,0,85,86,5,18,0,
        0,86,88,1,0,0,0,87,78,1,0,0,0,87,81,1,0,0,0,88,17,1,0,0,0,89,90,
        3,22,11,0,90,91,5,24,0,0,91,92,5,11,0,0,92,112,1,0,0,0,93,94,3,24,
        12,0,94,95,5,24,0,0,95,96,5,11,0,0,96,112,1,0,0,0,97,98,5,6,0,0,
        98,99,5,15,0,0,99,100,3,4,2,0,100,101,5,7,0,0,101,102,5,11,0,0,102,
        103,5,16,0,0,103,112,1,0,0,0,104,105,5,6,0,0,105,106,5,15,0,0,106,
        107,3,0,0,0,107,108,5,7,0,0,108,109,5,11,0,0,109,110,5,16,0,0,110,
        112,1,0,0,0,111,89,1,0,0,0,111,93,1,0,0,0,111,97,1,0,0,0,111,104,
        1,0,0,0,112,19,1,0,0,0,113,114,5,8,0,0,114,115,5,12,0,0,115,116,
        5,15,0,0,116,117,3,0,0,0,117,118,5,16,0,0,118,125,1,0,0,0,119,120,
        5,9,0,0,120,121,5,15,0,0,121,122,3,0,0,0,122,123,5,16,0,0,123,125,
        1,0,0,0,124,113,1,0,0,0,124,119,1,0,0,0,125,21,1,0,0,0,126,127,5,
        11,0,0,127,130,5,10,0,0,128,130,5,10,0,0,129,126,1,0,0,0,129,128,
        1,0,0,0,130,23,1,0,0,0,131,132,5,15,0,0,132,133,5,20,0,0,133,134,
        5,11,0,0,134,137,5,16,0,0,135,137,5,11,0,0,136,131,1,0,0,0,136,135,
        1,0,0,0,137,25,1,0,0,0,9,31,38,47,56,87,111,124,129,136
    ]

class ExpressionGrammarParser ( Parser ):

    grammarFileName = "ExpressionGrammarParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'sin'", "'cos'", "'tan'", "'cot'", "'e'", 
                     "'pow'", "','", "'log'", "'ln'", "'x'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'.'", "'^'", 
                     "'_'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUMBER", "LOGBASE", 
                      "ADD", "MUL", "LPAREN", "RPAREN", "LBRAC", "RBRAC", 
                      "PLUS", "MINUS", "TIMES", "DIV", "POINT", "POW", "UNDER", 
                      "WS" ]

    RULE_expr = 0
    RULE_term = 1
    RULE_factor = 2
    RULE_function = 3
    RULE_sinus = 4
    RULE_cosinus = 5
    RULE_tangent = 6
    RULE_cotangent = 7
    RULE_exponential = 8
    RULE_power = 9
    RULE_logarithm = 10
    RULE_variable = 11
    RULE_constant = 12

    ruleNames =  [ "expr", "term", "factor", "function", "sinus", "cosinus", 
                   "tangent", "cotangent", "exponential", "power", "logarithm", 
                   "variable", "constant" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    NUMBER=11
    LOGBASE=12
    ADD=13
    MUL=14
    LPAREN=15
    RPAREN=16
    LBRAC=17
    RBRAC=18
    PLUS=19
    MINUS=20
    TIMES=21
    DIV=22
    POINT=23
    POW=24
    UNDER=25
    WS=26

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
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.term()
                self.state = 28
                self.match(ExpressionGrammarParser.ADD)
                self.state = 29
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
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.factor()
                self.state = 35
                self.match(ExpressionGrammarParser.MUL)
                self.state = 36
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

        def variable(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.VariableContext,0)


        def constant(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.ConstantContext,0)


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
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(ExpressionGrammarParser.LPAREN)
                self.state = 41
                self.expr()
                self.state = 42
                self.match(ExpressionGrammarParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.constant()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.function()
                pass


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


        def power(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.PowerContext,0)


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
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.sinus()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.cosinus()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.tangent()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                self.cotangent()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 53
                self.exponential()
                pass
            elif token in [6, 10, 11, 15]:
                self.enterOuterAlt(localctx, 6)
                self.state = 54
                self.power()
                pass
            elif token in [8, 9]:
                self.enterOuterAlt(localctx, 7)
                self.state = 55
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
            self.state = 58
            self.match(ExpressionGrammarParser.T__0)
            self.state = 59
            self.match(ExpressionGrammarParser.LPAREN)
            self.state = 60
            self.expr()
            self.state = 61
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
            self.state = 63
            self.match(ExpressionGrammarParser.T__1)
            self.state = 64
            self.match(ExpressionGrammarParser.LPAREN)
            self.state = 65
            self.expr()
            self.state = 66
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
            self.state = 68
            self.match(ExpressionGrammarParser.T__2)
            self.state = 69
            self.match(ExpressionGrammarParser.LPAREN)
            self.state = 70
            self.expr()
            self.state = 71
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
            self.state = 73
            self.match(ExpressionGrammarParser.T__3)
            self.state = 74
            self.match(ExpressionGrammarParser.LPAREN)
            self.state = 75
            self.expr()
            self.state = 76
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
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(ExpressionGrammarParser.T__4)
                self.state = 79
                self.match(ExpressionGrammarParser.POW)
                self.state = 80
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.match(ExpressionGrammarParser.T__4)
                self.state = 82
                self.match(ExpressionGrammarParser.POW)
                self.state = 83
                self.match(ExpressionGrammarParser.LBRAC)
                self.state = 84
                self.expr()
                self.state = 85
                self.match(ExpressionGrammarParser.RBRAC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PowerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.VariableContext,0)


        def POW(self):
            return self.getToken(ExpressionGrammarParser.POW, 0)

        def NUMBER(self):
            return self.getToken(ExpressionGrammarParser.NUMBER, 0)

        def constant(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.ConstantContext,0)


        def LPAREN(self):
            return self.getToken(ExpressionGrammarParser.LPAREN, 0)

        def factor(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.FactorContext,0)


        def RPAREN(self):
            return self.getToken(ExpressionGrammarParser.RPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ExpressionGrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return ExpressionGrammarParser.RULE_power

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPower" ):
                listener.enterPower(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPower" ):
                listener.exitPower(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPower" ):
                return visitor.visitPower(self)
            else:
                return visitor.visitChildren(self)




    def power(self):

        localctx = ExpressionGrammarParser.PowerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_power)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.variable()
                self.state = 90
                self.match(ExpressionGrammarParser.POW)
                self.state = 91
                self.match(ExpressionGrammarParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.constant()
                self.state = 94
                self.match(ExpressionGrammarParser.POW)
                self.state = 95
                self.match(ExpressionGrammarParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.match(ExpressionGrammarParser.T__5)
                self.state = 98
                self.match(ExpressionGrammarParser.LPAREN)
                self.state = 99
                self.factor()
                self.state = 100
                self.match(ExpressionGrammarParser.T__6)
                self.state = 101
                self.match(ExpressionGrammarParser.NUMBER)
                self.state = 102
                self.match(ExpressionGrammarParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 104
                self.match(ExpressionGrammarParser.T__5)
                self.state = 105
                self.match(ExpressionGrammarParser.LPAREN)
                self.state = 106
                self.expr()
                self.state = 107
                self.match(ExpressionGrammarParser.T__6)
                self.state = 108
                self.match(ExpressionGrammarParser.NUMBER)
                self.state = 109
                self.match(ExpressionGrammarParser.RPAREN)
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
        self.enterRule(localctx, 20, self.RULE_logarithm)
        try:
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(ExpressionGrammarParser.T__7)
                self.state = 114
                self.match(ExpressionGrammarParser.LOGBASE)
                self.state = 115
                self.match(ExpressionGrammarParser.LPAREN)
                self.state = 116
                self.expr()
                self.state = 117
                self.match(ExpressionGrammarParser.RPAREN)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.match(ExpressionGrammarParser.T__8)
                self.state = 120
                self.match(ExpressionGrammarParser.LPAREN)
                self.state = 121
                self.expr()
                self.state = 122
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


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ExpressionGrammarParser.NUMBER, 0)

        def getRuleIndex(self):
            return ExpressionGrammarParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = ExpressionGrammarParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_variable)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.match(ExpressionGrammarParser.NUMBER)
                self.state = 127
                self.match(ExpressionGrammarParser.T__9)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.match(ExpressionGrammarParser.T__9)
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


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ExpressionGrammarParser.LPAREN, 0)

        def MINUS(self):
            return self.getToken(ExpressionGrammarParser.MINUS, 0)

        def NUMBER(self):
            return self.getToken(ExpressionGrammarParser.NUMBER, 0)

        def RPAREN(self):
            return self.getToken(ExpressionGrammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return ExpressionGrammarParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = ExpressionGrammarParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_constant)
        try:
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(ExpressionGrammarParser.LPAREN)
                self.state = 132
                self.match(ExpressionGrammarParser.MINUS)
                self.state = 133
                self.match(ExpressionGrammarParser.NUMBER)
                self.state = 134
                self.match(ExpressionGrammarParser.RPAREN)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.match(ExpressionGrammarParser.NUMBER)
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





