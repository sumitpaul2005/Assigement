# Recursion

# Factorial

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
    
# n = int(input("Enter the number : "))
# print(fact(n))


# Fibonacci Series

# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
    
# n = int(input("Enter the number : "))

# print(fibo(n))


# Prime number

# def prime(n,i=2):
#     if n <= 1:
#         return False
#     if i * i > n:
#         return True
#     if n % i == 0:
#         return False
    
#     return prime(n,i+1)

# n = int(input("Enter the number : "))

# if prime(n):
#     print("Prime number")
# else:
#     print("Not Prime number")


# Reverse number

def rev(n):
    if n == 0:
        return 0
    else:
        print(n)
        return rev(n-1)
    
n = int(input("Enter the number : "))
rev(n)