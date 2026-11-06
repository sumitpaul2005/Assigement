import pandas as pd 
import numpy as np 
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score,classification_report,roc_curve,roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC 
import seaborn as sns
import matplotlib.pyplot as plt

"""
df = pd.read_csv("Social_Network_Ads.csv")
print(df)

df["Gender"] = df["Gender"].map({'Male' : 1,'Female' : 0})

X = df[["Gender","Age","EstimatedSalary"]]
y = df["Purchased"]

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

model = AdaBoostClassifier(n_estimators=100,learning_rate=1)
model.fit(X_train,y_train)

pre = model.predict(X_test)
print(pre)

acc = accuracy_score(y_test,pre)
print(acc)

gre = GradientBoostingClassifier(n_estimators=100,learning_rate=1,max_depth=5,random_state=42)
gre.fit(X_train,y_train)

gpre = gre.predict(X_test)
print(gpre)

gacc = accuracy_score(y_test,gpre)
print(gacc)
"""

df = pd.read_csv("Social_Network_Ads.csv")
print(df)

# missing values :
print(df.isnull().sum())

#gender  : 
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

# feature selection : 
X=df[['Age','EstimatedSalary','Gender']]
y=df['Purchased']

# split data :
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42)

# scale data :
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

# model 

model = LogisticRegression()
model.fit(X_train,y_train)

y_predict = model.predict(X_test)
print("Predicted : ",y_predict)

# Accuracy Score

accuracy = accuracy_score(y_test,y_predict)
print("Predicted Value : ",accuracy)

# classification_report
classification_rep = classification_report(y_test,y_predict)
print("Classification Metrix : ",classification_rep)

#confusion matrix using  seaborn  ----> sns.heatmap 

confusion_matrix = pd.crosstab(y_test,
                               y_predict,
                               rownames=['Actual'],
                               colnames=['Predicted'])
print("Confusion Matrix : \n",confusion_matrix)
"""
confusion_matrix_plot = sns.heatmap(confusion_matrix,
                                    annot=True,
                                    fmt='d',
                                    cmap='Blues')
plt.show()
"""
# ROC Curve

curve = roc_curve(y_predict,y_test)
print(curve)

# Probability of positive class
y_prob = model.predict_proba(X_test)[:, 1]

# ROC values
fpr, tpr, thresholds = roc_curve(y_test, y_prob)

# AUC Score
auc_score = roc_auc_score(y_test, y_prob)

# Plot ROC Curve
plt.figure(figsize=(6,4)) 
plt.plot(fpr,tpr,label =f"AUC = {auc_score:.3f}",
         color='blue')

plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.grid(True)

plt.show()

