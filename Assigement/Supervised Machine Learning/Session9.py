import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler,LabelEncoder,MinMaxScaler,PolynomialFeatures
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression,Ridge,Lasso,ElasticNet
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error,root_mean_squared_error
from statsmodels.stats.outliers_influence import variance_inflation_factor


# Q1. Download a publicly available dataset of your choice (for example, a Flipkart product ratings dataset or Spotify song features) and split it into features (X) and target (y) for a regression problem.
"""
df = pd.read_csv("spotify-tracks-dataset-detailed.csv")
df = df.dropna(axis=0)
print(df)

X = df[['duration_ms','danceability','energy','key','loudness','mode','speechiness','acousticness','liveness','valence','tempo','time_signature',]]
y = df['popularity']


# Q2. Fit a Lasso regression model (L1 regularization) using scikit-learn's Lasso class on your dataset, and print out the coefficients for each feature.

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = Lasso(alpha=1)
model.fit(X_train,y_train)

for feature, coef in zip(X.columns, model.coef_):
    print(feature, ":", coef)
    """

# Q3. Fit a Ridge regression model (L2 regularization) using scikit-learn's Ridge class on the same dataset, and compare the coefficients to those from the Lasso model.<br><br><em><strong>Hint:</strong> Look for features where Lasso sets coefficients exactly to zero but Ridge does not.</em>
"""
Rmodel = Ridge(alpha=1)
Rmodel.fit(X_train,y_train)

print("Comparing 2 model Coefficient...")
print("Lasso : ",model.coef_)
print("Ridge : ",Rmodel.coef_)
"""

# Q4. Fit an ElasticNet regression model using scikit-learn's ElasticNet class, and observe how the coefficients differ from both Lasso and Ridge.<br><br><em><strong>Hint:</strong> Try changing the l1_ratio parameter and see how it affects the results.</em>
"""
Emodel = ElasticNet(alpha=1,l1_ratio=0.5)
Emodel.fit(X_train,y_train)

print("ElasticNet : ",Emodel.coef_)
"""

# Q5. Suppose you want to build a feature selector for a Zomato-style restaurant rating predictor. Use Lasso regression to select the most important features from your dataset, and list which features are kept (non-zero coefficients) and which are dropped.

df = pd.read_csv("Zomato Restaurant Dataset.csv")
print(df)

X = df[["votes","average_cost_for_two"]]
y = df["rating"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.3,
    random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = Lasso(alpha=1)
model.fit(X_train,y_train)

pre = model.predict(X_test)
print(pre)

feature_status = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
})

kept_features = feature_status[feature_status['Coefficient'] != 0]
dropped_features = feature_status[feature_status['Coefficient'] == 0]

print("--- KEPT FEATURES (Non-Zero Coefficients) ---")
print(kept_features.to_string(index=False))

print("\n--- DROPPED FEATURES (Zeroed Out) ---")
print(dropped_features.to_string(index=False))