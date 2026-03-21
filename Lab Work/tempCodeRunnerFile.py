input("Enter a sentence: ")

words = sentence.split()

for i in words:
    count = 0
    for j in words:
        if i == j:
            count = count + 1
    print(i, ":", count)