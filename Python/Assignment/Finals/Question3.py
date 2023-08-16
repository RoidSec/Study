"""
Study the following examples carefully and write a program that works exactly like the examples. The program does not
need to handle user input error.

For example:
Input	        Result
5               Enter number of equations: 5
7               Enter the last number: 7
                Equations:
                3 + 3 + 3 = 6 + 3 = 9
                4 + 4 + 4 = 8 + 4 = 12
                5 + 5 + 5 = 10 + 5 = 15
                6 + 6 + 6 = 12 + 6 = 18
                7 + 7 + 7 = 14 + 7 = 21
"""

numEquations = int(input("Enter number of equations: "))
numLast = int(input("Enter the last number: "))

numStart = (numLast - numEquations) + 1

print("Equations:")
for i in range(0, numEquations):
    while numStart <= numLast:
        print("{0} + {0} + {0} = {1} + {0} = {2}".format(numStart, (numStart + numStart), (numStart + numStart + numStart)))
        numStart += 1
