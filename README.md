# Bisection Algorithm using python

### The following algorithm determines the roots of a polynomial (with approx tolerance)
### function of any degree, such as : 
### `` an*X^n + a(n-1)*X^(n-1) + ... + a2*X^2 + a1*X + a0`` where ``an,...a2,a1,0`` are constants and ``x`` is the indeterminate.
#
##### The algorithms will determine the polynomial roots of the equation, using the Bisection Method,
##### from the given input of range (``a``,``b``) , ``step size`` and allowed ``tolerance`` values.
#
**included files :**
- **main.py** - contains basic input of the polynomial equation, start axis & end axis values and step size for each iteration.
- **my_tools.py** - constains :
- - - get_derivative(f) - computes & returns the derivative equation of a mathematical lambda expression ``f``
- - - max_steps(a, b, err) - computes & returns the approx number of steps required to determine a root, wheres (``a``,``b``) is the range of values,
- - - - and ``err`` is the tolerable error.
**The algoritm will than print the list of roots.**
#
**requirments :**
- python>3.0.
- Numpy version 1.19.3 (previous to 1.19.4 -> had some issues initializing it).
- Sympy - latest version.
- all input should be valid  -> no validations were made.
- all functions, **my_tools.py** functions infcluded, must recieve valid parameters! -> no validations were made.
