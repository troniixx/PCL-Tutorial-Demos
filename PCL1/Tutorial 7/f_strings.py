# We know that this is ALOT of information to take in, but we promise you that it will be worth it sooner or later :)
# Author: Mert Erol

# Introduction
"""
In Python, a string is a sequence of characters. Strings can contain anything from a single character to a whole novel.
"""

# F-strings: Formatted String Literals
name = "Kermit"
age = 5
greeting = f"Hello, {name}! You are {age} years old."
print(greeting)  # Output: Hello, Kermit! You are 5 years old.

# F-strings with expressions
a = 10
b = 20
print(f"The sum of {a} and {b} is {a + b}.")  # Output: The sum of 10 and 20 is 30.

# F-strings with formatting numbers
price = 49.99
print(f"The price is ${price:.2f}.")  # Output: The price is $49.99.

# F-strings with alignment
word = "Python"
print(f"{word:<10}")  # Left-align: Output: 'Python    '
print(f"{word:>10}")  # Right-align: Output: '    Python'
print(f"{word:^10}")  # Center-align: Output: '  Python  '

# F-strings with nested expressions
name = "Sam"
height = 1.75
weight = 68
bmi = weight / (height ** 2)
print(f"{name}'s BMI is {bmi:.2f}.")  # Output: Sam's BMI is 22.20.

# .format() Method

# Basic usage
animal = "chicken"
print("I love {}!".format(animal))  # Output: I love chicken!

# .format() with multiple placeholders
name = "Alice"
hobby = "painting"
print("My name is {} and I enjoy {}.".format(name, hobby))  # Output: My name is Alice and I enjoy painting.

# .format() with positional arguments
print("The {2} is {0} and the {1} is beautiful.".format("sky", "sea", "land"))  # Output: The land is sky and the sea is beautiful.

# .format() with keyword arguments
print("I have a {fruit} and a {vegetable}.".format(fruit="banana", vegetable="carrot"))  # Output: I have a banana and a carrot.

# .format() with formatting numbers
price = 123.456
print("The total price is ${:.2f}".format(price))  # Output: The total price is $123.46.

# .format() with alignment
word = "Python"
print("{:<10}".format(word))  # Left-align: Output: 'Python    '
print("{:>10}".format(word))  # Right-align: Output: '    Python'
print("{:^10}".format(word))  # Center-align: Output: '  Python  '

# .format() with large numbers and commas
large_number = 1000000
print("The number is {:,}".format(large_number))  # Output: The number is 1,000,000.

# F-strings for dictionaries
person = {"name": "Charlie", "age": 10}
print(f"{person['name']} is {person['age']} years old.")  # Output: Charlie is 10 years old.

# F-strings for lists
colors = ["red", "green", "blue"]
print(f"My favorite colors are {colors[0]}, {colors[1]}, and {colors[2]}.")  # Output: My favorite colors are red, green, and blue.

# Nested formatting in f-strings
nested_value = f"{f'{a} + {b} = {a + b}'} is the result of adding {a} and {b}."
print(nested_value)  # Output: '10 + 20 = 30 is the result of adding 10 and 20.'
