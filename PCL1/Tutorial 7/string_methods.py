# We know that this is ALOT of information to take in, but we promise you that it will be worth it sooner or later :)
# Author: Mert Erol

# capitalize() - Converts the first character to uppercase
sentence = "hello world"
print(sentence.capitalize())  # Output: Hello world

# casefold() - Converts string to lowercase, more aggressive than lower()
sentence = "Hello World"
print(sentence.casefold())  # Output: hello world

# count() - Counts occurrences of a substring
text = "banana"
print(text.count("a"))  # Output: 3

# find() - Finds the first occurrence of the substring
print(text.find("n"))  # Output: 2

# join() - Joins elements of an iterable into a single string
words = ["Hello", "world"]
print(" ".join(words))  # Output: Hello world

# replace() - Replaces occurrences of a substring with another
text = "I love apples"
print(text.replace("apples", "bananas"))  # Output: I love bananas

# split() - Splits string at a specified separator and returns a list
sentence = "one, two, three"
print(sentence.split(", "))  # Output: ['one', 'two', 'three']

# format() - Formats string into nicer output
animal = "chicken"
print("I love {}!".format(animal))  # Output: I love chicken!

# Additional Methods

# upper() - Converts all characters to uppercase
print(sentence.upper())  # Output: ONE, TWO, THREE

# lower() - Converts all characters to lowercase
print(sentence.lower())  # Output: one, two, three

# swapcase() - Swaps uppercase to lowercase and vice versa
print(sentence.swapcase())  # Output: ONE, TWO, THREE

# strip() - Removes leading and trailing whitespace
whitespace_text = "   Hello world   "
print(whitespace_text.strip())  # Output: Hello world

# startswith() - Checks if string starts with a specified substring
print(sentence.startswith("one"))  # Output: True

# endswith() - Checks if string ends with a specified substring
print(sentence.endswith("three"))  # Output: True

# isalpha() - Checks if all characters in the string are alphabetic
print("hello".isalpha())  # Output: True

# isdigit() - Checks if all characters in the string are digits
print("1234".isdigit())  # Output: True

# isnumeric() - Checks if all characters in the string are numeric
print("1234".isnumeric())  # Output: True