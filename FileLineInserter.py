# Write a program that inserts line number in front of lines of a file.
# Read the file from the sys.argv list
# Deal with a bad file being passed in
import sys

def check_for_number_seq(fin, seq):
    """
    This function checks if a file already has a line number sequence in front of it
    """
    with open(fin) as fout:
        for count, line in enumerate(fout):
            # Check if file already has a line number sequence
            if line.startswith("1") and count == 0: 
                continue
            if line.startswith("2") and count == 1:
                continue
            if line.startswith("3") and count == 2:
               sys.exit("Ended: File already has a line count")
            seq.append(f"{count + 1} {line}")

def insert_number(filename): # Add a default value to the function
    """
    Function that takes in a txt file from the command line (sys.argv) and inserts a line number in front of each line in the file.
    """
    words = []
    
    # Read the file and append each line to a list of tuples (line number, line context)
    check_for_number_seq(filename, words)
   
    # Overwrite the file with the list of tuples
    with open(filename, 'w') as fout:
        for newline in words:
            fout.write(newline)

def log(error):
    """
    This function logs the error, and prints it out. 
    """
    return f"There is an error: {error}"

# Exception handling: Catch a bad file input.
if __name__ == '__main__': # Code now runs as a script
    print(sys.argv) # Checks if code runs. 
    try:
        insert_number(sys.argv[1])
    except (IOError, FileNotFoundError) as e:
        print(log(e))
