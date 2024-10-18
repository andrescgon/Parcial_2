grammar LaplaceTransform;

// Tokens
FUNC : 'sin' | 'cos' | 'tan' | 'exp' | 'log' | 'sqrt' | 't'; // Funciones matemáticas
NUM  : [0-9]+ ( '.' [0-9]+ )? ; // Números, enteros o flotantes
ID   : [a-zA-Z_][a-zA-Z0-9_]* ; // Identificadores (variables)
OP   : '+' | '-' | '*' | '/' ; // Operadores
LPAR : '(' ;
RPAR : ')' ;
SEMI : ';' ;
WS   : [ \t\r\n]+ -> skip ; // Espacios en blanco

// Reglas
prog : statement* ;

statement
    : 'Laplace' LPAR expression RPAR SEMI  // Llamada a la función de Laplace
    ;

expression
    : term (OP term)* 
    ;

term
    : NUM 
    | ID 
    | FUNC LPAR expression RPAR 
    | LPAR expression RPAR
    ;
