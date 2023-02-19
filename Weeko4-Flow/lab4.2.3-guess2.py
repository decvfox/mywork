#lab4.2.3-guess2.py
# Guessing game
# Author: Declan Fox


number_to_guess = 30
guess = int(input("Please guess the number: "))

while guess != number_to_guess:
    if guess < number_to_guess:
        print("Too low. ", end = '')
    else: # I know it cant be equal or too low, so it must be too high
        print("Too high. ", end = '')
    guess = int(input("Please guess again: "))

print ("Well done! Yes the number was ", number_to_guess)