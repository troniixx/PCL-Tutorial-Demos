## decrypt a text by exchanging each character with the _previous_ character 
##   in the encoding table
## blanks and dots stay the same
## by Martin Volk

# my_string = "Bcopsnbm Dpspob jogfdujpo ovncfst jo Xfohfo dbmm uif mbshftu Txjtt tlj sbdf joup rvftujpo. Ju xjmm cf efdjefe bmsfbez po Tvoebz xifuifs uif tbgfuz dpodfqu dbo cf usvtufe boe uif fwfou dbo ublf qmbdf."

my_string = "If tfft uif nbo xjui uif ufmftdpqf"

print('Input: ', my_string, '\nOutput: ')

# for each character in the input string
for x in my_string:
	if (x == ' ') or (x == '.'):
		print(x, end='')
	else:
		# get the value in the encoding table and subtract 1
		y = ord(x) - 1
		# print the character for the value in the encoding table
		print(chr(y), end="")

print()