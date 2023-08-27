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
        4,1,15,104,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,1,4,1,25,8,1,11,1,12,1,26,
        1,2,3,2,30,8,2,1,2,1,2,1,2,1,2,1,2,4,2,37,8,2,11,2,12,2,38,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,4,2,50,8,2,11,2,12,2,51,1,3,1,3,1,
        4,5,4,57,8,4,10,4,12,4,60,9,4,1,4,1,4,3,4,64,8,4,1,4,1,4,1,5,5,5,
        69,8,5,10,5,12,5,72,9,5,1,6,5,6,75,8,6,10,6,12,6,78,9,6,1,7,5,7,
        81,8,7,10,7,12,7,84,9,7,1,7,1,7,1,8,5,8,89,8,8,10,8,12,8,92,9,8,
        1,8,1,8,1,9,1,9,1,9,5,9,99,8,9,10,9,12,9,102,9,9,1,9,0,0,10,0,2,
        4,6,8,10,12,14,16,18,0,2,1,0,1,3,1,0,7,9,106,0,20,1,0,0,0,2,24,1,
        0,0,0,4,29,1,0,0,0,6,53,1,0,0,0,8,58,1,0,0,0,10,70,1,0,0,0,12,76,
        1,0,0,0,14,82,1,0,0,0,16,90,1,0,0,0,18,95,1,0,0,0,20,21,3,2,1,0,
        21,22,5,0,0,1,22,1,1,0,0,0,23,25,3,4,2,0,24,23,1,0,0,0,25,26,1,0,
        0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,3,1,0,0,0,28,30,5,13,0,0,29,28,
        1,0,0,0,29,30,1,0,0,0,30,31,1,0,0,0,31,32,3,18,9,0,32,36,5,13,0,
        0,33,34,3,6,3,0,34,35,5,13,0,0,35,37,1,0,0,0,36,33,1,0,0,0,37,38,
        1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,49,1,0,0,0,40,41,3,8,4,0,
        41,42,5,13,0,0,42,50,1,0,0,0,43,44,3,14,7,0,44,45,5,13,0,0,45,50,
        1,0,0,0,46,47,3,16,8,0,47,48,5,13,0,0,48,50,1,0,0,0,49,40,1,0,0,
        0,49,43,1,0,0,0,49,46,1,0,0,0,50,51,1,0,0,0,51,49,1,0,0,0,51,52,
        1,0,0,0,52,5,1,0,0,0,53,54,7,0,0,0,54,7,1,0,0,0,55,57,5,4,0,0,56,
        55,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,61,1,0,0,
        0,60,58,1,0,0,0,61,63,3,10,5,0,62,64,5,14,0,0,63,62,1,0,0,0,63,64,
        1,0,0,0,64,65,1,0,0,0,65,66,3,12,6,0,66,9,1,0,0,0,67,69,5,10,0,0,
        68,67,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,11,1,
        0,0,0,72,70,1,0,0,0,73,75,5,11,0,0,74,73,1,0,0,0,75,78,1,0,0,0,76,
        74,1,0,0,0,76,77,1,0,0,0,77,13,1,0,0,0,78,76,1,0,0,0,79,81,5,5,0,
        0,80,79,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,85,
        1,0,0,0,84,82,1,0,0,0,85,86,5,15,0,0,86,15,1,0,0,0,87,89,5,6,0,0,
        88,87,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,93,1,
        0,0,0,92,90,1,0,0,0,93,94,7,1,0,0,94,17,1,0,0,0,95,100,5,12,0,0,
        96,97,5,14,0,0,97,99,5,12,0,0,98,96,1,0,0,0,99,102,1,0,0,0,100,98,
        1,0,0,0,100,101,1,0,0,0,101,19,1,0,0,0,102,100,1,0,0,0,12,26,29,
        38,49,51,58,63,70,76,82,90,100
    ]

class ReceitaParser ( Parser ):

    grammarFileName = "Receita.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Diurno'", "'Matutino'", "'Noturno'", 
                     "'Dosagem:'", "'Indica\\u00E7\\u00E3o:'", "'Aplica\\u00E7\\u00E3o:'", 
                     "'Oral'", "'Retal'", "'Intravenosa'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\\n'", "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMERO", "UNIDADE", "REMEDIO", 
                      "LINE_BREAK", "WS", "TEXTO" ]

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
    T__6=7
    T__7=8
    T__8=9
    NUMERO=10
    UNIDADE=11
    REMEDIO=12
    LINE_BREAK=13
    WS=14
    TEXTO=15

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
                if not (_la==12 or _la==13):
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

        def periodo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ReceitaParser.PeriodoContext)
            else:
                return self.getTypedRuleContext(ReceitaParser.PeriodoContext,i)


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
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 28
                self.match(ReceitaParser.LINE_BREAK)


            self.state = 31
            self.remedio()
            self.state = 32
            self.match(ReceitaParser.LINE_BREAK)
            self.state = 36 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 33
                self.periodo()
                self.state = 34
                self.match(ReceitaParser.LINE_BREAK)
                self.state = 38 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                    break

            self.state = 49 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 49
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [4, 10, 11, 13, 14]:
                        self.state = 40
                        self.dosagem()
                        self.state = 41
                        self.match(ReceitaParser.LINE_BREAK)
                        pass
                    elif token in [5, 15]:
                        self.state = 43
                        self.indicacao()
                        self.state = 44
                        self.match(ReceitaParser.LINE_BREAK)
                        pass
                    elif token in [6, 7, 8, 9]:
                        self.state = 46
                        self.aplicacao()
                        self.state = 47
                        self.match(ReceitaParser.LINE_BREAK)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 51 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
            self.state = 53
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


        def medida(self):
            return self.getTypedRuleContext(ReceitaParser.MedidaContext,0)


        def WS(self):
            return self.getToken(ReceitaParser.WS, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 55
                self.match(ReceitaParser.T__3)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self.quantidade()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 62
                self.match(ReceitaParser.WS)


            self.state = 65
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
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 67
                self.match(ReceitaParser.NUMERO)
                self.state = 72
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
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 73
                self.match(ReceitaParser.UNIDADE)
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 79
                self.match(ReceitaParser.T__4)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
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
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 87
                self.match(ReceitaParser.T__5)
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 93
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
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
            self.state = 95
            self.match(ReceitaParser.REMEDIO)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 96
                self.match(ReceitaParser.WS)
                self.state = 97
                self.match(ReceitaParser.REMEDIO)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





