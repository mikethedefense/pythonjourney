age = input('Please enter your age:')
age = int(age)
while age < 1 or age > 95:
    print('Age is not valid!')
    age = input('Please enter your age:')
    age = int(age)
print('Thank you for entering your age!')