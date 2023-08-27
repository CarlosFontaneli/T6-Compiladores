#!/usr/bin/env python
## coding: utf-8

## Generated from Receita.g4 by ANTLR 4.8

from antlr4 import *
from ReceitaVisitor import ReceitaVisitor

if __name__ is not None and "." in __name__:
    from .ReceitaParser import ReceitaParser
else:
    from ReceitaParser import ReceitaParser


class ReceitaGerador(ReceitaVisitor):
    ## Inicialização de listas e dicionários
    def __init__(self, utils):
        self.utils = utils
        self.remedios = {}
        self.prescricoes = {}

    def visitReceita_medica(self, ctx: ReceitaParser.Receita_medicaContext):
        self.utils.adicionarCodigo("<html>\n")
        self.utils.adicionarCodigo("<body>\n")
        self.utils.adicionarCodigo("<center>\n")  # deixa texto centralizado
        self.visitPrescricoes(ctx.prescricoes())
        self.utils.adicionarCodigo("</center>\n")
        self.utils.adicionarCodigo("</body>\n")
        self.utils.adicionarCodigo("</html>\n")

    def visitPrescricoes(self, ctx: ReceitaParser.PrescricoesContext):
        for prescricao in ctx.prescricao():
            self.visitPrescricao(prescricao)

    def visitPrescricao(self, ctx: ReceitaParser.PrescricaoContext):
        self.utils.adicionarCodigo("<p>\n")
        self.utils.adicionarCodigo(f"Remédio: {self.visitRemedio(ctx.remedio())}<br>\n")

        # Tratar período (repetido)
        periodos = ctx.periodo()
        if periodos:
            self.utils.adicionarCodigo("Período:")
            for periodo in periodos:
                self.utils.adicionarCodigo(f" {self.visitPeriodo(periodo)}")
            self.utils.adicionarCodigo("<br>\n")

        # Tratar dosagem (opcional, repetida)
        dosagens = ctx.dosagem()
        if dosagens:
            for dosagem in dosagens:
                self.utils.adicionarCodigo(
                    f"Dosagem: {self.visitDosagem(dosagem)}<br>\n"
                )

        # Tratar indicação (opcional, repetida)
        indicacoes = ctx.indicacao()
        if indicacoes:
            for indicacao in indicacoes:
                self.utils.adicionarCodigo(
                    f"Indicação: {self.visitIndicacao(indicacao)}<br>\n"
                )

        # Tratar aplicação (opcional, repetida)
        aplicacoes = ctx.aplicacao()
        if aplicacoes:
            for aplicacao in aplicacoes:
                self.utils.adicionarCodigo(
                    f"Aplicação: {self.visitAplicacao(aplicacao)}<br>\n"
                )

        self.utils.adicionarCodigo("</p>\n")

    def visitRemedio(self, ctx: ReceitaParser.RemedioContext):
        return " ".join([token.getText() for token in ctx.REMEDIO()])

    def visitPeriodo(self, ctx: ReceitaParser.PeriodoContext):
        return ctx.getText()

    def visitDosagem(self, ctx: ReceitaParser.DosagemContext):
        quantidade = ctx.quantidade().getText()  # e.g., "400"
        medida = ctx.medida().getText()  # e.g., "mg."
        return f"{quantidade}/{medida}"

    def visitIndicacao(self, ctx: ReceitaParser.IndicacaoContext):
        return ctx.TEXTO().getText()

    def visitAplicacao(self, ctx: ReceitaParser.AplicacaoContext):
        return ctx.getText()


del ReceitaParser
