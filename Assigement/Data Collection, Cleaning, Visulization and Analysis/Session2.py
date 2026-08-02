import numpy as np

# Create a 2D NumPy array representing the ratings (out of 5) given by 4 users to 5 different food items on Zomato. 
# Use slicing to extract the ratings given by the second and third users only.
"""
rating = np.array([
    [5,3,2,4,1],
    [3,2,5,4,2],
    [1,2,3,4,5],
    [5,4,3,2,1]
])

print(rating)
print(rating.shape)
print(rating[1:3])
"""

# Given a NumPy array of daily steps tracked for 10 days, use boolean indexing to select only the days where the steps were greater than 8000.
# <br><br><em><strong>Hint:</strong> Use an array like steps = np.array([7500, 8200, 9000, ...]) and apply a boolean condition.</em>
"""
days_step = np.array([7500, 8200, 9000, 6800, 10000, 7900, 8500, 7200, 9500, 8100])
print(days_step)
greater = days_step[days_step > 8000]
print(greater)
"""

# Create a NumPy array of IPL team scores for 8 matches. Use fancy indexing to select the scores from matches 2, 5, and 7, and print them.
"""
scores = np.array([60,102,105,110,200,206,250,270])
print(scores)
print(scores[[1,4,6]])
"""

# Suppose you have a NumPy array of product prices from Flipkart. Use broadcasting to apply a 10% discount to all prices and 
# print the new array.<br><br><em><strong>Constraint:</strong> Do not use any loops.</em>
"""
price = np.array([7500, 8200, 9000, 6800, 10000, 7900, 8500, 7200, 9500, 8100])

print(price)

discount = price * 0.1
new_price = price - discount

print(new_price)
"""

# Given a NumPy array of user ratings (can be negative, zero, or positive) for songs on Spotify, use boolean masking to
# set all negative ratings to zero, keeping other ratings unchanged.

rating = np.array([
    [0,3,2,-4,1],
    [3,2,5,4,2],
    [-1,2,3,4,-5],
    [5,4,-3,2,0]
])

print(rating)

new = np.where(rating > 0,rating,0) 
print(new)