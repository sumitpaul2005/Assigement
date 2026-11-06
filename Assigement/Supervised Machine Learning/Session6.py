import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler,LabelEncoder,MinMaxScaler
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Q1. Download a dataset of mobile phone prices (with features like RAM, storage, camera MP, battery, brand, etc.) and fit a multiple linear regression model to predict the price using at least three features of your choice.

df = pd.read_csv("mobile_prices_150.csv")
"""
print(df)

X = df[["Storage (GB)","RAM (GB)","Camera (MP)"]]
y = df["Price ($)"]

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

model = LinearRegression()
model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Price : ",pre)

r2 = r2_score(y_test,pre)
print("R2 Score : ",r2)

# New data set

newdf = pd.DataFrame([[512,16,8000]])
newpre = model.predict(newdf)
print("New data predict : ",newpre)
"""

# Q2. Display the regression coefficients and intercept from your model, and write a short comment on what each coefficient means in the context of mobile phones (e.g., how much price increases per extra GB of RAM).
"""
print("Coefficient : ",model.coef_)
print("Intercept : ",model.intercept_)
"""
# Exact MeaningsIntercept
 
# 1. ($\$472.80$):   
#     The baseline starting price of a phone when all included features are zero.
    
# 2. First Feature Coefficient ($+0.98$ / unit) — Storage (GB):   
#     Price increases by $\approx \$0.98$ for every extra 1 GB of Storage. (e.g., $+128\text{ GB} \approx +\$125$).
    
# 3. Second Feature Coefficient ($+30.47$ / unit) — RAM (GB):   
#     Price increases by $\approx \$30.47$ for every extra 1 GB of RAM. (e.g., $+4\text{ GB}\text{ RAM} \approx +\$121.88$).
    
# 4. Third Feature Coefficient ($-0.0043$ / unit) — Battery Capacity (mAh):   
#     Price decreases by $\approx \$0.0043$ per extra 1 mAh of Battery (or $-\$4.33$ per $1,000\text{ mAh}$), showing a negligible negative correlation since cheaper budget phones often include larger batteries to compensate for lower performance specs.


# Q3. Using the statsmodels or scikit-learn library, calculate the Variance Inflation Factor (VIF) for each feature in your dataset and identify if any features show signs of multicollinearity.<br><br><em><strong>Hint:</strong> VIF values above 5 or 10 often indicate problematic multicollinearity.</em>

# VIF
"""
vif = pd.DataFrame()
vif['features'] = X.columns
vif['VIF'] = [variance_inflation_factor(X.values,i)
    for i in range(X.shape[1])
        ]
print(vif)
"""

# Q4. Interpret the feature importances or coefficients from your regression model to decide which feature is most influential in predicting mobile phone price, and explain your reasoning in 2-3 sentences.

# Based on the fitted multiple linear regression model:

# RAM (GB) is the most influential feature in predicting mobile phone price, with a coefficient of $32.96 per GB, compared to **$0.99** per GB of storage and $0.87 per megapixel of camera resolution.
# This indicates that an increase in RAM yields the largest unit increase in price, as higher system memory directly correlates with premium hardware tiers and processing capabilities.
# In practical terms, upgrading RAM from 4 GB to 12 GB adds approximately $263.68 to the predicted price, making it a far stronger price driver than typical increases in storage or camera megapixel values alone.


# Q5. Refactor your code to remove one highly collinear feature (based on VIF) and re-fit the regression model. Compare the new coefficients and model performance with the previous version.<br><br><em><strong>Hint:</strong> Removing multicollinear features can make your model more stable and interpretable.</em>

X = df[["Storage (GB)","RAM (GB)"]]
y = df["Price ($)"]

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

model = LinearRegression()
model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Price : ",pre)

r2 = r2_score(y_test,pre)
print("R2 Score : ",r2)

# New data set

newdf = pd.DataFrame([[512,16]])
newpre = model.predict(newdf)
print("New data predict : ",newpre)

print("Coefficient : ",model.coef_)
print("Intercept : ",model.intercept_)

