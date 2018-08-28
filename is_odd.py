# Program that checks if a number is odd or even.
def is_odd(prompt): # Create function is_odd
    numberinput = int(input(prompt)) # Create user input  
    # Return Equation to see if number is odd
    return numberinput % 2 != 0
    
numberinput = is_odd(prompt = 'Please enter a number:') # Call the function is_odd
print(numberinput)
# Use different numbers to check if they are odd or even. Have fun!
