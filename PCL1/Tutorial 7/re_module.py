# Demo on Python's re Module (Regular Expressions)
# Author: Mert Erol

import re

# 1. re.findall() - Finds all matches of a pattern in a string and returns them as a list

# Example: Find all occurrences of a word in a sentence
text = "The rain in Spain falls mainly in the plain."
pattern = r"\bin\b"  # The word 'in'
matches = re.findall(pattern, text)
print("findall result:", matches)  # Output: ['in', 'in', 'in']

# Example: Find all numbers in a string
text_with_numbers = "My phone number is 12345 and my postal code is 67890."
numbers = re.findall(r"\d+", text_with_numbers)
print("Numbers found:", numbers)  # Output: ['12345', '67890']

# 2. re.search() - Searches for the first occurrence of a pattern in a string and returns a match object

# Example: Check if a word exists in a string
search_result = re.search(r"Spain", text)
if search_result:
    print("Found:", search_result.group())  # Output: Found: Spain
else:
    print("Not found")

# Example: Find a word at the beginning of a sentence
text = "Python is fun."
result = re.search(r"^Python", text)  # '^' matches the beginning of a string
if result:
    print("Starts with 'Python'")  # Output: Starts with 'Python'
else:
    print("Does not start with 'Python'")

# 3. re.split() - Splits a string by the occurrences of a pattern

# Example: Split by whitespace
text = "Split this text by whitespace."
words = re.split(r"\s+", text)
print("Words:", words)  # Output: ['Split', 'this', 'text', 'by', 'whitespace.']

# Example: Split by punctuation
sentence = "Hello! How are you? I'm fine."
split_sentence = re.split(r"[!?.]", sentence)
print("Split by punctuation:", split_sentence)  # Output: ['Hello', ' How are you', " I'm fine", '']

# 4. re.sub() - Replaces occurrences of a pattern with a specified string

# Example: Replace all occurrences of "in" with "out"
text = "The rain in Spain."
replaced_text = re.sub(r"in", "out", text)
print("Replaced text:", replaced_text)  # Output: The raout out Spaout.

# Example: Replace numbers with a placeholder
text_with_numbers = "Order number: 12345, Item number: 67890."
masked_text = re.sub(r"\d+", "[NUMBER]", text_with_numbers)
print("Masked text:", masked_text)  # Output: Order number: [NUMBER], Item number: [NUMBER].

# Additional Examples for each method

# re.findall() with complex pattern
text = "Email: test@example.com, Backup: backup@example.com"
emails = re.findall(r"\b\w+@\w+\.\w+\b", text)
print("Emails found:", emails)  # Output: ['test@example.com', 'backup@example.com']

# re.search() for specific pattern at the end of a string
text = "The document is at the end.pdf"
if re.search(r"\.pdf$", text):  # '$' matches the end of the string
    print("The text ends with '.pdf'")  # Output: The text ends with '.pdf'
else:
    print("The text does not end with '.pdf'")

# re.split() with capturing groups to keep delimiters
text = "apple,orange;banana:grape"
split_text = re.split(r"([,;:])", text)
print("Split with delimiters:", split_text)  # Output: ['apple', ',', 'orange', ';', 'banana', ':', 'grape']

# re.sub() with pattern replacement and backreference
text = "This is a test. Test this again."
result = re.sub(r"\b(T|t)est\b", r"\1est-case", text)
print("Sub with backreference:", result)  # Output: This is a Test-case. Test-case this again.
