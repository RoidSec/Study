"""
Creating an input form to gather address, suburb, postcode and state and format like the following:

Street Address
Suburb
State & Postcode
"""

streetAddress = input("what is your Street number and name: ")
suburb = input("what is your suburb: ")
state = input("what state do you live in: ")
postcode = input("what is your post code: ")

print(streetAddress,"\n"+suburb,"\n"+postcode,state)
