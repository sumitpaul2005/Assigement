def func(n):
    digit = 0
    space = 0
    letter = 0
    c = n.lower()
    for i in c:
        if i.isalpha():
            letter += 1
        elif i.isnumeric():
            digit += 1
        elif i.isspace():
            space += 1
    print("Letter : ",letter)
    print("Digit : ",digit)
    print("Space : ",space)

n = input("Enter the string : ")
func(n)
