# list

l = [25,36,20.25,"Python",True,260]
print(l)
print(type(l))
# l.append(200) #single value insert at last
# print(l)
# l.clear()
# print(l)
# l1 = l.copy()
# print(l1)

# l.count(50)
# print(l)

l.extend(["sumit",25,50.36])  #mutiple value can insert
print(l)

l.insert(3,"ABC")# it will insert at spcific index
print(l)

l.pop(3) # it will remove value by default last value if define index than remove that only 
print(l)

l.remove(20.25) # it will remove only spcific value that user mention
print(l)

l.reverse()
print(l)