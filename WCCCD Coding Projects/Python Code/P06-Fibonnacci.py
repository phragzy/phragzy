"""
Program: This program calculates fibonacci sequence
Author: Joseph
Date Written: 07/08/2024
Last Edited: 07/08/2024

Description: This program takes a user input, and calculates what number within the fibonacci to print out
"""


def main():
    user = int(input("Please enter a number to calculate fibonacci sequence: "))
    if user == 0:
        print(0)
    else:
        print("Using your number, the number in the fibonacci sequence is", fseq(user))


def fseq(x):
    if x < 3:
        return 1
    else:
        return fseq(x - 1) + fseq(x - 2)


if __name__ == "__main__":
    main()
