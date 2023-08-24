# !/usr/bin/env python
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
        self.periodos = {}
        self.pescricao_periodo = {}

    def visitReceita(self, ctx: ReceitaParser.Receita_medicaContext):
        self.utils.adicionarCodigo("<html>\n")
        self.utils.adicionarCodigo("<body>\n")
        self.utils.adicionarCodigo("<center>\n")  ## deixa texto centralizado
        self.visitPrescricoes(ctx.pescricoes())

        ## Se existem periodos, vamos imprimí-los primeiro
        if len(self.periodos) != 0:
            ## Ordenar
            remedios_periodos = list(self.periodos.keys())
            remedios_periodos.sort()

            ## Para cada periodo
            for tempo_periodo in remedios_periodos:
                ## Criar separador para agrupar contatos por letra
                separador = "a"

                ## Ordena remedios
                sorted_group = dict(
                    sorted(
                        self.periodos[tempo_periodo].items(), key=lambda item: item[0]
                    )
                )

                # TODO: ALTERAR HTML ABAIXO
                ## remedio do grupo
                self.utils.adicionarCodigo(
                    f"<p style=\"font-family:'verdana'\">Grupo: {tempo_periodo}<br></p>\n"
                )

                self.utils.adicionarCodigo(f'<p style="font-family:Courier New">')

                ## Para cada periodo
                for remedio, (dosagem, indicacao, aplicacao) in sorted_group.items():
                    ## Verificar se separador precisa ser mostrado
                    inicial = remedio[0].upper()
                    if inicial != separador:
                        # TODO: ALTERAR O HTML DAS INICIAS DOS PERIODOS PARA COLOCAR O PERIODO INTEIRO
                        self.utils.adicionarCodigo(f"<b>{inicial}</b><br>\n")
                        separador = inicial

                    # TODO ALTERAR HTML
                    ## Imprime informações do contato
                    self.utils.adicionarCodigo(f"{remedio}<br>\n")
                    if dosagem != []:
                        self.iterThrough("e-mail", dosagem)
                    if indicacao != []:
                        self.iterThrough("indicacao", indicacao)
                    if aplicacao != []:
                        self.iterThrough("endereço", aplicacao)

                    self.utils.adicionarCodigo("<br><br>\n")

                self.utils.adicionarCodigo(f"</p>\n")
        # TODO ALTERAR HTML
        self.utils.adicionarCodigo("<br><br><br><br>\n")

        ## Impressão de receitas que ñ possuem periodos
        if len(self.periodos) > 0 and len(self.pescricao_periodo) > 0:
            # TODO: alterar html
            self.utils.adicionarCodigo(
                '<p style="Serif">------- Outros Contatos -------</p>'
            )
        ## Ordena remedios
        self.pescricao_periodo = dict(
            sorted(self.pescricao_periodo.items(), key=lambda item: item[0])
        )
        # TODO: alterar html
        self.utils.adicionarCodigo(f'<p style="font-family:Courier New">')

        ## Separador de agrupamento
        separador = "a"
        for remedio, (dosagem, indicacao, aplicacao) in self.pescricao_periodo.items():
            inicial = remedio[0].upper()
            ## Caso letra inicial seja diferente da anterior
            if inicial != separador:
                self.utils.adicionarCodigo(f"<b>{inicial}</b><br><br>\n")
                separador = inicial

            self.utils.adicionarCodigo(f"{remedio}<br>\n")
            if dosagem != []:
                self.iterThrough("dosagem", dosagem)

            if indicacao != []:
                self.iterThrough("indicacao", indicacao)

            if aplicacao != []:
                self.iterThrough("aplicacao", aplicacao)

            self.utils.adicionarCodigo("<br><br>\n")

        self.utils.adicionarCodigo(f"</p>\n")

        self.utils.adicionarCodigo("</center>\n")
        self.utils.adicionarCodigo("</body>\n")
        self.utils.adicionarCodigo("</html>\n")

    def visitRemedio(self, ctx: ReceitaParser.RemedioContext):
        remedio = self.visitRemedio(ctx.remedio())
        periodo = None
        dosagem = []
        indicacao = []
        aplicacao = []

        if ctx.periodo() is not None:
            periodo = self.visitPeriodo(ctx.periodo())

        for c_dosagem in ctx.dosagem():
            dosagem.append(self.visitDosagem(c_dosagem))

        for c_indicacao in ctx.indicacao():
            # indicacao.append(self.padronizaIndicacao(self.visitIndicacao(c_indicacao)))
            indicacao.append(self.visitIndicacao(c_indicacao))

        for c_aplicacao in ctx.aplicacao():
            aplicacao.append(self.visitAplicacao(c_aplicacao))

        ## dosagem, indicacao e aplicacao são listas, pois contato pode ter mais de um
        ## Se está em grupo, colocamos na lista de acordo com respectivo grupo,
        ## caso contrário colocamos em contatos sem grupo
        if periodo is None:
            self.pescricao_periodo[remedio] = (dosagem, indicacao, aplicacao)
        else:
            self.periodos[periodo][remedio] = (dosagem, indicacao, aplicacao)

    def visitPeriodo(self, ctx: ReceitaParser.PeriodoContext):
        tempo_periodo = ctx.getText()
        ## Se o grupo ñ havia sido referenciado antes,
        ## cria um novo grupo com aquele remedio como identificador
        if tempo_periodo not in self.periodos:
            self.periodos[tempo_periodo] = {}

        return tempo_periodo

    def visitDosagem(self, ctx: ReceitaParser.DosagemContext):
        if ctx.quantidade() is not None:
            quantidade = self.visitQuantidade(ctx.quantidade())
        if ctx.medida() is not None:
            medida = self.visitiMedida(ctx.medida())

        return quantidade + "/" + medida

    def visitQuantidade(self, ctx: ReceitaParser.QuantidadeContext):
        return ctx.getText()

    def visitiMedida(self, ctx: ReceitaParser.MedidaContext):
        return ctx.getText()

    def visitIndicacao(self, ctx: ReceitaParser.IndicacaoContext):
        return ctx.getText()

    def visitAplicacao(self, ctx: ReceitaParser.AplicacaoContext):
        return ctx.getText()

    # TODO: pensar em uma logica similar ao endereco pra remedio no lugar de indicacao
    """ def visitAplicacao(self, ctx: ReceitaParser.aplicacaoContext):
        end = ""
        end += self.visitRua(ctx.rua()) + ", "
        end += ctx.NUMERO().getText() + ", "
        end += self.visitBairro(ctx.bairro())

        if ctx.cidade() is not None:
            end += ", " + self.visitCidade(ctx.cidade())
            end += " - "
            end += self.visitUf(ctx.uf())

        if ctx.cep() is not None:
            end += ", " + self.visitCep(ctx.cep())

        if ctx.pais() is not None:
            end += ", " + self.visitPais(ctx.pais())

        return end

    def visitCidade(self, ctx: ReceitaParser.CidadeContext):
        return ctx.getText()

    def visitBairro(self, ctx: ReceitaParser.BairroContext):
        return ctx.getText()

    def visitRua(self, ctx: ReceitaParser.RuaContext):
        return ctx.getText()

    def visitUf(self, ctx: ReceitaParser.UfContext):
        return ctx.getText()

    def visitPais(self, ctx: ReceitaParser.PaisContext):
        return ctx.getText()

    def visitCep(self, ctx: ReceitaParser.CepContext):
        return self.padronizaCEP(ctx.getText()) """

    def visitRemedio(self, ctx: ReceitaParser.RemedioContext):
        return ctx.getText()

    ## Procedimento que itera pela lista de dosagems, indicacaos e aplicacao de cada remedio
    ## 'tag' é o texto que será mostrado
    ## 'iterable' é a lista que vamos percorrer
    def iterThrough(self, tag, iterable):
        ## Imprime tag + primeiro elemento
        self.utils.adicionarCodigo(f"{tag}: {iterable[0]}")

        ## Se há mais elementos, imprimimos, separando por uma barra
        if len(iterable) > 1:
            i = 1
            while i < len(iterable):
                self.utils.adicionarCodigo(f" / {iterable[i]}")
                i += 1
        self.utils.adicionarCodigo("<br>\n")

    # TODO: PENSAR EM FORMAS DE ALTERAR ESSA PARTE
    """ ## Função para padronizar como CEPs são mostrados
    def padronizaCEP(self, cep):
        ## Se possui espaços ou não possui hífen
        if " " in cep or "-" not in cep:
            raw_cep = ""
            for c in cep:
                ## Só adiciona os números
                if c >= "0" and c <= "9":
                    raw_cep += c

            ## Separa devidamente
            cep = raw_cep[0] + raw_cep[1:5] + "-" + raw_cep[5:]

        return cep """

    """ ## Função para padronizar como indicacaos serão mostrados
    def padronizaIndicacao(self, indicacao):
        ## Devemos alterar caso falte o hífen no meio do indicacao
        ## ou caso haja espaços no número
        if "-" not in indicacao or " " in indicacao:
            ## Deparamos em ddd e número
            ddd = indicacao.split(")")[0][1:]
            indicacao_s_ddd = indicacao.split(")")[1]

            ddd_final = "("
            indicacao_final = ""

            ## De caractere em DDD ñ for espaço, acrescentamos à porção final
            for N in ddd:
                if N != " ":
                    ddd_final += N

            ddd_final += ")"

            ## Se caracter em número ñ for espaço
            ## ou hífen, acrescentamos, removemos o hífen
            ## pois sempre o colocaremos no final
            for N in indicacao_s_ddd:
                if N != " " and N != "-":
                    indicacao_final += N

            indicacao_final = indicacao_final[:4] + "-" + indicacao_final[4:]
            indicacao = ddd_final + indicacao_final

        return indicacao
        """


del ReceitaParser
