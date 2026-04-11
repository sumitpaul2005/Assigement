l = int(input("Enter the length of list : "))
li = []

di = {}

for i in range(0,l):
    keys = input("Enter the key : ")
    values = float(input("Enter the value : "))
    li.append((keys,values))

di = dict(li)

print(li)
print(di)