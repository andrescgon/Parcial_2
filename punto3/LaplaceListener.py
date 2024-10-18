# Generated from Laplace.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LaplaceParser import LaplaceParser
else:
    from LaplaceParser import LaplaceParser

# This class defines a complete listener for a parse tree produced by LaplaceParser.
class LaplaceListener(ParseTreeListener):

    # Enter a parse tree produced by LaplaceParser#expression.
    def enterExpression(self, ctx:LaplaceParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#expression.
    def exitExpression(self, ctx:LaplaceParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#integral.
    def enterIntegral(self, ctx:LaplaceParser.IntegralContext):
        pass

    # Exit a parse tree produced by LaplaceParser#integral.
    def exitIntegral(self, ctx:LaplaceParser.IntegralContext):
        pass


    # Enter a parse tree produced by LaplaceParser#function.
    def enterFunction(self, ctx:LaplaceParser.FunctionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#function.
    def exitFunction(self, ctx:LaplaceParser.FunctionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#argument.
    def enterArgument(self, ctx:LaplaceParser.ArgumentContext):
        pass

    # Exit a parse tree produced by LaplaceParser#argument.
    def exitArgument(self, ctx:LaplaceParser.ArgumentContext):
        pass



del LaplaceParser