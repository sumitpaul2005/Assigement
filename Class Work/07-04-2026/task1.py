# DSA -> Data Structure and Algorithm
# l = [10,50,6,60,3,12]
# left = 0
# right = len(l)-1

# while(left<right):
#     l[right],l[left] = l[left],l[right]
#     left += 1
#     right -= 1

# print(l)

# Palindrome

l = [1,2,3,4,3,2,1]
ans = "Yes"
le = 0
r = len(l)-1

while(le<r):
    if l[le] == l[r]:
        le += 1
        r -= 1
        continue
    else:
        ans = "No"
        break
print(ans)