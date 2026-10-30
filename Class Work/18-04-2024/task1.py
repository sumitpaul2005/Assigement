# Gussing the number game

import random

computer = random.randint(1,51)
print("*****************  Enter any number form 1 to 50  *****************")

while True:
    user = int(input("Enter the number : "))

    if user > 50:
        print("Please enter number between 1 - 50!!")
    
    elif user > computer:
        print("It is greater than the number!!")
    
    elif user == computer:
        print("You Win!!")
        break

    elif user < computer:
        print("It is smaller than the number!!")

    else:
        print("Invalid Input")
        
