# Generated from Receita.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ReceitaParser import ReceitaParser
else:
    from ReceitaParser import ReceitaParser

# This class defines a complete listener for a parse tree produced by ReceitaParser.
class ReceitaListener(ParseTreeListener):

    # Enter a parse tree produced by ReceitaParser#receita_medica.
    def enterReceita_medica(self, ctx:ReceitaParser.Receita_medicaContext):
        pass

    # Exit a parse tree produced by ReceitaParser#receita_medica.
    def exitReceita_medica(self, ctx:ReceitaParser.Receita_medicaContext):
        pass


    # Enter a parse tree produced by ReceitaParser#prescricoes.
    def enterPrescricoes(self, ctx:ReceitaParser.PrescricoesContext):
        pass

    # Exit a parse tree produced by ReceitaParser#prescricoes.
    def exitPrescricoes(self, ctx:ReceitaParser.PrescricoesContext):
        pass


    # Enter a parse tree produced by ReceitaParser#prescricao.
    def enterPrescricao(self, ctx:ReceitaParser.PrescricaoContext):
        pass

    # Exit a parse tree produced by ReceitaParser#prescricao.
    def exitPrescricao(self, ctx:ReceitaParser.PrescricaoContext):
        pass


    # Enter a parse tree produced by ReceitaParser#periodo.
    def enterPeriodo(self, ctx:ReceitaParser.PeriodoContext):
        pass

    # Exit a parse tree produced by ReceitaParser#periodo.
    def exitPeriodo(self, ctx:ReceitaParser.PeriodoContext):
        pass


    # Enter a parse tree produced by ReceitaParser#dosagem.
    def enterDosagem(self, ctx:ReceitaParser.DosagemContext):
        pass

    # Exit a parse tree produced by ReceitaParser#dosagem.
    def exitDosagem(self, ctx:ReceitaParser.DosagemContext):
        pass


    # Enter a parse tree produced by ReceitaParser#quantidade.
    def enterQuantidade(self, ctx:ReceitaParser.QuantidadeContext):
        pass

    # Exit a parse tree produced by ReceitaParser#quantidade.
    def exitQuantidade(self, ctx:ReceitaParser.QuantidadeContext):
        pass


    # Enter a parse tree produced by ReceitaParser#medida.
    def enterMedida(self, ctx:ReceitaParser.MedidaContext):
        pass

    # Exit a parse tree produced by ReceitaParser#medida.
    def exitMedida(self, ctx:ReceitaParser.MedidaContext):
        pass


    # Enter a parse tree produced by ReceitaParser#indicacao.
    def enterIndicacao(self, ctx:ReceitaParser.IndicacaoContext):
        pass

    # Exit a parse tree produced by ReceitaParser#indicacao.
    def exitIndicacao(self, ctx:ReceitaParser.IndicacaoContext):
        pass


    # Enter a parse tree produced by ReceitaParser#aplicacao.
    def enterAplicacao(self, ctx:ReceitaParser.AplicacaoContext):
        pass

    # Exit a parse tree produced by ReceitaParser#aplicacao.
    def exitAplicacao(self, ctx:ReceitaParser.AplicacaoContext):
        pass


    # Enter a parse tree produced by ReceitaParser#remedio.
    def enterRemedio(self, ctx:ReceitaParser.RemedioContext):
        pass

    # Exit a parse tree produced by ReceitaParser#remedio.
    def exitRemedio(self, ctx:ReceitaParser.RemedioContext):
        pass



del ReceitaParser