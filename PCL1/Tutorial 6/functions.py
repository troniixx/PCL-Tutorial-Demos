def tutorial(string):
    l = [1, 2, 3, "string"]
    
    for item in l:
        if item == string:
            print("Wow")
            
tutorial("string")

def greet(name="Guest"):
    print(f"Hello, {name}!")

def add_numbers(a, b):
    return a + b

def age_category(age):
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    else:
        return "Adult"


result = add_numbers(5, 3)
print("Sum:", result)

greet()
greet("Alice")

print("Age 10:", age_category(10))
print("Age 15:", age_category(15))
print("Age 25:", age_category(25))