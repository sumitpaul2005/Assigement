a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))

while b != 0:
    c = b
    b = a%b
    a = c
    
print("GCD is : ",a)