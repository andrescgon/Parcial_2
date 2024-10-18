grammar MapFunction;

// Reglas del parser
expr: mapFunction EOF;

mapFunction: ('MAP' | 'FILTER') '(' functionCall ',' iterable ')';

functionCall: 'None' | IDENTIFIER | lambdaExpr;

lambdaExpr: 'lambda' IDENTIFIER ':' booleanExpr;

booleanExpr: exprBody (('and' | 'or') exprBody)*;

exprBody: IDENTIFIER relOp NUMBER;

relOp: '>' | '<' | '>=' | '<=' | '==' | '!=';

iterable: list | tuple | dictionary;

list: '[' listElement (',' listElement)* ']';
tuple: '(' listElement (',' listElement)* ')';
dictionary: '{' pair (',' pair)* '}';

listElement: NUMBER | IDENTIFIER | 'None' | 'True' | 'False' | STRING | '""';

pair: STRING ':' (NUMBER | STRING | 'None' | 'True' | 'False');

// Reglas del lexer
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
OP: '*' | '+' | '-' | '/' | '^' | '**';
NUMBER: [0-9]+;
STRING: '\'' [a-zA-Z_0-9]* '\''; // Para cadenas
WS: [ \t\r\n]+ -> skip;
