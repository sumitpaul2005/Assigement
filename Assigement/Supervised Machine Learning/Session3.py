import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error

# Q1. Download a small sample of IPL match data (CSV) with some missing values in player stats. Load it using pandas and print the number of missing values in each column.

df = pd.read_csv("ipl_dataset.csv")
print(df)
print(df.isnull().sum())


# Q2. For the 'player_age' column in your IPL dataset, fill all missing values with the median age using pandas' fillna() method and display the updated column.

df['player_age'] = df['player_age'].fillna(df['player_age'].median())

print(df['player_age'])

# Q3. Suppose the 'team' column in your IPL dataset contains missing values. Replace all missing team names with the constant value 'Unknown' and print the first 10 rows.

df['team'] = df['team'].fillna('Unknown')
print(df["team"])

# Q4. Take the 'venue' column (categorical) from your IPL dataset and apply one-hot encoding using pandas' get_dummies(). Show the resulting DataFrame with the new columns.

df = pd.get_dummies(df, columns=['venue'], dtype=int)
print(df)

# Q5. Use LabelEncoder from sklearn to encode the 'player_role' column (e.g., Batsman, Bowler, Allrounder) in your IPL dataset, and display the mapping from original roles to encoded values.<br><br><em><strong>Hint:</strong> Use LabelEncoder's classes_ attribute to see the mapping.</em>

label_encoder = LabelEncoder()
df['player_role'] =label_encoder.fit_transform(df['player_role'])

print(df)