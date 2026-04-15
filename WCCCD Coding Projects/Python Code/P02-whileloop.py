"""
Program: P02-whileloop
Author: Joseph 
Date written: 06/10/2024
Last edited: 06/10/2024

Description: This prints out 1-150 using a while loop and tells if its divisible by 2, 3, 5, 7, or 11
"""
num = 0
while num < 150:
    num += 1
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
