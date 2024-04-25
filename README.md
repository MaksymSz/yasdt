# Yet Another Symbolic Differentiation Tool

TODO: Description

# Roadmap:

* Improve printing operators
* Do simple GUI

# Tests

3. `(-12.3*e^x + 7) / x` ugly printing

# Notes:

* Rebuild project:
    - Expression as ABC (Abstract Basic Class)
    - improve Sub printing
    - classes: Add, Mul, Sub, Div which repersent suitable operator
    - ~~Add and Mull with `flatten` method which work i.e. `Add(x, Add(x, x)).flattenn()` -> `Add(x, x, x,)`~~
    - ~~implement `__str__` as made in fluent python, add str representation of arguments to list, and then join this
      list to i.e. '\n'~~
    - for `Operator` and `Function` implement arithmetic operators, do this for generally working
      i.e `Operator() + Function() -> Add()`
    - generally test each of class, three tests for class, variable as argument, function as argument and operator as
      argument:
        - deriving
        - `__str__` representation
        - simplification
        - flatten if provided
    - make more test
