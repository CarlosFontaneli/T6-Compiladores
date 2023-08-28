grammar Receita;

receita_medica : prescricoes EOF;

prescricoes : prescricao+;

prescricao : LINE_BREAK? remedio LINE_BREAK 
            ( periodo LINE_BREAK ) 
            ( dosagem LINE_BREAK)   
            (aplicacao LINE_BREAK)?
            (indicacao LINE_BREAK)?;


periodo : ('Diurno' | 'Matutino' | 'Noturno');

dosagem : quantidade WS medida;

quantidade : NUMERO*;
NUMERO : [0-9]+;

medida : UNIDADE*;
UNIDADE : ('Comprimidos' | 'Mililitros' | 'Miligramas');


indicacao : TEXTO;

aplicacao : ('Oral' | 'Retal' | 'Intravenosa');

remedio : REMEDIO (WS REMEDIO)* ;

REMEDIO : [A-Z][a-z]*;

LINE_BREAK : '\n';

WS : ' ';

TEXTO : ([a-z] | ' ')+;