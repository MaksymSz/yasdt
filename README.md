# Yet Another Symbolic Differentiation Tool
TODO: Description

# Grammar:
TODO: Add grammar, and add syntax tree for example expression

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
  - 
