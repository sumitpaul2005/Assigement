# Python
"""
    1. List : Mutable -> []
    2. Dict : Mutable -> key and value -> {}
    3. Truple : Immutable -> ()
    4. Set : Mutable -> It store Unique elements
    5. String : Immutable
"""
"""
    Libraries : 
        Pandas
        Numpy
        Matplotlib
        Seaborn
"""
# Numpy -> matrix, 1D , 2D , 3D , Broadcasting , Data Analysis , List to convert Array
"""
    Numpy store data hemogeneous
    pip install numpy
"""


import numpy as np

#np.array
"""
a = np.array([1,2,3,4,5,6]) # One Dimensional array

print(a)
print(type(a))  # It will shows Type 
print(a.ndim)   # It shows the type of array

b = np.array([[1,2,3.25,4,5],[6,7,8,9,10]])  # If the data type int,float and string it will convert the values int the higest data type bytes

print(b)
print(type(a))
print(b.ndim)
"""

"""
c = np.array([[1,2,3],[4,5,6]])

# Array Attributes

print(c)
print(c.shape)  # It will shows how many rows and columns
print(c.ndim)   
print(c.size)   # It will shows the total number of value
print(c.itemsize)   # The value returned by itemsize is completely dependent on the data type (dtype) of your array
print(c.nbytes)  # It will show the total number of bytes
"""
"""
d = np.array([
    [
        [1,2,3],[4,5,6]
    ]
])

print(d)
print(d.ndim)
"""

# np.arange() , reshape()

"""
a = np.arange(10)
print(a)

b = np.arange(10,20)    # Start and Stop
print(b)

c = np.arange(1,20,2)   # Start , Stop and Step
print(c)

d = np.arange(1,10,dtype="float")     # it will convert the data type
print(d)

e = np.arange(1,21).reshape(5,4)    # It will convert into array
print(e)

f = np.arange(1,21,2).reshape(2,5)
print(f)

result = np.arange(1,33).reshape(2,2,2,4)
print(result)
print(result.ndim)
"""

# np.zeros(),np.ones(),np.full(),np.linespace() :

a = np.zeros(10,dtype="int").reshape(5,2)
print(a)    # It will shows 0 value and default data type will float

b = np.ones(20) # It will display only one
print(b)

c = np.full(10,fill_value=10)   # It will display the value 10 in 10 times
print(c)

d = np.full_like(a,fill_value=100)
print(d)

arr =np.linspace(1,12,3)  # stop -start /step -1   : 12 -1 / 2
print(arr)