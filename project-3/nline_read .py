def lastNlines(fname,n):
    with open(fname)as file:
        for line in (file.readlines()[:N]):
            print(line,end ='')

if __name__ =='__main__':
    fname = 'text.txt'
    N = 2
    try:
        lastNlines(fname,N)
    except:
         print('file not found')
