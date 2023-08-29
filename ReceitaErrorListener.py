from antlr4.error.ErrorListener import *


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
