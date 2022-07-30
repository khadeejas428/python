Num=int(input("enter number:"))
divisors_list=[]
for i in range(1,Num+1):
    if Num%i==0:
        divisors_list.append(i)
        print(divisors_list)