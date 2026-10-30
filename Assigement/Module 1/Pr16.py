li = list(map(int , input("Enter the number : ").split()))

dic = {}

for i in li:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

print(dic)