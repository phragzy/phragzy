"""
Program: This program is a semi useful calculator
Author: Joseph 
Date Written: 07/01/2024
Last edited: 07/01/2024

Description: This program takes 2 float numbers, and does the list of calculations and returns the answer to user.
"""
import math


def main():
    a = float(input("Please enter the 1st number: "))
    b = float(input("Please enter the 2nd number: "))
    print("The sum of these two numbers is: ", my_addition(a, b))
    print("The difference of 2nd number - 1st number is: ", my_subtract(a, b))
    print("These numbers multiplied together is: ", my_multiply(a, b))
    if my_divide(a, b) != None:
        print("The 1st number divided by 2nd number is: ", my_divide(a, b))
    print("The 1st number squared is: ", my_square(a))
    print("The 2nd number squared is: ", my_square(b))
    print("The 1st number cubed is: ", my_cube(a))
    print("The 2nd number cubed is: ", my_cube(b))
    if my_squareRoot(a) != None:
        print("The 1st numbers Square Root is: ", my_squareRoot(a))
    if my_squareRoot(b) != None:
        print("The 2nd numbers Square Root is: ", my_squareRoot(b))
    print("The 1st numbers fifth power is: ", my_fifthPower(a))
    print("The 2nd numbers fifth power is: ", my_fifthPower(b))


def my_addition(a, b):
    theSum = a + b
    return theSum


def my_subtract(a, b):
    difference = b - a
    return difference


def my_multiply(a, b):
    theSum = a * b
    return theSum


def my_divide(a, b):
    if b == 0:
        print("Error, cannot divide by Zero")
        return
    else:
        divide = a / b
        return divide


def my_square(a):
    square1 = a ** 2
    return square1


def my_cube(a):
    cube = a ** 3
    return cube


def my_squareRoot(a):
    if a < 0:
        print("Negative numbers cannot have a square root")
        return
    squareRoot = math.sqrt(a)
    return squareRoot


def my_fifthPower(a):
    fifth = a ** 5
    return fifth


if __name__ == "__main__":
    main()
