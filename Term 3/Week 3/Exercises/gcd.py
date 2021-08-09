def gcd(a,b):
    while a != b:
        if a>b:
            a=a-b
        else:
            b=b-a
        # end if
    #end while
    return (a)
#end function

# Define input Variables
def main():
    a = int(input("Enter a whole number: "))
    b = int(input("Enter a second whole number: "))
    c = gcd(a,b)
    print("GCD is: " + str (c))

if __name__ == "__main__":
    main()
