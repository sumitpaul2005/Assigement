s = "Java is best Programming"
print(s[4:18:3])

# Find Palindrome or not

n = input("Enter the string : ")

if n == n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")