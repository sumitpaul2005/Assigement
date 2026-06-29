# Inheritance

#                                               Single Level

# class A:
#     def fun1(self):
#         print("Method 1 !!")

# class B(A):
#     def fun2(self):
#         print("Method 2 !!")

# obj = B()
# obj.fun1()
# obj.fun2()

#                                                 Multilevel
# class A:
#     def fun1(self):
#         print("Method 1 !!")

# class B(A):
#     def fun2(self):
#         print("Method 2 !!")

# class C(B):
#     def fun3(self):
#         print("Method 3 !!")

# obj = C()
# obj.fun1()

# obj.fun2()
# obj.fun3()

#                                                   Multiple

# class A:
#     def fun1(self):
#         print("Method 1 !!")

# class B:
#     def fun2(self):
#         print("Method 2 !!")

# class C(B,A):
#     def fun3(self):
#         print("Method 3 !!")


# obj = C()
# obj.fun1()
# obj.fun2()
# obj.fun3()

#                                                   Herichical

# class A:
#     def fun1(self):
#         print("Method 1 !!")

# class B(A):
#     def fun2(self):
#         print("Method 2 !!")

# class C(A):
#     def fun3(self):
#         print("Method 3 !!")

# obj1 = B()
# obj2 = C()
# obj1.fun1()
# obj1.fun2()
# obj2.fun3()
# obj2.fun1()

#                                                    Hybrid

class A:
    def fun1(self):
        print("Method 1 !!")

class B(A):
    def fun2(self):
        print("Method 2 !!")

class C:
    def fun3(self):
        print("Method 3 !!")

class D(C,B):
    def fun4(self):
        print("Method 4 !!")

obj = D()
obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()