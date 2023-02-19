# lab3.1.1-sub.py
# Program to subtract on number from another.
# Author: Declan Fox

# input reads in a string so we need to convert it into an int
# so we can perform mathematical operations
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
answer= x-y

print("{} minus {} is {} ".format(x, y, answer))
