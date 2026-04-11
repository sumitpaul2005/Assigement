t = (1,2,3,"Hello",1)

print(type(t))
print(t)
print(t.count(1))
print(t.index(3))

l = list(t) # it will convert into list to add or modify the data

l.append(2500)

t1 = tuple(l) # it will convert the list into turple

print(t1)