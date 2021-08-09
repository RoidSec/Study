# Converts the string into uppercase
def convertUpper(str):
    newString = ""

# for loop restricts the
    for ch in str:
        if ch >='a' and ch <='z':
            newString = newString + chr(ord(ch) - 32)
        else:
            newString = newString + ch

    return newString

def replaceFullstops(str):
    newString = ""

    # Iterate through and replace periods with X
    for ch in str:
        if ch == ".":
            ch = "X"
            newString = newString + ch
        else:
            newString = newString + ch

    return newString

def joinLetters(str):
    concat = ""

    # Iterate through and concatenate
    for ch in str:
        if ch >='A' and ch <='Z':
            concat = concat + ch

    return concat

# Shift letters 
def shift(num, str):
    encryption = ""

    # Softcoded shift:
    shiftNum = num

    # Iterate and shift.
    for ch in str:
        # only shift if it is in uppercase
        if ch.isupper():
            # find the position in 0-25
            c_unicode = ord(ch)
            c_index = ord(ch) - ord("A")

            # shift characters
            newIndex = (int(c_index) + int(shiftNum)) % 26
            newUnicode = newIndex + ord("A")

            # captures
            newChar = chr(newUnicode)
            encryption = encryption + newChar

    return encryption
