import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler,LabelEncoder,MinMaxScaler,PolynomialFeatures
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression,Ridge,Lasso
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error,root_mean_squared_error
from statsmodels.stats.outliers_influence import variance_inflation_factor


# Q1. Download a publicly available dataset of your choice (for example, a Flipkart product ratings dataset or Spotify song features) and split it into features (X) and target (y) for a regression problem.

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
    

# Q3. Fit a Ridge regression model (L2 regularization) using scikit-learn's Ridge class on the same dataset, and compare the coefficients to those from the Lasso model.<br><br><em><strong>Hint:</strong> Look for features where Lasso sets coefficients exactly to zero but Ridge does not.</em>

