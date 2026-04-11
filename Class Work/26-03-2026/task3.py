s = input("Enter the string : ")
if len(s)%2 == 0:
    print(s)
else:
    mid = len(s)//2
    print(s[mid-1]+s[mid]+s[mid+1])