# Generated from javaTraductor.g4 by ANTLR 4.13.2
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
        4,1,14,109,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        5,0,29,8,0,10,0,12,0,32,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,40,8,1,1,
        1,1,1,1,1,1,1,1,2,4,2,47,8,2,11,2,12,2,48,1,3,1,3,1,3,3,3,54,8,3,
        1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,3,7,68,8,7,1,7,1,
        7,1,8,1,8,1,8,5,8,75,8,8,10,8,12,8,78,9,8,1,9,1,9,1,9,1,9,3,9,84,
        8,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,92,8,9,10,9,12,9,95,9,9,1,10,1,10,
        1,10,5,10,100,8,10,10,10,12,10,103,9,10,1,11,1,11,1,12,1,12,1,12,
        0,1,18,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,2,1,0,8,9,1,0,10,11,
        108,0,30,1,0,0,0,2,35,1,0,0,0,4,46,1,0,0,0,6,53,1,0,0,0,8,55,1,0,
        0,0,10,58,1,0,0,0,12,62,1,0,0,0,14,64,1,0,0,0,16,71,1,0,0,0,18,83,
        1,0,0,0,20,96,1,0,0,0,22,104,1,0,0,0,24,106,1,0,0,0,26,29,3,2,1,
        0,27,29,3,6,3,0,28,26,1,0,0,0,28,27,1,0,0,0,29,32,1,0,0,0,30,28,
        1,0,0,0,30,31,1,0,0,0,31,33,1,0,0,0,32,30,1,0,0,0,33,34,5,0,0,1,
        34,1,1,0,0,0,35,36,5,1,0,0,36,37,3,22,11,0,37,39,5,2,0,0,38,40,3,
        20,10,0,39,38,1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,42,5,3,0,0,
        42,43,5,4,0,0,43,44,3,4,2,0,44,3,1,0,0,0,45,47,3,6,3,0,46,45,1,0,
        0,0,47,48,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,5,1,0,0,0,50,54,
        3,8,4,0,51,54,3,10,5,0,52,54,3,12,6,0,53,50,1,0,0,0,53,51,1,0,0,
        0,53,52,1,0,0,0,54,7,1,0,0,0,55,56,5,5,0,0,56,57,3,18,9,0,57,9,1,
        0,0,0,58,59,3,24,12,0,59,60,5,6,0,0,60,61,3,18,9,0,61,11,1,0,0,0,
        62,63,3,18,9,0,63,13,1,0,0,0,64,65,3,22,11,0,65,67,5,2,0,0,66,68,
        3,16,8,0,67,66,1,0,0,0,67,68,1,0,0,0,68,69,1,0,0,0,69,70,5,3,0,0,
        70,15,1,0,0,0,71,76,3,18,9,0,72,73,5,7,0,0,73,75,3,18,9,0,74,72,
        1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,17,1,0,0,0,
        78,76,1,0,0,0,79,80,6,9,-1,0,80,84,3,14,7,0,81,84,3,24,12,0,82,84,
        5,12,0,0,83,79,1,0,0,0,83,81,1,0,0,0,83,82,1,0,0,0,84,93,1,0,0,0,
        85,86,10,5,0,0,86,87,7,0,0,0,87,92,3,18,9,6,88,89,10,4,0,0,89,90,
        7,1,0,0,90,92,3,18,9,5,91,85,1,0,0,0,91,88,1,0,0,0,92,95,1,0,0,0,
        93,91,1,0,0,0,93,94,1,0,0,0,94,19,1,0,0,0,95,93,1,0,0,0,96,101,3,
        24,12,0,97,98,5,7,0,0,98,100,3,24,12,0,99,97,1,0,0,0,100,103,1,0,
        0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,21,1,0,0,0,103,101,1,0,0,
        0,104,105,5,13,0,0,105,23,1,0,0,0,106,107,5,13,0,0,107,25,1,0,0,
        0,11,28,30,39,48,53,67,76,83,91,93,101
    ]

class javaTraductorParser ( Parser ):

    grammarFileName = "javaTraductor.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'('", "')'", "':'", "'return'", 
                     "'='", "','", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "NAME", "WS" ]

    RULE_file = 0
    RULE_funcDef = 1
    RULE_suite = 2
    RULE_stmt = 3
    RULE_returnStmt = 4
    RULE_assignStmt = 5
    RULE_exprStmt = 6
    RULE_funcCall = 7
    RULE_arguments = 8
    RULE_expr = 9
    RULE_parameters = 10
    RULE_funcName = 11
    RULE_varName = 12

    ruleNames =  [ "file", "funcDef", "suite", "stmt", "returnStmt", "assignStmt", 
                   "exprStmt", "funcCall", "arguments", "expr", "parameters", 
                   "funcName", "varName" ]

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
    NUMBER=12
    NAME=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(javaTraductorParser.EOF, 0)

        def funcDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(javaTraductorParser.FuncDefContext)
            else:
                return self.getTypedRuleContext(javaTraductorParser.FuncDefContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(javaTraductorParser.StmtContext)
            else:
                return self.getTypedRuleContext(javaTraductorParser.StmtContext,i)


        def getRuleIndex(self):
            return javaTraductorParser.RULE_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile" ):
                listener.enterFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile" ):
                listener.exitFile(self)




    def file_(self):

        localctx = javaTraductorParser.FileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 12322) != 0):
                self.state = 28
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 26
                    self.funcDef()
                    pass
                elif token in [5, 12, 13]:
                    self.state = 27
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 33
            self.match(javaTraductorParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcName(self):
            return self.getTypedRuleContext(javaTraductorParser.FuncNameContext,0)


        def suite(self):
            return self.getTypedRuleContext(javaTraductorParser.SuiteContext,0)


        def parameters(self):
            return self.getTypedRuleContext(javaTraductorParser.ParametersContext,0)


        def getRuleIndex(self):
            return javaTraductorParser.RULE_funcDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDef" ):
                listener.enterFuncDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDef" ):
                listener.exitFuncDef(self)




    def funcDef(self):

        localctx = javaTraductorParser.FuncDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_funcDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(javaTraductorParser.T__0)
            self.state = 36
            self.funcName()
            self.state = 37
            self.match(javaTraductorParser.T__1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 38
                self.parameters()


            self.state = 41
            self.match(javaTraductorParser.T__2)
            self.state = 42
            self.match(javaTraductorParser.T__3)
            self.state = 43
            self.suite()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuiteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(javaTraductorParser.StmtContext)
            else:
                return self.getTypedRuleContext(javaTraductorParser.StmtContext,i)


        def getRuleIndex(self):
            return javaTraductorParser.RULE_suite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuite" ):
                listener.enterSuite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuite" ):
                listener.exitSuite(self)




    def suite(self):

        localctx = javaTraductorParser.SuiteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_suite)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 45
                    self.stmt()

                else:
                    raise NoViableAltException(self)
                self.state = 48 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnStmt(self):
            return self.getTypedRuleContext(javaTraductorParser.ReturnStmtContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(javaTraductorParser.AssignStmtContext,0)


        def exprStmt(self):
            return self.getTypedRuleContext(javaTraductorParser.ExprStmtContext,0)


        def getRuleIndex(self):
            return javaTraductorParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = javaTraductorParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmt)
        try:
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.returnStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.assignStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.exprStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(javaTraductorParser.ExprContext,0)


        def getRuleIndex(self):
            return javaTraductorParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)




    def returnStmt(self):

        localctx = javaTraductorParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(javaTraductorParser.T__4)
            self.state = 56
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varName(self):
            return self.getTypedRuleContext(javaTraductorParser.VarNameContext,0)


        def expr(self):
            return self.getTypedRuleContext(javaTraductorParser.ExprContext,0)


        def getRuleIndex(self):
            return javaTraductorParser.RULE_assignStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)




    def assignStmt(self):

        localctx = javaTraductorParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.varName()
            self.state = 59
            self.match(javaTraductorParser.T__5)
            self.state = 60
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(javaTraductorParser.ExprContext,0)


        def getRuleIndex(self):
            return javaTraductorParser.RULE_exprStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStmt" ):
                listener.enterExprStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStmt" ):
                listener.exitExprStmt(self)




    def exprStmt(self):

        localctx = javaTraductorParser.ExprStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_exprStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcName(self):
            return self.getTypedRuleContext(javaTraductorParser.FuncNameContext,0)


        def arguments(self):
            return self.getTypedRuleContext(javaTraductorParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return javaTraductorParser.RULE_funcCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCall" ):
                listener.enterFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCall" ):
                listener.exitFuncCall(self)




    def funcCall(self):

        localctx = javaTraductorParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.funcName()
            self.state = 65
            self.match(javaTraductorParser.T__1)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12 or _la==13:
                self.state = 66
                self.arguments()


            self.state = 69
            self.match(javaTraductorParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(javaTraductorParser.ExprContext)
            else:
                return self.getTypedRuleContext(javaTraductorParser.ExprContext,i)


        def getRuleIndex(self):
            return javaTraductorParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = javaTraductorParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.expr(0)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 72
                self.match(javaTraductorParser.T__6)
                self.state = 73
                self.expr(0)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def funcCall(self):
            return self.getTypedRuleContext(javaTraductorParser.FuncCallContext,0)


        def varName(self):
            return self.getTypedRuleContext(javaTraductorParser.VarNameContext,0)


        def NUMBER(self):
            return self.getToken(javaTraductorParser.NUMBER, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(javaTraductorParser.ExprContext)
            else:
                return self.getTypedRuleContext(javaTraductorParser.ExprContext,i)


        def getRuleIndex(self):
            return javaTraductorParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = javaTraductorParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 80
                self.funcCall()
                pass

            elif la_ == 2:
                self.state = 81
                self.varName()
                pass

            elif la_ == 3:
                self.state = 82
                self.match(javaTraductorParser.NUMBER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 93
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 91
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = javaTraductorParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 85
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 86
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 87
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = javaTraductorParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 88
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 89
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 90
                        self.expr(5)
                        pass

             
                self.state = 95
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(javaTraductorParser.VarNameContext)
            else:
                return self.getTypedRuleContext(javaTraductorParser.VarNameContext,i)


        def getRuleIndex(self):
            return javaTraductorParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = javaTraductorParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.varName()
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 97
                self.match(javaTraductorParser.T__6)
                self.state = 98
                self.varName()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(javaTraductorParser.NAME, 0)

        def getRuleIndex(self):
            return javaTraductorParser.RULE_funcName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncName" ):
                listener.enterFuncName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncName" ):
                listener.exitFuncName(self)




    def funcName(self):

        localctx = javaTraductorParser.FuncNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_funcName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(javaTraductorParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(javaTraductorParser.NAME, 0)

        def getRuleIndex(self):
            return javaTraductorParser.RULE_varName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarName" ):
                listener.enterVarName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarName" ):
                listener.exitVarName(self)




    def varName(self):

        localctx = javaTraductorParser.VarNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_varName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(javaTraductorParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




