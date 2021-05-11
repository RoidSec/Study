"""
Display a form showing the below information -

Current date and time using the str method of datetime object:
[str date and time]

Current Date and Time using instance attributes:
Year:
Month:
Day:
Hour:
Minute:
Second:
Microsecond:

Current date and time using strftime:
[strftime date and time]

Current date and time using isoformat
[iso format date and time]
"""

import datetime
now = datetime.datetime.now()
print("Current date and time using the str method of datetime object:")
print(now,"\n")

print("Current Date and Time using instance attributes:")
print("Year:",now.year)
print("Month:",now.month)
print("Day:",now.day)
print("Hour:",now.hour)
print("Minute:",now.minute)
print("Second:",now.second)
print("Microsecond:",now.microsecond,"\n")

print("Current date and time using strftime:")
print(now.strftime("%c"), "\n")

print("Current date and time using isoformat")
print (now.isoformat())
