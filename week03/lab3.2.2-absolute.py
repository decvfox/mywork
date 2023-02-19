# lab3.2.2-absolute.py
# Give the absolute value of a number
#
# Author: Declan Fox


# In the question, number is ambiguous but the
# output implies that we should be dealing with floats
# So I am casting the input to a float
number = float(input("Enter a number: "))
absoluteValue = abs(number)

print(f'The absolute value of {number} is {absoluteValue}')