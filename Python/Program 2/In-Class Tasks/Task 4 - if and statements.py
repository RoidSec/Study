age = int(input("Age:"))
# this code works but is clunky 
"""
if age >= 13:
    if age<=19:
        print("Teenager")
    else:
        print("Not a Teenager")     
"""
        
# this code is much better to view and run      
if age >=13 and age <=19:
    print ("Teenager")
else:
    print ("Not a teen")
    
# both of these will work but the second is best to write