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
//    | logarithm
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

//logarithm
//    : LOG LOGBASE LPAREN expr RPAREN
//    | LOG LPAREN expr RPAREN
//    ;
//
//LOG
//    : 'log_'
//    | 'ln'
//    ;
//
//LOGBASE
//    : '0.' ('1' .. '9') ('0' .. '9')+
//    | '1.' ('1' .. '9') ('0' .. '9')+
//    | ('2' .. '9')+ ('.' ('0' .. '9')+)?
//    ;

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
