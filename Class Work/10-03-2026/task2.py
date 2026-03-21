while(True):
    menu = """
    Press 1 : Fibonaccie Series
    Press 2 : Factorial
    Press 3 : Prime Number
    Press 4 : Exit
    """

    cho = int(input("Enter your choices : "))
    
    if cho == 1:
        n = int(input("Enter the terms : "))
        n1 = 1
        n2 = 2
        print(n1)
        print(n2)
        for i in range(2,n+1):
            n3 = n1 + n2
            print(n3)
            n1 = n2
            n2 = n3
    
    elif cho == 2:
        n = int(input("Enter the number : "))
        fact = 1
        for i in range(1,i+1):
            fact *= i
        print("Factorial number is : ",fact)

    elif cho == 3:
        n = int(input("Enter the number : "))
        p = 0
        for i in range(1,n+1):
            if n%i == 0:
                p += 1
        if p == 2:
            print("Prime number")
        else:
            print("Not prime number")

    elif cho == 4:
        print("Thank you!!")
        break

    else:
        print("You enter wrong choice")
        break
