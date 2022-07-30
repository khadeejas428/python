from ast import Num
from operator import mod
from statistics import mode


Num=int(input("Enter a number:"))
mod=Num%2
if mod > 0 :
  print ("This number is odd")
else:
  print("This number is even")