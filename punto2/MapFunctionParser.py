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
        4,1,28,105,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,3,2,40,8,2,1,3,1,3,1,
        3,1,3,1,3,1,4,1,4,1,4,5,4,50,8,4,10,4,12,4,53,9,4,1,5,1,5,1,5,1,
        5,1,6,1,6,1,7,1,7,1,7,3,7,64,8,7,1,8,1,8,1,8,1,8,5,8,70,8,8,10,8,
        12,8,73,9,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,81,8,9,10,9,12,9,84,9,9,
        1,9,1,9,1,10,1,10,1,10,1,10,5,10,92,8,10,10,10,12,10,95,9,10,1,10,
        1,10,1,11,1,11,1,12,1,12,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,
        16,18,20,22,24,0,5,1,0,1,2,1,0,9,10,1,0,11,16,3,0,6,6,21,24,26,27,
        3,0,6,6,21,22,26,27,99,0,26,1,0,0,0,2,29,1,0,0,0,4,39,1,0,0,0,6,
        41,1,0,0,0,8,46,1,0,0,0,10,54,1,0,0,0,12,58,1,0,0,0,14,63,1,0,0,
        0,16,65,1,0,0,0,18,76,1,0,0,0,20,87,1,0,0,0,22,98,1,0,0,0,24,100,
        1,0,0,0,26,27,3,2,1,0,27,28,5,0,0,1,28,1,1,0,0,0,29,30,7,0,0,0,30,
        31,5,3,0,0,31,32,3,4,2,0,32,33,5,4,0,0,33,34,3,14,7,0,34,35,5,5,
        0,0,35,3,1,0,0,0,36,40,5,6,0,0,37,40,5,24,0,0,38,40,3,6,3,0,39,36,
        1,0,0,0,39,37,1,0,0,0,39,38,1,0,0,0,40,5,1,0,0,0,41,42,5,7,0,0,42,
        43,5,24,0,0,43,44,5,8,0,0,44,45,3,8,4,0,45,7,1,0,0,0,46,51,3,10,
        5,0,47,48,7,1,0,0,48,50,3,10,5,0,49,47,1,0,0,0,50,53,1,0,0,0,51,
        49,1,0,0,0,51,52,1,0,0,0,52,9,1,0,0,0,53,51,1,0,0,0,54,55,5,24,0,
        0,55,56,3,12,6,0,56,57,5,26,0,0,57,11,1,0,0,0,58,59,7,2,0,0,59,13,
        1,0,0,0,60,64,3,16,8,0,61,64,3,18,9,0,62,64,3,20,10,0,63,60,1,0,
        0,0,63,61,1,0,0,0,63,62,1,0,0,0,64,15,1,0,0,0,65,66,5,17,0,0,66,
        71,3,22,11,0,67,68,5,4,0,0,68,70,3,22,11,0,69,67,1,0,0,0,70,73,1,
        0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,71,1,0,0,0,74,
        75,5,18,0,0,75,17,1,0,0,0,76,77,5,3,0,0,77,82,3,22,11,0,78,79,5,
        4,0,0,79,81,3,22,11,0,80,78,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,
        82,83,1,0,0,0,83,85,1,0,0,0,84,82,1,0,0,0,85,86,5,5,0,0,86,19,1,
        0,0,0,87,88,5,19,0,0,88,93,3,24,12,0,89,90,5,4,0,0,90,92,3,24,12,
        0,91,89,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,96,
        1,0,0,0,95,93,1,0,0,0,96,97,5,20,0,0,97,21,1,0,0,0,98,99,7,3,0,0,
        99,23,1,0,0,0,100,101,5,27,0,0,101,102,5,8,0,0,102,103,7,4,0,0,103,
        25,1,0,0,0,6,39,51,63,71,82,93
    ]

class MapFunctionParser ( Parser ):

    grammarFileName = "MapFunction.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'MAP'", "'FILTER'", "'('", "','", "')'", 
                     "'None'", "'lambda'", "':'", "'and'", "'or'", "'>'", 
                     "'<'", "'>='", "'<='", "'=='", "'!='", "'['", "']'", 
                     "'{'", "'}'", "'True'", "'False'", "'\"\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IDENTIFIER", "OP", "NUMBER", "STRING", "WS" ]

    RULE_expr = 0
    RULE_mapFunction = 1
    RULE_functionCall = 2
    RULE_lambdaExpr = 3
    RULE_booleanExpr = 4
    RULE_exprBody = 5
    RULE_relOp = 6
    RULE_iterable = 7
    RULE_list = 8
    RULE_tuple = 9
    RULE_dictionary = 10
    RULE_listElement = 11
    RULE_pair = 12

    ruleNames =  [ "expr", "mapFunction", "functionCall", "lambdaExpr", 
                   "booleanExpr", "exprBody", "relOp", "iterable", "list", 
                   "tuple", "dictionary", "listElement", "pair" ]

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
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    IDENTIFIER=24
    OP=25
    NUMBER=26
    STRING=27
    WS=28

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
            self.state = 26
            self.mapFunction()
            self.state = 27
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 30
            self.match(MapFunctionParser.T__2)
            self.state = 31
            self.functionCall()
            self.state = 32
            self.match(MapFunctionParser.T__3)
            self.state = 33
            self.iterable()
            self.state = 34
            self.match(MapFunctionParser.T__4)
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
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.match(MapFunctionParser.T__5)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.match(MapFunctionParser.IDENTIFIER)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 38
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

        def booleanExpr(self):
            return self.getTypedRuleContext(MapFunctionParser.BooleanExprContext,0)


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
            self.state = 41
            self.match(MapFunctionParser.T__6)
            self.state = 42
            self.match(MapFunctionParser.IDENTIFIER)
            self.state = 43
            self.match(MapFunctionParser.T__7)
            self.state = 44
            self.booleanExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprBody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapFunctionParser.ExprBodyContext)
            else:
                return self.getTypedRuleContext(MapFunctionParser.ExprBodyContext,i)


        def getRuleIndex(self):
            return MapFunctionParser.RULE_booleanExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanExpr" ):
                listener.enterBooleanExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanExpr" ):
                listener.exitBooleanExpr(self)




    def booleanExpr(self):

        localctx = MapFunctionParser.BooleanExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_booleanExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.exprBody()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9 or _la==10:
                self.state = 47
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 48
                self.exprBody()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def IDENTIFIER(self):
            return self.getToken(MapFunctionParser.IDENTIFIER, 0)

        def relOp(self):
            return self.getTypedRuleContext(MapFunctionParser.RelOpContext,0)


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
        self.enterRule(localctx, 10, self.RULE_exprBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(MapFunctionParser.IDENTIFIER)
            self.state = 55
            self.relOp()
            self.state = 56
            self.match(MapFunctionParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MapFunctionParser.RULE_relOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelOp" ):
                listener.enterRelOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelOp" ):
                listener.exitRelOp(self)




    def relOp(self):

        localctx = MapFunctionParser.RelOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_relOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 129024) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
        self.enterRule(localctx, 14, self.RULE_iterable)
        try:
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.list_()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.tuple_()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 62
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

        def listElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapFunctionParser.ListElementContext)
            else:
                return self.getTypedRuleContext(MapFunctionParser.ListElementContext,i)


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
        self.enterRule(localctx, 16, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(MapFunctionParser.T__16)
            self.state = 66
            self.listElement()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 67
                self.match(MapFunctionParser.T__3)
                self.state = 68
                self.listElement()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.match(MapFunctionParser.T__17)
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

        def listElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapFunctionParser.ListElementContext)
            else:
                return self.getTypedRuleContext(MapFunctionParser.ListElementContext,i)


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
        self.enterRule(localctx, 18, self.RULE_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(MapFunctionParser.T__2)
            self.state = 77
            self.listElement()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 78
                self.match(MapFunctionParser.T__3)
                self.state = 79
                self.listElement()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self.match(MapFunctionParser.T__4)
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
        self.enterRule(localctx, 20, self.RULE_dictionary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(MapFunctionParser.T__18)
            self.state = 88
            self.pair()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 89
                self.match(MapFunctionParser.T__3)
                self.state = 90
                self.pair()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self.match(MapFunctionParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(MapFunctionParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(MapFunctionParser.IDENTIFIER, 0)

        def STRING(self):
            return self.getToken(MapFunctionParser.STRING, 0)

        def getRuleIndex(self):
            return MapFunctionParser.RULE_listElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListElement" ):
                listener.enterListElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListElement" ):
                listener.exitListElement(self)




    def listElement(self):

        localctx = MapFunctionParser.ListElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_listElement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 232783936) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(MapFunctionParser.STRING)
            else:
                return self.getToken(MapFunctionParser.STRING, i)

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
        self.enterRule(localctx, 24, self.RULE_pair)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(MapFunctionParser.STRING)
            self.state = 101
            self.match(MapFunctionParser.T__7)
            self.state = 102
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 207618112) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





