# Yet Another Symbolic Differentiation Tool
TODO: Description

# Grammar:
```md
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
LOGBASE
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
```

**_NOTE:_** *c* stands for Constant, *x* stands for Variable

# Roadmap:
* For better computation, add simplify after every differentiation
* More elementary functions:
  - [x] exponential function
  - [ ] polynomials
  - [x] power
  - [x] tangent and cotangent
  - [x] logarithm
* After getting known with parsing trees generated with ANTLR4 create class `ExpressionBuilder` for building expressions while traversing tree
* In future may add eval() function for plotting graphs and maybe general function plot() to plot visualization of given expression
* Improve printing operators
* Do simple GUI
* Add method, that generate latex notation for expression

# Tests
1. `x + x * x`
2. `x * x + x * x`
3. `sin(x) + cos(2x)`
4. `sin(e^x) * ln(x - 2x)`
5. `(x + 2x) * sin((-4)x + e^3) - cos(x * x)`
6. `e^{sin(2 * x)} + 3x^2 - 5`
7. `(-12.3e^3 + 7) / x`


# Notes:
* Rebuild project:
  - Expression as ABC (Abstract Basic Class)
  - classes: Add, Mul, Sub, Div which repersent suitable operator
  - Add and Mull with `flatten` method which work i.e. `Add(x, Add(x, x)).flattenn()` -> `Add(x, x, x,)`

**_NOTE:_** Example for `x+x+x` expression
```
e3 = Variable(1)
t2 = Variable(1)
e2 = Add(e3, t2)
t2 = Variable(1)
e1 = Add(e1, t1)
```
