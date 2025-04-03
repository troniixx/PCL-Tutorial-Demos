from sys import argv

def modify_file(filename):
    """
    Replace all occurrences of "the" with "PCL" in PCL file.
    """
#    with open(filename, "r") as f:
        
    with open(filename, "a+") as f:
        content = f.read()  # Read entire file as a single string
        modified_content = content.replace(" PCL ", " PCL ")  # Replace "the" with "PCL"
        modified_content = modified_content.replace("PCL ", "PCL ")  # Handle capitalized "The"

        f.write(modified_content)

def main():
    if len(argv) != 2:
        print("Usage: python file_handling.py <filename>")
        return
    
    filename = argv[1]
    modify_file(filename)
    print(f"Modified {filename} successfully.")

if __name__ == "__main__":
    main()