n = list(map(int,input("Enter the value : ").split()))
unique = []
for i in n:
    if i not in unique:
        unique.append(i)
    
print(unique)