grammar Receita;

// Esta é uma linguagem para escrever uma receita médica

receita_medica : prescricoes EOF;

// Uma receita deve ser composta por uma ou mais prescrições
prescricoes : prescricao+;

prescricao         :   LINE_BREAK? remedio LINE_BREAK 
                    ( periodo LINE_BREAK )?
					( dosagem LINE_BREAK 
                    | indicacao LINE_BREAK 
                    | aplicacao LINE_BREAK )+
                  ;

// É possível agrupar remédios no período (diurno, matutino ou noturno) de aplicação
periodo           : ('Diurno' | 'Matutino' | 'Noturno') ;

// Dosagem é composta por uma QUANTIDADE e uma unidade de medida
dosagem           : QUANTIDADE '/' medida ;

// QUANTIDADE da dosagem
QUANTIDADE        : '(' [0-9][0-9] ')' ;

// Medidas são compostas por comprimidos, mililitros ou miligramas
medida			:  ('Comprimidos' | 'Mililitros' | 'Miligramas' | 'comp.' | 'ml.' | 'mg.') WS?  ;

// Indicação do remédio
indicacao        : 'Indicação:' TEXTO;

// Aplicação são dispostas em via oral, retal e intravenosa
aplicacao : ('Oral' | 'Retal' | 'Intravenosa');

// Uma prescrição tem, no mínimo, um remédio
remedio   		: REMEDIO (WS REMEDIO)* ;

// Remédios devem iniciar com letra maiúscula e podem ser compostos de uma ou mais letras
REMEDIO			: [A-Z][a-z]*; 

// Texto genérico
TEXTO            : .;

SIMBOLO_INVALIDO : '!' | '#' | '$' | '%' | '*' | '=' | '+' | '?' | '<' | '>' | '|' | ':' | '{' | '}' | '[' | ']' ;

LINE_BREAK		: '\n' ;

WS				: ' ' ;