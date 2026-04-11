# l = [1 , 15 , 11 , 4 , 10]
# l.sort()
# print("Largest  : ",l[-1])
# print("Smallest : ",l[0])
# print("Second largest : ",l[-2])

# find unique number 

l = [10 , 20 , 10 , 30 , 20 , 40]
uqi = []
dup = []
for i in l:
    if i not in uqi:
        uqi.append(i)
    else:
        dup.append(i)

print("Unique number : ",uqi)
print("Duplicate number : ",dup)