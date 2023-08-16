#Version: 1.0
#
#Maths Quest
#Teaching times tables

# input for name
name = input("Welcome to Maths Quest!  What is your name? ")

# If the number input in the while loop is within 1 - 12 it will break the loop
# Asks again if a number outside of 1 - 12 is done
# Gives invalid input if they enter special characters e.g. $ ^ @ *
# Gives invalid input if people type out the number as a string e.g. Seven
while True:
    try:
        timesTable = int(input(name+" which times table would you like to practice? (1-12) "))
        if int(timesTable)>=1 and int(timesTable)<=12:
            break
    except:
        print ("Invalid input.")

#printing of instructions for the user to practice their timestables
print (name+ " on a piece of paper, write down the", timesTable ,"times tables from 1 to 12.  When you’re ready I’ll show you the answer so you can check your work.")

# ready check for printing results
# while loop to break if the user input's y,
# if input n will display an alternate message
# if input of not y or n it will say invalid input
while True:
    readyCheck = input("Are you Ready? (y/n) ")
    if readyCheck != 'y' and readyCheck != 'n':
        print ("Invalid input, Please enter y or n")
    elif readyCheck == 'n':
        print ("Its okay take your time, please enter y when ready")
    else:
        break

# printing of the timestables
for i in range(1,13):
        print(timesTable, "X" ,i, "=",timesTable * i)

# while loop for a valid input (y or n only)
# will only break loop if y or n is input

while True:
    checkforCorrect = input("Did you get them all correct? (y/n) ")
    if checkforCorrect == 'y' or checkforCorrect == 'n':
        break
    print ("Invalid input, Please enter y or n")

# different statements for if a user says they got them all right or got some wrong
if checkforCorrect == 'y':
        print("Great job! Thank you for playing Maths Quest.")
if checkforCorrect == 'n':
        print ("That is unfortunate, better luck next time! Thank you for playing Maths Quest.")
