s=input("enter a string: ")
s =s.casefold()
R=reversed(s)
if list(s)== list(R):
    print("The string is a palindrome.")
else:
        print("The string is not a palindrome.")