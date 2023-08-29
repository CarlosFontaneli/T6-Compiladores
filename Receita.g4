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
