import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Q1. Install Seaborn in your Python environment and use it to create a histplot showing the distribution of delivery times (in minutes) for 50 Zomato food orders. Generate random data if needed.
"""
df = pd.DataFrame(
    {"FoodName": [
        "Pizza", "Burger", "Biryani", "Dosa", "Pasta",
        "Sandwich", "Noodles", "Paneer Tikka", "Thali", "Momos",
        "Pizza", "Burger", "Biryani", "Dosa", "Pasta",
        "Sandwich", "Noodles", "Paneer Tikka", "Thali", "Momos",
        "Pizza", "Burger", "Biryani", "Dosa", "Pasta",
        "Sandwich", "Noodles", "Paneer Tikka", "Thali", "Momos",
        "Pizza", "Burger", "Biryani", "Dosa", "Pasta",
        "Sandwich", "Noodles", "Paneer Tikka", "Thali", "Momos",
        "Pizza", "Burger", "Biryani", "Dosa", "Pasta",
        "Sandwich", "Noodles", "Paneer Tikka", "Thali", "Momos"
    ],

    "DeliveryTime": [
        25, 32, 45, 28, 38,
        22, 35, 42, 50, 30,
        27, 40, 48, 25, 36,
        20, 33, 44, 55, 31,
        29, 37, 46, 26, 39,
        24, 34, 41, 52, 30,
        28, 35, 49, 27, 43,
        21, 32, 47, 58, 29,
        26, 39, 45, 24, 37,
        23, 36, 51, 33, 42
    ]}
)
print(df)
sns.set_theme(style="darkgrid")
sns.histplot(
    data=df,
    x="DeliveryTime",
    kde=True,
    bins=10,
    color="red"
)
plt.title("Delivery Time")
plt.show()
"""

# Q2. Load the 'tips' dataset from Seaborn and create a boxplot to visualize the distribution of total bill amounts by day of the week, similar to how Zomato might analyze spending patterns across weekdays.
"""
df = sns.load_dataset("tips")
print(df)

sns.set_theme(style="dark")
sns.boxplot(
    data=df,
    x="day",
    y="total_bill"
)
plt.title("Total bill by Days")
plt.show()
"""

# Q3. Simulate IPL match scores for 8 teams and use a violinplot to compare the run distributions per team. Style your plot using the 'darkgrid' Seaborn theme.
"""
df = pd.read_csv("IPL player stats.csv")
df = df.sort_values(["Runs"]).head(8)
print(df)

sns.set_theme(style="darkgrid")
sns.violinplot(
    data=df,
    x="Team",
    y="Runs"
)
plt.show()
"""

# Q4. Create a countplot that displays the number of songs per genre from a list of 40 Spotify tracks, with at least 4 different genres represented.<br><br><em><strong>Hint:</strong> Use a Python list or pandas DataFrame to store your data, then plot with Seaborn.</em>
"""
df = pd.DataFrame(
    {
        "SongName": [
        "Blinding Lights", "Shape of You", "Levitating", "Stay",
        "Perfect", "As It Was", "Flowers", "Havana",
        "Believer", "Thunder", "Enemy", "Radioactive",
        "One Dance", "God's Plan", "Starboy", "Peaches",
        "Bad Guy", "Lovely", "Ocean Eyes", "Therefore I Am",
        "Despacito", "Taki Taki", "Bailando", "Hips Don't Lie",
        "Bohemian Rhapsody", "Hotel California", "Dream On", "Sweet Child O Mine",
        "Lose Yourself", "Godzilla", "Mockingbird", "Without Me",
        "Someone Like You", "Hello", "Rolling in the Deep", "Easy On Me",
        "Closer", "Something Just Like This", "Don't Start Now", "New Rules"
    ],

    "Genre": [
        "Pop", "Pop", "Pop", "Pop", "Pop",
        "Pop", "Pop", "Pop", "Rock", "Rock",
        "Rock", "Rock", "Hip-Hop", "Hip-Hop", "Hip-Hop",
        "Hip-Hop", "R&B", "R&B", "R&B", "R&B",
        "Latin", "Latin", "Latin", "Latin", "Rock",
        "Rock", "Rock", "Rock", "Hip-Hop", "Hip-Hop",
        "Hip-Hop", "Hip-Hop", "R&B", "R&B", "R&B", "R&B",
        "Electronic", "Electronic", "Electronic", "Electronic"
    ]
    }
)

print(df)

sns.set_theme(style="ticks")
sns.countplot(
    data=df,
    x="Genre",
    color="red"
)
plt.title("Number of Spotify Songs per Genre")
plt.show()
"""
# Q5. Use Seaborn's kdeplot to visualize the distribution of daily step counts for a week, as if analyzing data from a fitness app. Apply the 'whitegrid' theme and customize the plot color.

df = pd.DataFrame(
    {
        "Day": [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ],
    "Steps": [
        6500, 8200, 7400, 9100, 6800, 10500, 7800
    ]
    }
)
print(df)

sns.set_theme(style="whitegrid")
sns.kdeplot(
    data=df,
    x="Steps",
    fill=True,
    color="green"
)
plt.title("Daily step counts")
plt.show()