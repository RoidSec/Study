#My age is this_year minus birth_year
# importing and establishing the current date to make a variable into the current year
from datetime import date
currentDate = date.today()

birthYear = int(input("What is your year of birth: "))
thisYear = currentDate.year
print ("you're", thisYear-birthYear, "this year.")
