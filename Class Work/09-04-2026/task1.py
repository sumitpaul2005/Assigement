# write prog with function of reverse,palindrome and sorting

def reverse():
    l = list(map(int,input("Enter the value of list : ").split()))
    left = 0
    right = len(l)-1

    while(left < right):
        l[right],l[left] = l[left],l[right]
        left += 1
        right -= 1

    print(l)

def palindrome():
    l = list(map(int,input("Enter the value of list : ").split()))
    left = 0
    right = len(l)-1
    ans = "Palindrome"
    while(left < right):
        if l[left] == l[right]:
            left += 1
            right -= 1
            continue
        else:
            ans = "Not Palindrome"
            break
    print(ans)

def sort():
    l = list(map(int,input("Enter the value of list : ").split()))
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] > l[j]:
                l[i],l[j] = l[j],l[i]

    print(l)

while True:
    menu = """
        Press 1 : Reverse number
        Press 2 : Palindrome
        Press 3 : Sorting
        Press 4 : Exit
    """
    print(menu)
    n = int(input("Enter your choices : "))

    if n == 1:
        reverse()
    elif n == 2:
        palindrome()
    elif n == 3:
        sort()
    elif n == 4:
        print("Thank you!!")
        break
    else:
        print("Invalid choice")
        break
    
