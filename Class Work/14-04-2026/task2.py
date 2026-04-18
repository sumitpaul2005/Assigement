#Key 1-30 values = keys square
# d = {}
# for i in range(1,31):
#     d[i] = i*i
# print(d)

# List1 = keys and list2 = values convert dictionary

# n = int(input("Enter the length of list : "))

# l1 = []
# l2 = []
# d = {}

# for i in range(0,n):
#     l1.append(int(input("Enter the key : ")))
#     l2.append(input("Enter the values : "))

# for i in range(0,n):
#     d[l1[i]] = l2[i]

# print(d)

# NESTED DICTIONARY

n = int(input("Enter the length of dictionary : "))

d1 = {}
d2 = {}

for i in range(0,n):
    k = int(input("Enter the key : "))
    m = int(input("Enter the number for this key : "))
    for j in range(0,m):
        k1 = int(input("Enter the keys : "))
        v2 = input("Enter the values : ")
        d2[k1] = v2
    d1[k] = d2

print(d1)