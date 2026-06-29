# file Management

# W -> Write
# file = open("task1.txt","w")
# file.write("Write In File")
# file.close()

# A = Append

# file = open("task1.txt","a")
# file.write("\nApend in file")
# file.close()

# R -> Read

# r = open("task1.txt","r")
# print(r.read())
# r.close()

# W+ -> Write + Read

wr = open("Task2.txt","w+")
wr.write("Write + Read")
wr.seek(0)
print(wr.read())
wr.close()