# Make a program to generate a strong password using the input given by the user. To generate a password,
# randomly take some words from the user input and then include numbers, special characters and 
# capital letters to generate the password. Also, keep a check that password length is more than 8 characters.
# Note: Include Exception handling wherever required. Also, make a ‘User’ class and 
# store the details like user id, name and password of each user as a tuple.

import random as r
user = input("Enter your name : ")


char = r(user)
final = char
print(final)