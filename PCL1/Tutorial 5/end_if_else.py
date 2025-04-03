x = int(input("Enter a number: "))

if x > 15:
    print("If block")
elif x == 10:
    print("Elif block")
else:
    print("if and elif were false")
    if True:
        print("Inside the else block")