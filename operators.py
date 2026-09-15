import math

def subtraction(a, b):

    return a - b

def aggregate(a, b):

    return a + b

def multiply(a, b):

    return a * b

def division(a, b):

    if b == 0:
        raise ValueError("You cannot divide by zero")

    return a / b

def square_root(a):

    if a <= 0:
        raise ValueError("Negative numbers are not allowed")

    return math.sqrt(a)

def log(a):
    if a <= 0:
        raise ValueError("Log just define for positive numbers ")

    return math.log(a)

def power(a, b):
    return math.pow(a, b)

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def arcsin(a):
    if a < -1 or a > 1:
        raise ValueError("Input must be between -1 and 1")
    return math.degrees(math.asin(a))
def arccos(a):
    if a < 0 or a > 1:
        raise ValueError("Input must be between -1 and 1")
    return math.degrees(math.acos(a))
