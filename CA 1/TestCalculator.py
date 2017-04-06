# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:08:49 2017

@author: 10354686
"""

# Import the Python unittest functions
import unittest

# Import the functions defined in the 'Calculator' file
from Calculator import *

# Create a class which extends unittest.TestCase
class TestCalculator(unittest.TestCase):
    # This function is defined to test the add function created
    def testAdd(self):
        self.assertEqual(add(2,2),4)
        self.assertEqual(add(5,3),8)
        self.assertEqual(add(4,0),4)
    
    # This function is defined to test the subtract function created
    def testSubtract(self):
        self.assertEqual(subtract(2,2),0)
        self.assertEqual(subtract(5,3),2)
        self.assertEqual(subtract(4,0),4)
  
    # This function is defined to test the multiply function created
    def testMultiply(self):
        self.assertEqual(multiply(2,2),4)
        self.assertEqual(multiply(5,3),15)
        self.assertEqual(multiply(4,0),0)

    # This function is defined to test the divide function created
    def testDivide(self):
        # 4 / 1 = 4
        # 4 / 2 = 2        
        # 2 / 2 = 1
        # 0 / 1 = 0
        # 5 / 4 = 1.25
        # Divide by zero - return error        
        self.assertEqual(divide(4,1),4)
        self.assertEqual(divide(4,2),2)
        self.assertEqual(divide(2,2),1)
        self.assertEqual(divide(0,1),0)
        self.assertEqual(divide(5,4),1.25)
        self.assertEqual(divide(5,0),'error')

    # This function is defined to test the exponent function created
    def testExponent(self):
        self.assertEqual(exponent(2,2),4)
        self.assertEqual(exponent(2,3),8)
        self.assertEqual(exponent(3,3),27)

    # This function is defined to test the square root function created
    def testSqrroot(self):
        self.assertEqual(sqrroot(4),2)
        self.assertEqual(sqrroot(16),4)
        self.assertEqual(sqrroot(36),6)

    # This function is defined to test the tan function created
    def testTan(self):
        self.assertEqual(tan(0),0)
        self.assertEqual(tan(0.5),0.5463024898437905)
        self.assertEqual(tan(1),1.5574077246549023)

    # This function is defined to test the cos function created
    def testCos(self):
        self.assertEqual(cos(0),1)
        self.assertEqual(cos(0.5),0.8775825618903728)
        self.assertEqual(cos(1),0.5403023058681397)
  
    # This function is defined to test the sin function created
    def testSin(self):
        self.assertEqual(sin(0),0)
        self.assertEqual(sin(0.5),0.479425538604203)
        self.assertEqual(sin(1),0.8414709848078965)
 
    # This function is defined to test the factorial function created
    def testFactorial(self):
        self.assertEqual(factorial(5),120)
        self.assertEqual(factorial(8),40320)
        self.assertEqual(factorial(6),720)

 
if __name__ == '__main__':
    unittest.main()