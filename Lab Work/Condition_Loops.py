# n = int(input("Enter the number : "))

# for i in range(1,11):
#     print(n," * ",i," = ",i*n)
    

# Find the year is leap year or not

year = int(input("Enter the Year : "))

if year % 400 == 0:
    print("It is a Leap Year")
elif year % 100 == 1:
    print("It is not a leap year")
elif year % 4 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")