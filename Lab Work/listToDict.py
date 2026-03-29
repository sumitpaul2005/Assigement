li = list(input("Enter the sentence: ").split())

dic = {}

for i in li:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1


print(dic)