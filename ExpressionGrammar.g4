grammar ExpressionGrammar;

start
    : expr EOF
    ;

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
    | VARIABLE
    | CONSTANT
    | function
    ;

function
    : sinus
    | cosinus
    | tangent
    | cotangent
    | exponential
    | logarithm
    ;

sinus
    : 'sin' LPAREN expr RPAREN
    ;
cosinus
    : 'cos' LPAREN expr RPAREN
    ;
tangent
    : 'tan' LPAREN expr RPAREN
    ;
cotangent
    : 'cot' LPAREN expr RPAREN
    ;
exponential
    : 'e' POW factor
    | 'e' POW LBRAC expr RBRAC
    ;

logarithm
    : 'log_' LOGBASE LPAREN expr RPAREN
    | 'ln' LPAREN expr RPAREN
    ;
fragment LOGBASE
    : '0.' ('1' .. '9') ('0' .. '9')+
    | '1.' ('1' .. '9') ('0' .. '9')+
    | ('2' .. '9')+ ('.' ('0' .. '9')+)?
    ;

VARIABLE
    : CONSTANT 'x'
    |'x'
    ;

CONSTANT
    : LPAREN '-' NUMBER RPAREN
    | NUMBER
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
