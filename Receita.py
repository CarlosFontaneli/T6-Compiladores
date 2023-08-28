## coding: utf-8

import sys
from antlr4 import *
from antlr4.error.ErrorListener import *
from antlr4.tree.Trees import Trees
from ReceitaLexer import ReceitaLexer
from ReceitaParser import ReceitaParser
from ReceitaListener import ReceitaListener
from ReceitaVisitor import ReceitaVisitor
from ReceitaGerador import ReceitaGerador
from ReceitaSemantico import ReceitaSemantico
from ReceitaUtils import ReceitaUtils

## Símbolos não permitidos
invalid_symbols = [
    "!",
    "#",
    "$",
    "%",
    "*",
    "=",
    "+",
    "?",
    "<",
    ">",
    "|",
    ":",
    "{",
    "}",
    "[",
    "]",
]


## Procedimento usado para escrever o erro no arquivo
def escreveSaida(linha, coluna, erro, tipo):
    if tipo == "extraneous/mismatched" or tipo == "eof":
        arquivo.write(f"Linha {linha}: erro proximo a '{erro}'\n")

    else:
        arquivo.write(f"Linha {linha}: simbolo '{erro}' nao identificado\n")


class ReceitaErrorListener(ErrorListener):
    ## Sobrescrevendo a função padrão "syntaxError" do antlr4
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        err = offendingSymbol.text

        if (
            "extraneous input" in msg or "mismatched" in msg
        ) and err not in invalid_symbols:
            escreveSaida(line, column, err, "extraneous/mismatched")

        elif len(msg.split("'")) > 1 and err not in invalid_symbols:
            if "<EOF>" in err:
                err = "EOF"
            escreveSaida(line, column, err, "eof")

        else:
            escreveSaida(line, column, err, "simbolo")

        arquivo.write("Fim da compilacao\n")
        exit()


def main(argv):
    ## Obtenção dos parâmetros da linha de comando
    input = FileStream(argv[1], encoding="utf-8")
    output_file = argv[2]

    global arquivo
    arquivo = open(output_file, "w")

    lexer = ReceitaLexer(input)
    lexer.removeErrorListeners()
    stream = CommonTokenStream(lexer)
    parser = ReceitaParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ReceitaErrorListener())
    tree = parser.receita_medica()

    printer = ReceitaListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    # Análise semântica
    utils = ReceitaUtils(output_file, tree)
    # s = ReceitaSemantico(utils)
    # s.visitReceita_medica(tree)

    # A geração de código é feita somente se não houver nenhum erro semântico
    if len(utils.errosSemanticos) == 0:
        c = ReceitaGerador(utils)
        c.visitReceita_medica(tree)

    # Fechamento do arquivo / gravação do buffer
    arquivo.close()


if __name__ == "__main__":
    # Função principal (início do programa)
    main(sys.argv)
