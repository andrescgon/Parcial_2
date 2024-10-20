# Generated from Laplace.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,53,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,1,4,1,24,8,1,11,1,12,
        1,25,1,1,1,1,4,1,30,8,1,11,1,12,1,31,3,1,34,8,1,1,2,1,2,1,3,1,3,
        1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,4,6,48,8,6,11,6,12,6,49,1,6,1,6,
        0,0,7,1,1,3,2,5,3,7,4,9,5,11,6,13,7,1,0,4,3,0,65,90,95,95,97,122,
        4,0,48,57,65,90,95,95,97,122,1,0,48,57,3,0,9,10,13,13,32,32,57,0,
        1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,
        0,0,0,0,13,1,0,0,0,1,15,1,0,0,0,3,23,1,0,0,0,5,35,1,0,0,0,7,37,1,
        0,0,0,9,39,1,0,0,0,11,43,1,0,0,0,13,47,1,0,0,0,15,19,7,0,0,0,16,
        18,7,1,0,0,17,16,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,
        0,20,2,1,0,0,0,21,19,1,0,0,0,22,24,7,2,0,0,23,22,1,0,0,0,24,25,1,
        0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,33,1,0,0,0,27,29,5,46,0,0,28,
        30,7,2,0,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,
        0,32,34,1,0,0,0,33,27,1,0,0,0,33,34,1,0,0,0,34,4,1,0,0,0,35,36,5,
        40,0,0,36,6,1,0,0,0,37,38,5,41,0,0,38,8,1,0,0,0,39,40,5,105,0,0,
        40,41,5,110,0,0,41,42,5,116,0,0,42,10,1,0,0,0,43,44,5,100,0,0,44,
        45,5,116,0,0,45,12,1,0,0,0,46,48,7,3,0,0,47,46,1,0,0,0,48,49,1,0,
        0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,51,1,0,0,0,51,52,6,6,0,0,52,14,
        1,0,0,0,6,0,19,25,31,33,49,1,6,0,0
    ]

class LaplaceLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IDENTIFIER = 1
    NUMBER = 2
    LPAREN = 3
    RPAREN = 4
    INT = 5
    DT = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'int'", "'dt'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "NUMBER", "LPAREN", "RPAREN", "INT", "DT", "WS" ]

    ruleNames = [ "IDENTIFIER", "NUMBER", "LPAREN", "RPAREN", "INT", "DT", 
                  "WS" ]

    grammarFileName = "Laplace.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


