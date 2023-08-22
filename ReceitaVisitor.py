# Generated from Receita.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ReceitaParser import ReceitaParser
else:
    from ReceitaParser import ReceitaParser

# This class defines a complete generic visitor for a parse tree produced by ReceitaParser.

class ReceitaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ReceitaParser#receita_medica.
    def visitReceita_medica(self, ctx:ReceitaParser.Receita_medicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ReceitaParser#prescricoes.
    def visitPrescricoes(self, ctx:ReceitaParser.PrescricoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ReceitaParser#prescricao.
    def visitPrescricao(self, ctx:ReceitaParser.PrescricaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ReceitaParser#periodo.
    def visitPeriodo(self, ctx:ReceitaParser.PeriodoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ReceitaParser#dosagem.
    def visitDosagem(self, ctx:ReceitaParser.DosagemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ReceitaParser#medida.
    def visitMedida(self, ctx:ReceitaParser.MedidaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ReceitaParser#indicacao.
    def visitIndicacao(self, ctx:ReceitaParser.IndicacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ReceitaParser#aplicacao.
    def visitAplicacao(self, ctx:ReceitaParser.AplicacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ReceitaParser#remedio.
    def visitRemedio(self, ctx:ReceitaParser.RemedioContext):
        return self.visitChildren(ctx)



del ReceitaParser