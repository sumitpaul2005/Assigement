import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler,LabelEncoder,MinMaxScaler
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error
from sklearn.tree import DecisionTreeRegressor

# Q1. Create a Python script that generates two arrays: one representing the number of hours you spend on Instagram each day for a week, and the other representing your daily phone battery percentage at the end of the day. Plot these as a scatter plot using matplotlib.

df = pd.read_csv("battery_data.csv")
"""
print(df)

plt.scatter(df[["Instagram_Hours"]],df[["Battery_Percentage"]],color="red")
plt.title("Battery Usage")
plt.xlabel("Instagram_Hours")
plt.ylabel("Battery_Percentage")
plt.show()
"""

# Q2. Using scikit-learn's LinearRegression, fit a simple linear regression model to predict daily battery percentage based on Instagram usage hours from your generated data. Print the model's slope (coefficient) and intercept.

X = df[["Instagram_Hours"]]
y = df["Battery_Percentage"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Predicted : ",pre)

print("Coeficient : ",model.coef_)
print("Intercept : ",model.intercept_)

r2 = r2_score(y_test,pre)
print("R2 Score : ",r2)


# Q3. Plot the regression line on top of your scatter plot to visualize the relationship between Instagram hours and battery percentage using matplotlib.<br><br><em><strong>Hint:</strong> Use model.predict() to get the predicted values for your x-axis data and plot them as a line.</em>

plt.plot(X,model.predict(X),color="blue")
plt.scatter(X,y,color="red")
plt.title("Acutal Vs Predicted Plot")
plt.xlabel("Instagram_Hours")
plt.ylabel("Battery_Percentage")
plt.show()

# Q4. Calculate the mean squared error (MSE) between your actual battery percentages and the predicted values from your regression model using sklearn.metrics.mean_squared_error. Print the MSE value and explain in one line what a lower MSE indicates.

MSE = mean_absolute_error(y_test,pre)
print("Mean Squared Error : ",MSE)

# A lower MSE indicates that the model's predictions are closer to the actual observed data points, representing a tighter fit and higher predictive accuracy.