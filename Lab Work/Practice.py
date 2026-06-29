# 1. Create a list of 10 numbers and print the largest and smallest number.

# l = list(map(int,input("Enter the value : ").split()))

# l.sort()
# print(l[-1])
# print(l[-2])

# 2. Find sum and average of list elements.

# l = list(map(int,input("Enter the value : ").split()))
# add = 0
# c = 0
# for i in l:
#     add += i
#     c += 1

# print(add)
# avg = add / c
# print(avg)

# 3. Remove duplicate elements from a list.

# l = list(map(int,input("Enter the value : ").split()))

# f = []

# for i in l:
#     if i not in f:
#         f.append(i)

# print(f)

# 5. Merge two lists into one.

# l1 = list(map(int,input("Enter the valueof 1st list : ").split()))
# l2 = list(map(int,input("Enter the value of 2nd list : ").split()))

# l3 = l1 + l2
# print(l3)

# Dictinory

# 1. Create a dictionary of student marks and print highest marks.

n = int(input("Enter the length : "))
d = {}

for i in range(n):
    name = input("Enter the name : ")
    marks = int(input("Enter the marks : "))
    d[name] = marks

print(d)
h = {}


print(d)