# Generated from C:/Users/Maksym/PycharmProjects/yasdt/grammars/ExpressionGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,23,166,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,
        5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,4,7,81,8,7,11,7,12,7,82,1,
        7,1,7,1,7,1,7,1,7,4,7,90,8,7,11,7,12,7,91,1,7,4,7,95,8,7,11,7,12,
        7,96,1,7,1,7,4,7,101,8,7,11,7,12,7,102,3,7,105,8,7,3,7,107,8,7,1,
        8,1,8,1,8,1,8,3,8,113,8,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,121,8,9,1,
        10,4,10,124,8,10,11,10,12,10,125,1,10,1,10,4,10,130,8,10,11,10,12,
        10,131,3,10,134,8,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,
        1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,
        1,22,1,22,1,23,4,23,161,8,23,11,23,12,23,162,1,23,1,23,0,0,24,1,
        1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,0,23,11,25,12,27,
        13,29,14,31,15,33,16,35,17,37,18,39,19,41,20,43,21,45,22,47,23,1,
        0,3,2,0,43,43,45,45,2,0,42,42,47,47,3,0,9,10,13,13,32,32,177,0,1,
        1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,
        0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,23,1,0,
        0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,
        0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,
        0,0,0,45,1,0,0,0,0,47,1,0,0,0,1,49,1,0,0,0,3,53,1,0,0,0,5,57,1,0,
        0,0,7,61,1,0,0,0,9,65,1,0,0,0,11,67,1,0,0,0,13,72,1,0,0,0,15,106,
        1,0,0,0,17,112,1,0,0,0,19,120,1,0,0,0,21,123,1,0,0,0,23,135,1,0,
        0,0,25,137,1,0,0,0,27,139,1,0,0,0,29,141,1,0,0,0,31,143,1,0,0,0,
        33,145,1,0,0,0,35,147,1,0,0,0,37,149,1,0,0,0,39,151,1,0,0,0,41,153,
        1,0,0,0,43,155,1,0,0,0,45,157,1,0,0,0,47,160,1,0,0,0,49,50,5,115,
        0,0,50,51,5,105,0,0,51,52,5,110,0,0,52,2,1,0,0,0,53,54,5,99,0,0,
        54,55,5,111,0,0,55,56,5,115,0,0,56,4,1,0,0,0,57,58,5,116,0,0,58,
        59,5,97,0,0,59,60,5,110,0,0,60,6,1,0,0,0,61,62,5,99,0,0,62,63,5,
        111,0,0,63,64,5,116,0,0,64,8,1,0,0,0,65,66,5,101,0,0,66,10,1,0,0,
        0,67,68,5,108,0,0,68,69,5,111,0,0,69,70,5,103,0,0,70,71,5,95,0,0,
        71,12,1,0,0,0,72,73,5,108,0,0,73,74,5,110,0,0,74,14,1,0,0,0,75,76,
        5,48,0,0,76,77,5,46,0,0,77,78,1,0,0,0,78,80,2,49,57,0,79,81,2,48,
        57,0,80,79,1,0,0,0,81,82,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,
        107,1,0,0,0,84,85,5,49,0,0,85,86,5,46,0,0,86,87,1,0,0,0,87,89,2,
        49,57,0,88,90,2,48,57,0,89,88,1,0,0,0,90,91,1,0,0,0,91,89,1,0,0,
        0,91,92,1,0,0,0,92,107,1,0,0,0,93,95,2,50,57,0,94,93,1,0,0,0,95,
        96,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,104,1,0,0,0,98,100,5,46,
        0,0,99,101,2,48,57,0,100,99,1,0,0,0,101,102,1,0,0,0,102,100,1,0,
        0,0,102,103,1,0,0,0,103,105,1,0,0,0,104,98,1,0,0,0,104,105,1,0,0,
        0,105,107,1,0,0,0,106,75,1,0,0,0,106,84,1,0,0,0,106,94,1,0,0,0,107,
        16,1,0,0,0,108,109,3,19,9,0,109,110,5,120,0,0,110,113,1,0,0,0,111,
        113,5,120,0,0,112,108,1,0,0,0,112,111,1,0,0,0,113,18,1,0,0,0,114,
        115,3,27,13,0,115,116,5,45,0,0,116,117,3,21,10,0,117,118,3,29,14,
        0,118,121,1,0,0,0,119,121,3,21,10,0,120,114,1,0,0,0,120,119,1,0,
        0,0,121,20,1,0,0,0,122,124,2,48,57,0,123,122,1,0,0,0,124,125,1,0,
        0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,133,1,0,0,0,127,129,5,46,
        0,0,128,130,2,48,57,0,129,128,1,0,0,0,130,131,1,0,0,0,131,129,1,
        0,0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,127,1,0,0,0,133,134,1,
        0,0,0,134,22,1,0,0,0,135,136,7,0,0,0,136,24,1,0,0,0,137,138,7,1,
        0,0,138,26,1,0,0,0,139,140,5,40,0,0,140,28,1,0,0,0,141,142,5,41,
        0,0,142,30,1,0,0,0,143,144,5,123,0,0,144,32,1,0,0,0,145,146,5,125,
        0,0,146,34,1,0,0,0,147,148,5,43,0,0,148,36,1,0,0,0,149,150,5,45,
        0,0,150,38,1,0,0,0,151,152,5,42,0,0,152,40,1,0,0,0,153,154,5,47,
        0,0,154,42,1,0,0,0,155,156,5,46,0,0,156,44,1,0,0,0,157,158,5,94,
        0,0,158,46,1,0,0,0,159,161,7,2,0,0,160,159,1,0,0,0,161,162,1,0,0,
        0,162,160,1,0,0,0,162,163,1,0,0,0,163,164,1,0,0,0,164,165,6,23,0,
        0,165,48,1,0,0,0,13,0,82,91,96,102,104,106,112,120,125,131,133,162,
        1,6,0,0
    ]

class ExpressionGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    LOGBASE = 8
    VARIABLE = 9
    CONSTANT = 10
    ADD = 11
    MUL = 12
    LPAREN = 13
    RPAREN = 14
    LBRAC = 15
    RBRAC = 16
    PLUS = 17
    MINUS = 18
    TIMES = 19
    DIV = 20
    POINT = 21
    POW = 22
    WS = 23

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'sin'", "'cos'", "'tan'", "'cot'", "'e'", "'log_'", "'ln'", 
            "'('", "')'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'.'", 
            "'^'" ]

    symbolicNames = [ "<INVALID>",
            "LOGBASE", "VARIABLE", "CONSTANT", "ADD", "MUL", "LPAREN", "RPAREN", 
            "LBRAC", "RBRAC", "PLUS", "MINUS", "TIMES", "DIV", "POINT", 
            "POW", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "LOGBASE", "VARIABLE", "CONSTANT", "NUMBER", "ADD", "MUL", 
                  "LPAREN", "RPAREN", "LBRAC", "RBRAC", "PLUS", "MINUS", 
                  "TIMES", "DIV", "POINT", "POW", "WS" ]

    grammarFileName = "ExpressionGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


