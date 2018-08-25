import time
import sys
category_1 = 'House'
category_2 = 'Schools'
type_1_h = 'Modern House'
type_2_h = 'Dollhouse'
type_3_h = 'Small House'
type_1_s = 'Daycare'
type_2_s = 'Elementary school'
print('Hello world, welcome to the Playmobile City.')
print('Here are the categories of Playmobile City: {} and {}'.format(category_1, category_2))
category = input('Enter the category you want:')
while True:
    if  category != category_1 and category != category_2:
        print('Invalid category.')
        category = input('Enter another:')
    else:
        break
    
if category == category_1:
    print('Here are the types of homes: \n{} \n{} and \n{}.'.format(type_1_h,type_2_h,type_3_h))
    category = input('Select one:')
        
if category == category_2: 
    print('Here are the types of schools: \n{} and \n{}'.format(type_1_s,type_2_s))
    category= input('Select one:')

while True:
    if category != type_1_h and category != type_2_h and category != type_3_h:
        print('Invalid type.')
        category = input('Enter another:')
    else:
        break

if  category == type_1_h:
    print('Searching for Modern House')
    time.sleep(2)
    print('We have found Modern House for you. Please go to Maria Selena store to go see it.')
    sys.exit() 
elif category == type_3_h:
    print('Searching for Small House')
    time.sleep(2)
    print('We have found Small House for you. Please go to Maria Selena store to go see it.')
    sys.exit()
elif category == type_2_h:
    print('Searching for DollHouse')
    time.sleep(2)
    print('We have found DollHouse for you. Please go to Maria Selena store to go see it.')
    sys.exit()

while True:
    if category != type_1_s and category != type_2_s:
        print('Invalid type')
        category=input('Enter another:')
    else:
        break 


if category == type_1_s:
    print('Searching for Daycare')
    time.sleep(2)
    print('We have found Daycare for you. Please go to Daycare We Love to register yourself')
    sys.exit()

elif category == type_2_s:
    print('Searching for elementary school')
    time.sleep(2)
    print('We have found elementary school for you. Please go to Elementary Saint Maria to register yourself.')
    sys.exit()


