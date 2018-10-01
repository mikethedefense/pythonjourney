import math 
leg_1 = int(input('What is the first leg length of the triangle?:')) # leg_1 is the side of the triangle
leg_2 = int(input('Second leg length?:')) # leg_2 is the side of the triangle
hypothenuse = math.sqrt(leg_1**2 + leg_2**2)
answer = round(hypothenuse,2)
print('The hypothenuse is',answer)
