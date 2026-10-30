n = int(input("Enter the length of dictionary : "))

if n < 3:
    print("Please enter more than 3 length")
else:
    dic = {}

    for i in range(1,n+1):
        k = input("Enter the key : ")
        v = int(input("Enter the value : "))
        dic[k] = v

    print("Dictionary : ",dic)
    lis = list(dic.items())

    for i in range(len(lis)):
        for j in range(i+1,len(lis)):
            if lis[i][1] < lis[j][1]:
                lis[i] , lis[j] = lis[j] , lis[i]

    Asc = {}

    for k,v in lis:
        Asc[k] = v

    print("Acesending order : ",Asc)

    last3 = list(Asc.items())

    print(last3[:3])