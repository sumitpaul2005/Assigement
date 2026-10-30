n = int(input("Enter the length of list : "))
list_truple = []

for i in range(1,n+1):
    str = input("Enter the Key : ")
    value = int(input("Enter the value : "))
    list_truple.append((str,value))

print("List of turple : ",list_truple)

dictionary = dict(list_truple)

print("Dictionary is : ",dictionary)