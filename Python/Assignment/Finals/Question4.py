"""
Study the pattern in the following examples carefully and write a program that works exactly like the examples. The
program does not need to handle user input error.

For example:
Input	        Result
23              Enter max number: 23
18              Enter min number: 18
a               Enter first letter: a
b               Enter second letter: b
                Display the pattern:
                a-23-23
                22-b-b
                a-21-21
                20-b-b
                a-19-19
                18-b-b
20              Enter max number: 20
14              Enter min number: 14
A               Enter first letter: A
v               Enter second letter: v
                Display the pattern:
                A-20-20
                19-v-v
                A-18-18
                17-v-v
                A-16-16
                15-v-v
                A-14-14
9               Enter max number: 9
3               Enter min number: 3
R               Enter first letter: R
p               Enter second letter: p
                Display the pattern:
                R-9-9
                8-p-p
                R-7-7
                6-p-p
                R-5-5
                4-p-p
                R-3-3
20              Enter max number: 20
13              Enter min number: 13
W               Enter first letter: W
j               Enter second letter: j
                Display the pattern:
                W-20-20
                19-j-j
                W-18-18
                17-j-j
                W-16-16
                15-j-j
                W-14-14
                13-j-j
"""
numMax = int(input("Enter max number: "))
numMin = int(input("Enter min number: "))
firstLetter = input("Enter first letter: ")
secondLetter = input("Enter second letter: ")

print("Display the pattern:")

while numMax >= numMin:
    print("{0}-{1}-{1}".format(firstLetter, numMax))
    numMax -= 1
    if (numMax >= numMin):
        print("{0}-{1}-{1}".format(numMax, secondLetter))
    numMax -= 1
