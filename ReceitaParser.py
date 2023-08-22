# Generated from Receita.g4 by ANTLR 4.13.0
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
        4,1,20,73,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,1,4,1,23,8,1,11,1,12,1,24,1,2,3,
        2,28,8,2,1,2,1,2,1,2,1,2,1,2,3,2,35,8,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,4,2,46,8,2,11,2,12,2,47,1,3,1,3,1,4,1,4,1,4,1,4,1,5,
        1,5,3,5,58,8,5,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,5,8,68,8,8,10,8,12,
        8,71,9,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,3,1,0,1,3,1,0,5,10,1,
        0,12,14,71,0,18,1,0,0,0,2,22,1,0,0,0,4,27,1,0,0,0,6,49,1,0,0,0,8,
        51,1,0,0,0,10,55,1,0,0,0,12,59,1,0,0,0,14,62,1,0,0,0,16,64,1,0,0,
        0,18,19,3,2,1,0,19,20,5,0,0,1,20,1,1,0,0,0,21,23,3,4,2,0,22,21,1,
        0,0,0,23,24,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,3,1,0,0,0,26,
        28,5,19,0,0,27,26,1,0,0,0,27,28,1,0,0,0,28,29,1,0,0,0,29,30,3,16,
        8,0,30,34,5,19,0,0,31,32,3,6,3,0,32,33,5,19,0,0,33,35,1,0,0,0,34,
        31,1,0,0,0,34,35,1,0,0,0,35,45,1,0,0,0,36,37,3,8,4,0,37,38,5,19,
        0,0,38,46,1,0,0,0,39,40,3,12,6,0,40,41,5,19,0,0,41,46,1,0,0,0,42,
        43,3,14,7,0,43,44,5,19,0,0,44,46,1,0,0,0,45,36,1,0,0,0,45,39,1,0,
        0,0,45,42,1,0,0,0,46,47,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,5,
        1,0,0,0,49,50,7,0,0,0,50,7,1,0,0,0,51,52,5,15,0,0,52,53,5,4,0,0,
        53,54,3,10,5,0,54,9,1,0,0,0,55,57,7,1,0,0,56,58,5,20,0,0,57,56,1,
        0,0,0,57,58,1,0,0,0,58,11,1,0,0,0,59,60,5,11,0,0,60,61,5,17,0,0,
        61,13,1,0,0,0,62,63,7,2,0,0,63,15,1,0,0,0,64,69,5,16,0,0,65,66,5,
        20,0,0,66,68,5,16,0,0,67,65,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,
        69,70,1,0,0,0,70,17,1,0,0,0,71,69,1,0,0,0,7,24,27,34,45,47,57,69
    ]

class ReceitaParser ( Parser ):

    grammarFileName = "Receita.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Diurno'", "'Matutino'", "'Noturno'", 
                     "'/'", "'Comprimidos'", "'Mililitros'", "'Miligramas'", 
                     "'comp.'", "'ml.'", "'mg.'", "'Indica\\u00E7\\u00E3o:'", 
                     "'Oral'", "'Retal'", "'Intravenosa'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\\n'", "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "QUANTIDADE", 
                      "REMEDIO", "TEXTO", "SIMBOLO_INVALIDO", "LINE_BREAK", 
                      "WS" ]

    RULE_receita_medica = 0
    RULE_prescricoes = 1
    RULE_prescricao = 2
    RULE_periodo = 3
    RULE_dosagem = 4
    RULE_medida = 5
    RULE_indicacao = 6
    RULE_aplicacao = 7
    RULE_remedio = 8

    ruleNames =  [ "receita_medica", "prescricoes", "prescricao", "periodo", 
                   "dosagem", "medida", "indicacao", "aplicacao", "remedio" ]

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
    QUANTIDADE=15
    REMEDIO=16
    TEXTO=17
    SIMBOLO_INVALIDO=18
    LINE_BREAK=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Receita_medicaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prescricoes(self):
            return self.getTypedRuleContext(ReceitaParser.PrescricoesContext,0)


        def EOF(self):
            return self.getToken(ReceitaParser.EOF, 0)

        def getRuleIndex(self):
            return ReceitaParser.RULE_receita_medica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReceita_medica" ):
                listener.enterReceita_medica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReceita_medica" ):
                listener.exitReceita_medica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceita_medica" ):
                return visitor.visitReceita_medica(self)
            else:
                return visitor.visitChildren(self)




    def receita_medica(self):

        localctx = ReceitaParser.Receita_medicaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_receita_medica)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.prescricoes()
            self.state = 19
            self.match(ReceitaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrescricoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prescricao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ReceitaParser.PrescricaoContext)
            else:
                return self.getTypedRuleContext(ReceitaParser.PrescricaoContext,i)


        def getRuleIndex(self):
            return ReceitaParser.RULE_prescricoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrescricoes" ):
                listener.enterPrescricoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrescricoes" ):
                listener.exitPrescricoes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrescricoes" ):
                return visitor.visitPrescricoes(self)
            else:
                return visitor.visitChildren(self)




    def prescricoes(self):

        localctx = ReceitaParser.PrescricoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prescricoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 21
                self.prescricao()
                self.state = 24 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==16 or _la==19):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrescricaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def remedio(self):
            return self.getTypedRuleContext(ReceitaParser.RemedioContext,0)


        def LINE_BREAK(self, i:int=None):
            if i is None:
                return self.getTokens(ReceitaParser.LINE_BREAK)
            else:
                return self.getToken(ReceitaParser.LINE_BREAK, i)

        def periodo(self):
            return self.getTypedRuleContext(ReceitaParser.PeriodoContext,0)


        def dosagem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ReceitaParser.DosagemContext)
            else:
                return self.getTypedRuleContext(ReceitaParser.DosagemContext,i)


        def indicacao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ReceitaParser.IndicacaoContext)
            else:
                return self.getTypedRuleContext(ReceitaParser.IndicacaoContext,i)


        def aplicacao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ReceitaParser.AplicacaoContext)
            else:
                return self.getTypedRuleContext(ReceitaParser.AplicacaoContext,i)


        def getRuleIndex(self):
            return ReceitaParser.RULE_prescricao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrescricao" ):
                listener.enterPrescricao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrescricao" ):
                listener.exitPrescricao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrescricao" ):
                return visitor.visitPrescricao(self)
            else:
                return visitor.visitChildren(self)




    def prescricao(self):

        localctx = ReceitaParser.PrescricaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_prescricao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 26
                self.match(ReceitaParser.LINE_BREAK)


            self.state = 29
            self.remedio()
            self.state = 30
            self.match(ReceitaParser.LINE_BREAK)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                self.state = 31
                self.periodo()
                self.state = 32
                self.match(ReceitaParser.LINE_BREAK)


            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 45
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [15]:
                    self.state = 36
                    self.dosagem()
                    self.state = 37
                    self.match(ReceitaParser.LINE_BREAK)
                    pass
                elif token in [11]:
                    self.state = 39
                    self.indicacao()
                    self.state = 40
                    self.match(ReceitaParser.LINE_BREAK)
                    pass
                elif token in [12, 13, 14]:
                    self.state = 42
                    self.aplicacao()
                    self.state = 43
                    self.match(ReceitaParser.LINE_BREAK)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 63488) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PeriodoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ReceitaParser.RULE_periodo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeriodo" ):
                listener.enterPeriodo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeriodo" ):
                listener.exitPeriodo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPeriodo" ):
                return visitor.visitPeriodo(self)
            else:
                return visitor.visitChildren(self)




    def periodo(self):

        localctx = ReceitaParser.PeriodoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_periodo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
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


    class DosagemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUANTIDADE(self):
            return self.getToken(ReceitaParser.QUANTIDADE, 0)

        def medida(self):
            return self.getTypedRuleContext(ReceitaParser.MedidaContext,0)


        def getRuleIndex(self):
            return ReceitaParser.RULE_dosagem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDosagem" ):
                listener.enterDosagem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDosagem" ):
                listener.exitDosagem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDosagem" ):
                return visitor.visitDosagem(self)
            else:
                return visitor.visitChildren(self)




    def dosagem(self):

        localctx = ReceitaParser.DosagemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dosagem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(ReceitaParser.QUANTIDADE)
            self.state = 52
            self.match(ReceitaParser.T__3)
            self.state = 53
            self.medida()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MedidaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WS(self):
            return self.getToken(ReceitaParser.WS, 0)

        def getRuleIndex(self):
            return ReceitaParser.RULE_medida

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMedida" ):
                listener.enterMedida(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMedida" ):
                listener.exitMedida(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMedida" ):
                return visitor.visitMedida(self)
            else:
                return visitor.visitChildren(self)




    def medida(self):

        localctx = ReceitaParser.MedidaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_medida)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2016) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 56
                self.match(ReceitaParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndicacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXTO(self):
            return self.getToken(ReceitaParser.TEXTO, 0)

        def getRuleIndex(self):
            return ReceitaParser.RULE_indicacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndicacao" ):
                listener.enterIndicacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndicacao" ):
                listener.exitIndicacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndicacao" ):
                return visitor.visitIndicacao(self)
            else:
                return visitor.visitChildren(self)




    def indicacao(self):

        localctx = ReceitaParser.IndicacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_indicacao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(ReceitaParser.T__10)
            self.state = 60
            self.match(ReceitaParser.TEXTO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AplicacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ReceitaParser.RULE_aplicacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAplicacao" ):
                listener.enterAplicacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAplicacao" ):
                listener.exitAplicacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAplicacao" ):
                return visitor.visitAplicacao(self)
            else:
                return visitor.visitChildren(self)




    def aplicacao(self):

        localctx = ReceitaParser.AplicacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_aplicacao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0)):
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


    class RemedioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REMEDIO(self, i:int=None):
            if i is None:
                return self.getTokens(ReceitaParser.REMEDIO)
            else:
                return self.getToken(ReceitaParser.REMEDIO, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(ReceitaParser.WS)
            else:
                return self.getToken(ReceitaParser.WS, i)

        def getRuleIndex(self):
            return ReceitaParser.RULE_remedio

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRemedio" ):
                listener.enterRemedio(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRemedio" ):
                listener.exitRemedio(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRemedio" ):
                return visitor.visitRemedio(self)
            else:
                return visitor.visitChildren(self)




    def remedio(self):

        localctx = ReceitaParser.RemedioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_remedio)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(ReceitaParser.REMEDIO)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 65
                self.match(ReceitaParser.WS)
                self.state = 66
                self.match(ReceitaParser.REMEDIO)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





