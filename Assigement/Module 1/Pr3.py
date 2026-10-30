sent = input("Enter the String : ")
word = sent.strip().lower().split()
f = {}

for i in word:
    if i in f:
        f[i] += 1
    else:
        f[i] = 1
        
for i, count in f.items():
    if count > 1:
        print(i," : ",count)
    else:
        print(i," : ",count)