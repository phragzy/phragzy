"""
Program: P03-PiApproximation
Author: Joseph 
Date written: 06/10/2024
Last edited: 06/10/2024

Description: This takes user input and calculates Pi
"""

uint = int(input("Please enter a Positive Number: "))
x = 0
i = 1
count = 0
if uint > 0:
    for count in range (1, uint, 2):
#while count <= uint:
        #count += 1
        x = x + i * (1 / count)
        i = i * (-1)
if uint < 0:
    print("Error, insert positive number")
pi = x * 4
print(pi)
