import random

# User Class

class User:
    def store(id,name,password):
        Details = (id,name,password)
        return Details
    
    def display(details):
        print("User Details : ",details)

# Generate Password

def Generate_password(word):
    try:

        if len(word) == 0:
            print("Enter some word!!")

        w1 = random.choice(word)
        w2 = random.choice(word)
        number = str(random.randint(10,99))
        special = random.choice(["@","#","$","%","&"])
        password = w1.upper() + number + w2 + special
        if len(password) < 8:
            print("PLease enter more than 8 character!!")
        else:
            return password
    except Exception as e:
        print("Error : ",e)


# Main Code

try:
    id = int(input("Enter the Id : "))
    Name = input("Enter the name : ")
    word = input("Enter some word for password : ").split()

    password = Generate_password(word)

    if password:
        print("Password Generate : ",password)
        user_details = User.store(id,Name,password)
        User.display(user_details)

except ValueError:
    print("Invalid Input!!")