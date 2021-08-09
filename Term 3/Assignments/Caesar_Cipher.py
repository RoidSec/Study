# Imports
import caesarModule

# Initial User input prompt:
string = input("What is your sentence: ")
shiftNum = input("By how many letters do you want to shift: ")

# Processing:
returnedString1 = caesarModule.convertUpper(string)
print("Capitalise: ",returnedString1)

returnedString2 = caesarModule.replaceFullstops(returnedString1)
print("Replace Fullstops: ", returnedString2)

returnString3 = caesarModule.joinLetters(returnedString2)
print("Concatenate: ", returnString3)

# Final output
returnedString4 = caesarModule.shift(shiftNum, returnString3)
print("Shift: " + str(returnedString4))
