#                                           Polymorphism

# Method Overriding

# class Myclass:
#     def fun1(self):
#         print("Method 1 !!!")

# class Myclass1(Myclass):
#     def fun1(self):
#         super().fun1()
#         print("Method 2 !!!")

# obj = Myclass1()
# obj.fun1()


#                                       Multilevel

# class Myclass:
#     def fun1(self):
#         super().fun1()
#         print("Method 1 !!!")

# class Myclass1:
#     def fun1(self):
#         print("Method 2 !!!")

# class Myclass2(Myclass,Myclass1):
#     def fun1(self):
#         super().fun1()
#         print("Method 3 !!!")

# obj = Myclass2()
# obj.fun1()

class A:
    def fun1(self):
        
        print("Method 1 !!!")

class B(A):
    def fun1(self):
        super().fun1()
        print("Method 2 !!!")
    
class C:
    def fun1(self):
        super().fun1()
        print("Method 3 !!!")

class D(C,B):
    def fun1(self):
        super().fun1()
        print("Method 4 !!!")

o = D()
o.fun1()