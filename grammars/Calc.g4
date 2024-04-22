grammar Calc;

expr
    : term
    | term ADD expr
    ;

term
    : factor
    | factor MUL term
    ;

factor
    : LPAREN expr RPAREN
    | NUMBER
    ;
// Lexer rules
ADD
    : '+'
    ;

MUL
    : '*'
    ;

LPAREN
    : '('
    ;

RPAREN
    : ')'
    ;
NUMBER: [0-9]+ ('.' [0-9]+)?;
WS: [ \t\r\n]+ -> skip;