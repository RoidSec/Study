#Author : Colin Prater
#Date   : 27/04/2021
#Version: 1.0
#
#Rock paper scissors game
#Two player

print ("Welcome to Rock, Paper, Scissors!")
print ("Let's begin...")
name1 = input("player 1: What's your name?")
name2 = input("Player 2: What's your name?")

print ("Hello " + name1 + " and " + name2)
print (name2 + ": close your eyes!")

choice1 = input(name1 + ":enter 'r' for rock, 'p' for paper, and 's' for scissors: ")
print ("Great choice! Now - cover your answer and ask " + name2 + " to chose. \n\n\n" )
choice2 = input(name2 + ":enter 'r' for rock, 'p' for paper, and 's' for scissors: ")

if choice1 == choice2:
    print("It's a Tie!")
else:
    if choice1 == "r":
        if choice2 == "s":
            print ("Congratulations" ,name1,"you win!")
        else:
            print ("Congratulations" ,name2,"you win!")
    if choice1 == "p":
        if choice2 == "r":
            print ("Congratulations" ,name1, "you win!")
        else:
            print ("Congratulations" ,name2,"you win!")
    if choice1 == "s":
        if choice2 == "p":
            print ("Congratulations" ,name1, "you win!")
        else:
            print ("Congratulations" ,name2,"you win!")

print("Thanks for playing Rock, Paper, Scissors")
