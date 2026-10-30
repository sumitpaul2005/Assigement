def prime(n):
    pri = 0
    for i in range(1,n+1):
        if n%i == 0:
            pri += 1
    
    return pri
n = int(input("Enter the number : "))
p = prime(n)
if p == 2:
    print("Prime number")
else:
    print("Not prime number")