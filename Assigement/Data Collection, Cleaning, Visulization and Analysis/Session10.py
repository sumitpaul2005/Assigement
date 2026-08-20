import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Q1. Install Matplotlib in your Python environment and create a simple line plot showing the number of daily steps you took over the last 7 days. Save the chart as steps_lineplot.png.
"""
df = pd.DataFrame(
    {
        "days" : [
    "Day 1", "Day 2", "Day 3", "Day 4", "Day 5",
    "Day 6", "Day 7", "Day 8", "Day 9", "Day 10",
    "Day 11", "Day 12", "Day 13", "Day 14", "Day 15",
    "Day 16", "Day 17", "Day 18", "Day 19", "Day 20"
],

    "steps" : [
    4500, 6200, 7100, 5800, 8300,
    9200, 7600, 6800, 10500, 8900,
    5400, 7300, 8100, 9600, 6700,
    11200, 8500, 7900, 10100, 9300
]
    }
)
print(df)

df = df.tail(7)
plt.plot(
    df["days"],df["steps"],color="red",linestyle="-"
)
plt.title("Last 7 days steps count")
plt.xlabel("Days")
plt.ylabel("Steps")
plt.legend(labels=["Steps"],loc="upper right")

for i,j in enumerate(df["steps"]):
    plt.text(
        i,j,f"{j:.2f}",ha="center"
    )
    
plt.savefig("steps_lineplot.png")
plt.show()
"""

# Q2. Using Matplotlib, create a scatter plot of 10 restaurants from your city with their Zomato ratings on the x-axis and average meal price on the y-axis. Add axis labels and a title to the chart.
"""
df = pd.DataFrame({
    "restaurant": [
        "Restaurant 1", "Restaurant 2", "Restaurant 3",
        "Restaurant 4", "Restaurant 5", "Restaurant 6",
        "Restaurant 7", "Restaurant 8", "Restaurant 9",
        "Restaurant 10"
    ],
    "rating": [3.8, 4.2, 4.5, 3.6, 4.0, 4.3, 3.9, 4.6, 4.1, 3.7],
    "avg_meal_price": [300, 450, 700, 250, 500, 650, 350, 800, 550, 280]
})

print(df)

plt.scatter(
    df["rating"],df["avg_meal_price"],color="green",alpha=0.5
)
plt.title("Rating and Avg Meal Price")
plt.xlabel("Rating")
plt.ylabel("Avg_meal_price")
plt.legend(labels=["Avg_Meal_Price"])

for i,j in zip(df["rating"],df["avg_meal_price"]):
    plt.text(
        i,j+6,f"{j:.2f}",color="Red",ha="center"
    )
plt.show()
"""

# Q3. Build a bar chart that shows the number of orders you or your friends placed on Swiggy, Zomato, and Domino’s in the last month. Use different colors for each bar and add a legend.
"""
df = pd.DataFrame(
    {
    "Platform": [
        "Swiggy", "Zomato", "Domino's", "McDonald's",
        "KFC", "Burger King", "Pizza Hut", "EatSure",
        "Swiggy", "Zomato", "Domino's", "McDonald's",
        "KFC", "Burger King", "Pizza Hut", "EatSure",
        "Swiggy", "Zomato", "Domino's", "KFC"
    ],
    "Orders": [
        12, 8, 5, 10,
        7, 6, 9, 4,
        15, 11, 7, 13,
        8, 5, 10, 6,
        14, 9, 8, 11
    ]
}
)
print(df)
data = df[df["Platform"].isin(["Swiggy", "Zomato", "Domino's"])]
result = data.groupby("Platform")["Orders"].sum()
print(result)
plt.bar(
    result.index,result.values,align="center",color=["red","blue","green"]
)
plt.title("Swiggy, Zomato, and Domino’s in the last month")
plt.xlabel("Platform")
plt.ylabel("Orders")
plt.grid()

for i,j in enumerate(result):
    plt.text(
        i,j,f"{j:.2f}",color="black",ha="center",fontsize=20
    )
plt.show()
"""

# Q4. Create a histogram of the durations (in minutes) of your last 20 Spotify listening sessions using Matplotlib. Set the number of bins to 5 and customize the color of the bars.
"""
df = pd.DataFrame({
    "Song_Name": [
        "Shape of You",
        "Believer",
        "Perfect",
        "Blinding Lights",
        "Heat Waves",
        "Faded",
        "Stay",
        "Havana",
        "Levitating",
        "Senorita",
        "Closer",
        "Attention",
        "Memories",
        "Counting Stars",
        "Cheap Thrills",
        "Lovely",
        "Despacito",
        "Let Me Love You",
        "Peaches",
        "Photograph"
    ],
    "Duration": [
        25, 40, 35, 60, 45,
        30, 55, 70, 20, 50,
        65, 35, 40, 80, 25,
        45, 55, 30, 75, 50
    ]
})

print(df)

plt.hist(
    df["Duration"],bins=5,color="red",histtype="bar",edgecolor="black"
)
plt.title("Spotify Listening Session Durations")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Sessions")
plt.show()
"""

# Q5. Customize a Matplotlib figure by creating a plot with two subplots: one line plot showing your daily Instagram screen time for a week, and one bar chart showing the number of posts you liked each day. Add appropriate titles, axis labels, and save the figure as social_media_usage.png.<br><br><em><strong>Hint:</strong> Use plt.subplots() to create multiple axes in one figure.</em>

df = pd.DataFrame(
    {
        "days" : ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "screen_time" : [2.5, 3, 2, 4, 3.5, 5, 4.5],
        "liked_posts" : [20, 25, 18, 30, 22, 35, 28]
    }
)
print(df)
plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.plot(
    df["days"],df["screen_time"]
)

for i,j in zip(df["days"],df["screen_time"]):
    plt.text(
        i,j,f"{j:.2f}",ha="center"
    )
    
plt.title("Daily Screen Time")
plt.xlabel("Days")
plt.ylabel("Screen Time")

plt.subplot(2,2,2)
plt.bar(
    df["days"],df["liked_posts"],width=0.5,align="center",color="green"
)

for i,j in enumerate(df["liked_posts"]):
    plt.text(
        i,j,f"{j:.2f}",ha="center"
    )
    
plt.title("Daily Liked Posts")
plt.xlabel("Days")
plt.ylabel("Liked Posts")

plt.show()