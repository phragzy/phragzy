"""
Program: P-04 Integer Average
Author: Joseph 
Date Written: 06/24/24
Last Edited: 06/25/24

Description: This program takes the text document filled with numbers, and adds them line by line and then prints the sum,
length, and average within the line
"""
txt = open("P-04-integers-input.data", "r")
y = open("P-04-Joseph-integers-output.data", "w")
for line in txt:
    i = line.split(",")
    length = len(i)
    total = 0
    for x in i:
        number = float(x)
        total += number
    print("The Sum is: " + str(total) + ", The length is: " + str(length) + ", The average is: " + str(total / length), file = y)
txt.close()
