def lis(n):
    u = []
    for i in n:
        if i not in u:
            u.append(i)
        
    return u

n = list(map(int, input("Enter the value : ").split()))
uq = lis(n)
print(uq)