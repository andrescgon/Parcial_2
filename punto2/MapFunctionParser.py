# Generated from MapFunction.g4 by ANTLR 4.13.2
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
        4,1,16,128,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,2,1,2,3,2,33,8,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,3,4,48,8,4,1,5,1,5,1,5,3,5,53,8,5,1,6,1,6,1,6,1,6,5,6,59,
        8,6,10,6,12,6,62,9,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,73,
        8,6,10,6,12,6,76,9,6,1,6,3,6,79,8,6,1,7,1,7,1,7,1,7,5,7,85,8,7,10,
        7,12,7,88,9,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,99,8,7,10,
        7,12,7,102,9,7,1,7,3,7,105,8,7,1,8,1,8,1,8,1,8,5,8,111,8,8,10,8,
        12,8,114,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,126,8,9,
        1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,0,129,0,20,1,0,0,0,2,23,1,
        0,0,0,4,32,1,0,0,0,6,34,1,0,0,0,8,47,1,0,0,0,10,52,1,0,0,0,12,78,
        1,0,0,0,14,104,1,0,0,0,16,106,1,0,0,0,18,117,1,0,0,0,20,21,3,2,1,
        0,21,22,5,0,0,1,22,1,1,0,0,0,23,24,5,1,0,0,24,25,5,2,0,0,25,26,3,
        4,2,0,26,27,5,3,0,0,27,28,3,10,5,0,28,29,5,4,0,0,29,3,1,0,0,0,30,
        33,5,13,0,0,31,33,3,6,3,0,32,30,1,0,0,0,32,31,1,0,0,0,33,5,1,0,0,
        0,34,35,5,5,0,0,35,36,5,13,0,0,36,37,5,6,0,0,37,38,3,8,4,0,38,7,
        1,0,0,0,39,40,5,13,0,0,40,41,5,14,0,0,41,48,5,15,0,0,42,43,5,13,
        0,0,43,44,5,7,0,0,44,45,5,13,0,0,45,46,5,2,0,0,46,48,5,4,0,0,47,
        39,1,0,0,0,47,42,1,0,0,0,48,9,1,0,0,0,49,53,3,12,6,0,50,53,3,14,
        7,0,51,53,3,16,8,0,52,49,1,0,0,0,52,50,1,0,0,0,52,51,1,0,0,0,53,
        11,1,0,0,0,54,55,5,8,0,0,55,60,5,15,0,0,56,57,5,3,0,0,57,59,5,15,
        0,0,58,56,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,63,
        1,0,0,0,62,60,1,0,0,0,63,79,5,9,0,0,64,65,5,8,0,0,65,66,5,10,0,0,
        66,67,5,13,0,0,67,74,5,10,0,0,68,69,5,3,0,0,69,70,5,10,0,0,70,71,
        5,13,0,0,71,73,5,10,0,0,72,68,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,
        0,74,75,1,0,0,0,75,77,1,0,0,0,76,74,1,0,0,0,77,79,5,9,0,0,78,54,
        1,0,0,0,78,64,1,0,0,0,79,13,1,0,0,0,80,81,5,2,0,0,81,86,5,15,0,0,
        82,83,5,3,0,0,83,85,5,15,0,0,84,82,1,0,0,0,85,88,1,0,0,0,86,84,1,
        0,0,0,86,87,1,0,0,0,87,89,1,0,0,0,88,86,1,0,0,0,89,105,5,4,0,0,90,
        91,5,2,0,0,91,92,5,10,0,0,92,93,5,13,0,0,93,100,5,10,0,0,94,95,5,
        3,0,0,95,96,5,10,0,0,96,97,5,13,0,0,97,99,5,10,0,0,98,94,1,0,0,0,
        99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,103,1,0,0,0,102,
        100,1,0,0,0,103,105,5,4,0,0,104,80,1,0,0,0,104,90,1,0,0,0,105,15,
        1,0,0,0,106,107,5,11,0,0,107,112,3,18,9,0,108,109,5,3,0,0,109,111,
        3,18,9,0,110,108,1,0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,
        1,0,0,0,113,115,1,0,0,0,114,112,1,0,0,0,115,116,5,12,0,0,116,17,
        1,0,0,0,117,118,5,10,0,0,118,119,5,13,0,0,119,120,5,10,0,0,120,125,
        5,6,0,0,121,126,5,15,0,0,122,123,5,10,0,0,123,124,5,13,0,0,124,126,
        5,10,0,0,125,121,1,0,0,0,125,122,1,0,0,0,126,19,1,0,0,0,11,32,47,
        52,60,74,78,86,100,104,112,125
    ]

class MapFunctionParser ( Parser ):

    grammarFileName = "MapFunction.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'MAP'", "'('", "','", "')'", "'lambda'", 
                     "':'", "'.'", "'['", "']'", "'''", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IDENTIFIER", "OP", "NUMBER", "WS" ]

    RULE_expr = 0
    RULE_mapFunction = 1
    RULE_functionCall = 2
    RULE_lambdaExpr = 3
    RULE_exprBody = 4
    RULE_iterable = 5
    RULE_list = 6
    RULE_tuple = 7
    RULE_dictionary = 8
    RULE_pair = 9

    ruleNames =  [ "expr", "mapFunction", "functionCall", "lambdaExpr", 
                   "exprBody", "iterable", "list", "tuple", "dictionary", 
                   "pair" ]

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
    T__10=11
    T__11=12
    IDENTIFIER=13
    OP=14
    NUMBER=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mapFunction(self):
            return self.getTypedRuleContext(MapFunctionParser.MapFunctionContext,0)


        def EOF(self):
            return self.getToken(MapFunctionParser.EOF, 0)

        def getRuleIndex(self):
            return MapFunctionParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = MapFunctionParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.mapFunction()
            self.state = 21
            self.match(MapFunctionParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(MapFunctionParser.FunctionCallContext,0)


        def iterable(self):
            return self.getTypedRuleContext(MapFunctionParser.IterableContext,0)


        def getRuleIndex(self):
            return MapFunctionParser.RULE_mapFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapFunction" ):
                listener.enterMapFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapFunction" ):
                listener.exitMapFunction(self)




    def mapFunction(self):

        localctx = MapFunctionParser.MapFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mapFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(MapFunctionParser.T__0)
            self.state = 24
            self.match(MapFunctionParser.T__1)
            self.state = 25
            self.functionCall()
            self.state = 26
            self.match(MapFunctionParser.T__2)
            self.state = 27
            self.iterable()
            self.state = 28
            self.match(MapFunctionParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MapFunctionParser.IDENTIFIER, 0)

        def lambdaExpr(self):
            return self.getTypedRuleContext(MapFunctionParser.LambdaExprContext,0)


        def getRuleIndex(self):
            return MapFunctionParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = MapFunctionParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_functionCall)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(MapFunctionParser.IDENTIFIER)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.lambdaExpr()
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


    class LambdaExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MapFunctionParser.IDENTIFIER, 0)

        def exprBody(self):
            return self.getTypedRuleContext(MapFunctionParser.ExprBodyContext,0)


        def getRuleIndex(self):
            return MapFunctionParser.RULE_lambdaExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaExpr" ):
                listener.enterLambdaExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaExpr" ):
                listener.exitLambdaExpr(self)




    def lambdaExpr(self):

        localctx = MapFunctionParser.LambdaExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_lambdaExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(MapFunctionParser.T__4)
            self.state = 35
            self.match(MapFunctionParser.IDENTIFIER)
            self.state = 36
            self.match(MapFunctionParser.T__5)
            self.state = 37
            self.exprBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MapFunctionParser.IDENTIFIER)
            else:
                return self.getToken(MapFunctionParser.IDENTIFIER, i)

        def OP(self):
            return self.getToken(MapFunctionParser.OP, 0)

        def NUMBER(self):
            return self.getToken(MapFunctionParser.NUMBER, 0)

        def getRuleIndex(self):
            return MapFunctionParser.RULE_exprBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprBody" ):
                listener.enterExprBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprBody" ):
                listener.exitExprBody(self)




    def exprBody(self):

        localctx = MapFunctionParser.ExprBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_exprBody)
        try:
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(MapFunctionParser.IDENTIFIER)
                self.state = 40
                self.match(MapFunctionParser.OP)
                self.state = 41
                self.match(MapFunctionParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(MapFunctionParser.IDENTIFIER)
                self.state = 43
                self.match(MapFunctionParser.T__6)
                self.state = 44
                self.match(MapFunctionParser.IDENTIFIER)
                self.state = 45
                self.match(MapFunctionParser.T__1)
                self.state = 46
                self.match(MapFunctionParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_(self):
            return self.getTypedRuleContext(MapFunctionParser.ListContext,0)


        def tuple_(self):
            return self.getTypedRuleContext(MapFunctionParser.TupleContext,0)


        def dictionary(self):
            return self.getTypedRuleContext(MapFunctionParser.DictionaryContext,0)


        def getRuleIndex(self):
            return MapFunctionParser.RULE_iterable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterable" ):
                listener.enterIterable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterable" ):
                listener.exitIterable(self)




    def iterable(self):

        localctx = MapFunctionParser.IterableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_iterable)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.list_()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.tuple_()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.dictionary()
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


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(MapFunctionParser.NUMBER)
            else:
                return self.getToken(MapFunctionParser.NUMBER, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MapFunctionParser.IDENTIFIER)
            else:
                return self.getToken(MapFunctionParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return MapFunctionParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)




    def list_(self):

        localctx = MapFunctionParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(MapFunctionParser.T__7)
                self.state = 55
                self.match(MapFunctionParser.NUMBER)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 56
                    self.match(MapFunctionParser.T__2)
                    self.state = 57
                    self.match(MapFunctionParser.NUMBER)
                    self.state = 62
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 63
                self.match(MapFunctionParser.T__8)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(MapFunctionParser.T__7)
                self.state = 65
                self.match(MapFunctionParser.T__9)
                self.state = 66
                self.match(MapFunctionParser.IDENTIFIER)
                self.state = 67
                self.match(MapFunctionParser.T__9)
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 68
                    self.match(MapFunctionParser.T__2)
                    self.state = 69
                    self.match(MapFunctionParser.T__9)
                    self.state = 70
                    self.match(MapFunctionParser.IDENTIFIER)
                    self.state = 71
                    self.match(MapFunctionParser.T__9)
                    self.state = 76
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 77
                self.match(MapFunctionParser.T__8)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TupleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(MapFunctionParser.NUMBER)
            else:
                return self.getToken(MapFunctionParser.NUMBER, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MapFunctionParser.IDENTIFIER)
            else:
                return self.getToken(MapFunctionParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return MapFunctionParser.RULE_tuple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple" ):
                listener.enterTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple" ):
                listener.exitTuple(self)




    def tuple_(self):

        localctx = MapFunctionParser.TupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tuple)
        self._la = 0 # Token type
        try:
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(MapFunctionParser.T__1)
                self.state = 81
                self.match(MapFunctionParser.NUMBER)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 82
                    self.match(MapFunctionParser.T__2)
                    self.state = 83
                    self.match(MapFunctionParser.NUMBER)
                    self.state = 88
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 89
                self.match(MapFunctionParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.match(MapFunctionParser.T__1)
                self.state = 91
                self.match(MapFunctionParser.T__9)
                self.state = 92
                self.match(MapFunctionParser.IDENTIFIER)
                self.state = 93
                self.match(MapFunctionParser.T__9)
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 94
                    self.match(MapFunctionParser.T__2)
                    self.state = 95
                    self.match(MapFunctionParser.T__9)
                    self.state = 96
                    self.match(MapFunctionParser.IDENTIFIER)
                    self.state = 97
                    self.match(MapFunctionParser.T__9)
                    self.state = 102
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 103
                self.match(MapFunctionParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DictionaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapFunctionParser.PairContext)
            else:
                return self.getTypedRuleContext(MapFunctionParser.PairContext,i)


        def getRuleIndex(self):
            return MapFunctionParser.RULE_dictionary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDictionary" ):
                listener.enterDictionary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDictionary" ):
                listener.exitDictionary(self)




    def dictionary(self):

        localctx = MapFunctionParser.DictionaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_dictionary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(MapFunctionParser.T__10)
            self.state = 107
            self.pair()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 108
                self.match(MapFunctionParser.T__2)
                self.state = 109
                self.pair()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115
            self.match(MapFunctionParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MapFunctionParser.IDENTIFIER)
            else:
                return self.getToken(MapFunctionParser.IDENTIFIER, i)

        def NUMBER(self):
            return self.getToken(MapFunctionParser.NUMBER, 0)

        def getRuleIndex(self):
            return MapFunctionParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)




    def pair(self):

        localctx = MapFunctionParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(MapFunctionParser.T__9)
            self.state = 118
            self.match(MapFunctionParser.IDENTIFIER)
            self.state = 119
            self.match(MapFunctionParser.T__9)
            self.state = 120
            self.match(MapFunctionParser.T__5)
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.state = 121
                self.match(MapFunctionParser.NUMBER)
                pass
            elif token in [10]:
                self.state = 122
                self.match(MapFunctionParser.T__9)
                self.state = 123
                self.match(MapFunctionParser.IDENTIFIER)
                self.state = 124
                self.match(MapFunctionParser.T__9)
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





