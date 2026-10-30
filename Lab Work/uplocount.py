def f(str1):
    s = str1
    u = 0
    l = 0
    for i in s:
        if i.isupper():
            u += 1
        else:
            l += 1
    return u,l

str1 = input("Enter the string : ")
u,l = f(str1)

print("Upper case = : ",u)
print("Lower case = : ",l)