def multiply(a,b):  #Create the function in which will multiply 2 numbers
    product=a*b #Create the product variable which will store the multiplication
    product=int(product) #Convert the string to an integer
    return product #Return the result
   
if __name__=="__main__": #Create the if name==main which will initialize the whole program
    print(multiply(12,4)) #Call the function with by printing it (or else it will output to nothing)
#Use other numbers
