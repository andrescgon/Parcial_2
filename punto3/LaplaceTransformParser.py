# Generated from LaplaceTransform.g4 by ANTLR 4.13.2
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
        4,1,9,42,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,24,8,2,10,2,12,
        2,27,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,40,8,3,
        1,3,0,0,4,0,2,4,6,0,0,42,0,11,1,0,0,0,2,14,1,0,0,0,4,20,1,0,0,0,
        6,39,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,13,1,0,0,0,11,9,1,0,0,0,
        11,12,1,0,0,0,12,1,1,0,0,0,13,11,1,0,0,0,14,15,5,1,0,0,15,16,5,6,
        0,0,16,17,3,4,2,0,17,18,5,7,0,0,18,19,5,8,0,0,19,3,1,0,0,0,20,25,
        3,6,3,0,21,22,5,5,0,0,22,24,3,6,3,0,23,21,1,0,0,0,24,27,1,0,0,0,
        25,23,1,0,0,0,25,26,1,0,0,0,26,5,1,0,0,0,27,25,1,0,0,0,28,40,5,3,
        0,0,29,40,5,4,0,0,30,31,5,2,0,0,31,32,5,6,0,0,32,33,3,4,2,0,33,34,
        5,7,0,0,34,40,1,0,0,0,35,36,5,6,0,0,36,37,3,4,2,0,37,38,5,7,0,0,
        38,40,1,0,0,0,39,28,1,0,0,0,39,29,1,0,0,0,39,30,1,0,0,0,39,35,1,
        0,0,0,40,7,1,0,0,0,3,11,25,39
    ]

class LaplaceTransformParser ( Parser ):

    grammarFileName = "LaplaceTransform.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Laplace'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'('", "')'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "FUNC", "NUM", "ID", "OP", 
                      "LPAR", "RPAR", "SEMI", "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_expression = 2
    RULE_term = 3

    ruleNames =  [ "prog", "statement", "expression", "term" ]

    EOF = Token.EOF
    T__0=1
    FUNC=2
    NUM=3
    ID=4
    OP=5
    LPAR=6
    RPAR=7
    SEMI=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LaplaceTransformParser.StatementContext)
            else:
                return self.getTypedRuleContext(LaplaceTransformParser.StatementContext,i)


        def getRuleIndex(self):
            return LaplaceTransformParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = LaplaceTransformParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 8
                self.statement()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(LaplaceTransformParser.LPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(LaplaceTransformParser.ExpressionContext,0)


        def RPAR(self):
            return self.getToken(LaplaceTransformParser.RPAR, 0)

        def SEMI(self):
            return self.getToken(LaplaceTransformParser.SEMI, 0)

        def getRuleIndex(self):
            return LaplaceTransformParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = LaplaceTransformParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(LaplaceTransformParser.T__0)
            self.state = 15
            self.match(LaplaceTransformParser.LPAR)
            self.state = 16
            self.expression()
            self.state = 17
            self.match(LaplaceTransformParser.RPAR)
            self.state = 18
            self.match(LaplaceTransformParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LaplaceTransformParser.TermContext)
            else:
                return self.getTypedRuleContext(LaplaceTransformParser.TermContext,i)


        def OP(self, i:int=None):
            if i is None:
                return self.getTokens(LaplaceTransformParser.OP)
            else:
                return self.getToken(LaplaceTransformParser.OP, i)

        def getRuleIndex(self):
            return LaplaceTransformParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = LaplaceTransformParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.term()
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 21
                self.match(LaplaceTransformParser.OP)
                self.state = 22
                self.term()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def NUM(self):
            return self.getToken(LaplaceTransformParser.NUM, 0)

        def ID(self):
            return self.getToken(LaplaceTransformParser.ID, 0)

        def FUNC(self):
            return self.getToken(LaplaceTransformParser.FUNC, 0)

        def LPAR(self):
            return self.getToken(LaplaceTransformParser.LPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(LaplaceTransformParser.ExpressionContext,0)


        def RPAR(self):
            return self.getToken(LaplaceTransformParser.RPAR, 0)

        def getRuleIndex(self):
            return LaplaceTransformParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = LaplaceTransformParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_term)
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.match(LaplaceTransformParser.NUM)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.match(LaplaceTransformParser.ID)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.match(LaplaceTransformParser.FUNC)
                self.state = 31
                self.match(LaplaceTransformParser.LPAR)
                self.state = 32
                self.expression()
                self.state = 33
                self.match(LaplaceTransformParser.RPAR)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.match(LaplaceTransformParser.LPAR)
                self.state = 36
                self.expression()
                self.state = 37
                self.match(LaplaceTransformParser.RPAR)
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





