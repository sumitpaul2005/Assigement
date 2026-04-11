n = list(map(int,input("Enter the value : ").split()))
uq = []
for i in n:
    if i not in uq:
        uq.append(i)
    
print(uq)