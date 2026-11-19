import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler,LabelEncoder,MinMaxScaler,PolynomialFeatures
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split,GridSearchCV
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

# Q1. Download a sample credit card fraud dataset (with imbalanced classes) from Kaggle or UCI, split it into train and test sets, and train a logistic regression classifier using scikit-learn.

df = pd.read_csv("creditcard.csv")
print(df)

X = df.drop('Class',axis=1)
y = df['Class']

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Predicted : ",pre)

acc = accuracy_score(y_test,pre)
print("Accuracy : ",acc)

# Q2. Plot the ROC curve for your classifier using sklearn.metrics.roc_curve and matplotlib, and display the AUC score on the plot.
"""
fpr,tpr,threshold = roc_curve(y_test,pre)
auc = roc_auc_score(y_test,pre)

plt.plot(fpr,tpr,label = f"Logistic Regrassion (AUC = {auc:.4f})")
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.grid(True)

plt.show()
"""
# Q3. Plot the Precision-Recall curve for your model using sklearn.metrics.precision_recall_curve and matplotlib, and explain in one line why this curve is useful for imbalanced datasets.<br><br><em><strong>Hint:</strong> Focus on how precision and recall behave when the positive class is rare.</em>
"""
y_prob = model.predict_proba(X_test)[:,1]
precision,recall,threshold = precision_recall_curve(y_test,y_prob)

plt.plot(recall,precision,label="Logistic Regression",color="red")
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend()
plt.grid()
plt.show()
"""

# Q4. Calculate the log loss (cross-entropy loss) for your test set predictions using sklearn.metrics.log_loss and print the result.

y_prob = model.predict_proba(X_test)[:,1]
log = log_loss(y_test,y_prob)
print("Log Loss : ",log)

# Q5. Change the class distribution in your test set to be even more imbalanced (e.g., only 2% positive class), re-calculate accuracy, AUC, and log loss, and write 2 lines explaining which metric is most misleading and why.<br><br><em><strong>Hint:</strong> Accuracy can be high even if the model ignores the minority class.</em>

positive = np.where(y_test == 1)[0]
negative = np.where(y_test == 0)[0]

n_negative = int(len(negative) * 0.02 / 0.98)

np.random.seed(42)

selected_negative = np.random.choice(
    negative,
    size=n_negative,
    replace=False
)

# Combine samples
selected = np.concatenate([positive, selected_negative])
np.random.shuffle(selected)

# Create new test data
y_test_new = y_test.iloc[selected]
y_prob_new = y_prob[selected]

# Predict using probability threshold
y_pred_new = (y_prob_new >= 0.5).astype(int)

# Calculate metrics
acc = accuracy_score(y_test_new, y_pred_new)
auc = roc_auc_score(y_test_new, y_prob_new)
loss = log_loss(y_test_new, y_prob_new)

print("Accuracy :", acc)
print("AUC Score :", auc)
print("Log Loss :", loss)