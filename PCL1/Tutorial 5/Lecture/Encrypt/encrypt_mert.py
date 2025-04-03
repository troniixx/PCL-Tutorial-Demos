## encrypt a text by exchanging each character with the _next_ character 
##  in the encoding table
## blanks and dots stay the same, in order to preserve the text structure
##   which of course leads to ambiguities :-(
##   e.g. '-' on position 45 will be converted to 46 --> '.'
## by Martin Volk, modified by Mert Erol
my_string = "He sees the man with the telescope"

print("Input: ", my_string, "\nOutput: ")

out = ""

for my_char in my_string:
    
    if (my_char == " ") or (my_char == "."):
        
        out += my_char
        
    else:
        
        my_new_char = ord(my_char) + 1
        
        out += chr(my_new_char)
        
print(out)