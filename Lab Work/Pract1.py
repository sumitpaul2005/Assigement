# 1 . Function create account  ==>  user password 
# 2 . Function login account  ==> user password  login success  ==>  ac ==> 25000 

# 3 . deposit  ==> amt  ==> 5000  after deposit ==> 30000 
# 4. with draw ==> amt  
#     if bal -amt >=10000     ==> 
#         bal -amt
#     else :
#         min bal  require 10K 
# 5 . check  balance ==> balance


        
import random

d = {}

class Bank:

    def account(self):
        print("\n----- Create Account -----")

        name = input("Enter Name : ")
        email = input("Enter Email : ")
        ph = input("Enter Mobile Number : ")

        if len(ph) == 10 and ph.isdigit():

            if ph in d:
                print("Account already exists!")
                return

            bal = 25000

            d[ph] = {
                "name": name,
                "email": email,
                "bal": bal
            }

            print("Account Created Successfully!")
            print("Opening Balance =", bal)

        else:
            print("Invalid Mobile Number!")

    def login(self):
        print("\n----- Login -----")

        name = input("Enter Name : ")
        ph = input("Enter Mobile Number : ")

        if ph in d and d[ph]["name"].lower() == name.lower():

            otp = random.randint(100000, 999999)
            print("Your OTP is :", otp)

            user_otp = int(input("Enter OTP : "))

            if user_otp == otp:
                print("Login Successful!")
                self.mobile = ph
                return True
            else:
                print("Incorrect OTP!")
                return False

        else:
            print("Invalid Name or Mobile Number!")
            return False

    def Depo(self):
        print("\n----- Deposit -----")

        amount = int(input("Enter Amount : "))

        if amount > 0:
            d[self.mobile]["bal"] += amount
            print("Deposit Successful!")
            print("Current Balance :", d[self.mobile]["bal"])
        else:
            print("Invalid Amount!")

    def Withdraw(self):
        print("\n----- Withdraw -----")

        amount = int(input("Enter Amount : "))

        balance = d[self.mobile]["bal"]

        if amount <= 0:
            print("Invalid Amount!")

        elif balance - amount >= 10000:
            d[self.mobile]["bal"] -= amount
            print("Withdrawal Successful!")
            print("Remaining Balance :", d[self.mobile]["bal"])

        else:
            print("Minimum balance of ₹10000 must be maintained!")

    def Balance(self):
        print("\nCurrent Balance :", d[self.mobile]["bal"])

    def AccountDetails(self):
        print("\n----- Account Details -----")

        print("Name    :", d[self.mobile]["name"])
        print("Email   :", d[self.mobile]["email"])
        print("Mobile  :", self.mobile)
        print("Balance :", d[self.mobile]["bal"])

    def Exit(self):
        print("\nThank You for Using Our Bank!")


obj = Bank()

while True:

    print("\n========== BANK MANAGEMENT SYSTEM ==========")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        obj.account()

    elif choice == 2:

        if obj.login():

            while True:

                print("\n----------- MENU -----------")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. View Balance")
                print("4. Account Details")
                print("5. Logout")

                ch = int(input("Enter Choice : "))

                if ch == 1:
                    obj.Depo()

                elif ch == 2:
                    obj.Withdraw()

                elif ch == 3:
                    obj.Balance()

                elif ch == 4:
                    obj.AccountDetails()

                elif ch == 5:
                    print("Logged Out Successfully!")
                    break

                else:
                    print("Invalid Choice!")

    elif choice == 3:
        obj.Exit()
        break

    else:
        print("Invalid Choice!")