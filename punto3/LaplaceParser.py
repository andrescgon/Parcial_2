# Generated from Laplace.g4 by ANTLR 4.13.2
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
        4,1,7,32,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,0,1,0,
        3,0,15,8,0,3,0,17,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,
        3,3,3,30,8,3,1,3,0,0,4,0,2,4,6,0,0,31,0,16,1,0,0,0,2,18,1,0,0,0,
        4,24,1,0,0,0,6,29,1,0,0,0,8,17,3,2,1,0,9,14,3,4,2,0,10,11,5,3,0,
        0,11,12,3,6,3,0,12,13,5,4,0,0,13,15,1,0,0,0,14,10,1,0,0,0,14,15,
        1,0,0,0,15,17,1,0,0,0,16,8,1,0,0,0,16,9,1,0,0,0,17,1,1,0,0,0,18,
        19,5,5,0,0,19,20,5,3,0,0,20,21,3,4,2,0,21,22,5,4,0,0,22,23,5,6,0,
        0,23,3,1,0,0,0,24,25,5,1,0,0,25,5,1,0,0,0,26,30,3,0,0,0,27,30,5,
        2,0,0,28,30,5,1,0,0,29,26,1,0,0,0,29,27,1,0,0,0,29,28,1,0,0,0,30,
        7,1,0,0,0,3,14,16,29
    ]

class LaplaceParser ( Parser ):

    grammarFileName = "Laplace.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'int'", "'dt'" ]

    symbolicNames = [ "<INVALID>", "IDENTIFIER", "NUMBER", "LPAREN", "RPAREN", 
                      "INT", "DT", "WS" ]

    RULE_expression = 0
    RULE_integral = 1
    RULE_function = 2
    RULE_argument = 3

    ruleNames =  [ "expression", "integral", "function", "argument" ]

    EOF = Token.EOF
    IDENTIFIER=1
    NUMBER=2
    LPAREN=3
    RPAREN=4
    INT=5
    DT=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integral(self):
            return self.getTypedRuleContext(LaplaceParser.IntegralContext,0)


        def function(self):
            return self.getTypedRuleContext(LaplaceParser.FunctionContext,0)


        def LPAREN(self):
            return self.getToken(LaplaceParser.LPAREN, 0)

        def argument(self):
            return self.getTypedRuleContext(LaplaceParser.ArgumentContext,0)


        def RPAREN(self):
            return self.getToken(LaplaceParser.RPAREN, 0)

        def getRuleIndex(self):
            return LaplaceParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = LaplaceParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 16
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.integral()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 9
                self.function()
                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 10
                    self.match(LaplaceParser.LPAREN)
                    self.state = 11
                    self.argument()
                    self.state = 12
                    self.match(LaplaceParser.RPAREN)


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


    class IntegralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(LaplaceParser.INT, 0)

        def LPAREN(self):
            return self.getToken(LaplaceParser.LPAREN, 0)

        def function(self):
            return self.getTypedRuleContext(LaplaceParser.FunctionContext,0)


        def RPAREN(self):
            return self.getToken(LaplaceParser.RPAREN, 0)

        def DT(self):
            return self.getToken(LaplaceParser.DT, 0)

        def getRuleIndex(self):
            return LaplaceParser.RULE_integral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegral" ):
                listener.enterIntegral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegral" ):
                listener.exitIntegral(self)




    def integral(self):

        localctx = LaplaceParser.IntegralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_integral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(LaplaceParser.INT)
            self.state = 19
            self.match(LaplaceParser.LPAREN)
            self.state = 20
            self.function()
            self.state = 21
            self.match(LaplaceParser.RPAREN)
            self.state = 22
            self.match(LaplaceParser.DT)
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

        def IDENTIFIER(self):
            return self.getToken(LaplaceParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return LaplaceParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = LaplaceParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(LaplaceParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LaplaceParser.ExpressionContext,0)


        def NUMBER(self):
            return self.getToken(LaplaceParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(LaplaceParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return LaplaceParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = LaplaceParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_argument)
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(LaplaceParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.match(LaplaceParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





