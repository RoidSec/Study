# Input a string value and to convert it to code.
# First, convert the input string to uppercase 
# discarding numeric and any special characters.
# The code will be such that A=00, B=01, C=02
# upto Z=25.

# input a string
in_str = input("What is the string to convert ")

# convert to uppercase
in_str = in_str.upper()

# for each character in input string
for i in range(len(in_str)):
    # find the next character
    next_char = in_str[i]
    # find ASCII value of next character
    next_ascii = ord(next_char)
    if (next_ascii >= 65 and next_ascii <=90):
        # output ASCII value minus 65
        print ("{:0>2d}".format(next_ascii - 65), end="")
    