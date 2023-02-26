#  lab5.1.7-weekday.py
# Program that outputs whether or not today is a weekday
# ref https://docs.python.org/3/library/datetime.html
# https://docs.python.org/3/library/time.html?highlight=time#module-time
#Author: Declan Fox

import datetime, time

weekday = time.strftime("%A")
date_time = datetime.datetime.now() # for testing use datetime.date.fromisoformat('2023-02-24') 
weekday_number = date_time.isoweekday()

print(f'Today is {weekday}, day {weekday_number} of the week')

if weekday_number > 5:
    print('It is the weekend, yay!')
else:
    print('Yes, unfortunately today is a weekday.')    