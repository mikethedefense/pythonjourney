# Write a function that reads a CSV file
# It should return a list of dictionaries using the first row as key names, and each subsequent row as values for those keys

def read_file(filename):
    with open(filename) as fin:
        print(add_info_to_dict(fin))

def add_info_to_dict(seq):
    results = [] 
    for line in seq:
        name, address, age = line.split(',')
        results.append({"name": name, "address": address, "age": int(age)})
    return results

directory = r"D:\Python Programs\Python Learning New\FileInputOutput\info.csv"
information = [("Mike","1000 CrossRd", 21), ("John", "10310 Washington St", 18), ("Paul","3412 Kennedy Rd",25)]
info(directory, information)
