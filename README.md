# Yet Another Symbolic Differentiation Tool
TODO: Description

# Grammar:
**_TODO_** delete left-side factorization in **U_EXP**, delete **I** by move his productions to **F**
**_TODO_** add Subtraction and Deriving operators
```md
grammar expressions;

expr
  : term
  | expr OPER1 term
  ;

term
  : factor
  | term OPER1 factor
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
  - [ ] exponential function
  - [x] polynomials
  - [x] power
  - [ ] tangent and cotangent
  - [ ] logarithm
* After getting known with parsing trees generated with ANTLR4 create class `ExpressionBuilder` for building expressions while traversing tree
* In future may add eval() function for plotting graphs and maybe general function plot() to plot visualization of given expression
* Do simple GUI
* Add method, that generate latex notation for expression

# Tests
Custom test, e.i. some large expressions etc.

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
