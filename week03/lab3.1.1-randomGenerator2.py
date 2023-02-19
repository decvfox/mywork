# lab3.1.1-randomGenerator2.py
# program that prints out a random number from a user defined range
# Author: declan Fox

import random

first = int(input("Enter first number in range: "))
last = int(input("Enter the last number in range: "))
number = random.randint(first,last)

print("here is a random number {}".format(number))
