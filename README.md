# Bisection Algorithm using python

### The following algorithm determines the roots of a polynomial (with approx tolerance)
### function of any degree, such as : 
### `` an*X^n + a(n-1)*X^(n-1) + ... + a2*X^2 + a1*X + a0`` where ``an,...a2,a1,0`` are constants and ``x`` is the indeterminate.
#
##### The algorithms will determine the polynomial roots of the equation, using the Bisection Method,
##### from the given input of range (``a``,``b``) , ``step size`` and allowed ``tolerance`` values.
#
**included files :**
- **main.py** - contains : 
  - bisection_method(p, start, end, tol=1e-6) - given the following ``p`` (polynomial lambda equation), ``start`` & ``end`` values (examined range of X axis),
  ``tol`` (the allowed tolerable error) - the function computes & returns the root in range (``a``,``b``).
  - find_polynomial_roots(p, start, end, step_size, tol) -  given the following ``p`` (polynomial lambda equation), ``start`` & ``end`` values (examined range of X axis),
  ``step_size`` (size of movment between values on X axis) and ``tol`` (the allowed tolerable error) - the function computes & returns the list of polynomial roots, using the       bisection_method() function.
- **my_tools.py** - constains :
  - get_derivative(f) - computes & returns the derivative equation of a mathematical lambda expression ``f``
  - max_steps(a, b, err) - computes & returns the approx number of steps required to determine a root, wheres (``a``,``b``) is the range of values,
      and ``err`` is the tolerable error.
**The algoritm will than print the list of roots.**
#
**requirments :**
- python>3.0.
- Numpy version 1.19.3 (previous to 1.19.4 -> had some issues initializing it).
- Sympy - latest version.
- all input should be valid  -> no validations were made.
- all functions, **my_tools.py** functions infcluded, must recieve valid parameters! -> no validations were made.
