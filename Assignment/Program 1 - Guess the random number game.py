#Author : Colin Prater
#Date   : 11/05/2021
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

# while loop for the user's guess so that if they guess anything other than 1-6 it will give them an error and ask them to enter a valid guess
while True:
    guessUser = int(input("What is your guess? "))
    if (int(guessUser)<guessMin or int(guessUser)>guessMax):
        print ("Invalid input. Please enter a number between",guessMin,"and",guessMax)
    else:
        break

# generate a random number in the correct parameters and an if else statement to determine of the user won or lost the game
secretNumber = random.randint(guessMin,guessMax)
if (guessUser != secretNumber):
    print("You lose - the number was",secretNumber)
else:
    print("Congratulations, you got it right!")

print("Thank you for playing Guess the number.")
