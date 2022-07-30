import random


a=random.randint(1,9)
b=int(input("Guess a number:"))
print(a)
if a>b:
    print("too low")
elif a<b:
    print("too high")
else :
    print("exactly right")
    