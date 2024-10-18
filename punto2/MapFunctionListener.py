# Generated from MapFunction.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MapFunctionParser import MapFunctionParser
else:
    from MapFunctionParser import MapFunctionParser

# This class defines a complete listener for a parse tree produced by MapFunctionParser.
class MapFunctionListener(ParseTreeListener):

    # Enter a parse tree produced by MapFunctionParser#expr.
    def enterExpr(self, ctx:MapFunctionParser.ExprContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#expr.
    def exitExpr(self, ctx:MapFunctionParser.ExprContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#mapFunction.
    def enterMapFunction(self, ctx:MapFunctionParser.MapFunctionContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#mapFunction.
    def exitMapFunction(self, ctx:MapFunctionParser.MapFunctionContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#functionCall.
    def enterFunctionCall(self, ctx:MapFunctionParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#functionCall.
    def exitFunctionCall(self, ctx:MapFunctionParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#lambdaExpr.
    def enterLambdaExpr(self, ctx:MapFunctionParser.LambdaExprContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#lambdaExpr.
    def exitLambdaExpr(self, ctx:MapFunctionParser.LambdaExprContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#booleanExpr.
    def enterBooleanExpr(self, ctx:MapFunctionParser.BooleanExprContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#booleanExpr.
    def exitBooleanExpr(self, ctx:MapFunctionParser.BooleanExprContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#exprBody.
    def enterExprBody(self, ctx:MapFunctionParser.ExprBodyContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#exprBody.
    def exitExprBody(self, ctx:MapFunctionParser.ExprBodyContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#relOp.
    def enterRelOp(self, ctx:MapFunctionParser.RelOpContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#relOp.
    def exitRelOp(self, ctx:MapFunctionParser.RelOpContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#iterable.
    def enterIterable(self, ctx:MapFunctionParser.IterableContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#iterable.
    def exitIterable(self, ctx:MapFunctionParser.IterableContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#list.
    def enterList(self, ctx:MapFunctionParser.ListContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#list.
    def exitList(self, ctx:MapFunctionParser.ListContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#tuple.
    def enterTuple(self, ctx:MapFunctionParser.TupleContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#tuple.
    def exitTuple(self, ctx:MapFunctionParser.TupleContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#dictionary.
    def enterDictionary(self, ctx:MapFunctionParser.DictionaryContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#dictionary.
    def exitDictionary(self, ctx:MapFunctionParser.DictionaryContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#listElement.
    def enterListElement(self, ctx:MapFunctionParser.ListElementContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#listElement.
    def exitListElement(self, ctx:MapFunctionParser.ListElementContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#pair.
    def enterPair(self, ctx:MapFunctionParser.PairContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#pair.
    def exitPair(self, ctx:MapFunctionParser.PairContext):
        pass



del MapFunctionParser