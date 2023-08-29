# Linguagem Receita

A linguagem Receita é utilizada para descrever prescrições médicas, indicando o medicamento a ser tomado, o período em que deve ser tomado, a dosagem a ser administrada, além de opcionalmente incluir a aplicação e a indicação da prescrição. Neste arquivo, explicaremos como a linguagem funciona, fornecendo exemplos de código e instruções para testar e executar programas escritos na linguagem Receita.

## Código da linguagem

```antlr
// Esta é uma linguagem para descrever prescrições médicas (medicamentos, período, dosagem, aplicação e indicação).

// Uma prescrição médica é composta por um ou mais contatos.
receita_medica : prescricoes EOF;

// Para compor a lista de prescrições, é necessário ter pelo menos uma prescrição.
prescricoes : prescricao+;

// Uma prescrição é composta por um medicamento, período, dosagem, aplicação e indicação.
prescricao : LINE_BREAK? remedio LINE_BREAK
            ( periodo LINE_BREAK )
            ( dosagem LINE_BREAK )
            ( aplicacao LINE_BREAK )?
            ( indicacao LINE_BREAK )?;

// Um medicamento é um texto que começa com letra maiúscula, seguido por letras minúsculas (ou seja, segue o padrão de nome de pessoa).
remedio : REMEDIO (WS REMEDIO)* ;

// Um período é definido como 'Diurno', 'Matutino' ou 'Noturno'.
periodo : ('Diurno' | 'Matutino' | 'Noturno');

// A dosagem é definida como uma quantidade seguida por uma unidade de medida.
dosagem : quantidade WS medida;

// A quantidade é uma sequência de dígitos (números).
quantidade : NUMERO*;
NUMERO : [0-9]+;

// A unidade de medida pode ser 'Comprimidos', 'Mililitros' ou 'Miligramas'.
medida : UNIDADE*;
UNIDADE : ('Comprimidos' | 'Mililitros' | 'Miligramas');

// A aplicação é definida como 'Oral', 'Retal' ou 'Intravenosa'.
aplicacao : ('Oral' | 'Retal' | 'Intravenosa');

// A indicação é um texto em letras minúsculas que descreve a razão da prescrição.
indicacao : TEXTO;

// Um texto é composto por letras minúsculas ou espaços.
TEXTO : ([a-z] | ' ')+;

// Espaço em branco, incluindo quebras de linha.
WS : ' ';

// Quebra de linha.
LINE_BREAK : '\n';

```

## Estrutura da Linguagem

A linguagem Receita possui a seguinte estrutura básica:

1. A primeira linha contém o nome do medicamento.
2. A segunda linha contém o período em que o medicamento deve ser tomado.
3. A terceira linha contém a dosagem a ser administrada.
4. As linhas subsequentes (opcionais) podem conter a aplicação do medicamento e a indicação da prescrição.

## Exemplo de Código

Aqui está um exemplo de um programa na linguagem Receita:

```txt
Dipirona
Matutino
300 Miligramas
Oral
febre
```

Neste exemplo, o programa descreve uma prescrição médica para o medicamento "Dipirona". O medicamento deve ser tomado no período "Matutino" e a dosagem é de "300 Miligramas". Além disso, a prescrição informa que o medicamento deve ser administrado "Oralmente" e é indicado para tratar a "Febre".

## Execução da Linguagem

Para executar a linguagem Receita usando o ANTLR4, siga os seguintes passos:

1. Instale o ANTLR4 em seu sistema, caso ainda não tenha feito isso.
2. Abra o terminal e navegue até o diretório que contém o arquivo "Receita.g4".
3. Execute o seguinte comando para gerar os arquivos de parser e lexer em Python:

```shell
antlr4 -Dlanguage=Python3 Receita.g4 -visitor
```

4. Após gerar os arquivos, você pode executar programas escritos na linguagem Receita usando o seguinte comando:

```shell
python3 Receita.py <arquivo_entrada.txt> <arquivo_saida.html>
```

## Testes Automatizados

Para rodar os testes automatizados da linguagem Receita, siga os passos abaixo:

1. Certifique-se de que você possui o Python 3 instalado.
2. Navegue até o diretório que contém os arquivos de teste (por exemplo, "testes").
3. Execute o seguinte comando para rodar os testes automatizados:

```shell
python3 RodaTestes.py
```

Os testes automatizados verificarão o funcionamento correto da linguagem Receita em diferentes cenários.

Agora você está pronto para explorar e testar a linguagem Receita! Sinta-se à vontade para criar seus próprios programas de prescrições médicas e testá-los com os comandos fornecidos acima.
