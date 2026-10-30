import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("pandas\movies.csv")
df = df.drop(columns=["Unnamed: 0"])
print(df)

# Box plot
"""
box = plt.boxplot(df['budget'])
plt.title("Budget Outlier")
plt.show()
"""

# Pie chart
"""
df = df.head(10)
p = plt.pie(
    df['vote_average'],
    labels=df['title'],
    autopct='1%.1f%%'
)
plt.title("Vote Average")
plt.show()
"""

# Line plot
"""
df = df.head(10)
line = plt.plot(
    df['title'],
    df['revenue'],
    color = 'red'
)
plt.title("Revenue Of Movie")
plt.legend(labels=["Revenue"],loc = 'upper right')
plt.xlabel('Title')
plt.ylabel('Revenue')
plt.show()
"""

# Scatter plot
"""
df = df.head(10)
t = df["title"]
p = df["popularity"]
s = plt.scatter(
    t,p,
    color="red"
)
for i in range(len(p)):
    plt.text(
        t[i],
        p[i]+1,
        str(p[i]),
        ha = "center",
        color = "black",
        fontsize=10
    )
plt.title("Movies and Popularity")
plt.xlabel('Title')
plt.ylabel('Popularity')
plt.show()
"""

# Bar Plot
"""
df = df.head(10)
t = df['title']
vote = df["vote_count"]

bar = plt.bar(
    t,
    vote,
    align = "center",
    color = "red",
    alpha = 0.5,
    width=0.5
)

for i in bar:
    plt.text(
        i.get_x() + i.get_width()/2,
        i.get_height() + 1,
        i.get_height(),
        ha = "center",
        color = "blue",
        fontsize = 12
    )

plt.title("Title and Vote count")
plt.legend(labels=['Vote_Count'],loc = "upper right")
plt.ylabel('Vote Count')
plt.xlabel("Id")
plt.show()
"""

# Subplot

