# Generated from RationalExpr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RationalExprParser import RationalExprParser
else:
    from RationalExprParser import RationalExprParser

# This class defines a complete listener for a parse tree produced by RationalExprParser.
class RationalExprListener(ParseTreeListener):

    # Enter a parse tree produced by RationalExprParser#prog.
    def enterProg(self, ctx:RationalExprParser.ProgContext):
        pass

    # Exit a parse tree produced by RationalExprParser#prog.
    def exitProg(self, ctx:RationalExprParser.ProgContext):
        pass


    # Enter a parse tree produced by RationalExprParser#expr.
    def enterExpr(self, ctx:RationalExprParser.ExprContext):
        pass

    # Exit a parse tree produced by RationalExprParser#expr.
    def exitExpr(self, ctx:RationalExprParser.ExprContext):
        pass


    # Enter a parse tree produced by RationalExprParser#term.
    def enterTerm(self, ctx:RationalExprParser.TermContext):
        pass

    # Exit a parse tree produced by RationalExprParser#term.
    def exitTerm(self, ctx:RationalExprParser.TermContext):
        pass


    # Enter a parse tree produced by RationalExprParser#factor.
    def enterFactor(self, ctx:RationalExprParser.FactorContext):
        pass

    # Exit a parse tree produced by RationalExprParser#factor.
    def exitFactor(self, ctx:RationalExprParser.FactorContext):
        pass



del RationalExprParser