# Abstraction
# It means hinding some data

from abc import ABC  # abc class from ABC library

class Emp(ABC): # Abstract Class 
    def sal(self):  # Abstract method
        pass

class Emp2(Emp):
    def sal(self):
        return 5000
    
class Emp3(Emp):
    def sal(self):
        return 4000
    
o = Emp2()
print(o.sal())

o1 = Emp3()
print(o1.sal())