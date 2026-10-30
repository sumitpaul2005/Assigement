# 2.Write a program in Python that asks 2 strings from the user and interchanges first 3 characters 
# of both the strings.
# eg:
# input strings:
# color
# full
# Output:
# fulor
# coll

s1 = input("Enter the String : ")
s2 = input("Enter the String : ")

str1 = s2[:3] + s1[3:]
str2 = s1[:3] + s2[3:]

print(str1)
print(str2)
