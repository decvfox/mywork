# lab3.1.1-randomfruit.py
# This program prints out a random fruit
# Author Declan Fox

import random

fruits = ['Apple', 'Orange', 'Banana', 'Pear']

# we want a random number between 0 and lenght-1
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print("A Random Fruit: {}".format(fruit))
