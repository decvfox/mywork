# lab3.2.4-convert.py
#
# Take an input of an amount in the form 0f X.XX (dollars and cents)
# there may or may not be a minus sign and the bank takes in the amount in cents 
# This program takes in a float amount of dollars and returns the absolute amount in cent.
#ref https://www.w3schools.com/python/python_strings_modify.asp
# Author: Declan Fox

# I haven't taken in a float as I wanted to use integers for accuracy
amount = input("Enter a dollars and cent value: ")
dollars, cents = amount.split(".")
dollars, cents = int(dollars), int(cents)
value = (dollars * 100) + cents # converts amount to cents
absoluteValue = abs(value)

print(f'The absolute value of {amount} in cents is {absoluteValue}')