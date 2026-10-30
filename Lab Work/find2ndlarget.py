def f(l):
    l.sort()
    print(l[-2])

l = list(map(int, input("Enter the number : ").split()))

f(l)