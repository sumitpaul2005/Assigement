# Sorting 

#Asc Order

# l = list(map(int, input("Enter the number : ").split()))

# for i in range(0,len(l)):
#     for j in range(i+1,len(l)):
#         if l[i] > l[j]:
#             l[j],l[i] = l[i],l[j]

# print("Sorting in Ascending Order : ",l)

#Desc Order 

# l = list(map(int, input("Enter the number : ").split()))

# for i in range(0,len(l)):
#     for j in range(i+1,len(l)):
#         if l[i] < l[j]:
#             l[j],l[i] = l[i],l[j]

# print("Sorting in Descending Order : ",l)

# Reverse without inbuit method

l = list(map(int, input("Enter the number : ").split()))

print("Before Reverse : ",l)
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
            l[j],l[i] = l[i],l[j]

print("Reverse List : ",l)