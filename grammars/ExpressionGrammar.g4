grammar ExpressionGrammar;

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
    | variable
    | constant
    | function
    ;

function
    : sinus
    | cosinus
    | tangent
    | cotangent
    | exponential
    | power
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
power
    : variable POW NUMBER
    | constant POW NUMBER
    | 'pow' LPAREN factor ',' NUMBER RPAREN
    | 'pow' LPAREN expr ',' NUMBER RPAREN
    ;

logarithm
    : 'log' LOGBASE LPAREN expr RPAREN
    | 'ln' LPAREN expr RPAREN
    ;


variable
    : NUMBER 'x'
    |'x'
    ;

constant
    : LPAREN '-' NUMBER RPAREN
    | NUMBER
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

WS
    : [ \r\n\t]+ -> skip
    ;
