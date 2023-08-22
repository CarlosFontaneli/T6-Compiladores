from ReceitaParser import ReceitaParser


class ReceitaUtils:
    ## Listas de erros e de código
    def __init__(self, arquivo, tree):
        self.errosSemanticos = []
        self.codigo = []
        self.ref_arquivo = arquivo

    ## Adiciona a mensagem de erro
    def adicionarErroSemantico(self, t, mensagem):
        linha = t.line
        self.errosSemanticos.append(f"Linha {linha}: {mensagem}")

    ## Adiciona o código HTML na lista correspondente
    def adicionarCodigo(self, string):
        self.codigo.append(string)

    def __del__(self):
        self.arquivo = open(self.ref_arquivo, "w")

        if len(self.errosSemanticos) > 0:
            for erro in self.errosSemanticos:
                self.arquivo.write(erro + "\n")
            self.arquivo.write("Fim da compilacao\n")

        else:
            for linha in self.codigo:
                self.arquivo.write(linha)

        self.arquivo.close()
