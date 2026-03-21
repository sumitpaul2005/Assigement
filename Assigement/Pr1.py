n = int(input("Enter the Number : "))
sum = 0
if(n <= 0):
    print("It is an negative number : ")
else:
    for i in range(n+1):
        sum = sum + i
    print("Sum of ",n,"number is ",sum)
    