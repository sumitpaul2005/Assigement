import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

df = pd.read_csv("CAR DETAILS FROM CAR DEKHO.csv")
print(df.head())

f = {"Petrol" : 0, "Diesel" : 1 , "LPG" : 2 , "CNG" : 3 , "Electric" : 4}
df["fuel"] = df["fuel"].map(f)

s = {"Individual" : 0, "Dealer" : 1, "Trustmark Dealer" : 2}
df["seller_type"] = df["seller_type"].map(s)

t = {"Manual" : 0, "Automatic" : 1}
df["transmission"] = df["transmission"].map(t)

o = {"First Owner" : 0, "Second Owner" : 1, "Third Owner" : 2, "Fourth & Above Owner" : 3, "Test Drive Car" : 4}
df["owner"] = df["owner"].map(o)
 
print(df)
print(df.isnull().sum())

# Feature Seclection

X = df[["year","km_driven","fuel","seller_type","transmission","owner"]]
y = df["selling_price"]

# Split

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

#Scaler

scaler = StandardScaler()
X_train_scaler = scaler.fit_transform(X_train)
X_test_scaler = scaler.transform(X_test)

#Model 

model = LinearRegression()
# rfe = RFE(model,n_features_to_select=2)
# rfe.fit(X_train_scaler,y_train)

# print(rfe.support_)

model.fit(X_train_scaler,y_train)

# Predict

y_predict = model.predict(X_test_scaler)
print(y_predict)

#R2 score

R2_Score = r2_score(y_test,y_predict)
print(R2_Score)

#R2 score Train

R2_Score_train = model.score(X_train_scaler,y_train)
R2_Score_test = model.score(X_test_scaler,y_test)
print(R2_Score_train)
print(R2_Score_test)

# diffrence

diff = R2_Score_train - R2_Score_test
print(diff)

if R2_Score_train < 0.70 and R2_Score_test < 0.70:
    print("Underfitting (Model too simple, performance is poor on both sets)")
elif diff > 0.10:
    print("Overfitting (Model learned training noise)")
else:
    print("Good Fit")
    
    
# Lasso 

modellasso = Lasso(alpha=1)
modellasso.fit(X_train_scaler,y_train)

lassopridect = modellasso.predict(X_test_scaler)
print("Lasso Predict : ",lassopridect)

lassoR2Score = r2_score(y_test,lassopridect)
print("Lasso R2 Score : ",lassoR2Score)

# Ridge 

modelRidge = Ridge(alpha=1)
modelRidge.fit(X_train_scaler,y_train)

Ridgepridect = modelRidge.predict(X_test_scaler)
print("Lasso Predict : ",lassopridect)

RidgeR2Score = r2_score(y_test,Ridgepridect)
print("Ridge R2 Score : ",RidgeR2Score)

# ElasticNet 

modelElastic = ElasticNet(alpha=1,l1_ratio=0.5)
modelElastic.fit(X_train_scaler,y_train)

Elasticpridect = modelElastic.predict(X_test_scaler)
print("ElasticNet Predict : ",Elasticpridect)

ElasticR2Score = r2_score(y_test,Elasticpridect)
print("ElasticNet R2 Score : ",ElasticR2Score)