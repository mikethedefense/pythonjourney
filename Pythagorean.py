import math 
legs = int(input('What is the first leg length of the triangle?:'))
other = int(input('Second leg length?:'))
hypothenuse = math.sqrt(legs**2 + other**2)
print('The hypothenuse is',hypothenuse)
