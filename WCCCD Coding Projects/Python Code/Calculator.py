"""
File: calculator.py
Description:
"""
import math


class Calculator(object):
    """Description"""
    def __init__(self, a, b):
        """Description"""
        self.num1 = a
        self.num2 = b

    def getFirst(self):
        """gets 1st number"""
        return self.num1

    def getSecond(self):
        """gets 2nd number"""
        return self.num2

    def setFirst(self, a):
        """Change 1st variable"""
        self.num1 = a

    def setSecond(self, a):
        """change 2nd variable"""
        self.num2 = a

    def add(self):
        """Adds the 2 numbers together"""
        return self.num1 + self.num2

    def subtract(self):
        """Subtracts 1st number from 2nd number"""
        return self.num1 - self.num2

    def multiply(self):
        """Multiplies 1st and 2nd number"""
        return self.num1 * self.num2

    def divide(self):
        """Divides 1st by 2nd number"""
        if self.num2 == 0:
            print("Cannot divide by zero")
            return None
        else:
            return self.num1 / self.num2

    def sqrt(self, x):
        """returns square root"""
        if x == 1:
            if self.num1 < 0:
                print("Square Root cannot have a negative number.")
                return None
            return math.sqrt(self.num1)
        elif x == 2:
            if self.num2 < 0:
                print("Square Root cannot have a negative number.")
            return math.sqrt(self.num2)
        else:
            return None

    def square(self, x):
        """Prints the square of the number"""
        if x == 1:
            return self.num1 ** 2
        elif x == 2:
            return self.num2 ** 2
        else:
            return None

    def cube(self, x):
        """prints the cube"""
        if x == 1:
            return self.num1 ** 3
        elif x == 2:
            return self.num2 ** 3
        else:
            return None

    def fifth(self, x):
        if x == 1:
            return self.num1 ** 5
        elif x == 2:
            return self.num2 ** 5
        else:
            return None

    def __str__(self):
        return str(self.num1) + " " + str(self.num2)

    def setValue(self, p, q):
        if q == 1:
            self.num1 = p
        elif q == 2:
            self.num2 = p

    def getValue(self, a, b):
        if a == 1:
            return self.num1
        elif b == 2:
            return self.num2
