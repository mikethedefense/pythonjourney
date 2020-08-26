# Camel Case Function Converter to Kebab or Snake Case

def camel_converter(word, separator):
    '''
    This function converts a camel cased word into a snake case or kebab case depending if separator is True or False
    '''
    new_string = []
    
    for i in word:
        if separator == False:
            if i.isupper(): 
                new_string.append("_")
                new_string.append(i)
            else:
                new_string.append(i)
        elif separator == True:
            if i.isupper(): 
                new_string.append("-")
                new_string.append(i)
            else:
                new_string.append(i)
        else:
            return None
    
    return "".join(new_string[1:]) # Init new_string and start from Index[1] to the end 
    
print(camel_converter("HelloMyFriend", True )) # Function Call    
