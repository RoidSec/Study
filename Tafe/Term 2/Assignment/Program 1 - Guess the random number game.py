#Author : Colin Prater
#Date   : 29/04/2021
#Version: 1.0
#
#Guess the random number game
#One player vs. the computer

# Imports and establishing the variable parameters for the guessing game
import random
guessMin = 1
guessMax = 6

# Input for the user's name and guess, establishing to the user that they can only use numbers 1 - 6
name = input("What is your name? ")
print ("Hi "+name)
print("Please enter a number between:",guessMin,"and",guessMax)

# while loop for the user's guess so that if they guess anything other than 1-6 it will give them an error
# and ask them to enter a valid guess, will break when a valid input is given
while True:
    guessUser = int(input("What is your guess? "))
    if (int(guessUser)>=guessMin and int(guessUser)<=guessMax):
        break
    else:
        print ("Invalid input. Please enter a number between",guessMin,"and",guessMax)

# generate a random number in the correct parameters
# if else statement to determine if the user won or lost the game
secretNumber = random.randint(guessMin,guessMax)
if (guessUser != secretNumber):
    print("You lose - the number was",secretNumber)
else:
    print("Congratulations, you got it right!")

print("Thank you for playing Guess the number.")
