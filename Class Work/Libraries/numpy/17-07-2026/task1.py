"""
1. maths : + - * / 
2. stats function  : mean , std , var , sum , max , min , argmax , argmin ,
3. linear algebra  : inv , det ,T 
4.random  module  
5.matrix multiplication
7. flattern ,ravel 
"""

import numpy as np

# math function -> + , - , * , / , %

"""
a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

b = np.array([
    [10,11,12],
    [14,15,16],
    [17,18,19]
])

print(a)
print(b)
print("Addition : \n",a + b)
print("Substraction : \n",a - b)
print("Division : \n",a / b)
print("Reminder : \n",a % b)
print("Multiplication : \n",a * b)
"""

# matrix  multiplication : np.matmul,np.dot ,a@b 
"""
a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

b = np.array([
    [10,11,12],
    [14,15,16],
    [17,18,19]
])

print(np.matmul(a,b))
print(np.dot(a,b))
print(a@b)
"""

# ex :  
"""
a = np.array([
    [1,2,3],
])
b=np.array([
    [6,7,8],
    [9,10,11],
    [12,13,14]
])

print(a@b) #  it can be not possible when A -> 3x1 b -> 3x3 but it possible when A -> 1x3 B -> 3x3 coloumn should be same  
"""

# indetity matrix , transpose matrix
"""
a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(np.identity(3))  # it will put 1 when the number are same (1,1) (2,2) (0,0)
print(np.transpose(a))  # it will swap the row into column and column into row
"""

# stats function  : mean , std , var , sum , max , min , argmax , argmin
"""
a=np.array([
    [6,7,8],
    [9,4,11],
    [12,13,14]
]) 

print("Mean : \n",a.mean())
print("Median : \n",np.median(a))
print("Standard divation : \n",a.std())
print("Var :\n",a.var())

print(a.sum())
print(a.sum(axis=0))  # sum  of col wise 
print(a.sum(axis=1))  # sum  of row wise

print(a.max())
print(a.max(axis=0))  # max  of col wise
print(a.max(axis=1))  # max  of row wise

print(a.argmax())
print(a.argmax(axis=0))  # argmax  of col wise  ===> max value index 
print(a.argmax(axis=1))  # argmax  of row wise

print(a.min())
print(a.min(axis=0))  # min  of col wise
print(a.min(axis=1))  # min  of row wise

print(a.argmin())
print(a.argmin(axis=0))  # argmin  of col wise  ===> min value index 
print(a.argmin(axis=1))  # argmin  of row wise
"""

# linalg : 
"""
a=np.array([
    [6,7,8],
    [9,4,11],
    [12,13,14]
]) 

result =np.linalg.det(a)
result =np.linalg.inv(a)
print(result)
"""

# random  module  : 

import random
"""
a = np.random.random((3,3))
a = np.random.randint(low=1 , high=10, size=(4,3))
ar = np.random.sample(6)   # it will create unique number between 0 to 1
print(ar)
"""

# shallow copy  :   It will change the original value also, it share the address
"""
l1 =[1,2,34,56,78]

l2 = l1
l2[3] = 99

print("l1 = \n",l1)
print("l2 = \n",l2)

# Deep copy : it will create copy the elements

l1 =[1,2,34,56,78]

l2 = l1.copy()
l2[3] = 99

print("l1 = \n",l1)
print("l2 = \n",l2)
"""

# flatten  :  convert any demensional array to 1d array.  it is called Deep copy

a=np.array([
    [6,7,8],
    [9,4,11],
    [12,13,14]
])   
f_array=a.flatten()

f_array[2]=99

print("original array :-\n",a)
print("flattern array :-\n",f_array)

"""
# ravel :  convert any demensional array to 1d array. shallow copy
a=np.array([
    [6,7,8],
    [9,4,11],
    [12,13,14]
])   
r_array=a.ravel()

r_array[2]=99

print("original array :-\n",a)
print("ravel array :-\n",r_array)"""