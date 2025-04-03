x = 5

if x == 5:
    print("x is equal to 5")
    
x = 10

if x < 5:
    print("x is less than 5")
elif x == 5:
    print("x is equal 5")
else:
    print("x is greater than 5")
    
x = 15

if x < 10:
    if x == 15:
        print("x is equal 15")
    else:
        print("x is greater than 10 but not 15")
else:
    print("x is 10 or less")