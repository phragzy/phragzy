"""
Program: This program uses lambda to generate the sum, and multiples within a range.
Author: Joseph
Date Written: 07/10/2024
Last Edited: 07/10/2024

Description: This program generates the sum of every number between 1 and 10,000, as
well as multiples each number from 1-50
"""
from functools import reduce
print("Addition of the first 10000 numbers:", reduce(lambda x, y: x + y, range(10001)))
print("Multiplication of the first 50 numbers:", reduce(lambda c, d: c * d, range(1, 51)))
