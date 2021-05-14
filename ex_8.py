# Write a Python program to extract year, month, date and time using Lambda.

import datetime

time = datetime.datetime.now()
print(time)

year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
print(f"the year is {year(time)}")
print(f"the month is {month(time)}")
print(f"the day is {day(time)}")
