while True:
    menu = """
        Press 1 : Ascending Order
        Press 2 : Descending Order
        Press 3 : Unique number 
        Press 4 : Reverse list
        Press 5 : Exit
    """
    print(menu)
    n = int(input("Enter your choices : "))

    if n == 1:
        l = list(map(int, input("Enter the value : ").split()))

        for i in range(0,len(l)):
            for j in range(i+1,len(l)):
                if l[i] > l[j]:
                    l[j] , l[i] = l[i] , l[j]

        print("Ascending order : ",l)

    elif n == 2:
        l = list(map(int, input("Enter the value : ").split()))

        for i in range(0,len(l)):
            for j in range(i+1,len(l)):
                if l[i] < l[j]:
                    l[j] , l[i] = l[i] , l[j]

        print("Descending order : ",l)

    elif n == 3:
        l = list(map(int, input("Enter the value : ").split()))
        u = []
        for i in l:
            if i not in u:
                u.append(i)

        print("Unique number : ",u)
    
    elif n == 4:
        l = list(map(int, input("Enter the value : ").split()))

        for i in range(0,len(l)):
            for j in range(i+1,len(l)):
                l[j] , l[i] = l[i] , l[j]

        print("Reverse order : ",l)

    elif n == 5:
        print("Thank you!!")
        break

    else:
        print("You enter wrong choices")
        break