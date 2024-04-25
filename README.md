# Yet Another Symbolic Differentiation Tool
TODO: Description

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
8. `(x + 2)^2 + sin(2*e^{tan(x)*cot(4)} + 3*cos(ln(x)/log_2(2))) - 1`
9. `2+2*2`


# Notes:
* Rebuild project:
  - Expression as ABC (Abstract Basic Class)
  - classes: Add, Mul, Sub, Div which repersent suitable operator
  - ~~Add and Mull with `flatten` method which work i.e. `Add(x, Add(x, x)).flattenn()` -> `Add(x, x, x,)`~~
  - ~~implement `__str__` as made in fluent python, add str representation of arguments to list, and then join this list to i.e. '\n'~~
  - for `Operator` and `Function` implement arithmetic operators, do this for generally working i.e `Operator() + Function() -> Add()`
  - generally test each of class, three tests for class, variable as argument, function as argument and operator as argument:
    - deriving
    - `__str__` representation
    - simplification
    - flatten if provided
  - make more test

**_NOTE:_** Example for `x+x+x` expression
```
e3 = Variable(1)
t2 = Variable(1)
e2 = Add(e3, t2)
t2 = Variable(1)
e1 = Add(e1, t1)
```
