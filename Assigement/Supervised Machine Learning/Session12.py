import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler,LabelEncoder,MinMaxScaler,PolynomialFeatures
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression,Ridge,Lasso,ElasticNet
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error,root_mean_squared_error,accuracy_score,confusion_matrix,classification_report
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB,MultinomialNB
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier,plot_tree,export_text

# Q1. Load the Iris dataset using scikit-learn, train a DecisionTreeClassifier, and plot the resulting decision tree using plot_tree().
"""
iris = load_iris()
X = iris.data
y = iris.target

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.4,
    random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Predicted : ",pre)

acc = accuracy_score(y_test,pre)
print("Accuracy : ",acc)

plot_tree(
    model,feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True
)
plt.show()
"""

# Q2. Change the splitting criterion of your DecisionTreeClassifier from 'gini' to 'entropy' and compare the accuracy scores for both on the same dataset.<br><br><em><strong>Hint:</strong> Use the 'criterion' parameter when initializing the classifier.</em>
"""
iris = load_iris()
X = iris.data
y = iris.target

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.4,
    random_state=42
)

model = DecisionTreeClassifier(criterion='entropy',random_state=42)
model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Predicted : ",pre)

acc = accuracy_score(y_test,pre)
print("Entropy Accuracy : ",acc)

model = DecisionTreeClassifier(criterion='gini',random_state=42)
model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Predicted : ",pre)

acc = accuracy_score(y_test,pre)
print("Gini Accuracy : ",acc)
"""

# Q3. Limit the maximum depth of your decision tree to 2 and visualize the new tree structure. Observe and briefly describe how the tree's decisions have changed compared to the full-depth tree.
"""
iris = load_iris()
X = iris.data
y = iris.target

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.4,
    random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Predicted : ",pre)

acc = accuracy_score(y_test,pre)
print("Maximum Depth Accuracy : ",acc)

model = DecisionTreeClassifier(max_depth=2,random_state=42)
model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Predicted : ",pre)

acc = accuracy_score(y_test,pre)
print("Depth of 2 Accuracy : ",acc)
"""

# Q4. Use the feature_importances_ attribute of your trained DecisionTreeClassifier to display the importance score for each feature in the Iris dataset. Sort and print the features from most to least important.
"""
iris = load_iris()
X = iris.data
y = iris.target

model = DecisionTreeClassifier(random_state=42)

model.fit(X, y)

importance = model.feature_importances_

df = pd.DataFrame({
    'Feature': iris.feature_names,
    'Importance': importance
})

df = df.sort_values(by='Importance', ascending=False)
print(df)
"""

# Q5. Pick any dataset from Kaggle (such as a simple food delivery ratings or IPL match stats CSV), train a decision tree, and interpret the first three splits in your own words — explain which feature and value the tree is using at each split and why it might help classification.<br><br><em><strong>Hint:</strong> Use plot_tree() with feature_names and read the conditions shown at each node.</em>

df = pd.read_csv("food_delivery_ratings_500.csv")

print(df.isnull().sum())

X = df[['delivery_time_mins', 'food_temp_celsius', 'distance_km', 'order_value_inr', 'driver_rating']]
y = df['good_rating']

# 2. Split into train (80%) and test (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train Decision Tree (max_depth=2 shows the top 3 splits cleanly)
clf = DecisionTreeClassifier(criterion='gini', max_depth=2, random_state=42)
clf.fit(X_train, y_train)

print(f"Test Accuracy: {clf.score(X_test, y_test):.2%}")

# 4. Visualize the tree
plt.figure(figsize=(14, 7))
plot_tree(
    clf,
    feature_names=list(X.columns),
    class_names=['Poor (0)', 'Good (1)'],
    filled=True,
    rounded=True,
    fontsize=10
)
plt.title("Decision Tree on 500 Food Delivery Records")
plt.show()