def input_function(prompt): #This function reads user input like the example at line 5
    prompt = input(prompt)
    return prompt

like = input_function('Do I like you? Yes or No:')
if like == "Yes":
    print('I actually hate you')
    print('Thank you for falling for my random joke')
else:
    print("You smart boy")
    print('Thank you for not falling for my random joke')
