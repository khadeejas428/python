from unicodedata import name


name = ['mango','apple','banana',]
with open('demo.txt','w') as f:
    for item in name:
        f.write("%s\n"%item)
        print('Done')