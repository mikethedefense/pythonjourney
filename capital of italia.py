score = 0
a=input ("What is the capital of italy:")
if a=="rome" or a=="Rome":
    print ("ecco")
    score= score+1
else:
    print("male")
primera=input("What is the capital of Canada:")
if primera=="ottawa" or primera=="Ottawa":
    print("ecco")
    score=score+1
else:
    print("Male")

if score == 2:
    print("You got 100%!")
elif score ==1:
    print("You got 50%")
elif score ==0:
    print("You got 0%")
print("Your score: \n{}".format(score))