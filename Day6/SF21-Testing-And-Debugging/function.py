from decimal import DivisionByZero

def add(x, y):
    return x + y

def product(x, y):
    return x * y

def division(x, y):
    if y ==0:
        raise DivisionByZero
    return x/y