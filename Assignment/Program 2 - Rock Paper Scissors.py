#Author : Colin Prater
#Date   : 11/05/2021
#Version: 1.0
#
#Rock paper scissors game
#Two player
from getpass import getpass

print ("Welcome to Rock, Paper, Scissors!")
print ("Let's begin...")
name1 = input("player 1: What's your name? ")
name2 = input("Player 2: What's your name? ")
winner1 = "Congratulations " + name1 + " you win!"
winner2 = "Congratulations " + name2 + " you win!"
choicePrompt = ": enter 'r' for rock, 'p' for paper, and 's' for scissors: "

print ("Hello " + name1 + " and " + name2)
print (name2 + ": close your eyes!")

choice1 = getpass(name1 + choicePrompt )
print ("Great choice! Now - cover your answer and ask " + name2 + " to chose. \n\n\n" )
choice2 = getpass(name2 + choicePrompt )

print (name1 + " chose " + choice1)
print (name2 + " chose " + choice2)

if choice1 == choice2:
    print("It's a Tie!")
else:
    if choice1 == "r":
        if choice2 == "s":
            print (winner1)
        else:
            print (winner2)
    if choice1 == "p":
        if choice2 == "r":
            print (winner1)
        else:
            print (winner2)
    if choice1 == "s":
        if choice2 == "p":
            print (winner1)
        else:
            print (winner2)


print("Thanks for playing Rock, Paper, Scissors")
