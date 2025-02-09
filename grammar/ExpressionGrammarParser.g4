parser grammar ExpressionGrammarParser;

options {
    tokenVocab = ExpressionGrammarLexer;
}

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
    | LPAREN expr RPAREN POW NUMBER
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
    : SIN LPAREN expr RPAREN
    ;
cosinus
    : COS LPAREN expr RPAREN
    ;
tangent
    : TAN LPAREN expr RPAREN
    ;
cotangent
    : COT LPAREN expr RPAREN
    ;
exponential
    : EXP POW factor
    | EXP POW LBRAC expr RBRAC
    ;
power
    : variable POW NUMBER
    | constant POW NUMBER
    ;

logarithm
    : LOG LOGBASE LPAREN expr RPAREN
    | LN LPAREN expr RPAREN
    ;


variable
    : NUMBER VAR
    | VAR
    ;

constant
    : LPAREN MINUS NUMBER RPAREN
    | NUMBER
    ;

