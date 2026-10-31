import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler,LabelEncoder,MinMaxScaler
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error
from sklearn.tree import DecisionTreeRegressor

# Q1. Download a small dataset of IPL cricket player stats (e.g., runs, wickets, matches, strike rate) and apply StandardScaler from scikit-learn to scale all numeric features. Save the scaled data to a new CSV file named ipl_scaled.csv.

"""
df = pd.read_csv("ipl_dataset.csv")

# Fill missing values
df['player_age'] = df['player_age'].fillna(df['player_age'].median())
df['runs'] = df['runs'].fillna(df['runs'].mean())
df['average'] = df['average'].fillna(df['average'].mean())
df['strike_rate'] = df['strike_rate'].fillna(df['strike_rate'].median())
df['economy'] = df['economy'].fillna(df['economy'].median())
df['wickets'] = df['wickets'].fillna(df['wickets'].mean())
df['team'] = df['team'].fillna('Unknown')

df = pd.get_dummies(df, columns=['venue'], dtype=int)

print(df.isnull().sum())

X = df.drop(['player', 'team', 'runs','player_role'], axis=1)
y = df['runs']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Apply StandardScaler
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Display scaled data
print("Scaled Training Data:")
print(X_train)

print("\nScaled Testing Data:")
print(X_test)

# Save scaled dataset
scaled_df = pd.DataFrame(X_train, columns=X.columns)
scaled_df.to_csv("ipl_scaled.csv", index=False)

print("\nScaled data saved as ipl_scaled.csv")
"""

# Q2. Using a dataset of Flipkart product ratings (features: price, rating, number of reviews, discount), apply MinMaxScaler so that all features are scaled between 0 and 1. Print the minimum and maximum value for each column before and after scaling.<br><br><em><strong>Hint:</strong> Use pandas to load the data and scikit-learn's MinMaxScaler for scaling.</em>
"""
df = pd.read_csv("Flipkart Product Ratings.csv")

print("Before Scaling:")
print(df[['price', 'rating', 'reviews', 'discount']].agg(['min', 'max']))

# Features and target
X = df[['price', 'rating', 'reviews', 'discount']]
y = df['rating']


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Apply MinMaxScaler
scaler = MinMaxScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

X_train = pd.DataFrame(X_train, columns=X.columns)
X_test = pd.DataFrame(X_test, columns=X.columns)

print("\nAfter Scaling - Training Data:")
print(X_train.agg(['min', 'max']))

print("\nAfter Scaling - Testing Data:")
print(X_test.agg(['min', 'max']))
"""

# Q3. Given a Spotify songs dataset (features: danceability, energy, tempo, popularity), use correlation analysis to select the top 2 features most related to 'popularity'. List the selected features and explain your choice in one line each.
"""
df = pd.read_csv("spotify.csv", encoding="latin1")

cols = ['Danceability', 'Energy', 'Tempo', 'Popularity']
df = df[cols]

# Calculate correlation
corr = df.corr()

print("Correlation with Popularity:")
print(corr['Popularity'])

top_features = corr['Popularity'].drop('Popularity').abs().nlargest(2)

print("\nTop 2 Features:")
print(top_features)
"""

# Q4. Take a Zomato restaurant dataset and use scikit-learn's RFE (Recursive Feature Elimination) with a DecisionTreeRegressor to select the 3 most important features for predicting 'average cost for two'. List the selected features and the RFE ranking.
"""
df = pd.read_csv("Zomato Restaurant Dataset.csv")

df['online_order'] = df['online_order'].map({'Yes': 1, 'No': 0})
df['table_booking'] = df['table_booking'].map({'Yes': 1, 'No': 0})

X = df[['rating', 'votes', 'price_range',
        'online_order', 'table_booking']]

y = df['average_cost_for_two']

X = X.fillna(X.median())
y = y.fillna(y.median())

model = DecisionTreeRegressor(random_state=42)

rfe = RFE(estimator=model, n_features_to_select=3)
rfe.fit(X, y)

print("Selected Features:")
print(X.columns[rfe.support_].tolist())

print("\nRFE Ranking:")
for feature, rank in zip(X.columns, rfe.ranking_):
    print(feature, ":", rank)
"""

# Q5. Given a BookMyShow movie ratings dataset, detect outliers in the 'user ratings' column using the IQR method. Remove the outliers and display how many rows were dropped.<br><br><em><strong>Hint:</strong> Calculate Q1, Q3, and IQR; filter out rows outside [Q1 - 1.5*IQR, Q3 + 1.5*IQR].</em>

df = pd.read_csv("BookMyShow.csv")

Q1 = df['user ratings'].quantile(0.25)
Q3 = df['user ratings'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df_clean = df[
    (df['user ratings'] >= lower) &
    (df['user ratings'] <= upper)
]

dropped = len(df) - len(df_clean)

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Limit:", lower)
print("Upper Limit:", upper)

print("\nOriginal Rows:", len(df))
print("Rows After Removing Outliers:", len(df_clean))
print("Total Rows Dropped:", dropped)
