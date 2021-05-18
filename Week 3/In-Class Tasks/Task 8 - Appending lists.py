# append (adding to a list)
dayList = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
dayList[5]= "Friday"
dayList.append("Crazy Day")
print(dayList)
print(dayList[2])

dayList[5] = dayList[5] + " yo"
print (dayList[5])

print("Today its",dayList[5])