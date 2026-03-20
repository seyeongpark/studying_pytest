# apps/mycalc.py

def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both a and b must be numbers.")
    return a + b

# add(2, 4.3) 

def substract(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both a and b must be numbers.")
    return a - b

def divide(a,b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both a and b must be numbers.")
    if b == 0: 
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b