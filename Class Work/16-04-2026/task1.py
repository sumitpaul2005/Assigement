# Write a program of Sign up , login ,forget password , display all data stored and exit

import random

d = {}
d1 = {}
OTP = random.randint(1000,9999)

while True:
    menu = """
        Press 1 : Sign Up
        Press 2 : Login
        Press 3 : Forget Password
        Press 4 : Display all records
        Press 5 : Exit
    """
    print(menu)

    cho = int(input("Enter your choices : "))

    if cho == 1:
        name = input("Enter your name : ")
        email = input("Enter your email : ")
        ph = int(input("Enter your number : "))
        password = int(input("Enter your password : "))
        conform_password = int(input("Enter conform password : "))

        if password == conform_password:
            d1['name'] = name
            d1['email'] = email
            d1['ph'] = ph
            d1['password'] = password
            d[ph] = {'name' : d1['name'], 'email' : d1['email'], 'password' : d1['password']}
            print("Sign up seccessfully!!")
        else:
            print("Password and confrom password does not same!!")

    elif cho == 2:
        email1 = input("Enter email : ")
        password = int(input("Enter password : "))

        if d1['email'] == email1 and d1['password'] == password:
            print("Successfully Login!!")
        else:
            print("Does not match")
        
    elif cho == 3:
        ph1 = int(input("Enter mobile number : "))
        
        if d1['ph'] == ph1:
            print(OTP)
            otp = int(input("Enter OTP : "))
            if otp == OTP:
                password = int(input("Enter new password : "))
                d1["password"] = password
            else:
                print("Invalid OTP!!")
        else:
            print("Mobile number does not match!!")

    elif cho == 4:
        print(d)

    elif cho == 5:
        print("Thank uh!!!")
        break

    else:
        print("You enter wrong choice!!!")
