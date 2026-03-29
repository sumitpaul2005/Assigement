sent = input("Enter the String : ")
word = sent.strip().lower().split()
# print(word.count("is"))
for i in word:
    print(word[i].count(i))
        