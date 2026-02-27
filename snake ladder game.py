# snake water gun game

import random
# random is used to take any random number fro mthe computer

def check(comp,user):
    if(comp==user):
        return 0
    
    if(comp==0 and user==1):
        return -1
    
    if(comp==2 and user==0):
        return -1
    
    if(comp==1 and user==0):
        return -1
    
    else:
        return 1



comp= random.randint(0,2)
# random.randint(0,2) means it gives an integer value from 0 to 2
user = int(input("Enter 0 for snake,1 for water and 2 for gun: "))

score = check(comp,user)

print("You",user)
print("Computer",comp)

if(score == 0):
    print("It's a draw")
elif (score ==-1):
    print("you lose")
else:
    print("You won")
    print(f"score:{score}")