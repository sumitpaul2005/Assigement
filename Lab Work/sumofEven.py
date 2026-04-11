def even(li):
    sum = 0
    for i in li:
        if i%2 == 0:
            sum += i
    print(sum)


li = list(map(int,input("Enter the number : ").split()))

even(li)
