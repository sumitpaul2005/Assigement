# Dictionary 
# Collection of data but store in key and values pair key must be unique.
# It is mutable
# It is denoted by {} curly braces
# key + value = Item
# 1:"A"

d = {1:"A",2:"B",3:"Hello"}
print(d)
print(d.get(3))# it will shows key values
print(d.keys()) # it will shows all key 
print(d.values()) # it will shows all values
print(d.items()) # it will shows all dictionary values and keys

d.pop(2) # it will remove specified keys values
print(d)

d.popitem() #it will remove by default last data
print(d)

d.update({4:"Sumit"}) # it will update data
print(d)

t = (1,2,3,4)
dic = {}
print(dic.fromkeys(t)) # it will define keys
print(dic.fromkeys(t,20)) # it will define all keys value 20