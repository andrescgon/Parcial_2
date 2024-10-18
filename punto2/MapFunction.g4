grammar MapFunction;

// Reglas del parser
expr: mapFunction EOF;

mapFunction: 'MAP' '(' functionCall ',' iterable ')';

functionCall: IDENTIFIER | lambdaExpr;

lambdaExpr: 'lambda' IDENTIFIER ':' exprBody;

exprBody: IDENTIFIER OP NUMBER | IDENTIFIER '.' IDENTIFIER '(' ')';

iterable: list | tuple | dictionary; // Agregar diccionario a las opciones

list: '[' NUMBER (',' NUMBER)* ']' | '[' '\'' IDENTIFIER '\'' (',' '\'' IDENTIFIER '\'' )* ']';
tuple: '(' NUMBER (',' NUMBER)* ')' | '(' '\'' IDENTIFIER '\'' (',' '\'' IDENTIFIER '\'' )* ')';
dictionary: '{' pair (',' pair)* '}'; // Nueva regla para diccionarios

pair: '\''IDENTIFIER '\'' ':' (NUMBER | '\'' IDENTIFIER '\'' ); // Clave: valor, donde el valor puede ser un número o un identificador

// Reglas del lexer
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
OP: '*' | '+' | '-' | '/' | '^' | '**';
NUMBER: [0-9]+;

// Ignorar espacios
WS: [ \t\r\n]+ -> skip;




