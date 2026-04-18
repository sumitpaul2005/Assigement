def revmove(lis):
    l = []
    com = []
    for i in lis:
        if i not in l:
            l.append(i)
        else:
            com.append(i)

    return com,l

l1 = list(map(int, input("Enter the value of 1st list : ").split()))
l2 = list(map(int,input("Enter the value of 2nd list : ").split()))

l3 = l1 + l2

print("Final list : ",revmove(l3))
print("Common element are : ",revmove(l3))