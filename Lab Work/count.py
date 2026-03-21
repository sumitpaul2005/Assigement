s = input("Enter the string : ")

str = s.strip().split()

for i in str:
    c = 0
    for j in str:
        if i == j:
            c += 1
    print(i, ":" ,c)
