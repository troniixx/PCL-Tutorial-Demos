# Tokenize the lines
tokenized_lines = []  # empty list

with open("Tutorial 5 Demos/story.txt", "r") as inp:
    lines = inp.readlines()  # get each line of the input file as a list
    for line in lines:
        tokens = line.split(" ")  # get each line of the input file as a list of tokens
        for token in tokens:  # iterate over the tokens in each line
            tokenized_lines.append(token)  # Use append for each token and add it to the list of tokens

# Write each token to the output file
#! If the file exists, it will be overwritten
#! If it doesnt: it will be created
with open("Tutorial 5 Demos/story_tokenized.txt", "w") as out:
    for token in tokenized_lines:
        out.write(token + "\n")  # Write each token on a new line
