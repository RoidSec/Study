def maxOfTwoValues(a,b):
    if (a>b):
        return(a)
    else:
        return(b)

num1 = int(input("Enter a whole number: "))
num2 = int(input("Enter a second whole number: "))
biggest = maxOfTwoValues(num1, num2)
print("The Biggest number is", biggest)