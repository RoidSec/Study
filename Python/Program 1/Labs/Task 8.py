import random
randomNumbers = random.sample(range(1, 99), 7)
print("I think the lottery’s winning numbers are:", randomNumbers[0:6], "and the powerball is ["+str(randomNumbers[6])+ "]")
