def f(l1,l2):
    l3 = []
    for i in l1:
        if i in l2:
                l3.append(i)
    print(l3)

l1 = list(map(int,input("Enter the number : ").split()))
l2 = list(map(int,input("Enter the number : ").split()))
f(l1,l2)