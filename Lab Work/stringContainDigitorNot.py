def f(n):
    s = n.split()
    if s.isdigit():
        print("Yes ")
    else:
        print("No")

s = input("Enter the value : ")
f(s)