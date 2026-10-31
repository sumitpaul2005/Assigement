import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Q1. Download the 'Spotify Top 50 Songs' dataset from Kaggle, load it into a pandas DataFrame, and identify which columns should be used as features and which as the label if you want to predict a song's popularity score.

df = pd.read_csv("spotify.csv", encoding="latin1")
print(df)
"""
X = df[['Beats_Per_Minute', 'Energy', 'Danceability',
        'Loudness_dB', 'Liveness', 'Valence',
        'Length', 'Acousticness', 'Speechiness']]

y = df['Popularity']
"""
# Q2. Split the loaded Spotify dataset into training and test sets using sklearn's train_test_split function, with 80% for training and 20% for testing. Print the number of rows in each set.
"""
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))
"""

# Q3. Given a simple linear regression model predicting song popularity from danceability, intentionally use only 5% of the data for training and 95% for testing. Observe the model's performance and explain whether this is likely to cause underfitting or overfitting.<br><br><em><strong>Hint:</strong> Look at the accuracy or error on both train and test sets to support your answer.</em>

X = df[['Danceability']]
y = df['Popularity']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.95, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

train_r2_score = r2_score(y_train, train_pred)
test_r2_score = r2_score(y_test, test_pred)

print("Training R2 Score:", train_r2_score)
print("Testing R2 Score:", test_r2_score)

diff_train_test = train_r2_score - test_r2_score
print("Difference:", diff_train_test)

# Check overfitting or underfitting

if train_r2_score < 0.70 and test_r2_score < 0.70:
    print("Model is underfitting")

elif diff_train_test > 0.10:
    print("Model may be overfitting")

else:
    print("Model has similar performance on both sets")
    
# Q4. Draw or find a graph online that visually explains the bias–variance tradeoff, and write a short note describing how this tradeoff would affect predictions in a Zomato restaurant rating predictor app.

# Model complexity
x = np.linspace(1, 10, 100)

# Bias and variance
bias = 10 / x
variance = x / 10

# Total error
total_error = bias + variance

plt.plot(x, bias, label="Bias²")
plt.plot(x, variance, label="Variance")
plt.plot(x, total_error, label="Total Error")

plt.xlabel("Model Complexity")
plt.ylabel("Error")
plt.title("Bias-Variance Tradeoff")

plt.legend()
plt.grid()
plt.show()

# Short note for Zomato
# - High Bias: Model is too simple and cannot predict restaurant ratings accurately (underfitting).
# - High Variance: Model memorizes training data and gives poor predictions for new restaurants (overfitting).
# - Balanced Model: Learns patterns from restaurant data and predicts ratings more accurately.
# Conclusion: Zomato should use a balanced model to reduce both bias and variance and improve restaurant rating predictions.

# Q5. Give a real example (outside of healthcare/hospital) of overfitting from any app you use (e.g., Instagram, Flipkart, Swiggy), and explain in 2-3 lines why it might happen in that scenario.
"""
Example: Instagram Recommendation System

Instagram may show me too many cricket videos because I watched several cricket reels recently. This is an example of overfitting because the recommendation system may focus too much on my recent activity and ignore my other interests.

Why it happens: The model gives too much importance to recent viewing history instead of learning my overall interests.
"""