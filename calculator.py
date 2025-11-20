"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    """Return b / a. Raise ZeroDivisionError if a == 0."""
    if a == 0:
        raise ZeroDivisionError("division by zero")
    return b / a

def log(a, b):
    """Return logarithm of b with base a.

    Raise ValueError for invalid base or argument (base <= 0, base == 1, or b <= 0).
    """
    if a <= 0 or a == 1:
        raise ValueError("invalid base for logarithm")
    if b <= 0:
        raise ValueError("logarithm undefined for non-positive values")
    return math.log(b, a)

def exp(a, b):
    return a ** b

