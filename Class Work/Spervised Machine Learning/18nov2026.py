import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split,GridSearchCV,KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import roc_auc_score,roc_curve,accuracy_score

# Read the CSV file into a DataFrame
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Display the first five rows and last five rows.
print(df.head())
print(df.tail())

# Check the number of rows and columns (dataset shape).
print(df.shape)

# Inspect column names and data types.
print(df.info())

# Generate descriptive statistics for numerical columns.
