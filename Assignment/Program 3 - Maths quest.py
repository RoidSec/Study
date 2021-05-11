#Author : Colin Prater
#Date   : 11/05/2021
#Version: 1.0
#
#Maths Quest
#Teaching times tables

# inital inputs for data
name = input("Welcome to Maths Quest!  What is your name? ")

while True:
    timesTable = int(input(name+" which times table would you like to practice? (1-12) "))
    if (int(timesTable)<1 or int(timesTable)>12):
        print ("Invalid input.")
    else:
        break

print (name+ " on a piece of paper, write down the", timesTable ,"times table's from 1 to 12.  When you’re ready I’ll show you the answer so you can check your work.")

# ready check for printing works
while True:
    if input("Are you Ready? ") == "y":
        break

# printing of the timestables
for i in range(1,13):
        print(timesTable, "X" ,i, "=",timesTable * i)

checkforCorrect = input("Did you get them all correct? (y/n) ")
while True:
    if checkforCorrect == "y":
        print("Great job! Thank you for playing Maths Quest.")
    elif checkforCorrect == "n":
        print ("That is unfortunate, better luck next time! Thank you for playing Maths Quest.")
    break
