import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error

df = pd.read_csv("housing.csv")
df["total_bedrooms"] = df["total_bedrooms"].fillna(df["total_bedrooms"].median())
print(df.isnull().sum())

"""
plt.figure(figsize=(10,10))
plt.scatter(
    df["median_income"].head(10),
    df["median_house_value"].head(10)
)
plt.title("House value")
plt.xlabel("Income")
plt.ylabel("House Value")
plt.show()
"""

# Features Selection

X = df[["median_income"]]
y = df["median_house_value"]

# Split

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# 5. Feature Selection with Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# Slope, Intercept

print("Slope : ",model.coef_)
print("Intercept : ",model.intercept_)

# Predicted 

y_test_predict = model.predict(X_test)
print("Predicted values : ",y_test_predict)

# Compare Actual vs Predicted

result = pd.DataFrame(
    {
        'Actual' : y_test.values,
        'Predicted' : y_test_predict
    }
)

print(result)

# Evaluation

R2_Score = r2_score(y_test,y_test_predict)
print("R2 Score : ",R2_Score)

MSE = mean_squared_error(y_test,y_test_predict)
print("MSE : ",MSE)

MAE = mean_absolute_error(y_test,y_test_predict)
print("MAE : ",MAE)

RMSE = np.sqrt(MSE)
print("RMSE : ",RMSE)

# New Data set predicted

newdf = pd.DataFrame({
    "median_income" : [15000,56000]
})

new_data_predicted = model.predict(newdf)
print("New Data set Predicted : ",new_data_predicted)

# Check overfitting or underfitting

train_r2_score = model.score(X_train,y_train)
test_r2_score = model.score(X_test,y_test)

print("Train Score : ",train_r2_score)
print("Test Score : ",test_r2_score)

# diffrence

diff_train_test = train_r2_score - test_r2_score
print("Difffrence Train test : ",diff_train_test)

if train_r2_score < 0.70 and test_r2_score < 0.70:
    print("Model UnderFitting")
elif diff_train_test > 0.10:
    print("Model OverFitting")
else:
    print("Model is Good")


