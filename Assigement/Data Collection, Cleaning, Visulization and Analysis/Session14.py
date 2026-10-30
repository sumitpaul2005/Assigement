import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Q1. Download a small dataset of IPL cricket matches (CSV or Excel), load it into a pandas DataFrame, and perform univariate analysis by printing the summary statistics (mean, median, min, max, std) for the 'total_runs' column.
"""
df = pd.read_csv("IPL Cricket Matches.csv")
print(df)

print(df["total_runs"].describe())
"""
# Q2. Using a dataset of Flipkart product reviews (at least columns: 'rating', 'category'), create a bar plot showing the count of reviews for each rating (1-5 stars) using matplotlib or seaborn.
"""
df = pd.read_csv("flipkart_reviews.csv")

print(df)

rating_count = df["rating"].value_counts().sort_index()

plt.figure(figsize=(8, 5))

sns.barplot(
    x=rating_count.index,
    y=rating_count.values
)

plt.title("Flipkart Reviews by Rating")
plt.xlabel("Rating (Stars)")
plt.ylabel("Number of Reviews")

plt.show()
"""

# Q3. Take a dataset of Zomato restaurant listings (with 'average_cost_for_two' and 'user_rating' columns) and create a scatterplot to visualize the relationship between cost and user rating.<br><br><em><strong>Hint:</strong> Use seaborn's scatterplot() function and label the axes clearly.</em>
"""
df = pd.read_csv("Zomato restaurant listings.csv")
print(df)

sns.set_theme(style="dark")
sns.scatterplot(
    data=df,
    x=df["average_cost_for_two"],
    y=df["user_rating"],
    color="red"
)
plt.title("Average cost for two Vs User rating")
plt.show()
"""

# Q4. For a BookMyShow movie dataset (with 'genre' and 'box_office_collection' columns), use groupby analysis to find the average box office collection for each genre and display the results as a sorted table.
"""
df = pd.read_csv("bookmyshow_movies.csv")
print(df)

result = df.groupby(["genre"])["box_office_collection"].sum().sort_values()
print(result)
"""

# Q5. Use the seaborn 'pairplot' function on a Spotify songs dataset (with at least 'danceability', 'energy', 'valence', and 'popularity' columns) to visualize pairwise relationships between these features. Briefly describe one interesting pattern you observe.

df = pd.read_csv("spotify_songs.csv")
print(df)

sns.pairplot(
    data=df,
    vars=["danceability","energy","valence","popularity"],
    kind="reg"
)
plt.show()