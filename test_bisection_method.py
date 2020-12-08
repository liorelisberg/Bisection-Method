import unittest
from bisection_method_main import find_polynomial_roots


class TestBisectionMethod(unittest.TestCase):

    #f(x)=x^3-3x
    def test_FX(self):
        roots = find_polynomial_roots(lambda x: x ** 3 - 3 * x ** 2, -4, 8, 0.35)
        self.assertAlmostEqual(roots[0].__round__() , 3)

    #d(x)=x^2+6x
    def test_DX(self):
        roots = find_polynomial_roots(lambda x: x ** 2 + 6 * x, -6.5, -5.5, 0.10)
        self.assertAlmostEqual(roots[0].__round__(), -6)

    #g(x)=x^2+6x
    def test_GX(self):
        roots = find_polynomial_roots(lambda x: x ** 3 - 6 * x + 4, 0, 1, 0.01)
        self.assertAlmostEquals(roots[0], 0.7,1)

if __name__ == '__main__':
    unittest.main()
