# Fibonacci Series..

n = int(input("Enter the terms : "))
n1 = 1
n2 = 2

for i in range(2,n+1):
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3
    