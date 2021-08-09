#counts the number of capitals in a string
def countUpper(str):
    count = 0
    for ch in str:
        if (ch >= 'A' and ch <= 'Z'):
            count= count + 1
    return(count)

#converts the string into uppercase
def convertUpper(str):
    newstr = ""
    for ch in str:
        if ch >='a' and ch <='z':
            newstr = newstr + chr(ord(ch) -32)
        else:
            newstr = newstr + ch
        
    return(newstr)

# uses convertUpper and strips all non-alpha characters
def convertUpper2(str):
    newstr1 = convertUpper(str)
    newstr2 = ""
    for ch in newstr1:
        if ch >= 'A' and ch <= 'Z':
            newstr2 = newstr2 + ch
    return(newstr2)

# uses convertUpper2 and orders them from A - Z
def sortString(str):
    return ''.join(sorted(str))