n = int(input("Enter the number of list : "))

list_turple = []
for i in range(1,n+1):
    str = input("Enter the string : ")
    num = int(input("Enter the number : "))
    list_turple.append((str,num))

print("List with Turple : ",list_turple)
list1 = []
list2 = []

for i in list_turple:
    list1.append(i[0])
    list2.append(i[1])

print(list1)
print(list2)