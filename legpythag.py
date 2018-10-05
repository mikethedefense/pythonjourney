import math
hypo = int(input("Enter the hyopthenuse of the triangle:")) #Finding the hypothenuse
leg = int(input("Enter the leg of the triangle:")) #This is the leg of the triangle that has been already assigned
calculation = math.sqrt(hypo-leg)
answer = round(calculation,1)
print("The leg of the triangle is",answer)
