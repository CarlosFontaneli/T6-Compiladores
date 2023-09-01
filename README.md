# Autores

### Aquila Oliveira, 759313

### Carlos Eduardo Fontaneli , 769949

### Ingrid Lira dos Santos, 790888

## [Vídeo Explicativo Sobre a Linguagem:](https://drive.google.com/file/d/12v9iCT0SsVgJGvGxYeyJExYdzhF9dYmd/view?usp=sharing)

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

# Análises Semânticas Detalhadas

## 1. ReceitaSemantico.py

O arquivo `ReceitaSemantico.py` contém a classe `ReceitaSemantico`, que é responsável por realizar as verificações semânticas durante a análise da linguagem de receitas médicas. As principais análises realizadas são:

### 1.1. Verificação de Remédios Repetidos

A função `visitPrescricoes` itera pelas prescrições de remédios e verifica se algum remédio está sendo prescrito mais de uma vez. Se um remédio já estiver presente na lista de remédios, é emitido um erro semântico indicando a repetição.

### 1.2. Verificação de Dosagem Excedente

A função `visitDosagem` verifica se a dosagem de um remédio não excede limites pré-definidos. Para dosagens em mililitros (ml) ou miligramas (mg), a função verifica se a quantidade é maior que 1000. Se a dosagem exceder esse valor, é emitido um erro semântico.

### 1.3. Verificação de Dosagem de Comprimidos

A função `checkDosagemRange` verifica se a dosagem de comprimidos não excede um limite específico (10 comprimidos). Se a quantidade exceder esse limite, é emitido um erro semântico.

## 2. ReceitaGerador.py

O arquivo `ReceitaGerador.py` contém a classe `ReceitaGerador`, responsável por gerar o código HTML a partir das regras da linguagem. As principais análises realizadas são:

### 2.1. Geração de Código HTML

A função `visitReceita_medica` gera o código HTML para representar uma receita médica. Isso inclui as prescrições de remédios, períodos, dosagens, aplicações e indicações. Cada parte da prescrição é formatada conforme as regras definidas.

## 3. ReceitaUtils.py

O arquivo `ReceitaUtils.py` contém a classe `ReceitaUtils`, que é responsável por armazenar erros semânticos e o código HTML gerado. A análise semântica em si não é realizada nesse arquivo, mas ele é utilizado para coletar informações relevantes e gerar a saída.

### 3.1. Armazenamento de Erros Semânticos

A função `adicionarErroSemantico` armazena erros semânticos em uma lista para posterior exibição ou gravação. Isso permite que erros como remédios repetidos ou dosagens excedentes sejam registrados durante a análise semântica.

### 3.2. Armazenamento de Código Gerado

A função `adicionarCodigo` armazena o código HTML gerado em uma lista, para posterior gravação em um arquivo. Isso permite que o código gerado seja mantido em memória antes de ser gravado no arquivo de saída.

---

As análises semânticas detalhadas acima garantem que a linguagem de receitas médicas seja analisada corretamente e que erros semânticos sejam identificados e relatados de maneira apropriada.
