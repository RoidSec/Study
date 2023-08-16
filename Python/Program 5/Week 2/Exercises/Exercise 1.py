# Input
in_str = (input("What is your phrase? "))
#converts the string into uppercase
in_str = in_str.upper()

# while more characters in input

for i in range (len(in_str)):
# find the next character
    next_char = in_str[i]
# find ascii value of next character
    next_ascii = ord(next_char)
    if (next_ascii == 88):
        print (".")
# restricting the ascii to have no special characters
    if (next_ascii >= 65 and next_ascii <=90):

# output of ASCII value minus 65 (adding a 0 on characters that are single digit)
            print ("{:02d}".format(next_ascii - 65), end = " ")
