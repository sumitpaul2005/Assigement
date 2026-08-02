"""
task :1 take a 2d array 5*5 all element are 1 . and  print  like  this  .
hint  : use  np.ones () , slicing  ,  fancy indexing
input  : 
1 1 1 1 1 
1 1 1 1 1 
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1

output :
1 1 1 1 1 
1 0 0 0 1 
1 0 9 0 1
1 0 0 0 1
1 1 1 1 1.
"""

import numpy as np
"""
arr = np.ones(25,dtype="int").reshape(5,5)
print(arr)

a = arr.flatten().reshape(5,5)
a[1:4:2,1:4] = 0
a[2:3,1:4:2] = 0
a[2:3,2:3] = 9
print(a)
"""

"""task :2 take a 2d array 5*5  . and  print  like  this  .

input  : 
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

output  : [[4,5],
            [19,20],
            [24,25]]"""

# arr = np.array([
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],
#     [16,17,18,19,20],
#     [21,22,23,24,25]
# ])

# print(arr[[0,3,4],3:])
"""
task :3 take a 2d array 5*5  . and  print  like  this  .

input  : 
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

output   : [[8,9],
            [17,18]]

"""

arr = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
])

result = np.array([
    arr[1,2:4],
    arr[3,1:3]
])
print(result)