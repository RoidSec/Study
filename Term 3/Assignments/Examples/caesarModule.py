# Converts the string into uppercase
def convertUpper(str):
    newstr = ""
    for ch in str:
        if ch >='a' and ch <='z':
            newstr = newstr + chr(ord(ch) -32)
        else:
            newstr = newstr + ch
    upperCase = convertUpper(str)
    joinLetters = ""
    for ch in upperCase:
        if ch >= 'A' and ch <= 'Z':
            joinLetters = joinLetters + ch
    return(joinLetters)
    return(newstr)

# Uses convertUpper and strips all non-alpha characters to output joinLetters
# joinLetters has all the letters in capital and removes all non-alpha characters
