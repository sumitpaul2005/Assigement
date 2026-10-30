# User input

# n = int(input("Enter the length of list : "))
# l = []
# for i in range(0,n):
#     l.append(int(input("Enter the value : ")))

# print("List value are : ",l)

# Sorting withot inbuilt method

n = int(input("Enter the length of list : "))
l = []
temp = 0

for i in range(0,n):
    l.append(int(input("Enter the value : ")))
print(l)

for i in range(0,len(l)):
    for j in range(0,n-i-1):
        if l[j] > l[j+1]:
            temp = l[j]
            l[j] = l[j+1]
            l[j+1] = temp

print(l) 