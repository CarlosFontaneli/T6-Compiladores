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
        4,1,12,80,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,1,4,1,25,8,1,11,1,12,1,26,
        1,2,3,2,30,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,43,
        8,2,1,2,1,2,1,2,3,2,48,8,2,1,3,1,3,1,4,1,4,1,4,1,4,1,5,5,5,57,8,
        5,10,5,12,5,60,9,5,1,6,5,6,63,8,6,10,6,12,6,66,9,6,1,7,1,7,1,8,1,
        8,1,9,1,9,1,9,5,9,75,8,9,10,9,12,9,78,9,9,1,9,0,0,10,0,2,4,6,8,10,
        12,14,16,18,0,2,1,0,1,3,1,0,4,6,76,0,20,1,0,0,0,2,24,1,0,0,0,4,29,
        1,0,0,0,6,49,1,0,0,0,8,51,1,0,0,0,10,58,1,0,0,0,12,64,1,0,0,0,14,
        67,1,0,0,0,16,69,1,0,0,0,18,71,1,0,0,0,20,21,3,2,1,0,21,22,5,0,0,
        1,22,1,1,0,0,0,23,25,3,4,2,0,24,23,1,0,0,0,25,26,1,0,0,0,26,24,1,
        0,0,0,26,27,1,0,0,0,27,3,1,0,0,0,28,30,5,10,0,0,29,28,1,0,0,0,29,
        30,1,0,0,0,30,31,1,0,0,0,31,32,3,18,9,0,32,33,5,10,0,0,33,34,3,6,
        3,0,34,35,5,10,0,0,35,36,1,0,0,0,36,37,3,8,4,0,37,38,5,10,0,0,38,
        42,1,0,0,0,39,40,3,16,8,0,40,41,5,10,0,0,41,43,1,0,0,0,42,39,1,0,
        0,0,42,43,1,0,0,0,43,47,1,0,0,0,44,45,3,14,7,0,45,46,5,10,0,0,46,
        48,1,0,0,0,47,44,1,0,0,0,47,48,1,0,0,0,48,5,1,0,0,0,49,50,7,0,0,
        0,50,7,1,0,0,0,51,52,3,10,5,0,52,53,5,11,0,0,53,54,3,12,6,0,54,9,
        1,0,0,0,55,57,5,7,0,0,56,55,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,
        58,59,1,0,0,0,59,11,1,0,0,0,60,58,1,0,0,0,61,63,5,8,0,0,62,61,1,
        0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,13,1,0,0,0,66,
        64,1,0,0,0,67,68,5,12,0,0,68,15,1,0,0,0,69,70,7,1,0,0,70,17,1,0,
        0,0,71,76,5,9,0,0,72,73,5,11,0,0,73,75,5,9,0,0,74,72,1,0,0,0,75,
        78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,19,1,0,0,0,78,76,1,0,0,
        0,7,26,29,42,47,58,64,76
    ]

class ReceitaParser ( Parser ):

    grammarFileName = "Receita.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Diurno'", "'Matutino'", "'Noturno'", 
                     "'Oral'", "'Retal'", "'Intravenosa'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\\n'", "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUMERO", "UNIDADE", 
                      "REMEDIO", "LINE_BREAK", "WS", "TEXTO" ]

    RULE_receita_medica = 0
    RULE_prescricoes = 1
    RULE_prescricao = 2
    RULE_periodo = 3
    RULE_dosagem = 4
    RULE_quantidade = 5
    RULE_medida = 6
    RULE_indicacao = 7
    RULE_aplicacao = 8
    RULE_remedio = 9

    ruleNames =  [ "receita_medica", "prescricoes", "prescricao", "periodo", 
                   "dosagem", "quantidade", "medida", "indicacao", "aplicacao", 
                   "remedio" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NUMERO=7
    UNIDADE=8
    REMEDIO=9
    LINE_BREAK=10
    WS=11
    TEXTO=12

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
            self.state = 20
            self.prescricoes()
            self.state = 21
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
            self.state = 24 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 23
                self.prescricao()
                self.state = 26 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9 or _la==10):
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


        def dosagem(self):
            return self.getTypedRuleContext(ReceitaParser.DosagemContext,0)


        def aplicacao(self):
            return self.getTypedRuleContext(ReceitaParser.AplicacaoContext,0)


        def indicacao(self):
            return self.getTypedRuleContext(ReceitaParser.IndicacaoContext,0)


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
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 28
                self.match(ReceitaParser.LINE_BREAK)


            self.state = 31
            self.remedio()
            self.state = 32
            self.match(ReceitaParser.LINE_BREAK)

            self.state = 33
            self.periodo()
            self.state = 34
            self.match(ReceitaParser.LINE_BREAK)

            self.state = 36
            self.dosagem()
            self.state = 37
            self.match(ReceitaParser.LINE_BREAK)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0):
                self.state = 39
                self.aplicacao()
                self.state = 40
                self.match(ReceitaParser.LINE_BREAK)


            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 44
                self.indicacao()
                self.state = 45
                self.match(ReceitaParser.LINE_BREAK)


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

        def quantidade(self):
            return self.getTypedRuleContext(ReceitaParser.QuantidadeContext,0)


        def WS(self):
            return self.getToken(ReceitaParser.WS, 0)

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
            self.quantidade()
            self.state = 52
            self.match(ReceitaParser.WS)
            self.state = 53
            self.medida()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantidadeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self, i:int=None):
            if i is None:
                return self.getTokens(ReceitaParser.NUMERO)
            else:
                return self.getToken(ReceitaParser.NUMERO, i)

        def getRuleIndex(self):
            return ReceitaParser.RULE_quantidade

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantidade" ):
                listener.enterQuantidade(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantidade" ):
                listener.exitQuantidade(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantidade" ):
                return visitor.visitQuantidade(self)
            else:
                return visitor.visitChildren(self)




    def quantidade(self):

        localctx = ReceitaParser.QuantidadeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_quantidade)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 55
                self.match(ReceitaParser.NUMERO)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def UNIDADE(self, i:int=None):
            if i is None:
                return self.getTokens(ReceitaParser.UNIDADE)
            else:
                return self.getToken(ReceitaParser.UNIDADE, i)

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
        self.enterRule(localctx, 12, self.RULE_medida)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 61
                self.match(ReceitaParser.UNIDADE)
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 14, self.RULE_indicacao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
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
        self.enterRule(localctx, 16, self.RULE_aplicacao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0)):
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
        self.enterRule(localctx, 18, self.RULE_remedio)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(ReceitaParser.REMEDIO)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 72
                self.match(ReceitaParser.WS)
                self.state = 73
                self.match(ReceitaParser.REMEDIO)
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





