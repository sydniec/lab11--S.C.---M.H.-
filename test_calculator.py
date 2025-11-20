# https://github.com/sydniec/lab11--S.C.---M.H.-
# Partner 1: sydniec
# Partner 2: Rakibul Hai

import unittest
from calculator import *



class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-2, -3), 1)
    # ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(-1, -1), 1)
        self.assertEqual(mul(-4, 10), -40)
        self.assertEqual(mul(8, 8), 64)
        self.assertEqual(mul(18, 0), 0)

    def test_divide(self):
        self.assertAlmostEqual(div(-1, 1), -1)
        self.assertAlmostEqual(div(-8, 64), -8)
        self.assertAlmostEqual(div(4, 0), 0)
        self.assertAlmostEqual(div(15, 225), 15)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(math.e, math.e**2), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 10)
    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, 0)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(1, 1), math.sqrt(2))
        self.assertAlmostEqual(hypotenuse(-4, 3), 5)
        self.assertAlmostEqual(hypotenuse(-3, -3), math.sqrt(18))
        self.assertAlmostEqual(hypotenuse(2, 3), math.sqrt(13))

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(225), 15)

# Do not touch this
if __name__ == "__main__":
    unittest.main()