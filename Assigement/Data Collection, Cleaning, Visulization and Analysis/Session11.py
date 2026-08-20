import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Q1. Use plt.subplots() to create a 2x2 grid of subplots and plot four different types of charts (line, bar, scatter, and pie) using any sample data of your choice.
"""
df = pd.read_csv("swiggy_orders.csv")
print(df)

cus1 = df.groupby(["customer_name"])["delivery_time"].sum().sort_values(ascending=False)
cus2 = df.groupby(["customer_name"])["rating"].sum().sort_values(ascending=False)
cus3 = df.groupby(["customer_name"])["quantity"].sum().sort_values(ascending=False)
cus4 = df.groupby(["delivery_time"])["quantity"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,15))

plt.subplot(2,2,1)
plt.bar(
    cus1.index,cus1
)
plt.title("Customer Name Vs Delivery Time")
plt.xlabel("Customer Name")
plt.ylabel("Delivery time")
plt.xticks(rotation=90)

plt.subplot(2,2,2)
plt.scatter(
    cus2.index,cus2
)
plt.title("Customer Name Vs Rating")
plt.xlabel("Customer Name")
plt.ylabel("Rating")
plt.xticks(rotation=90)

plt.subplot(2,2,3)
plt.plot(
    cus3.index,cus3
)
plt.title("Customer Name Vs Payment")
plt.xlabel("Customer Name")
plt.ylabel("Payment Method")
plt.xticks(rotation=90)

plt.subplot(2,2,4)
plt.pie(
    cus4.values,labels=cus4.index,autopct="%1.1f%%",radius=1.5
)

plt.subplots_adjust(hspace=0.5, wspace=0.4)
plt.show()
"""

# Q2. Plot a comparison of average delivery times for Zomato, Swiggy, and Domino's using a bar chart, and style each bar with a different color, linestyle, and linewidth using Matplotlib plot styling options.
"""
df = pd.read_csv("food_delivery_30.csv")

avg = df.groupby(["Platform"])["Delivery_Time"].mean()
print(avg)

plt.bar(
    avg.index,avg,color=["red","blue","yellow"]
)
plt.title("Average Delivery time")
plt.xlabel("Platform name")
plt.ylabel("Average time")
plt.show()
"""

# Q3. Create a multi-axis chart that shows the number of Instagram followers (left y-axis) and average daily posts (right y-axis) for five influencers. Use different colors and markers for each axis.
"""
df = pd.DataFrame(
    {
        "influencers" : ["Aisha", "Rahul", "Priya", "Arjun", "Neha"],

        "followers" : [1200000, 850000, 1500000, 650000, 1000000],
        "daily_posts" : [3.2, 2.5, 4.1, 1.8, 3.5]
    }
)

print(df)
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(
    df["influencers"],
    df["followers"],
    color="blue",
    marker="o",
    linestyle="-",
    linewidth=2,
    markersize=8,
    label="Followers"
)

ax1.set_xlabel("Influencers")
ax1.set_ylabel("Number of Followers", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

ax2 = ax1.twinx()

ax2.plot(
    df["influencers"],
    df["daily_posts"],
    color="red",
    marker="s",
    linestyle="--",
    linewidth=2,
    markersize=8,
    label="Average Daily Posts"
)


ax2.set_ylabel("Average Daily Posts", color="red")
ax2.tick_params(axis="y", labelcolor="red")

plt.title("Instagram Followers vs Average Daily Posts")

ax1.grid(axis="x", linestyle=":", alpha=0.5)

plt.tight_layout()
plt.show()
"""

# Q4. Plot the number of tickets sold for five recent Bollywood movies (categorical) versus their IMDB ratings (numeric) using a scatter plot. Add annotations to display the movie names above each point.
"""
df = pd.read_csv("MoviesIMBD.csv")

result = df.groupby("Movie").agg({
    "Ticket_Sold": "sum",
    "IMDB_Rating": "mean"
}).reset_index()

print(result)

plt.figure(figsize=(10, 6))

plt.scatter(
    result["Ticket_Sold"],
    result["IMDB_Rating"],
    color="red",
    alpha=0.5,
    s=100
)

for i, row in result.iterrows():

    plt.annotate(
        row["Movie"],
        (row["Ticket_Sold"], row["IMDB_Rating"]),
        xytext=(0, 10),
        textcoords="offset points",
        ha="center"
    )

plt.title("Movie Ticket Sales vs IMDb Rating")
plt.xlabel("Total Tickets Sold")
plt.ylabel("Average IMDb Rating")

plt.grid(True)

plt.tight_layout()
plt.show()
"""

# Q5. Add a custom text annotation to a Matplotlib chart showing Flipkart's monthly sales, marking the highest sales point with the label 'Big Billion Days'.<br><br><em><strong>Hint:</strong> Use the ax.annotate() function to place the label at the correct data point.</em>

df = pd.DataFrame({
    "Month": [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ],
    "Sales": [
        45000, 48000, 52000, 50000, 55000, 58000,
        60000, 62000, 68000, 125000, 75000, 70000
    ]
}
)

print(df)

max_index = df["Sales"].idxmax()
max_month = df.loc[max_index, "Month"]
max_sales = df.loc[max_index, "Sales"]

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(
    df["Month"],
    df["Sales"],
    marker="o",
    linewidth=2
)

ax.annotate(
    "Big Billion Days",
    xy=(max_month, max_sales),
    xytext=(max_month, max_sales + 15000),
    arrowprops=dict(
        arrowstyle="->",
        linewidth=2
    ),
    fontsize=12,
    fontweight="bold"
)

ax.set_title("Flipkart Monthly Sales")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")

ax.grid(
    True,
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()
plt.show()