import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("directors.csv")
df = df.drop(columns=['Unnamed: 0'])
print(df)
"""
print(df.info())
print(df.describe())

print(df.isnull().sum())
"""

df['id'] = df["id"].fillna(df["id"].mean())
df['gender'] = df["gender"].fillna(df["gender"].mode()[0])

f = {"Male" : 0,"Female" : 1}
df["gender"] = df["gender"].map(f)
print(df.isnull().sum())
print(df)
X = df["gender"]
y = df["id"]

X_train,X_test,Y_train,Y_test = train_test_split(X,
                                                 y,
                                                 test_size=0.2,
                                                 random_state=42)

