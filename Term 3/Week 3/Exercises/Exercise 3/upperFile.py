from countupperfile import countUpper, convertUpper, convertUpper2, sortString

string = input("What is your sentence? ")
count = countUpper(string)

print("The original count is: " + str(count))

string1 = convertUpper(string)
print(string1)

alphaOnly = convertUpper2(string)
print(alphaOnly)

alphaBet = sortString(alphaOnly)
print(alphaBet)
