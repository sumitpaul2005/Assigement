import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler,LabelEncoder,MinMaxScaler,PolynomialFeatures
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split,GridSearchCV,cross_val_score
from sklearn.linear_model import LinearRegression,LogisticRegression,Ridge,Lasso,ElasticNet
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error,root_mean_squared_error,accuracy_score,confusion_matrix,classification_report,roc_curve,roc_auc_score,precision_recall_curve,log_loss
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB,MultinomialNB
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier,plot_tree,export_text
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier,AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.datasets import load_iris

# Q1. Load the Iris dataset using scikit-learn and use cross_val_score() with a KNeighborsClassifier to compute the average accuracy using 5-fold cross-validation.
"""
i = load_iris()

X = i.data
y = i.target

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

model = KNeighborsClassifier(
    n_neighbors=2
)
model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Predicted : ",pre)

acc = accuracy_score(y_test,pre)
print("Accuracy : ",acc)

cross = cross_val_score(
    model,
    X_train,
    y_train,
    cv=5,
    scoring="accuracy"
)

print("Cross Validation Score : ",cross)
"""

# Q2. For a dataset of your choice (e.g., Titanic or any from scikit-learn), perform 10-fold cross-validation using cross_val_score() with a DecisionTreeClassifier and print the accuracy for each fold.

df = pd.read_csv("Titanic-Dataset_2.csv")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Sex"] = df["Sex"].map({"male" : 1,"female" : 0})
print(df.isnull().sum())

X = df[["Sex","Age","SibSp","Parch"]]
y = df["Survived"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = DecisionTreeClassifier(criterion="gini",max_depth=4,random_state=42)
model.fit(X_train,y_train)


cross = cross_val_score(model,X_train,y_train,cv=10,scoring="accuracy")
print("Cross Validation : ",cross)