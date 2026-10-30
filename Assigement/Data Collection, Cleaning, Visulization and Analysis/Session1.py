import numpy as np

# Create a NumPy array called followers using np.array() that stores the follower counts for 5 Instagram influencers: [1200, 15000, 67000, 340000, 1250000]. Print the array, its shape, number of dimensions, and data type.
"""insta = np.array(
    [1200, 15000, 67000, 340000, 1250000]
)

print(insta)
print(insta.shape)
print(insta.ndim)
print(insta.dtype)
"""

# Use np.arange() to generate an array of order IDs for 10 consecutive Zomato orders starting from 101. Print the array and its size.
"""
ids = np.arange(101,111)
print(ids)
print(ids.size)
"""

# Create a 3x3 NumPy array using np.eye() to represent a 'like' identity matrix for a new Spotify playlist feature. Print the matrix and explain what the diagonal values represent in a comment.
"""
spotify = np.eye(3)
print(spotify)

Explanation
np.eye(3) creates a 3 × 3 identity matrix.
The diagonal elements are 1 because each playlist is considered identical to itself (a "like" or self-match).
All non-diagonal elements are 0, representing no direct match between different playlists.
"""

"""
Convert a Python list of cricket scores [45, 67, 120, 89, 54] to a NumPy array, then use the .itemsize attribute to print how many bytes each score takes in memory.<br><br><em><strong>Hint:</strong>
Use np.array() for conversion and .itemsize for memory size.</em>?
"""

cricket_scores = [45, 67, 120, 89, 54]
arr = np.array(cricket_scores)
print(cricket_scores)
print(arr)
print(arr.itemsize)