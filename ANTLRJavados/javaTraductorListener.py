# Generated from javaTraductor.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .javaTraductorParser import javaTraductorParser
else:
    from javaTraductorParser import javaTraductorParser

# This class defines a complete listener for a parse tree produced by javaTraductorParser.
class javaTraductorListener(ParseTreeListener):

    # Enter a parse tree produced by javaTraductorParser#file.
    def enterFile(self, ctx:javaTraductorParser.FileContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#file.
    def exitFile(self, ctx:javaTraductorParser.FileContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#funcDef.
    def enterFuncDef(self, ctx:javaTraductorParser.FuncDefContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#funcDef.
    def exitFuncDef(self, ctx:javaTraductorParser.FuncDefContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#suite.
    def enterSuite(self, ctx:javaTraductorParser.SuiteContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#suite.
    def exitSuite(self, ctx:javaTraductorParser.SuiteContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#stmt.
    def enterStmt(self, ctx:javaTraductorParser.StmtContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#stmt.
    def exitStmt(self, ctx:javaTraductorParser.StmtContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#returnStmt.
    def enterReturnStmt(self, ctx:javaTraductorParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#returnStmt.
    def exitReturnStmt(self, ctx:javaTraductorParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#assignStmt.
    def enterAssignStmt(self, ctx:javaTraductorParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#assignStmt.
    def exitAssignStmt(self, ctx:javaTraductorParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#exprStmt.
    def enterExprStmt(self, ctx:javaTraductorParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#exprStmt.
    def exitExprStmt(self, ctx:javaTraductorParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#funcCall.
    def enterFuncCall(self, ctx:javaTraductorParser.FuncCallContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#funcCall.
    def exitFuncCall(self, ctx:javaTraductorParser.FuncCallContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#arguments.
    def enterArguments(self, ctx:javaTraductorParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#arguments.
    def exitArguments(self, ctx:javaTraductorParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#expr.
    def enterExpr(self, ctx:javaTraductorParser.ExprContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#expr.
    def exitExpr(self, ctx:javaTraductorParser.ExprContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#parameters.
    def enterParameters(self, ctx:javaTraductorParser.ParametersContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#parameters.
    def exitParameters(self, ctx:javaTraductorParser.ParametersContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#funcName.
    def enterFuncName(self, ctx:javaTraductorParser.FuncNameContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#funcName.
    def exitFuncName(self, ctx:javaTraductorParser.FuncNameContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#varName.
    def enterVarName(self, ctx:javaTraductorParser.VarNameContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#varName.
    def exitVarName(self, ctx:javaTraductorParser.VarNameContext):
        pass



del javaTraductorParser