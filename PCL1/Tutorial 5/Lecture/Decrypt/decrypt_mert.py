## decrypt a text by exchanging each character with the _previous_ character 
##   in the encoding table
## blanks and dots stay the same
## by Martin Volk, modified by Mert Erol

my_string = "If tfft uif nbo xjui uif ufmftdpqf"

print("Input: ", my_string, "\nOutput: ")

out = ""

for x in my_string:
    if (x == " ") or (x == "."):
        out += x
    else:
        y = ord(x) - 1
        out += chr(y)
        
print(out)