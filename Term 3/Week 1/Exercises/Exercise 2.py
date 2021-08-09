#greatest common divisor of two integers

# Input two values
num1 = int(input("What if your first number? "))
num2 = int(input("What if your second number? "))

#while number1 is not equal to number2
while num1 != num2:
# if num1 is greater than num2
    if (num1 > num2):
        num1 = num1 - num2
    else:
        num2 = num2 - num1
    break

print ("The GCD is:", num1)