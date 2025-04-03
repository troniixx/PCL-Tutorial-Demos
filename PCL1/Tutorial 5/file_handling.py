# Open the input file
inp = open("Tutorial 5 Demos/story.txt", "r")
lines = inp.readlines() # get each line of the input file as a list
tokenized_lines = [] # empty list

# Tokenize the lines
for line in lines:
    tokens = line.split(" ") # get each line of the input file as a list of tokens
    for token in tokens: # iterate over the tokens in each line
        tokenized_lines.append(token)  # Use append for each token and add it to the list of tokens

# Close the input file
inp.close()

# Open the output file
#! If the file exists, it will be overwritten
#! If it doesnt: it will be created
out = open("Tutorial 5 Demos/story_tokenized.txt", "w")

# Write each token to the output file
for token in tokenized_lines:
    out.write(token + "\n")  # Write each token on a new line

# Close the output file
out.close()
