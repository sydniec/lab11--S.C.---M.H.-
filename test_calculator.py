import unittest
import math
from calculator import *

# https://github.com/sydniec/lab11--S.C.---M.H.-
# Partner 1: sydniec
# Partner 2: Rakibul Hai


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(0, 5), -5)
        self.assertEqual(sub(-2, -3), 1)
    # ##########################

    ######## Partner 1
    # partner 1 tests (left for partner)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(log(10, 100), 2)
        self.assertAlmostEqual(log(2, 8), 3)
        self.assertAlmostEqual(log(math.e, math.e**2), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(1, 10)
    # ##########################

    ######## Partner 1
    # partner 1 tests (left for partner)

# Do not touch this
if __name__ == "__main__":
    unittest.main()