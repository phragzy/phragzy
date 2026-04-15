"""
Program - Calculator
Author: Joseph 
Date Written: 07/23/2024
Last Edited: 07/24/2024

Description: This calculator imports from calculator and runs calculations on X, Y, and Z
"""

from Calculator import Calculator


def main():
    x = Calculator(2.5, 5)
    y = Calculator(20.5, 17.3)
    z = Calculator(-10.2, 0)

    """X solutions below"""
    print(x.getFirst(), "+", x.getSecond(), "=", x.add())
    print(x.getFirst(), "-", x.getSecond(), "=", x.subtract())
    print(x.getFirst(), "*", x.getSecond(), "=", x.multiply())
    if x.divide() is not None:
        print(x.getFirst(), "/", x.getSecond(), "=", x.divide())
    if x.sqrt(1) is not None:
        print("The Square Root of", x.getFirst(), "is:", x.sqrt(1))
    if x.sqrt(2) is not None:
        print("The Square Root of", x.getSecond(), "is:", x.sqrt(2))
    print(x.getFirst(), "squared is:", x.square(1))
    print(x.getSecond(), "squared is:", x.square(2))
    print(x.getFirst(), "cubed is:", x.cube(1))
    print(x.getSecond(), "cubed is:", x.cube(2))
    print(x.getFirst(), "to the fifth power is:", x.fifth(1))
    print(x.getSecond(), "to the fifth power is:", x.fifth(2))
    print("\n")
    """Y solutions below"""
    print(y.getFirst(), "+", y.getSecond(), "=", y.add())
    print(y.getFirst(), "-", y.getSecond(), "=", y.subtract())
    print(y.getFirst(), "*", y.getSecond(), "=", y.multiply())
    if y.divide() is not None:
        print(y.getFirst(), "/", y.getSecond(), "=", y.divide())
    if y.sqrt(1) is not None:
        print("The Square Root of", y.getFirst(), "is", y.sqrt(1))
    if y.sqrt(2) is not None:
        print("The Square Root of", y.getSecond(), "is", y.sqrt(2))
    print(y.getFirst(), "squared is:", y.square(1))
    print(y.getSecond(), "squared is:", y.square(2))
    print(y.getFirst(), "cubed is:", y.cube(1))
    print(y.getSecond(), "cubed is:", y.cube(2))
    print(y.getFirst(), "to the fifth power is:", y.fifth(1))
    print(y.getSecond(), "to the fifth power is:", y.fifth(2))
    print("\n")
    """Z solutions below"""
    print(z.getFirst(), "+", z.getSecond(), "=", z.add())
    print(z.getFirst(), "-", z.getSecond(), "=", z.subtract())
    print(z.getFirst(), "*", z.getSecond(), "=", z.multiply())
    if z.divide() is not None:
        print(z.getFirst(), "/", z.getSecond(), "=", z.divide())
    if z.sqrt(1) is not None:
        print("The Square Root of", z.getFirst(), "is", z.sqrt(1))
    if z.sqrt(2) is not None:
        print("The Square Root of", z.getSecond(), "is", z.sqrt(2))
    print(z.getFirst(), "squared is:", z.square(1))
    print(z.getSecond(), "squared is:", z.square(2))
    print(z.getFirst(), "cubed is:", z.cube(1))
    print(z.getSecond(), "cubed is:", z.cube(2))
    print(z.getFirst(), "to the fifth power is:", z.fifth(1))
    print(z.getSecond(), "to the fifth power is:", z.fifth(2))
    print("\n")


if __name__ == "__main__":
    main()
