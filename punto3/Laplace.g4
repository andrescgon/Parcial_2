grammar Laplace;

// Reglas de entrada
expression
    : integral
    | function (LPAREN argument RPAREN)? // Soporta funciones con un argumento
    ;

integral
    : INT LPAREN function RPAREN DT // Sintaxis para la integral
    ;

function
    : IDENTIFIER // Nombre de la función (por ejemplo, f, g)
    ;

argument
    : expression // Permite la recursión de expresiones
    | NUMBER     // Para números
    | IDENTIFIER // Para variables
    ;

// Tokens
IDENTIFIER
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

NUMBER
    : [0-9]+ ('.' [0-9]+)? // Números enteros y flotantes
    ;

LPAREN
    : '('
    ;

RPAREN
    : ')'
    ;

INT
    : 'int'
    ;

DT
    : 'dt'
    ;

WS
    : [ \t\r\n]+ -> skip // Ignorar espacios en blanco
    ;
