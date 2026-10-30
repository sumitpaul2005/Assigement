#                                           Print 1 to 10 n number using for loop

# for i in range(1,11):
#     print(i)

# Print Reverse number

# for i in range(10,0,-1):
#     print(i)

#                                                       Factorial

# n = int(input("Enter the the number : "))
# fact = 1
# for i in range(1,n+1):
#     fact *= i

# print(fact)

#                                                       Find Odd Even number

# for i in range(5):
#     n = int(input("Enter the the number : "))
#     if n % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

#                                                       Print Table

# n = int(input("Enter the the number : "))

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

#                                                       Prime Number

# n = int(input("Enter the the number : "))
# prime = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         prime += 1

# if prime == 2:
#     print("Prime Number")
# else:
#     print("Not Prime Number")  

#                                                       Reverse Number

# n = int(input("Enter the the number : "))
# rem = 0 
# rev = 0
# while(n != 0):
#     rem = n % 10
#     rev = rev * 10 + rem
#     n = n // 10

# print(rev)