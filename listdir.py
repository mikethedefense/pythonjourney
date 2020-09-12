# Make a function that returns all the directory contents in a directory.
# Return the contents are files or directories 
import os 

def list_dir(directory):
    data = os.listdir(directory) # list all the directories and assign them to the data variable
    for count, name in enumerate(data): # Loop through the list and enumerate it 
        new = os.path.join(directory, name) # join the directory and the name to check if it is a dir or a file
        return f"{count + 1}: {name}  Is Dir:{os.path.isdir(new)}  Is File:{os.path.isfile(new)}"

d = r"D:"  # The directory you want to put

# Exception handling
try:
    print(list_dir(d))
except (IOError, FileNotFoundError):
    print("File not found")
