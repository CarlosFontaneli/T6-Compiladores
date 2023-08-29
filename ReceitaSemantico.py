from antlr4 import *
from ReceitaParser import ReceitaParser
from ReceitaVisitor import ReceitaVisitor


class ReceitaSemantico(ReceitaVisitor):
    def __init__(self, utils):
        self.utils = utils
        self.prescricoes = []
        self.remedios = []

    def visitPrescricoes(self, ctx: ReceitaParser.PrescricoesContext):
        for prescricao in ctx.prescricao():
            dados = self.visitPrescricao(prescricao)
            self.checkDosagem(dados["dosagem"])
            self.prescricoes.append(dados)

    def visitPrescricao(self, ctx: ReceitaParser.PrescricaoContext):
        remedio = ctx.remedio().getText()

        if remedio in self.remedios:
            self.utils.adicionarErroSemantico(
                remedio, mensagem=f"Repeticação de remédio: {remedio}"
            )
        else:
            self.remedios.append(remedio)
        periodo = ctx.periodo().getText()
        dosagem = self.visitDosagem(ctx.dosagem())
        aplicacao = ctx.aplicacao().getText() if ctx.aplicacao() else None
        indicacao = ctx.indicacao().getText() if ctx.indicacao() else None
        return {
            "remedio": remedio,
            "periodo": periodo,
            "dosagem": dosagem,
            "aplicacao": aplicacao,
            "indicacao": indicacao,
        }

    def visitDosagem(self, ctx: ReceitaParser.DosagemContext):
        quantidade = int(ctx.quantidade().getText())
        medida = ctx.medida().getText()
        self.checkDosagemRange(quantidade, medida)
        return {"quantidade": quantidade, "medida": medida}

    def checkDosagem(self, dosagem):
        if dosagem["medida"] == "Mililitros" or dosagem["medida"] == "Miligramas":
            if dosagem["quantidade"] > 1000:
                self.utils.adicionarErroSemantico(
                    dosagem["quantidade"],
                    mensagem=f"Dosagem excede 1000 {dosagem['medida']}",
                )

    def checkDosagemRange(self, quantidade, medida):
        if medida == "Comprimidos":
            if quantidade > 10:
                self.utils.adicionarErroSemantico(
                    quantidade, mensagem=f"Dosagem excede 10 {medida}"
                )
