lexer grammar ExpressionGrammarLexer;

VAR
    : 'x'
    ;

SIN
    : 'sin'
    ;

COS
    : 'cos'
    ;

TAN
    : 'tan'
    ;

COT
    : 'cot'
    ;

EXP
    : 'e'
    ;

LOG
    : 'log'
    ;

LN
    : 'ln'
    ;

NUMBER
    : '-'? [0-9]+ ('.' [0-9]+)?
    ;

LOGBASE
    : UNDER '0.' ('1' .. '9') ('0' .. '9')+
    | UNDER '1.' ('1' .. '9') ('0' .. '9')+
    | UNDER ('2' .. '9')+ ('.' ('0' .. '9')+)?
    ;

ADD
    : '+'
    | '-'
    ;

MUL
    : '*'
    | '/'
    ;

LPAREN
    : '('
    ;

RPAREN
    : ')'
    ;

LBRAC
    : '{'
    ;

RBRAC
    : '}'
    ;

PLUS
    : '+'
    ;

MINUS
    : '-'
    ;

TIMES
    : '*'
    ;

DIV
    : '/'
    ;

POINT
    : '.'
    ;

POW
    : '^'
    ;

UNDER
    : '_'
    ;

COMMA
    : ','
    ;

WS
    : [ \r\n\t]+ -> skip
    ;