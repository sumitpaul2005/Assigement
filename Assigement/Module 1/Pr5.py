str = input("Enter the string: ")

if len(str) < 3:
    print(str)

elif str.endswith("ing"):
    str = str + "ly"
    print(str)

else:
    str += "ing"
    print(str)