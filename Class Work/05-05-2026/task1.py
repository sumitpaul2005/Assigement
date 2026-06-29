# Polymorphism

# class Myclass:
#     def a(self):
#         print("Method 1 !!!")
#         a = 10
#         self.a = a # self.a is a pointer it store address of a

#     def b(self):
#         print(self.a)

# o = Myclass()
# o.a()
# o.b()


# Banking Programme
import random

class Bank():
    def acc_open(self):
        name = input("Enter your name : ")
        ph = int(input("Enter your mobile number : "))
        self.acc = acc = random.randint(000000000000,999999999999)
        balance = 5000
        self.bal = balance
        print("Successfully Account Open!!!")

    def deposite(self):
        ac = int(input("Enter Account number : "))
        if ac == self.acc:
            amt = int(input("Enter amount : "))
            self.bal += amt
        else:
            print("Invalid Account number!!")

    def withdraw(self):
        if self.bal > 5000:
            amt = int(input("Enter amount : "))
            a = self.bal
            net = a - amt
            if net >= 5000:
                self.bal -= amt
            else:
                print("You can't withdraw!!")
        else:
            print("You balance is 5000 !!")
    
    def check_bal(self):
        print("Account number : ",self.acc)
        print("Balance : ",self.bal)

o = Bank()
print("Press 1 for Open Account")
print("Press 2 for Exit")
cho = int(input("Enter your choice : "))
if cho == 1:
    o.acc_open()
    while True:
        menu = """
            Press 1 for Deposit
            Press 2 for Withdraw
            Press 3 for Check Balance
            Press 4 for Exit
        """
        print(menu)
        c = int(input("Enter your choice : "))
         
        if c == 1:
            o.deposite()
        
        elif c == 2:
            o.withdraw()
        
        elif c == 3:
            o.check_bal()

        elif c == 4:
            print("Thank you!!")
            break
        else:
            print("Invalid input!!")
