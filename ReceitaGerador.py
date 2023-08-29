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
        self.utils.adicionarCodigo("<head>\n")
        self.utils.adicionarCodigo("<style>\n")
        self.utils.adicionarCodigo("body { font-family: Arial, sans-serif; }\n")
        self.utils.adicionarCodigo(".container { width: 80%; margin: 0 auto; }\n")
        self.utils.adicionarCodigo(".header { text-align: center; background-color: #f2f2f2; padding: 10px; }\n")
        self.utils.adicionarCodigo(".prescricao { border: 1px solid #ccc; padding: 10px; margin-bottom: 20px; }\n")
        self.utils.adicionarCodigo("</style>\n")
        self.utils.adicionarCodigo("</head>\n")
        self.utils.adicionarCodigo("<body>\n")
        
        self.utils.adicionarCodigo("<div class='container'>\n")
        self.utils.adicionarCodigo("<div class='header'>\n")
        self.utils.adicionarCodigo("<h1>Receita Médica</h1>\n")
        self.utils.adicionarCodigo("</div>\n")
        
        self.utils.adicionarCodigo("<div class='prescricao'>\n")
        self.utils.adicionarCodigo("<h2>Prescrições</h2>\n")
        self.visitPrescricoes(ctx.prescricoes())  # Preencha essa parte de acordo com sua implementação
        self.utils.adicionarCodigo("</div>\n")
        
        self.utils.adicionarCodigo("</div>\n")  # Fim do container
        
        self.utils.adicionarCodigo("</body>\n")
        self.utils.adicionarCodigo("</html>\n")

    def visitPrescricoes(self, ctx: ReceitaParser.PrescricoesContext):
        for prescricao in ctx.prescricao():
            self.visitPrescricao(prescricao)

    def visitPrescricao(self, ctx: ReceitaParser.PrescricaoContext):
        self.utils.adicionarCodigo("<p>\n")
        print(f"Remedio {self.visitRemedio(ctx.remedio())}")
        self.utils.adicionarCodigo(f"Remédio: {self.visitRemedio(ctx.remedio())}<br>\n")

        # Tratar período (repetido)
        periodo = ctx.periodo()
        if periodo is not None:
            self.utils.adicionarCodigo("Período:")
            print(f"Periodo {self.visitPeriodo(periodo)}")
            self.utils.adicionarCodigo(f" {self.visitPeriodo(periodo)}")
            self.utils.adicionarCodigo("<br>\n")

        # Tratar dosagem (opcional, repetida)
        dosagem = ctx.dosagem()
        if dosagem is not None:
            print(f"Dosagem {self.visitDosagem(dosagem)}")
            self.utils.adicionarCodigo(f"Dosagem: {self.visitDosagem(dosagem)}<br>\n")

        # Tratar aplicação (opcional, repetida)
        aplicacao = ctx.aplicacao()
        if aplicacao is not None:
            print(f"Aplicacao: {self.visitAplicacao(aplicacao)}")
            self.utils.adicionarCodigo(
                f"Aplicação: {self.visitAplicacao(aplicacao)}<br>\n"
            )

        # Tratar indicação (opcional, repetida)
        indicacao = ctx.indicacao()
        if indicacao is not None:
            print(f"Indicacao: {self.visitIndicacao(indicacao)}")
            self.utils.adicionarCodigo(
                f"Indicação: {self.visitIndicacao(indicacao)}<br>\n"
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
