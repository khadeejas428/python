def sublist (E):
    lists = [[]]
    for i in range (len(E) + 1):
        for j in range (i):
            lists.append(E[j:i])
    return lists

L=[1,2,3,4]
print(sublist(L))
