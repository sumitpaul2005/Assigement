# Operator Overloading

class User:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("Constructor Calling")

    def __str__(self):  # it will always return value, if don't retrun then write "".
        return f"{self.a},{self.b}"
    
    def __add__(self, other):  # it will Add the obj
        x = self.a + other.a
        y = self.b + other.b
        return x,y
    
o = User(10,20)
print(o) # it will call str

o1 = User(20,30)
print(o1)
print("Addition : ",o+o1)