# Converts the string into uppercase
def convertUpper(sentence):
    newString = ""

    for ch in sentence:
        if ch >='a' and ch <='z':
            newString = newString + chr(ord(ch) - 32)
        else:
            newString = newString + ch

    return newString

# Fullstop Replacement
def replaceFullstops(sentence):
    newString = ""

    # Iterate through and replace periods with X
    for ch in sentence:
        if ch == ".":
            ch = "X"
            newString = newString + ch
        else:
            newString = newString + ch

    return newString

# Concatenate
def joinLetters(sentence):
    concat = ""

    # Iterate through and concatenate
    for ch in sentence:
        if ch >='A' and ch <='Z':
            concat = concat + ch

    return concat