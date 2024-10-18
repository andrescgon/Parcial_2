grammar RationalExpr;

// La regla inicial
prog: expr EOF;

// Operaciones de suma y resta
expr: expr ('+' | '-') term 
    | term;

// Operaciones de multiplicación y división
term: term ('*' | '/') factor
    | factor;

// Fracciones
factor: FRACTION
      | INT
      | '(' expr ')';

// Definición de la fracción (num/den)
FRACTION: INT '/' INT;

// Definición de enteros
INT: '-'? [0-9]+;

// Ignorar espacios en blanco
WS: [ \t\r\n]+ -> skip;
