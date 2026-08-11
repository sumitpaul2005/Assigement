import pandas as pd
import numpy as np

"""
Q1. Download a sample CSV file of IPL player stats (include columns like player name, runs, matches, 
and some missing values). Load it into a pandas DataFrame and use isnull() and notnull() to print how 
many missing values are present in each column.
"""

# df = pd.read_csv("IPL player stats.csv",sep=",")
# print(df)
# print(df.isnull())
# print(df.notnull())

"""
Q2. Using the loaded IPL player stats DataFrame, apply dropna(axis=0, how='any') to remove all rows with 
any missing data and display the shape of the DataFrame before and after dropping.
"""

# df = df.dropna(axis=0, how="any")
# print(df)

"""
Q3. For the 'runs' column in your IPL player stats DataFrame, use fillna() to replace missing values with 
the mean of the column. Print the updated column to verify the changes.
"""

# df = df.fillna(df[["Runs"]].mean().astype(int))
# print(df)

"""
Q4. Simulate a Zomato-style restaurant ratings dataset with some missing ratings. Use forward fill 
(method='ffill') to fill missing values in the ratings column, then use backward fill (method='bfill') 
for any remaining missing values. Show the before and after results.
"""

df = pd.DataFrame({
    "Restaurant": [
        "Spice Villa",
        "Burger Hub",
        "Pizza Point",
        "Food Palace",
        "Tandoori House",
        "Cafe Delight",
        "BBQ Nation",
        "South Express",
        "Chinese Corner",
        "Royal Biryani"
    ],
    "rating": [4.5, np.nan, 4.2, np.nan, np.nan, 4.8, 4.6, np.nan, 4.1, np.nan]
})
print(df)
# df["rating"] = df["rating"].ffill()
# print(df)
df["rating"] = df["rating"].bfill()
print(df)


"""
Q4. Pick any one column with missing values from your dataset and explain which missingness mechanism 
(MCAR, MAR, or MNAR) is most likely and why, using 2-3 sentences.<br><br><em><strong>Hint:</strong> 
Think about whether the missing data is random or related to other factors in the dataset.</em>


**Example Answer (Using the `Rating` column):**

The missing values in the **`Rating`** column are most likely **MAR (Missing At Random)**. The missing ratings may depend on another variable in the dataset, such as whether a restaurant is new or has received only a few customer reviews, rather than on the rating value itself. Therefore, the missingness is related to other observed factors and not completely random.
"""