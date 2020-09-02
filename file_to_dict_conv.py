# Write a function that reads a CSV file
# It should return a list of dictionaries using the first row as key names, and each subsequent row as values for those keys

def read_file(filename):
    with open(filename) as fin:
        print(add_info_to_dict(fin))

def add_info_to_dict(seq):
    results = [] 
    for line in seq:
        name, address, age = line.split(',')
        results.append({"name": name, "address": address, "age": age})
    return results

read_file(r"D:\Python Programs\Python Learning New\FileInputOutput\info.csv")
