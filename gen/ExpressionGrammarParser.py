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
        4,1,20,96,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,0,1,0,3,0,28,8,
        0,1,1,1,1,1,1,1,1,1,1,3,1,35,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,
        44,8,2,1,3,1,3,1,3,1,3,1,3,3,3,51,8,3,1,4,1,4,1,4,1,4,1,4,1,5,1,
        5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,82,8,8,1,9,1,9,1,9,3,9,87,8,9,1,10,
        1,10,1,10,1,10,1,10,3,10,94,8,10,1,10,0,0,11,0,2,4,6,8,10,12,14,
        16,18,20,0,0,96,0,27,1,0,0,0,2,34,1,0,0,0,4,43,1,0,0,0,6,50,1,0,
        0,0,8,52,1,0,0,0,10,57,1,0,0,0,12,62,1,0,0,0,14,67,1,0,0,0,16,81,
        1,0,0,0,18,86,1,0,0,0,20,93,1,0,0,0,22,28,3,2,1,0,23,24,3,2,1,0,
        24,25,5,8,0,0,25,26,3,0,0,0,26,28,1,0,0,0,27,22,1,0,0,0,27,23,1,
        0,0,0,28,1,1,0,0,0,29,35,3,4,2,0,30,31,3,4,2,0,31,32,5,9,0,0,32,
        33,3,2,1,0,33,35,1,0,0,0,34,29,1,0,0,0,34,30,1,0,0,0,35,3,1,0,0,
        0,36,37,5,10,0,0,37,38,3,0,0,0,38,39,5,11,0,0,39,44,1,0,0,0,40,44,
        3,18,9,0,41,44,3,20,10,0,42,44,3,6,3,0,43,36,1,0,0,0,43,40,1,0,0,
        0,43,41,1,0,0,0,43,42,1,0,0,0,44,5,1,0,0,0,45,51,3,8,4,0,46,51,3,
        10,5,0,47,51,3,12,6,0,48,51,3,14,7,0,49,51,3,16,8,0,50,45,1,0,0,
        0,50,46,1,0,0,0,50,47,1,0,0,0,50,48,1,0,0,0,50,49,1,0,0,0,51,7,1,
        0,0,0,52,53,5,1,0,0,53,54,5,10,0,0,54,55,3,0,0,0,55,56,5,11,0,0,
        56,9,1,0,0,0,57,58,5,2,0,0,58,59,5,10,0,0,59,60,3,0,0,0,60,61,5,
        11,0,0,61,11,1,0,0,0,62,63,5,3,0,0,63,64,5,10,0,0,64,65,3,0,0,0,
        65,66,5,11,0,0,66,13,1,0,0,0,67,68,5,4,0,0,68,69,5,10,0,0,69,70,
        3,0,0,0,70,71,5,11,0,0,71,15,1,0,0,0,72,73,5,5,0,0,73,74,5,19,0,
        0,74,82,3,4,2,0,75,76,5,5,0,0,76,77,5,19,0,0,77,78,5,12,0,0,78,79,
        3,0,0,0,79,80,5,13,0,0,80,82,1,0,0,0,81,72,1,0,0,0,81,75,1,0,0,0,
        82,17,1,0,0,0,83,84,5,7,0,0,84,87,5,6,0,0,85,87,5,6,0,0,86,83,1,
        0,0,0,86,85,1,0,0,0,87,19,1,0,0,0,88,89,5,10,0,0,89,90,5,15,0,0,
        90,91,5,7,0,0,91,94,5,11,0,0,92,94,5,7,0,0,93,88,1,0,0,0,93,92,1,
        0,0,0,94,21,1,0,0,0,7,27,34,43,50,81,86,93
    ]

class ExpressionGrammarParser ( Parser ):

    grammarFileName = "ExpressionGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'sin'", "'cos'", "'tan'", "'cot'", "'e'", 
                     "'x'", "<INVALID>", "<INVALID>", "<INVALID>", "'('", 
                     "')'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'.'", 
                     "'^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUMBER", "ADD", 
                      "MUL", "LPAREN", "RPAREN", "LBRAC", "RBRAC", "PLUS", 
                      "MINUS", "TIMES", "DIV", "POINT", "POW", "WS" ]

    RULE_expr = 0
    RULE_term = 1
    RULE_factor = 2
    RULE_function = 3
    RULE_sinus = 4
    RULE_cosinus = 5
    RULE_tangent = 6
    RULE_cotangent = 7
    RULE_exponential = 8
    RULE_variable = 9
    RULE_constant = 10

    ruleNames =  [ "expr", "term", "factor", "function", "sinus", "cosinus", 
                   "tangent", "cotangent", "exponential", "variable", "constant" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NUMBER=7
    ADD=8
    MUL=9
    LPAREN=10
    RPAREN=11
    LBRAC=12
    RBRAC=13
    PLUS=14
    MINUS=15
    TIMES=16
    DIV=17
    POINT=18
    POW=19
    WS=20

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
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.term()
                self.state = 24
                self.match(ExpressionGrammarParser.ADD)
                self.state = 25
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
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.factor()
                self.state = 31
                self.match(ExpressionGrammarParser.MUL)
                self.state = 32
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
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.match(ExpressionGrammarParser.LPAREN)
                self.state = 37
                self.expr()
                self.state = 38
                self.match(ExpressionGrammarParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.constant()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 42
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
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.sinus()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.cosinus()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.tangent()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.cotangent()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 49
                self.exponential()
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
            self.state = 52
            self.match(ExpressionGrammarParser.T__0)
            self.state = 53
            self.match(ExpressionGrammarParser.LPAREN)
            self.state = 54
            self.expr()
            self.state = 55
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
            self.state = 57
            self.match(ExpressionGrammarParser.T__1)
            self.state = 58
            self.match(ExpressionGrammarParser.LPAREN)
            self.state = 59
            self.expr()
            self.state = 60
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
            self.state = 62
            self.match(ExpressionGrammarParser.T__2)
            self.state = 63
            self.match(ExpressionGrammarParser.LPAREN)
            self.state = 64
            self.expr()
            self.state = 65
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
            self.state = 67
            self.match(ExpressionGrammarParser.T__3)
            self.state = 68
            self.match(ExpressionGrammarParser.LPAREN)
            self.state = 69
            self.expr()
            self.state = 70
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
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(ExpressionGrammarParser.T__4)
                self.state = 73
                self.match(ExpressionGrammarParser.POW)
                self.state = 74
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.match(ExpressionGrammarParser.T__4)
                self.state = 76
                self.match(ExpressionGrammarParser.POW)
                self.state = 77
                self.match(ExpressionGrammarParser.LBRAC)
                self.state = 78
                self.expr()
                self.state = 79
                self.match(ExpressionGrammarParser.RBRAC)
                pass


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
        self.enterRule(localctx, 18, self.RULE_variable)
        try:
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.match(ExpressionGrammarParser.NUMBER)
                self.state = 84
                self.match(ExpressionGrammarParser.T__5)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(ExpressionGrammarParser.T__5)
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
        self.enterRule(localctx, 20, self.RULE_constant)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.match(ExpressionGrammarParser.LPAREN)
                self.state = 89
                self.match(ExpressionGrammarParser.MINUS)
                self.state = 90
                self.match(ExpressionGrammarParser.NUMBER)
                self.state = 91
                self.match(ExpressionGrammarParser.RPAREN)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
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





