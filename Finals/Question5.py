"""
Write a program to ask the user to enter positive even integers and store them in a list, and then display this list at
the end.

The program must handle errors and invalid inputs so that all errors and invalid inputs are ignored by the program.

The program must work exactly like the following example.

For example:
Input	        Result
emu             Enter a positive even integer (or EXIT to quit): emu
0               Enter a positive even integer (or EXIT to quit): 0
2               Enter a positive even integer (or EXIT to quit): 2
3.4             Enter a positive even integer (or EXIT to quit): 3.4
100             Enter a positive even integer (or EXIT to quit): 100
5               Enter a positive even integer (or EXIT to quit): 5
20              Enter a positive even integer (or EXIT to quit): 20
cat             Enter a positive even integer (or EXIT to quit): cat
20              Enter a positive even integer (or EXIT to quit): 20
-10             Enter a positive even integer (or EXIT to quit): -10
EXIT            Enter a positive even integer (or EXIT to quit): EXIT
                This is what you have entered
                [2, 100, 20, 20]
"""

inp = input("Enter a positive even integer (or EXIT to quit): ")

numList = []

if inp == "EXIT":
    print("This is what you have entered")
    print(numList)
else:
    while inp != "EXIT":
        try:
            if int(inp) >= 1:
                if int(inp) % 2 == 0:
                    numList.append(int(inp))
        except ValueError as e:
            pass

        inp = input("Enter a positive even integer (or EXIT to quit): ")

print("This is what you have entered")
print(numList)
