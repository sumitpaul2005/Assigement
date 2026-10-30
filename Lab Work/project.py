# Make a program to generate a strong password using the input given by the user. To generate a password,
# randomly take some words from the user input and then include numbers, special characters and 
# capital letters to generate the password. Also, keep a check that password length is more than 8 characters.
# Note: Include Exception handling wherever required. Also, make a ‘User’ class and 
# store the details like user id, name and password of each user as a tuple.

# import random

# class User:
#     def userDetails(self,id,name,password):
#         details = (id,name,password)
#         return details
    
#     def display(details):
#         print("User Details : ",details)

# def password_Generater(word):
#     try:
#         if len(word) == 0:
#             raise ValueError("Enter minimum 8 characters!!")
        
#         w1 = random.choice(word)
#         w2 = random.choice(word)
#         num = str(random.randint(10,99))
#         spe = random.choice(["@","#","$","%","&"])

#         password = w1.upper() + num + w2 + spe

#         if len(password) >= 8:
#             return password
        
#         else:
#             print("Password must be 8 character or more!!, PLease enter more word!!")
            
        
#     except Exception as e:
#         print("Error",e)
#         return None


# try:
#     id = int(input("Enter the Id : "))
#     name = input("Enter the name : ")
#     text = input("Enter some word : ")
#     word = text.split()

#     password = password_Generater(word)
#     if password:
#         print("Generate Password : ",password)
#         user = User.userDetails(id,name,password)
#         User.display(user)
# except ValueError:
#     print("Invalid input !!")


1.
# Write a python program to sum of the first n positive integers.
# l = list(map(int,input("Enter the values : ").split()))
# sum = 0
# for i in l:
#     if i > 0:
#         sum += i
    
# print("Total Sum : ",sum)

2.
# Write a Python program to count occurrences of a substring in a string.
# s = input("Enter the string : ").split()
# st = input("Enter the sub string : ").split()
# count = s.count(st)

# print(count)

# Check whether a year is a leap year.

# year = int(input("Enter the year : "))

# if year % 400 == 0:
#     print("It is leap year : ",year)
# else:
#     print("Not a leap year")

# Count vowels in a string.

# str = input("Enter the string : ")

# count = 0
# for i in str:
#     if i in "aeiou":
#         count += 1
    
# print(count)


# Calculate the sum of all list elements.

# l = list(map(int,input("Enter the number : ").split()))
# sum = 0
# for i in l:
#     sum += i

# print(sum)

# Sort a list in ascending order.

# l = list(map(int,input("Enter the number : ").split()))

# s = sorted(l)

# print(s)

# Create a tuple and print its elements.

# n = tuple(map(int,input("Enter the value : ")))
# print(n)
# print(type(n))

# Count how many times an element appears in a tuple.

# n = tuple(map(int,input("Enter the value : ")))
# c = 0
# for i in n:
#     c += 1

# print(c)

# Create a dictionary of student details.
# n = int(input("Enter the length of dictinary : "))
# d = {}
# for i in range(n):
#     key = int(input("Enter student roll number : "))
#     val = input("Enter student name : ")
#     d[key] = val

# print(d)

# Create a class Calculator with methods for add, subtract, multiply.

class calculator:
    def add(n):
        sum = 0
        for i in range(n):
            v = int(input("Enter the number : "))
            sum += v
        print(sum)

    def sub(n):
        sub = 0
        for i in range(n):
            v = int(input("Enter the number : "))
            sub = v
        print(sum)