# Imports
import convert_to_caesar
import encrypt_caesar

# commandline argument  
#shiftNum = sys.argv[1]
#string = sys.argv[2]

# Input for testing functionality only
#shift = input("what Shift? ")
#string = input("what string? ")

# try catch for errors
'''
try:
    convertedText = convert_to_caesar(string)
    encryptedText = encrypt_caesar(convertText,shiftNum)
    print (encryptedText)
except valueError as err:
    print("Error: ", err)
'''
#TESTING
string = ("Hello there")


# Processing:
returnedString1 = convert_to_caesar.convertUpper(string)
print("Capitalise: ",returnedString1)

returnedString2 = convert_to_caesar.replaceFullstops(returnedString1)
print("Replace Fullstops: ", returnedString2)

returnString3 = convert_to_caesar.joinLetters(returnedString2)
print("Concatenate: ", returnString3)

# Final output
returnedString4 = encrypt_caesar.shift(shift, returnString3)
print("Shift: " + str(returnedString4))
