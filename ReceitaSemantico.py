#!/usr/bin/env python
# coding: utf-8

from ReceitaVisitor import ReceitaVisitor
from ReceitaParser import ReceitaParser


class ReceitaSemantico(ReceitaVisitor):
    # Inicializações de listas e dicionários a serem utilizados
    def __init__(self, utils):
        self.utils = utils
        self.prescricoes = []
        self.periodos = {}

    # Visita a primeira regra da gramática
    def visitReceita_medica(self, ctx: ReceitaParser.Receita_medicaContext):
        return self.visitPrescricoes(ctx.prescricoes())

    def visitPrescricoes(self, ctx: ReceitaParser.PrescricoesContext):
        return self.visitChildren(ctx)

    def visitPrescricao(self, ctx: ReceitaParser.PrescricaoContext):
        return {
            "remedio": self.visitRemedio(ctx.remedio()),
            "periodo": [self.visitPeriodo(p) for p in ctx.periodo()],
            "dosagem": [self.visitDosagem(p) for p in ctx.dosagem()],
            "indicacao": [self.visitIndicacao(p) for p in ctx.indicacao()],
            "aplicacao": [self.visitAplicacao(p) for p in ctx.aplicacao()],
        }

    def visitRemedio(self, ctx: ReceitaParser.RemedioContext):
        return ctx.getText()

    def visitDosagem(self, ctx: ReceitaParser.DosagemContext):
        return self.visitChildren(ctx)

    def visitMedida(self, ctx: ReceitaParser.MedidaContext):
        return ctx.getText()

    def visitIndicacao(self, ctx: ReceitaParser.IndicacaoContext):
        return ctx.getText()

    def visitAplicacao(self, ctx: ReceitaParser.AplicacaoContext):
        return ctx.getText()

    def visitPeriodo(self, ctx: ReceitaParser.PeriodoContext):
        return ctx.getText()
