import numpy as np
import random 

# Create two NumPy arrays representing the daily step counts of two friends over a week and use element-wise addition, subtraction, 
# multiplication, and division to compare their activity levels.
"""
friend1 = np.array([7500, 8200, 9000, 6800, 10000, 7900, 8500])
friend2 = np.array([8000, 6500, 7800, 3600, 5600, 2300, 5000])

print("Friend 1 Array : ",friend1)
print("Friend 2 Array : ",friend2)

print("Addition : ",friend1+friend2)
print("Subtraction : ",friend1-friend2)
print("Multiplication : ",friend1*friend2)
print("Division : ",friend1/friend2)
"""

# Simulate a Spotify-like 'Recommended Songs' feature: Given two 3x3 matrices representing user-song interaction scores (user preferences 
# and song popularity), use dot() and matmul() to compute the final recommendation matrix and explain the difference between the two 
# results.
"""
song1 = np.random.randint(low=1,high=10,size=(3,3))
song2 = np.random.randint(low=1,high=10,size=(3,3))

print(song1)
print(song2)

print("Matrix Multiplication : ",np.dot(song1,song2))
print("Matrix Multiplication : ",np.matmul(song1,song2))

Difference between dot() and matmul()

np.dot()	                                                                np.matmul()
General-purpose dot product function.	                                    Specifically designed for matrix multiplication.
Works with 1D, 2D, and higher-dimensional arrays.	                        Uses the @ operator and follows matrix multiplication rules.
For 2D arrays, it performs standard matrix multiplication.	                For 2D arrays, it gives the same result as dot().
Behavior differs for arrays with more than 2 dimensions.	                Supports broadcasting for stacks of matrices, making it
"""


# Given a 4x4 NumPy matrix representing the pixel brightness of a small Instagram image, use transpose (T) to rotate the image and then 
# calculate the mean, median, standard deviation, and variance of the pixel values.
"""
arr = np.random.randint(low=100,high=1000,size=(4,4))
print(arr)

print("Mean : ",np.mean(arr))
print("Median : ",np.median(arr))
print("Standard Deviation : ",np.std(arr))
print("Variance : ",np.var(arr))
"""


# Take a 3x3 NumPy matrix representing a Zomato restaurant rating correlation grid and use np.linalg.inv(), np.linalg.det(), and 
# np.linalg.eig() to compute its inverse, determinant, and eigenvalues/eigenvectors.<br><br><em><strong>Hint:</strong> 
# If the matrix is not invertible, modify one value and try again.</em>
"""
rating = np.random.randint(low=0,high=10,size=(3,3))

print(rating)
print("Inverse : ",np.linalg.inv(rating))
print("Determinant : ",np.linalg.det(rating))
print("Eigenvalues : ",np.linalg.eig(rating))
"""

# Create a NumPy array of shape (2, 6) representing the number of orders placed on Swiggy in two cities over 6 days. 
# Reshape it to (3, 4), flatten it, split it into two equal parts, and then stack both parts vertically.

order = np.random.randint(low=20,high=33,size=(2,6))
print("Old Order : ",order)
new = order.reshape(3,4)
print("New Order : ",new)

fl = new.flatten()
fl[2] = 50
print("Flatten : ",fl)

spl1,spl2 = np.split(fl,2)
print("Split 1 : ",spl1)
print("Split 2 : ",spl2)

v = np.vstack((spl1,spl2))
print("Vertically : ",v)