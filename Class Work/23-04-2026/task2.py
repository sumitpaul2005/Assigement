# Login Using File Handelling

import random

d = {}
while True:
    try:

        menu = """
            Press 1 : Sign up
            Press 2 : Login
            Press 3 : Forget Password
            Press 4 : Display all records
            Press 5 : Exit
        """
        print(menu)
        c = int(input("Enter your choices : "))

        if c == 1:
            name = input("Enter your name : ")
            email = input("Enter your email : ")
            ph = int(input("Enter your mobile number : "))
            password = int(input("Enter your password : "))
            conpass = int(input("Enter your Confrom Password : "))
            
            if password == conpass:
                print("Sign up Successfully!!!")
                d[ph] = {'name' : name, 'email' : email, 'password' : password}
            else:
                print("Password and Confrom Password does not same!!!")

        elif c == 2:
            ph = int(input("Enter your mobile number : "))
            password = int(input("Enter your password : "))
            if ph in d and d[ph]['password'] == password:
                print("Login Successfully!!")
            else:
                print("Details Invalid!!!")

        elif c == 3:
            ph1 = int(input("Enter your ph number : "))
            if ph in d:
                otp = random.randint(100000,999999)
                print("OTP is : ",otp)
                o = int(input("Enter OTP : "))
                if otp == o:
                    password = int(input("Enter your new Password : "))
                    print("Successfully Password changed!!")
                    d['password'] = password
                else:
                    print("OTP Incorrect!!")
            else:
                print("Ph number is incorrect!!!")
            
        elif c == 4:
            print(d)

        elif c == 5:
            print("Thank you!!!")
            break
        
        else:
            print("You enter wrong choices!!!")
            break
    
    except Exception as e:
        print(e)