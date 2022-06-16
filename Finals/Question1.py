"""
Soft drinks are sold in 3 box sizes:
- small box: $15 each
- medium box: $20 each
- large box: $25 each

Study the following examples carefully and write a program that works exactly like the examples. The program does not
need to handle user input error.

For example:
Input	    Result
2           How many small boxes? 2
3           How many medium boxes? 3
0           How many large boxes? 0
            Small boxes: 2 x $15 = $30
            Medium boxes: 3 x $20 = $60
            Large boxes: 0 x $25 = $0
            Total cost: $30 + $60 + $0 = $90
"""

smallBoxes = int(input("How many small boxes? "))
mediumBoxes = int(input("How many medium boxes? "))
largeBoxes = int(input("How many large boxes? "))

print("Small boxes: {0} x $15 = ${1}".format(smallBoxes, (smallBoxes * 15)))
print("Medium boxes: {0} x $20 = ${1}".format(mediumBoxes, (mediumBoxes * 20)))
print("Large boxes: {0} x $25 = ${1}".format(largeBoxes, (largeBoxes * 25)))
print("Total cost: ${0} + ${1} + ${2} = ${3}".format((smallBoxes * 15), (mediumBoxes * 20), (largeBoxes * 25), (smallBoxes * 15) + (mediumBoxes * 20) + (largeBoxes * 25)))
