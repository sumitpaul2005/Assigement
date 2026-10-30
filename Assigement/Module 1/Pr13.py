n = int(input("Enter the length of dictionary : "))
dictionary = {}
for i in range(1,n+1):
    k = input("Enter the key : ")
    v = int(input("Enter the values : "))
    dictionary[k] = v

print("Dictionary : ",dictionary)
Acs = {}
Desc = {}
lis = list(dictionary.items())

for i in range(0,len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i][1] > lis[j][1]:
            lis[i], lis[j] = lis[j] , lis[i]

for k,v in lis:
    Acs[k] = v

print("Acsending order : ",Acs)

for i in range(0,len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i][1] < lis[j][1]:
            lis[i], lis[j] = lis[j] , lis[i]

for k,v in lis:
    Desc[k] = v

print("Descending order : ",Desc)