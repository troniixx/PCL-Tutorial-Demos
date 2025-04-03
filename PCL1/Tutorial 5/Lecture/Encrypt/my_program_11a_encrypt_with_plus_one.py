## encrypt a text by exchanging each character with the _next_ character 
##  in the encoding table
## blanks and dots stay the same, in order to preserve the text structure
##   which of course leads to ambiguities :-(
##   e.g. '-' on position 45 will be converted to 46 --> '.'
## by Martin Volk

# possible input strings
my_string = "He sees the man with the telescope"

# my_string = "Auffälligkeiten bei den Corona-Infektionszahlen in Wengen stellen das grösste Schweizer Skirennen infrage. Ob dem Schutzkonzept vertraut und der Anlass durchgeführt wird, entscheidet sich voraussichtlich bereits am Sonntag."

# my_string = "Abnormal Corona infection numbers in Wengen call the largest Swiss ski race into question. It will be decided already on Sunday whether the safety concept can be trusted and the event can take place."  # reference 1 (by me)


print('Input: ', my_string, '\nOutput: ')

# for each character in the input string
for my_char in my_string:
    
	# if the character is the blank or the dot, then do not encrypt
	if (my_char == ' ') or (my_char == '.'):
    
		# the _end=''_ prevents the print command from producing a newline symbol
		print(my_char, end='')
	else:
    
		# get the value in the encoding table and add 1 for the next character
		my_new_char = ord(my_char) + 1

		# print the new character for the value in the encoding table
		# e.g. for input 'A' print 'B', for input 'B' print 'C' etc.
		#! default: print("a") == print("a", end = "\n")
		print(chr(my_new_char), end="")


# print a newline in the end
print()

