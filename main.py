import math

from my_tools import *


# paragraph 1 - bisection_method
def bisection_method(p, start, end, tol=1e-6):
    a, b = start, end
    c, k = 0, 0
    steps = max_steps(start, end, tol)  # calculate the max steps possible

    # while the diff af a&b is not smaller than tol, and k is not greater than the max possible steps
    while abs(b - a) > tol and k < steps:
        c = (a + b) / 2  # c gets the average value of a & b
        if p(c) * p(a) < 0:  # if sign changed between steps
            b = c  # move forward
        else:
            a = c  # move backward

        if c == 0:  # if c=0, than 0 is a root
            return c
        k += 1

    return c  # return the current root


# paragraph 2 - find_polynomial_roots
def find_polynomial_roots(p, start, end, step_size, tol):
    a = start
    roots = list()
    while a + step_size <= end:  # while current value is still in range
        b = a + step_size  # b is equal to the next step
        if p(a) * p(b) < 0:  # if sign changed between steps
            root = bisection_method(p, a, b, tol)  # get the root in range (a,b)
            roots.append(root)  # append to list of roots
        a = b  # a gets the next step

    dp = get_derivative(p)  # derivative of p
    a, b = start, 0  # reset values
    while a + step_size <= end:  # while current value is still in range
        b = a + step_size  # b is equal to the next step
        if dp(a) * dp(b) < 0:  # if sign changed between steps
            root = bisection_method(dp, a, b, tol)  # get the root in range (a,b)

            # check if the root is or close to zero
            if math.isclose(p(root), 0.0, abs_tol=tol):
                roots.append(root)  # append to list of roots
        a = b  # a gets the next step

    return roots


# paragraph 3 - main
if __name__ == '__main__':
    # polynomial function input
    print('Insert Polynomial function :')
    fx = input('Y = ')

    # start, end, step size inputs
    start = float(input('Insert start for computing range :\t'))
    end = float(input('Insert end for computing range :\t'))
    step_size = float(input('Insert step size for computing range :\t'))

    # get the list of roots from the function
    roots = find_polynomial_roots(lambda x: eval(fx), start, end, step_size)

    # output
    print('The roots of the polynomial function Y = {} :'.format(fx))
    print(" ".join(map(str, roots)))

    # test
    # f0 = 'x ** 3 - 3 * x ** 2'
    # fx = lambda x: x ** 3 - 3 * x ** 2
    # start, end, step_size = -4.6, 8, 0.35
    # roots = find_polynomial_roots(fx, start, end, step_size, 1e-6)
    # # output
    # print('The roots of the polynomial function Y = {} :'.format(f0))
    # print(" ".join(map(str, roots)))
