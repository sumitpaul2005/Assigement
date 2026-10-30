str1 = input("Enter the 1st sentence: ")
str2 = input("Enter the 2nd sentence: ")

a = ""
b = ""

print("Before swaping: ",str1,str2)

a = str2[:2] + str1[2:]
b = str1[:2] + str2[2:]

print("After swaping: ",a,b)