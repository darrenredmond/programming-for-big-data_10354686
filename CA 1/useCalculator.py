# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:38:25 2017

@author: 10354686
"""
# Import the calcul functions
from Calculator import *

print '''
********************************************************************************
                           Welcome to my Calculator
       This calculator allows you to use a number of different functions
           To use the calculator, simply follow the instructions

********************************************************************************
'''

operator_list = ['+','-','*','/','**','sqrt','tan','cos','sin','fact']

# Function to accept input and convert to lower
def text(message):
    while True:
        str_input = raw_input(message)   
        lowercase = str_input.lower()
        if lowercase in operator_list:
            return lowercase
            break
        else:
            print 'Error: Please choose a valid option!'
            continue

# Define function to accept input and convert to float
def input(message):
    while True:
        str_input = raw_input(message)
        try:    
            input = float(str_input)
            return input
            break
        except:
            print 'Error: Please enter a numerical value!'
            continue

while True:            
    operator = text("""Step 1: Please choose an operator by typing the indicated values;
    
    Addition         >    '+'
    Subtraction      >    '-'
    Multiplication   >    '*'
    Division         >    '/'
    Exponent         >    '**'
    Square Root      >    'sqrt'
    Tangent          >    'tan'
    Cosine           >    'cos'
    Sine             >    'sin'
    Factorial        >    'fact'
    
    Choose the operator:
    \n""")
    
    num1 = input('Step 2: Please provide the first number:\n')
    if operator == '+' or operator == '-' or operator == '*' or operator == '/' or operator == '**':
        num2 = input('Step 3: Please provide the second number:\n')
        
    if operator == '+':
        result = add(num1,num2)

    elif operator == '-':
        result = subtract(num1,num2)
        
    elif operator == '*':
        result = multiply(num1,num2)
        
    elif operator == '/':
        result = divide(num1,num2)

    elif operator == '**':
        result = exponent(num1,num2)

    elif operator == 'sqrt':
        result = sqrroot(num1)

    elif operator == 'tan':
        result = tan(num1)

    elif operator == 'cos':
        result = cos(num1)

    elif operator == 'sin':
        result = sin(num1)  

    elif operator == 'fact':
        result = factorial(num1)
        
    else:
        print 'Error'
        continue
        
    if operator == '+' or operator == '-' or operator == '*' or operator == '/' or operator == '**':  
        print '{} {} {} is equal to: {}'.format(num1,operator,num2,result)
        
    else:
        print '{} {} is equal to: {}'.format(operator,num1,result)
        
    choice = raw_input("Please type 'quit' to quit or anything else to calculate again\n")
    if choice == 'quit':
        print 'Have a nice day...'
        quit()
    else:
        continue
