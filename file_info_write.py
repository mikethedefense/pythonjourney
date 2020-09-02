# Write function to write into a .csv file
# It should accept a filename and a list of tuples of name, age and address
# The file should create a header row with the following info from the list of tuples

def info(filename, seq):
    with open(filename, 'w') as fin: 
        for name, address, age in seq:
            fin.write(f"{name},{address},{age}\n")

directory = r"D:\Python Programs\Python Learning New\FileInputOutput\info.csv"
information = [("Mike","1000 CrossRd", 21), ("John", "10310 Washington St", 18), ("Paul","3412 Kennedy Rd",25)]
info(directory, information)
