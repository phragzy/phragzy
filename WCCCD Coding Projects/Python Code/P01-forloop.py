"""
Program: P01-forloop
Author: Joseph
Date written: 06/09/2024
Last edited: 06/10/2024

Description: This prints out 1-150 and tells if its divisible by 2, 3, 5, 7, or 11
"""
#num = int(input("Please enter a number between 1-150: "))
for num in range(1, 151):
    divisible = False
    if num % 2 == 0:
        print(str(num) + " is divisible by 2")
        divisible = True
    if num % 3 == 0:
        print(str(num) + " is divisible by 3")
        divisible = True
    if num % 5 == 0:
        print(str(num) + " is divisible by 5")
        divisible = True
    if num % 7 == 0:
        print(str(num) + " is divisible by 7")
        divisible = True
    if num % 11 == 0:
        print(str(num) + " is divisible  by 11")
        divisible = True
    if not divisible:
        print(str(num) + " is not divisible by any of the numbers provided")
