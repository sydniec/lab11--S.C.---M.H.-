"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

# First example
def square_root(a):
    assert a > 0, "ValueError"
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a *b

def divide(a, b):
    assert a != 0, "ZeroDivisionError"
    return b / a

def logarithm(a, b):
    assert b > 0, "ValueError"
    assert a > 0, "ValueError"
    assert a != 1, "ValueError"
    return math.log(a, b)

def exponent(a, b):
    return a ** b

