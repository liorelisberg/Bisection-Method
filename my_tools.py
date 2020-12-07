import inspect
import numpy as np
from sympy import symbols


# Returns step number to reach the desired accuracy
def max_steps(a, b, err):
    s = int(np.floor(- np.log2(err / (b - a)) / np.log2(2) - 1))
    return s


def get_derivative(f):
    x = symbols('x')
    dev_f = eval('lambda x: {}'.format(f(x).diff(x)))
    return dev_f