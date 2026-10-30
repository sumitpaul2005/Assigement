# Write a programe Stone , Paper and Sissors , if user score more than 400 than print Awsome

import random

print("*********************  Enter your choice!!  *********************")
score = 0
l = ["rock" , "paper" , "sissor"]
i = 0
while i < 6:
    computer = random.choice(l)
    user = input("Enter user input : ")

    if user not in l:
        print("Please enter from the choice!!")

    elif user == computer:
        print("Tie!!")
        i += 1

    elif((user == "rock" and computer == "sissor") or (user == "paper" and computer == "rock") or (user == "sissor" and computer == "paper")):
        print("User Win !!!")
        score += 100
        i += 1

    else:
        print("Computer Win !!!")
        i += 1

    
if score >= 400:
    print("You play Awsome!!",score)
elif score == 0:
    print("You have 0 score!!")
else:
    print("You play well!!",score)