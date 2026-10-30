# l = int(input("Enter the length of list : "))
# li = []

# di = {}

# for i in range(0,l):
#     keys = input("Enter the key : ")
#     values = float(input("Enter the value : "))
#     li.append((keys,values))

# di = dict(li)

# print(li)
# print(di)

#                               Create a dictionary with 5 student names and their marks.
                                # ➤ Find the student with the highest marks.

n = int(input("Enter the number of student : "))
d = {}
for i in range(n):
    k = input("Enter the name of student : ")
    v = int(input("Enter the marks of students : "))
    d[k] = v

print(d)
 
lis = list(d.items())
for i in range(0,len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i][1] > lis[j][1]:
            lis[i], lis[j] = lis[j] , lis[i]

d.clear()
for k,v in lis:
    d[k] = v
print(d)