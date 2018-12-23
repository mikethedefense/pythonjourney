import math
#This program incorporates both pythagorean solutions: finding the hypothenuse and the leg of a triangle
prompt = int(input("Guessing you need help to figure out the Pythagorean thrum. We got you covered. What do you need help with: \n1: Hypothenuse \n2: Attempting to find the leg length \n Enter a number:"))
options = [1,2]
while True:
    if prompt not in options:
        print("Invalid number")
        prompt = int(input("Enter another:"))
    else:
        break
if prompt ==1:
    print("You have selected Hypothenuse")
    leg_1 = int(input('What is the first leg length of the triangle?:')) # leg_1 is the side of your triangle
    leg_2 = int(input('Second leg length?:')) # leg_2 is the side of the triangle
    hypothenuse = math.sqrt(leg_1**2 + leg_2**2)
    answer = round(hypothenuse,2)
    print('The hypothenuse is',answer)
elif prompt ==2:
    print("You have selected Attempting to find leg length")
    hypo = int(input("Enter the hyopthenuse of the triangle:")) #Finding the hypothenuse
    leg = int(input("Enter the leg of the triangle:")) #This is the leg of the triangle that has been already assigned
    calculation = math.sqrt(hypo**2-leg**2)
    answer = round(calculation,1)
    print("The leg of the triangle is",answer)
