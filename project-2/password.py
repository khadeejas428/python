from lib2to3.pygram import Symbols
import random
import string 


lower_case ="abcdefghijklmnopqrestuvwxyz"
upper_case ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "!@#$%^&*()."


string = lower_case + upper_case + number + symbols
lenght = 8
password ="".join(random.sample(string,lenght))

print("Your new Password is :-" +password)
