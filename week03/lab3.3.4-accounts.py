# lab3.3.4-accounts.py
# Replaces the first 6 digits in a 10 character account number with Xs
# ref https://www.w3schools.com/python/python_strings_slicing.asp
# Author: Declan Fox

account_number = input("Please enter an 10 digit account number: ")
visible_number = account_number[6:10] 
hidden_number = 'XXXXXX'
print(hidden_number + visible_number)