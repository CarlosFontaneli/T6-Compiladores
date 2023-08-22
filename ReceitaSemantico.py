# !/usr/bin/env python
## coding: utf-8

from ReceitaVisitor import ReceitaVisitor
from ReceitaParser import ReceitaParser


class ReceitaSemantico(ReceitaVisitor):
    ## Inicializações de listas e dicionários a serem utilizados
    def __init__(self, utils):
        self.utils = utils
        self.prescricoes = []
        self.periodos = {}
        self.periodos_ctx = {}

    ## Os 'visit' abaixo sobrescrevem aqueles gerados como padrão pelo antlr4
    ## Isso é feito para que, ao dar match em cada regra da gramática, o programa tenha o comportamento desejado

    ## Visita a primeira regra da gramática
    def Receita(self, ctx: ReceitaParser.ReceitaContext):
        self.visitRemedios(ctx.contatos())
        self.chekPeriodo()

    ## 'visitPrescricoes' verifica duplicatas internas (repetições de remedio em uma mesma receita)
    ## e duplicatas externas (ocorrência do mesmo indicacao ou dosagem em dois contatos diferentes)
    ## Para isso são utilizadas listas e um dicionário
    def visitPrescricoes(self, ctx: ReceitaParser.PrescricoesContext):
        counter = 0

        if ctx.prescricao() is not None:
            for i, c in enumerate(ctx.prescricao()):
                flag_externa = 0

                ## Caso seja o primeiro contato
                if counter == 0:
                    ## Inicialização do dicionário
                    dados = {
                        "remedio": None,
                        "dosagem": None,
                        "indicao": None,
                        "aplicacao": None,
                    }

                    ## Obtenção das informações do contato
                    remedio, dosagem, indicacao, aplicacao = self.visitAplicacao(c)

                    ## Verificação de duplicata interna
                    flag_interna = 0

                    tmp_remedio = []
                    for j, e in enumerate(remedio):
                        if e not in tmp_remedio:
                            tmp_remedio.append(e)
                        else:
                            flag_interna = 1
                            self.utils.adicionarErroSemantico(
                                ctx.prescricao()[i].remedio()[j].l1,
                                f"remedio '{e}' duplicado",
                            )

                    """ tmp_indicacao = []
                    for j, t in enumerate(indicacao):
                        if t not in tmp_indicacao:
                            tmp_indicacao.append(t)
                        else:
                            flag_interna = 1
                            self.utils.adicionarErroSemantico(
                                ctx.prescricao()[i].indicacao()[j].ddd,
                                f"indicacao '{t}' duplicado",
                            ) """

                    ## A verificação da duplicata externa não é aplicável aqui, pois trata-se do primeiro contato

                    ## Se nenhum erro foi encontrado, as informações são adicionadas ao dicionário
                    if flag_interna == 0:
                        dados = {
                            "remedio": remedio,
                            "dosagem": dosagem,
                            "indicacao": indicacao,
                            "aplicacao": aplicacao,
                        }
                        self.prescricoes.append(dados)
                    counter += 1

                else:
                    remedio, dosagem, indicacao, aplicacao = self.visitPrescricao(c)

                    ## Verificação de duplicata interna
                    flag_interna = 0

                    tmp_remedio = []
                    for j, e in enumerate(remedio):
                        if e not in tmp_remedio:
                            tmp_remedio.append(e)
                        else:
                            flag_interna = 1
                            self.utils.adicionarErroSemantico(
                                ctx.prescricao()[i].remedio()[j].l1,
                                f"remedio '{e}' duplicado",
                            )

                    """ tmp_indicacao = []
                    for j, t in enumerate(indicacao):
                        if t not in tmp_indicacao:
                            tmp_indicacao.append(t)
                        else:
                            flag_interna = 1
                            self.utils.adicionarErroSemantico(
                                ctx.prescricao()[i].indicacao()[j].ddd,
                                f"indicacao '{t}' duplicado",
                            ) """

                    ## Verificação de duplicata externa
                    for j, e in enumerate(remedio):
                        for dic in self.prescricoes:
                            for item in dic["remedio"]:
                                if e == item:
                                    self.utils.adicionarErroSemantico(
                                        ctx.prescricao()[i].remedio()[j].l1,
                                        f"remedio '{e}' duplicado",
                                    )
                                    flag = 1

                    """ for j, t in enumerate(indicacao):
                        for dic in self.contatos:
                            for item in dic["indicacao"]:
                                if t == item:
                                    self.utils.adicionarErroSemantico(
                                        ctx.prescricao()[i].indicacao()[j].ddd,
                                        f"indicacao '{t}' duplicado",
                                    )
                                    flag = 1 """

                    ## Se nenhum erro for encontrado os dados são adicionados ao dicionário
                    if flag_externa == 0 and flag_interna == 0:
                        dados = {
                            "remedio": remedio,
                            "dosagem": dosagem,
                            "indicacao": indicacao,
                            "aplicacao": aplicacao,
                        }
                        self.contatos.append(dados)

                counter += 1

    ## Esse 'visit' retorna informações de um mesmo contato e é utilizado em 'visitPrescricoes'
    ## Como é permitida a declaração de vários dosagems, indicacaos e endereços, são utilizadas listas
    def visitPrescricao(self, ctx: ReceitaParser.PrescricaoContext):
        periodo = None
        remedio = self.visitRemedio(ctx.remedio())
        dosagem = []
        indicacao = []
        aplicacao = []

        if ctx.periodo() is not None:
            remedio_periodo, periodo_ctx = self.visitPeriodo(ctx.periodo())
            self.periodos_ctx[remedio_periodo] = periodo_ctx

            if remedio_periodo not in self.periodos:
                self.periodos[remedio_periodo] = []
                self.periodos[remedio_periodo].append(remedio)
            else:
                self.periodos[remedio_periodo].append(remedio)

        if ctx.dosagem() is not None:
            for e in ctx.dosagem():
                dosagem.append(self.visitDosagem(e))

        if ctx.indicacao() is not None:
            for t in ctx.indicacao():
                indicacao.append(self.visitIndicacao(t))

        if ctx.aplicacao() is not None:
            for e in ctx.aplicacao():
                aplicacao.append(self.visitAplicacao(e))

        return remedio, dosagem, indicacao, aplicacao

    ## Os 'visit' abaixo retornam as strings correspondentes a cada informação reconhecida
    ## por suas respectivas regras (dosagem, indicacao, endereço), para serem utilizadas em 'visitPrescricao'

    ## Caso essas regras sejam compostas por outras, a string a ser retornada é montada a partir
    ## da visita a essas; caso contrário, é retornado apenas o texto reconhecido (ctx.getText())

    def visitRemedio(self, ctx: ReceitaParser.remedioContext):
        return ctx.getText()

    def visitDosagem(self, ctx: ReceitaParser.dosagemContext):
        quantidade = self.visitQuantidade(ctx.quantidade())
        medida = self.visitMedida(ctx.medida())

        return quantidade + "/" + medida

    def visitQuantidade(self, ctx: ReceitaParser.QuantidadeContext):
        return ctx.getText()

    def visitMedida(self, ctx: ReceitaParser.MedidaContext):
        return ctx.getText()

    def visitIndicacao(self, ctx: ReceitaParser.IndicacaoContext):
        return ctx.getText()

    def visitAplicacao(self, ctx: ReceitaParser.AplicacaoContext):
        aplicacao = self.visitRua(ctx.rua())
        aplicacao += ", " + ctx.NUMERO().getText() + ", "
        aplicacao += self.visitBairro(ctx.bairro())

        if ctx.cidade() is not None:
            aplicacao += ", " + self.visitCidade(ctx.cidade())
            aplicacao += "-" + self.visitUf(ctx.uf())

        if ctx.cep() is not None:
            aplicacao += ", " + self.visitCep(ctx.cep())

        if ctx.pais() is not None:
            aplicacao += ", " + self.visitPais(ctx.pais())

        return aplicacao

    def visitDescritor_rua(self, ctx: ReceitaParser.Descritor_ruaContext):
        return ctx.getText()

    def visitRua(self, ctx: ReceitaParser.RuaContext):
        remedio_rua = self.visitDescritor_rua(ctx.descritor_rua())
        remedio_rua += " " + ctx.n1.text

        if ctx.n2 is not None:
            for n in ctx.n2:
                remedio_rua += " " + n.text

        return remedio_rua

    def visitBairro(self, ctx: ReceitaParser.BairroContext):
        return ctx.getText()

    def visitCidade(self, ctx: ReceitaParser.CidadeContext):
        return ctx.getText()

    def visitUf(self, ctx: ReceitaParser.UfContext):
        return ctx.getText()

    def visitCep(self, ctx: ReceitaParser.CepContext):
        return ctx.getText()

    def visitPais(self, ctx: ReceitaParser.PaisContext):
        return ctx.getText()

    def visitPeriodo(self, ctx: ReceitaParser.periodoContext):
        if ctx.remedio_periodo(0).remedio() is not None:
            return (ctx.getText(), ctx.remedio_periodo(0).remedio_g)
        return (ctx.getText(), ctx.remedio_periodo(0).letra)

    ## Verificação de tamanho do periodo
    ## Não é permitido que um periodo tenha apenas 1 contato
    def chekPeriodo(self):
        for periodo in self.periodos.keys():
            if len(self.periodos[periodo]) == 1:
                self.utils.adicionarErroSemantico(
                    self.periodos_ctx[periodo],
                    f"periodo '{periodo}' com apenas 1 membro",
                )
