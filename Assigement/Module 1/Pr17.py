2#Factorial
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

#Even 
def even(n):
    total = 0
    for i in range(2,n+1,2):
        total += (i**2) / factorial(i)
    return total

#Odd
def odd(n):
    total = 0
    for i in range(1,n+1,2):
        total += (i**2) / factorial(i)
    return total


n = int(input("Enter the number : "))

print("Even number of series : ",even(n))
print("Odd number of series : ",odd(n))

