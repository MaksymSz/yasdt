# Yet Another Symbolic Differentiation Tool
TODO: Description

# Grammar:
**_TODO_** delete left-side factorization in **U_EXP**, delete **I** by move his productions to **F**
```md
E &rarr; T | E+T
T &rarr; F | T+F
F &rarr; (E) | I
I &rarr; x | c | U
U &rarr; U_FUNCNAME

U_SIN &rarr; sin(E)
U_COS &rarr; cos(E)
U_TAN &rarr; tan(E)
U_COT &rarr; cot(E)
U_EXP &rarr; e^U | e^{E}
U_POW &rarr; E^c
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
