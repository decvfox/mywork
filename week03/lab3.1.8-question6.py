# lab3.1.1-question6.py
# Solution to Question 6
# Author: declan Fox

#message = 'I have eaten ' + 99 + ' burritos.' - Can't join int to str

#fix 1: Add 99 as a str
message = 'I have eaten ' + '99' + ' burritos.'
print (message)

#fix 2: Format using old str.format() style
message = 'I have eaten {} burritos.'.format(99)
print (message)

#fix 3: Format using latest f-strings formating style
message = f'I have eaten {99} burritos.'
print (message)
