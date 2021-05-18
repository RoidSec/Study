# Print out all the days
dayList = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for day in dayList:
    print(day)
    
# Print only 1 value on the list
print("Thank god its",dayList[5])

# Print our only the week day names
for day in dayList:
    if day != "Sunday" and day != "Saturday":
        print (day)