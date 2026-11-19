import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler,LabelEncoder,MinMaxScaler,PolynomialFeatures
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression,Ridge
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error,root_mean_squared_error
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Q1. Use sklearn's PolynomialFeatures() to transform a dataset of mobile phone prices (features: RAM, storage) into polynomial features up to degree 2, and print the resulting feature matrix.
"""
df = pd.read_csv("mobile_prices_150.csv")
print(df.isnull().sum())

X = df[["RAM (GB)","Storage (GB)"]]
y = df["Price ($)"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

model = PolynomialFeatures(degree=2)
X_poly = model.fit_transform(X)

feature_names = model.get_feature_names_out(["RAM (GB)","Storage (GB)"])
df_poly = pd.DataFrame(X_poly, columns=feature_names)

print("Transformed Polynomial Feature Matrix")
print(df_poly)
"""

# Q2. Train both a LinearRegression and a Polynomial Regression (degree=3) model on a dataset of Zomato restaurant ratings versus number of reviews, then plot both predictions on the same chart to compare their fits.<br><br><em><strong>Hint:</strong> Use matplotlib for plotting and clearly label both curves.</em>
"""
df = pd.read_csv("Zomato Restaurant Dataset.csv")
print(df)

X = df[["rating","votes","price_range"]]
y = df["average_cost_for_two"]

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

linearmodel = LinearRegression()
linearmodel.fit(X_train,y_train)

linearPred = linearmodel.predict(X_test)
print("Linear Model : ",linearPred)

poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X_train)

ploymodel = LinearRegression()
ploymodel.fit(X_poly,y_train)

polyPred = ploymodel.predict(poly.transform(X_test))
print("Polynomial Predicted : ",polyPred)

plt.plot(X,linearmodel.predict(X),color="red",label="Linear")
plt.plot(X,ploymodel.predict(poly.transform(X)),color="blue",label="Poly")
plt.xlabel("Actual Cost")
plt.ylabel("Predicted Cost")
plt.title("Linear vs Polynomial Regression")
plt.show()
"""

# Q3. Given a dataset where the relationship between followers and posts for Instagram users is non-linear, fit a polynomial regression model (degree=4) and check for overfitting by plotting the training and validation errors for degrees 1 to 5.
"""
df = pd.read_excel("MainDataset- Instagram.xlsx")
print(df.isnull().sum())

X = df[["Number of Posts"]]
y = df["Number of Followers"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.3,random_state=42
)

train_error = []
validation_error = []

for i in range(1, 6):

    poly = PolynomialFeatures(degree=i)

    X_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)

    model = LinearRegression()
    model.fit(X_poly, y_train)

    trainPred = model.predict(X_poly)
    testPred = model.predict(X_test_poly)

    r2 = r2_score(y_test, testPred)

    print("Degree:", i, "R2 Score:", r2)

    train_error.append(mean_squared_error(y_train, trainPred))
    validation_error.append(mean_squared_error(y_test, testPred))
    
plt.plot(range(1, 6), train_error, marker="o", label="Training Error")
plt.plot(range(1, 6), validation_error, marker="o", label="Validation Error")

plt.xlabel("Polynomial Degree")
plt.ylabel("Mean Squared Error")
plt.title("Polynomial Regression - Overfitting Detection")
plt.legend()
plt.grid()
plt.show()
"""

# Q4. Add L2 regularization (Ridge regression) to your polynomial regression model (degree=3) on a Flipkart product price prediction dataset, and compare the model's performance with and without regularization.<br><br><em><strong>Hint:</strong> Use Ridge from sklearn.linear_model and explain any difference in test error.</em>

df = pd.read_csv("Flipkart Product Ratings.csv")
print(df)

X = df[['rating','reviews','discount']]
y = df['price']

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.3,random_state=42
)

poly = PolynomialFeatures(degree=3)

X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

scaler = StandardScaler()

X_train_scaler = scaler.fit_transform(X_train_poly)
X_test_scaler = scaler.transform(X_test_poly)

# With Ridge Regularization
model = Ridge(alpha=1)
model.fit(X_train_scaler, y_train)

Rpre = model.predict(X_test_scaler)

print("\nWith Ridge Regularization:")
print("Prediction:", Rpre)
print("MSE:", mean_squared_error(y_test, Rpre))
print("R2 Score:", r2_score(y_test, Rpre))

# Without Regularization
linear_model = LinearRegression()
linear_model.fit(X_train_scaler, y_train)

linear_pred = linear_model.predict(X_test_scaler)

print("\nWithout Regularization:")
print("Prediction:", linear_pred)
print("MSE:", mean_squared_error(y_test, linear_pred))
print("R2 Score:", r2_score(y_test, linear_pred))

# Ridge Regression performs better than Polynomial Regression without regularization because its R² score (-1.307) is higher than the unregularized model's score (-16.477). L2 regularization helps control large coefficients and reduces overfitting. However, both models need improvement because their R² scores are negative.

# Q5. Use ChatGPT or Copilot to generate Python code that demonstrates underfitting and overfitting using polynomial regression on a synthetic dataset, then run the code and explain in your own words how model degree affects bias and variance.
"""
Underfitting and Overfitting Using Polynomial Regression

Objective: To demonstrate underfitting and overfitting using Polynomial Regression on a synthetic dataset and understand how model degree affects bias and variance.

Polynomial Degrees Used:

1. Degree 1 – Underfitting
2. Degree 4 – Good Fit
3. Degree 10 – Overfitting

Execution Output

| Degree | Training MSE | Testing MSE |
| ------ | ------------ | ----------- |
| 1      | 0.6797       | 0.4274      |
| 4      | 0.2143       | 0.1928      |
| 10     | 0.0295       | 0.3673      |

Explanation

1\. Underfitting (Degree 1): The model is too simple to understand the actual data pattern. It has high bias and gives poor predictions.

2\. Good Fit (Degree 4): The model learns the actual data pattern properly and provides better predictions with balanced bias and variance.

3\. Overfitting (Degree 10): The model learns the training data too closely, including noise. It has high variance and performs poorly on unseen data.

Bias and Variance

- Bias: Error caused by a model being too simple.
- Variance: Error caused by a model being too sensitive to training data.

Conclusion

Polynomial degree affects the complexity of a regression model. A low degree causes underfitting, while a high degree can cause overfitting. In this experiment, Degree 4 performs best because it has the lowest testing MSE of 0.1928. Therefore, selecting the correct polynomial degree helps achieve better prediction accuracy.
"""