#Rock paper scissors game
#Two player

print ("Welcome to Rock, Paper, Scissors!")
print ("Let's begin...")
name1 = input("player 1: What's your name? ")
name2 = input("Player 2: What's your name? ")
winner1 = "Congratulations " + name1 + " you win!"
winner2 = "Congratulations " + name2 + " you win!"
choicePrompt = ": enter 'r' for rock, 'p' for paper, and 's' for scissors: "

# Displays a greeting and starts the game by telling the 2nd player to close their eyes
print ("Hello " + name1 + " and " + name2)
print (name2 + ": close your eyes!\n")

# while loop for player 1's guess to make sure they have a vaild r, p or s input
print("Okay", name1)
while True:
    choice1 = input("What is your guess? ")
    if choice1 == 'r' or choice1 == 'p' or choice1 == 's':
        break
    print ("Invalid input", name1 + ". Please enter r, p or s")

print ("Great choice! Now - cover your answer and ask " + name2 + " to chose. \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" )


# while loop for player 2 just like player 1's while loop to capture the correct input
print("Okay", name2)
while True:
    choice2 = input("What is your guess? ")
    if choice2 == 'r' or choice2 == 'p' or choice2 == 's':
        break
    print ("Invalid input", name2 + ". Please enter r, p or s")

# printing of the choices to show what each user chose to prevent people thinking someone was cheating
print (name1 + " chose: " + choice1)
print (name2 + " chose: " + choice2)


# if else statement to determine the winner of the game
# will see if both players picked the same letter and end the game there
# if statements are based off of player 1's choice in relation to player 2
# as there are 3 choices in this game we can choose statements to define two letters per if else statement and the third
# will be caught in the else statement.
# e.g. if the choice1 is r then we know choice1 wins if the outcome is s and we can determite a winner there
# the else statement is for if they chose p as thats the only other option(it would tie if they both chose r)
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

# a final statement showing the end of the game
print("Thanks for playing Rock, Paper, Scissors")
