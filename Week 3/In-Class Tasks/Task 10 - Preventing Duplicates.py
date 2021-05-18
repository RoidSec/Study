# adding users to the database
nameList = []
name = "dummy value" 

while name != "":
    name = input("Customer name: ")
    
# only let non-blank names into the list
    if name != "":
        if name in nameList:
            print("Identical name given, please enter a valid name")
        else:
            nameList.append(name)

print ("List of all Users added:\n")
for name in nameList:
    print (name)

 