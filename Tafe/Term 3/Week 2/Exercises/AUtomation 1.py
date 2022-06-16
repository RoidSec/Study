name = (input("what is your name? "))

name = name.upper()
newName = ""
for everyLetter in name:
    if (everyLetter >= 'A' and everyLetter <= 'Z'):
        newName= newName + everyLetter
        
print (newName)