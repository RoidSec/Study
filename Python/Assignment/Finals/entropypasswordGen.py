import string
from random import randrange
import math

lCase1 = string.ascii_lowercase

lCase2 = lCase1[randrange(0, 26)]

lCase3 = lCase1[randrange(0, 26)]

uCase1 = string.ascii_uppercase

uCase2 = uCase1[randrange(0, 26)]

mix = string.ascii_letters

mixed1 = mix[randrange(0, 52)]
mixed2 = mix[randrange(0, 52)]
mixed3 = mix[randrange(0, 52)]
mixed4 = mix[randrange(0, 52)]

twoDigits = randrange(10, 100)

letters = string.ascii_letters

twoLetters = letters[randrange(0, 52)] + letters[randrange(0, 52)]

symbols = ["$", "9", "5", "v", "w", "J"]

symbols2 = [0,1,2,3,4,5,6,7,8,9,"%","^","&","*","#","@","!"]

l = len(symbols2)

symbol1 = symbols2[randrange(0, l)]

symbol2 = symbols2[randrange(0, l)]

#symbol3 = symbols[randrange(0, l)]

#password = lCase2 + uCase2 + str(twoDigits) + twoLetters + symbol1 + symbol2

password = lCase2 + lCase3 + mixed1 + mixed2 + mixed3 + mixed4 + str(symbol1) + str(symbol2)

print(password)

entropy = math.log(26 * 26 * 100 * 1 * 52 * 52 * 6 * 6 * 6, 2)

entropy2 = math.log(26 * 26 * 52 * 52 * 52 * 52 * 17 * 17, 2)

# print("The entropy of the password is: {0:0.1f}".format(entropy))

print("The entropy of the password is: {0:0.1f}".format(entropy2))
