#Author : Colin Prater
#Date   : 11/05/2021
#Version: 1.0
#
#Guess the random number game
#One player vs. the computer

import random
guessMin = 1
guessMax = 6

#ask the user for their name and their guess
name = input("What is your name? ")
print ("Hi " + name)
print("Please enter a number between: ", guessMin, " and ", guessMax)

while True:
    guessUser = int(input("What is your guess? "))
    if (int(guessUser)<guessMin or int(guessUser)>guessMax):
        print ("Invalid input. Try again.")
    else:
        break

# generate a random number and tell the user if they won or lost
secretNumber = random.randint(guessMin,guessMax)
if (guessUser != secretNumber):
    print("You lose - the number was",secretNumber)
else:
    print("Congratulations, you got it right!")
