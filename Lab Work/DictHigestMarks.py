n = int(input("Enter the length : "))
dic = {}
for i in range(0,n):
    key = input("Enter the name of student : ")
    marks = int(input("Enter the marks : "))
    dic[key] = marks

print(dic)

l = list(dic.items()).sort()
l.sort()

print(l)