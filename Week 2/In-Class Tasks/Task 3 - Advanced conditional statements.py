# program to tell the used what
grade = int(input("Input the mark: "))
if grade <50:
    print("FL")
elif grade <65:
    print("PS")
elif grade <75:
    print("CR")
elif grade <85:
    print("DN")
else:
    print("HD")
