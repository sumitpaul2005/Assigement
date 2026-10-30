def Great():
    a = int(input("Enter the number : "))
    b = int(input("Enter the number : "))
    c = int(input("Enter the number : "))

    if a > b and a > c:
        print(a," is greater number")
    elif b > a and b > c:
        print(b," is greater number")
    else:
        print(c," is greater number")

def prime():
    n = int(input("Enter the number : "))
    p = 0
    for i in range(1,n+1):
        if n%i == 0:
            p += 1
    if p == 2:
        print("Prime number")
    else:
        print("Not prime")

def pattern():
    for i in range(1,6):
        print("*"*i)

def Exit():
    print("Thank you!!")
    

while(True):
    menu = """
    Press 1 : Greater number find
    Press 2 : Prime number
    Press 3 : Pattern
    Press 4 : Exit
    """

    c = int(input("Enter your choice: "))

    if c == 1:
        Great()
    
    elif c == 2:
        prime()
    
    elif c == 3:
        pattern()

    elif c == 4:
        Exit()
        break

    else:
        print("You enter wrong choice")
        