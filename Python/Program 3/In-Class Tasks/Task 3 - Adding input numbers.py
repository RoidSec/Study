# While loop - keep adding numbers until user says to stop
num1 = 0
total = 0
#entering a dummy value to make sure the loop is formed
userInput = "y"
while userInput == "y":
    num1 = int(input("Enter a number:"))
    total = total + num1
    userInput = input("continue y/n? ")
print ("The total was: " + str(total))
