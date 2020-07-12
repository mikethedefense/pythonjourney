nums = "1"
questions = ["How are you?", "What is your name?"] 
letters = ["a","b"]
answers = []
i = 0
for num in nums:
    for letter in letters:
        print(num,letter,':',questions[i])
        answers.append(input())
        i += 1
    

print("Your answers:", "\n", "1.", "\t", answers[0], "\n" , "2.", "\t", answers[1])
    
