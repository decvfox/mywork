# lab3.3.4-accounts.py
# Replaces all but the last 4 digits in an account number of any length with Xs
# ref https://www.w3schools.com/python/python_strings_slicing.asp

# Author: Declan Fox

hidden_number = ''
account_number = input("Please enter an account number: ")
visible_number = account_number[(len(account_number)- 4):len(account_number)] 

for i in range(0, (len(account_number)- 4)):
    hidden_number += 'X'
print(hidden_number + visible_number)
