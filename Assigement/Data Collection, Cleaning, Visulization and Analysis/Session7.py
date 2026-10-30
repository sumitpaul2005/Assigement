import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Q1. Given a CSV file containing Zomato restaurant ratings, use pandas to detect outliers in the 'user_rating' column using the IQR method and print the indices of the detected outliers.
"""
df = pd.read_csv("ZomatoRestaurents.csv")

print(df)

Q3 = df["user_rating"].quantile(0.75)
Q1 = df["user_rating"].quantile(0.25)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outlier = df[(df["user_rating"] < lower_bound) | (df["user_rating"] > upper_bound)]

print("Outlier is ",outlier)
"""

# Q2. Create a boxplot for the 'order_amount' column from a Swiggy orders dataset using matplotlib, and visually identify any outliers present.<br><br><em><strong>Hint:</strong> Use plt.boxplot() and label your axes for clarity.</em>
"""
df = pd.read_csv("Swiggy.csv")
print(df)

plt.boxplot(
    df["order_amount"]
)
plt.title("Order Amount")
plt.xlabel("customer_name")
plt.ylabel("order_amount")
plt.show()
"""

# Q3. Apply winsorization to the 'transaction_amount' column in a Paytm transactions DataFrame to cap all values above the 95th percentile and below the 5th percentile, then display the updated column statistics.

df = pd.read_csv("Paytm.csv")
print(df)

lower_bound = df["transaction_amount"].quantile(0.05)
upper_bound = df["transaction_amount"].quantile(0.95)
print(lower_bound)
print(upper_bound)

df["Winsorization of amt"] = df["transaction_amount"].clip(upper=upper_bound)
print(df)


# Q4. You have a DataFrame of Flipkart product prices stored as strings with currency symbols (e.g., '₹1,299'). Convert this column to numeric type using pandas, ensuring all non-numeric characters are removed.<br><br><em><strong>Hint:</strong> Use str.replace() and astype().</em>

df = pd.DataFrame({
    'product': ['Samsung Galaxy', 'iPhone 15', 'Redmi Note 13', 'Realme P3', 'OnePlus Nord'],
    'price': ['₹1,299', '₹69,999', '₹14,999', '₹12,499', '₹24,999']
})
print(df)

df = df["price"].str.replace('[₹,]',"",regex=True).astype(int)
print(df)

# Q5. Fix the following code snippet where the 'is_premium' column in a Spotify user DataFrame is a mix of boolean, string, and integer types. Convert the entire column to boolean type, treating 'True', 1, and 'yes' as True, and everything else as False.

df = pd.DataFrame({
    'user_id' : [101, 102, 103, 104, 105, 106, 107],
    'name' : ['Amit', 'Riya', 'Rahul', 'Neha', 'Karan', 'Priya', 'Vikas'],
    'is_premium' : [True, 'False', 1, 'yes', 0, 'No', 'True']
    }
)

print(df)

df = df["is_premium"].map({"True":True,1:True,"yes":True,"False":False,0:False,"No":False})
df.drop(columns=['is_premium'],inplace=True)
print(df)

