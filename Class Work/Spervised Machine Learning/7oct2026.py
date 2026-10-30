import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix,classification_report

df = pd.read_csv("heart.csv")
print(df)

# print(df.isnull().sum())

# Features 

X = df[["age",  "sex" , "cp", "trestbps",  "chol", "fbs",  "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"]]
y = df["target"]

# Split

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# model

model = LogisticRegression()
model.fit(X_train,y_train)

# Predict

y_predict = model.predict(X_test)
print("Predict : ",y_predict)

# accuracy

Accuracy_score = accuracy_score(y_test,y_predict)
print(Accuracy_score * 100)

# Overfitting

train_predict = model.predict(X_train)
test_predict = model.predict(X_test)

train_score = accuracy_score(y_train,train_predict)
test_score = accuracy_score(y_test,test_predict)

diff =  train_score - test_score 
print("Diff : ",diff)

print("overfitting :",f"{diff*100:.2f}%")
