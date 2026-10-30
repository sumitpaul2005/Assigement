def large(l):
   l.sort()
   return l[-2]

lis = list(map(int,input("Enter the number : ").split()))
print(lis)
print("2nd largest number is : ",large(lis))