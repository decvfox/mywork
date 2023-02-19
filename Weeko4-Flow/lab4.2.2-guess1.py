# lab4.2.2-guess1.py
# Guessing game
# Author: Declan Fox


number_to_guess = 30
guess = int(input("Please guess the number:"))

while guess != number_to_guess:
    print ("Wrong")
    guess = int(input("Please guess again:"))
print ("Well done! Yes the number was ", number_to_guess)