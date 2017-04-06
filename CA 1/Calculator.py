# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Import the Python Math functions
import math 

# This is my add function. It takes two numbers and adds them
def add(first, second):
    number_types = (int, long, float, complex)
 
    if isinstance(first, number_types) and isinstance(second, number_types):
        return first + second
    else:    
        raise ValueError

# This is my subtract function. It takes two numbers and subtracts the second from the first 
def subtract(first, second):
    number_types = (int, long, float, complex)
 
    if isinstance(first, number_types) and isinstance(second, number_types):
        return first - second
    else:    
        raise ValueError

# This is my multiply function. It takes two numbers and multiplies them    
def multiply(first, second):
    number_types = (int, long, float, complex)
 
    if isinstance(first, number_types) and isinstance(second, number_types):
        return first * second
    else:    
        raise ValueError

# This is my divide function. It takes two numbers and divides the second from the first    
def divide(first, second):
    response = None
    if second == 0:
        response = 'error'
        return response
    else:
        number_types = (int, long, float, complex)
 
        if isinstance(first, number_types) and isinstance(second, number_types):
            return first / float(second)
        else:    
            raise ValueError

# This is my exponent function. It takes two numbers and returns the first number to the power of the second  number    
def exponent(first, second):
    number_types = (int, long, float, complex)
 
    if isinstance(first, number_types) and isinstance(second, number_types):
        return first ** second
    else:    
        raise ValueError
    
# This is my square root function. It calculates the square root of a number
def sqrroot(first):
    number_types = (int, long, float, complex)
 
    if isinstance(first, number_types):
        return math.sqrt(first)
    else:    
        raise ValueError

    
# This is my Tan function, it calculates the tangent of a number
def tan(first):
    number_types = (int, long, float, complex)
 
    if isinstance(first, number_types):
        return math.tan(first)
    else:    
        raise ValueError
    
# This is my Cos function, it calculates the cosine of a number
def cos(first):
    number_types = (int, long, float, complex)
 
    if isinstance(first, number_types):
        return math.cos(first)
    else:    
        raise ValueError
    
# This is my Sin function, it calculates the sine of a number
def sin(first):
    number_types = (int, long, float, complex)
 
    if isinstance(first, number_types):
        return math.sin(first)
    else:    
        raise ValueError
    
# This is my Factorial function, it calculates the factorial of a number
def factorial(first):
    number_types = (int, long, float, complex)
 
    if isinstance(first, number_types):
        return math.factorial(first)
    else:    
        raise ValueError
 
       

     


