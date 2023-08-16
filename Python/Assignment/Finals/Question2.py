"""
Study the following examples carefully and write a program that works exactly like the examples. The program does not
need to handle user input error.

For example:
Input	        Result
2               Enter the 1st positive integer: 2
5               Enter the 2nd positive integer: 5
                Here are the equations:
                2 x 2 x 2 + 5 x 5 x 5
                = 4 x 2 + 25 x 5
                = 8 + 125
                = 133

10              Enter the 1st positive integer: 10
20              Enter the 2nd positive integer: 20
                Here are the equations:
                10 x 10 x 10 + 20 x 20 x 20
                = 100 x 10 + 400 x 20
                = 1000 + 8000
                = 9000
"""

num1 = int(input("Enter the 1st positive integer: "))
num2 = int(input("Enter the 2nd positive integer: "))

print("Here are the equations:")
print("{0} x {0} x {0} + {1} x {1} x {1}".format(num1, num2))
print("= {0} x {1} + {2} x {3}".format((num1 * num1), num1, (num2 * num2), num2))
print("= {0} + {1}".format((num1 * num1 * num1), (num2 * num2 * num2)))
print("= {0}".format((num1 * num1 * num1) + (num2 * num2 * num2)))