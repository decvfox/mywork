# lab3.2.1-round.py
# rounds a number
# be careful of round, it rounds to the nearest even number
# eg 4.5 rounds to 4
# but 5.5 rounds to 6
# so do not use it where accuracy is essential
# Author: Declan Fox

numberToRound = float(input("Enter a float number: "))
roundedNumber = round(numberToRound)

print ( f'{numberToRound} rounded is {roundedNumber}')