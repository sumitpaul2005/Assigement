import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler,LabelEncoder,MinMaxScaler
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression,RidgeClassifier
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error,root_mean_squared_error
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Q1. Given two arrays: one with actual delivery times and one with predicted delivery times for 10 Zomato orders, calculate the Mean Squared Error (MSE) and Root Mean Squared Error (RMSE) using Python.
"""
actual = [30, 40, 25, 50, 35, 45, 60, 20, 55, 40]
predicted = [32, 38, 27, 48, 37, 42, 58, 22, 53, 43]

MSE = mean_absolute_error(actual,predicted)
print("MSE : ",MSE)

RMSE = root_mean_squared_error(actual,predicted)
print("RMSE : ",RMSE)
"""
# Q2. For a Flipkart product price prediction task, you have arrays of actual prices and predicted prices. Write a function to compute the Mean Absolute Error (MAE) and R² score, and print both values.<br><br><em><strong>Hint:</strong> Use sklearn.metrics.mean_absolute_error and sklearn.metrics.r2_score.</em>
"""
def calculate_error(actual,predicted):
    print("MAE : ",mean_absolute_error(actual,predicted))
    print("R2 Score : ",r2_score(actual,predicted))
    

actual = [500, 800, 1200, 1500, 2000, 2500, 3000, 3500, 4000, 4500]
predicted = [550, 750, 1100, 1600, 1900, 2600, 2900, 3400, 4200, 4400]
calculate_error(actual,predicted)
"""
# Q3. Create a residual plot for a dataset of actual vs predicted movie ratings (scale 1-5) for 20 movies, using matplotlib. Label the axes and briefly describe what the plot tells you about your model's errors.
"""
actual = [4.5, 3.8, 4.2, 2.9, 3.5, 4.8, 3.1, 4.0, 2.5, 3.7,
          4.4, 3.3, 4.9, 2.8, 3.6, 4.1, 3.0, 4.6, 2.7, 3.9]

predicted = [4.3, 4.0, 4.0, 3.2, 3.4, 4.6, 3.3, 3.8, 2.8, 3.5,
             4.2, 3.5, 4.7, 3.0, 3.8, 4.0, 3.2, 4.4, 2.9, 4.1]

residual = np.array(actual) - np.array(predicted)

plt.scatter(predicted,residual,color="red")
plt.xlabel("Predicted Movie Ratings")
plt.ylabel("Residuals")
plt.title("Residual Plot for Movie Ratings")
plt.grid()
plt.show()
"""
# Explanation
# 1. Actual: Original movie ratings.
# 2. Predicted: Model predicted ratings.
# 3. Residuals: Difference between actual and predicted ratings.

# Formula:

# Residual = Actual - Predicted


# Conclusion
# - Residual near 0 means prediction is accurate.
# - Positive residual means the model predicted a lower rating.
# - Negative residual means the model predicted a higher rating.
# - Randomly scattered points around zero generally indicate a good model fit.
# Overall: The residuals are relatively small and lie between -0.3 and +0.2, indicating that the model predictions are fairly close to actual movie ratings.

# Q4. You have two models predicting the delivery time for Swiggy orders. Model A has an RMSE of 8 minutes and R² of 0.65, Model B has an RMSE of 6 minutes and R² of 0.55. Which model would you choose and why? Explain your reasoning based on the evaluation metrics.

## Answer: Choose Model B

"""
I would choose Model B because it has a lower RMSE of 6 minutes, compared to Model A's 8 minutes.

Comparison

| Evaluation Metric | Model A   | Model B   |
| ----------------- | --------- | --------- |
| RMSE              | 8 minutes | 6 minutes |
| R² Score          | 0.65      | 0.55      |

Explanation

1. RMSE: Lower RMSE means smaller prediction errors. Model B is better because its RMSE is 6 minutes.
2. R² Score: Higher R² means the model explains more variation in delivery times. Model A is better because its R² is 0.65.

Conclusion

I would choose Model B because it has a lower RMSE, meaning its delivery time predictions have smaller errors on average (in the RMSE sense).

However, Model A has a higher R² score, so the final choice depends on the business requirement. For accurate delivery time predictions, Model B is preferable.
"""

# Q5. Compare two regression models for predicting Spotify song popularity: calculate MSE, RMSE, MAE, and R² for both models using sklearn, then identify which model is likely overfitting based on the results.<br><br><em><strong>Hint:</strong> Overfitting often shows very low error on training data but much higher error on test data.</em>

df = pd.read_csv("spotify.csv")
X = df[["Beats_Per_Minute", "Energy", "Danceability", "Tempo"]]
y = df["Popularity"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model1 = LinearRegression()
model2 = RidgeClassifier(random_state=42) 

model1.fit(X_train, y_train)
model2.fit(X_train, y_train)

def evaluate_model(model, name):
    pred_train = model.predict(X_train)
    pred_test = model.predict(X_test)
    
    print(f"\n--- {name} ---")
    print(f"Train MSE: {mean_squared_error(y_train, pred_train):.4f} | Test MSE: {mean_squared_error(y_test, pred_test):.4f}")
    print(f"Train R2:  {r2_score(y_train, pred_train):.4f}  | Test R2:  {r2_score(y_test, pred_test):.4f}")

evaluate_model(model1, "Linear Regression")
evaluate_model(model2, "Decision Tree Regressor")