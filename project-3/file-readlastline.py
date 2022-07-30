from tkinter import N

def lastNlines(fname,n):
    with open(fname)as file:
        for line in (file.readlines()[-N:]):
            print(line,end ='')

if __name__ =='__main__':
    fname = 'file1.txt'
    N = 2
    try:
        lastNlines(fname,N)
    except:
         print('file not found')