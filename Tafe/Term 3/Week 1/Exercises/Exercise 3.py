price = 1.50
discount = 0
amount = int(input("chocs are $1.50 how many you want? "))

if amount > 20:
    discount = 0.9
else:
    price = price
    
print ("The price for " + str(amount) + " bars is $" + str(price * amount - discount))
