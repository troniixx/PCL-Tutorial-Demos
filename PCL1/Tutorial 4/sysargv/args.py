# Import the sys module to handle command-line arguments
import sys
#from sys import argv


# Function to check if the correct number of arguments is provided
def check_arguments():
    if len(sys.argv) != 3:
        print("Usage: python3 file_handling_demo_open_close.py <input_file> <output_file>")
        sys.exit()

# Main function to demonstrate file handling with open() and close()
def main():
    # Check arguments
    check_arguments()

    # Get the input and output file names from command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Open the input file for reading ('r')
    infile = open(input_file, "r")

    # Open the output file for writing ('w')
    outfile = open(output_file, "w")

    # Iterate over each line in the input file
    for line in infile:
        # Process the line (e.g., here we simply strip extra spaces and print it)
        processed_line = line.strip()

        # Print each processed line to the terminal
        print("Writing:", processed_line)

        # Write the processed line to the output file
        outfile.write(processed_line + "\n")

    # Close both files after finishing
    infile.close()
    outfile.close()

    print(f"Done! The content from {input_file} has been written to {output_file}.")
    print(sys.argv)
    
# Run the main function (ignore this for now)
if __name__ == "__main__":
    main()
