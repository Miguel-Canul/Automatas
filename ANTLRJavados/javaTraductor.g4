grammar javaTraductor;

// Reglas principales
file: (funcDef | stmt)* EOF;
funcDef: 'def' funcName '(' parameters? ')' ':' suite;
suite: stmt+;

stmt
    : returnStmt
    | assignStmt
    | exprStmt
    ;

returnStmt: 'return' expr;
assignStmt: varName '=' expr;
exprStmt: expr;

// Llamada a función
funcCall: funcName '(' arguments? ')';
arguments: expr (',' expr)*;

// Expresiones aritméticas
expr: expr op=('*'|'/') expr
    | expr op=('+'|'-') expr
    | funcCall
    | varName
    | NUMBER
    ;

parameters: varName (',' varName)*;
funcName: NAME;
varName: NAME;

// Tokens
NUMBER: [0-9]+;
NAME: [a-zA-Z_][a-zA-Z0-9_]*;

// Ignorar espacios y líneas en blanco
WS: [ \t\r\n]+ -> skip;
