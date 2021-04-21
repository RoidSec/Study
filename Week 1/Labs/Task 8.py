"""
Research how Python can generate random numbers. Make a simple program that makes 7 random
numbers – 6 of them are “winning numbers” and 1 is the powerball. Output these to the screen in this format:

	I think the lottery’s winning numbers are [1 2 3 4 5 6] and the powerball should be [7]. 
"""

import random
randomNumbers = random.sample(range(1, 99), 7)
print("I think the lottery’s winning numbers are:", randomNumbers[0:6], "and the powerball is ["+str(randomNumbers[6])+ "]")
