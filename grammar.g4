grammar expressions;

expr
    : term
    | expr ADD term
    ;

term
    : factor
    | term MUL factor
    ;

factor
    : LPAREN E RPAREN
    | arg
    ;

arg
    : VARIABLE
    | CONSTANT
    | function
    ;

function
    : sin
    | cos
    | tan
    | cot
    | exp
    | power
    | log
    ;

sin
    : 'sin' LPAREN E RPAREN
    ;
cos
    : 'cos' LPAREN E RPAREN
    ;
tan
    : 'tan' LPAREN E RPAREN
    ;
cot
    : 'cot' LPAREN E RPAREN
    ;
exp
    : 'e' POW arg
    | 'e' POW LBRAC expr RBRAC
    ;
power
    : factor POW CONSTANT
    ;
log
    : 'log_' LOGBASE LPAREN E RPAREN
    | 'ln' LPAREN E RPAREN
    ;
fragment LOGBASE
    : '0.' ('1' .. '9') ('0' .. '9')+
    | '1.' ('1' .. '9') ('0' .. '9')+
    | ('2' .. '9')+ ('.' ('0' .. '9')+)?
    ;

VARIABLE
    : CONSTANT 'x'
    ;

CONSTANT
    : LPAREN '-' NUMBER RPAREN
    : NUMBER
    ;

fragment NUMBER
    : ('0' .. '9')+ ('.' ('0' .. '9')+)?
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

WS
    : [ \r\n\t]+ -> skip
    ;
