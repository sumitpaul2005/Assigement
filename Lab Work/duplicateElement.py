l = list(map(int, input("Enter the elements : ").split()))
u = []
for i in l:
    if i not in u:
        u.append(i)
print(u)