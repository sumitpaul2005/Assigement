# Make a program to generate a strong password using the input given by the user. To generate a password,
# randomly take some words from the user input and then include numbers, special characters and 
# capital letters to generate the password. Also, keep a check that password length is more than 8 characters.
# Note: Include Exception handling wherever required. Also, make a ‘User’ class and 
# store the details like user id, name and password of each user as a tuple.

import random

class User:
    def userDetails(id,name,password):
        details = (id,name,password)
        return details
    
    def display(details):
        print("User Details : ",details)

def password_Generater(word):
    try:
        if len(word) == 0:
            raise ValueError("Enter minimum 8 characters!!")
        
        w1 = random.choice(word)
        w2 = random.choice(word)
        num = str(random.randint(10,99))
        spe = random.choice(["@","#","$","%","&"])

        password = w1.upper() + num + w2 + spe

        if len(password) >= 8:
            return password
        
        else:
            print("Password must be 8 character or more!!, PLease enter more word!!")
            
        
    except Exception as e:
        print("Error",e)
        return None


try:
    id = int(input("Enter the Id : "))
    name = input("Enter the name : ")
    text = input("Enter some word : ")
    word = text.split()

    password = password_Generater(word)
    if password:
        print("Generate Password : ",password)
        user = User.userDetails(id,name,password)
        User.display(user)
except ValueError:
    print("Invalid input !!")