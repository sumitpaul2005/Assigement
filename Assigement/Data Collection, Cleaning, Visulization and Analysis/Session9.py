import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Q1. Given a list of delivery timestamps as strings (e.g., ['2024-06-01 14:30', '2024-06-02 09:15', '2024-06-03 20:45']), use pandas and pd.to_datetime() to convert them into datetime objects and print the result.
"""
df = pd.DataFrame(
    {
    "delivery_timestamps" : [
    '2024-06-01 14:30',
    '2024-06-02 09:15',
    '2024-06-03 20:45',
    '2024-06-04 12:10',
    '2024-06-05 18:30',
    '2024-06-06 08:45',
    '2024-06-07 16:20']
    }
)

print(df)

df["delivery_timestamps"] = pd.to_datetime(df["delivery_timestamps"])
print(df)
"""

# Q2. Load a CSV file containing order dates from a Flipkart-style order history (column: 'order_date', format: 'YYYY-MM-DD HH:MM:SS'). Extract the year, month, and weekday for each order and add them as new columns in the DataFrame.
"""
df = pd.read_csv("Flipkart-style.csv")

print(df)

df["order_date"] = pd.to_datetime(df["order_date"])
print(df)

df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["day"] = df["order_date"].dt.day
df["day_name"] = df["order_date"].dt.day_name()
print(df)
"""

# Q3. Set the 'order_date' column as the index of your DataFrame and use resampling to calculate the total number of orders placed each week.<br><br><em><strong>Hint:</strong> Use df.resample('W').size() after setting the datetime index.</em>
"""
df = pd.read_csv("Flipkart-style.csv")
print(df)

df["order_date"] = pd.to_datetime(df["order_date"])

df.set_index("order_date",inplace=True)

weekly_order = df.resample("W").size()
print(weekly_order)
"""

# Q4. Suppose you have a DataFrame of Instagram posts with a 'posted_at' column in UTC. Convert these timestamps to 'Asia/Kolkata' timezone and display the first 5 converted times.
"""
df = pd.DataFrame(
    {
    "post_id": [101, 102, 103, 104, 105, 106],
    "username": ["user1", "user2", "user3", "user4", "user5", "user6"],
    "posted_at": [
        "2024-06-01 08:30:00",
        "2024-06-01 12:45:00",
        "2024-06-02 05:15:00",
        "2024-06-02 14:20:00",
        "2024-06-03 09:10:00",
        "2024-06-03 18:30:00"
    ]
}
)
print(df)

df["posted_at"] = pd.to_datetime(df["posted_at"])
df["Asia/Kolkata"] = df["posted_at"].dt.tz_convert("Asia/Kolkata")
print(df)
"""

# Q5. Create a new feature called 'is_weekend' in your DataFrame that marks True if an order was placed on Saturday or Sunday, and False otherwise.<br><br><em><strong>Constraint:</strong> Do not use any external libraries except pandas and numpy.</em>

df = pd.read_csv("Flipkart-style.csv")
print(df)

df["order_date"] = pd.to_datetime(df["order_date"])
df["day_name"] = df["order_date"].dt.day_name()
print(df)
df["is_weekend"] = np.where(df["day_name"].isin(["Sunday","Saturday"]),True,False)
print(df)