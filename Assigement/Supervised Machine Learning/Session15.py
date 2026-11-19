import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler,LabelEncoder,MinMaxScaler,PolynomialFeatures
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.linear_model import LinearRegression,LogisticRegression,Ridge,Lasso,ElasticNet
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error,root_mean_squared_error,accuracy_score,confusion_matrix,classification_report
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB,MultinomialNB
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier,plot_tree,export_text
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier,AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.datasets import load_iris


# Q1. Install scikit-learn if you haven't already, then load the iris dataset and fit a GradientBoostingClassifier to classify the flower species. Print the model's accuracy on the test set.
"""
iris = load_iris()
X = iris.data
y = iris.target

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.3,
    random_state=42
)

model = GradientBoostingClassifier(loss="log_loss",
                                   n_estimators=50,
                                   max_depth=3,
                                   random_state=42)

model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Predicted : ",pre)

acc = accuracy_score(y_test,pre)
print("Accuracy : ",acc)
"""

# Q2. Using the Flipkart product review dataset (or any small CSV with positive/negative labels), train an AdaBoostClassifier to predict if a review is positive or negative. Show the classification report (precision, recall, f1-score) for your model.<br><br><em><strong>Hint:</strong> You can use sklearn's AdaBoostClassifier and train_test_split.</em>
"""
df = pd.read_csv("flipkart_reviews.csv")
print(df)

vet = CountVectorizer()
X = vet.fit_transform(df["Sentiment"])
y = df["Review"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.3,
    random_state=42
)

model = AdaBoostClassifier(
    n_estimators=300,random_state=42
)

model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Predicted : ",pre)

acc = accuracy_score(y_test,pre)
print("Accuracy : ",acc)

classReport = classification_report(y_test,pre)
print("Classification Reports : \n",classReport)
"""

# Q3. Explain in your own words the difference between a weak learner and a strong learner, and give one real-world example of each from apps you use (like Instagram, Zomato, or Paytm).
"""
**1. Weak Learner:**

A weak learner is a machine learning model that gives predictions slightly better than random guessing. It is not very accurate when used alone.

**Example:** Instagram – A simple recommendation model may suggest posts based on only one factor, such as likes. It may not always recommend the most interesting posts.

**2. Strong Learner:**

A strong learner is a model that gives highly accurate predictions by combining multiple weak learners or using a powerful learning method.

**Example:** Zomato – Its recommendation system can consider multiple factors, such as ratings, food preferences, order history, and location, to recommend suitable restaurants.

Difference Table

| Weak Learner             | Strong Learner           
| ------------------------ | ------------------------ 
| Less accurate            | More accurate            
| Makes simple predictions | Makes better predictions 
| Uses limited patterns    | Learns multiple patterns 
| May perform poorly alone | Performs better overall  

**Conclusion:** A weak learner gives basic predictions, while a strong learner gives more accurate predictions. In Boosting algorithms like AdaBoost, multiple weak learners are combined to create a strong learner.
"""

# Q4. Modify your GradientBoostingClassifier code to tune the n_estimators and learning_rate parameters. Try at least 3 different combinations and report which one gives the best accuracy.<br><br><em><strong>Hint:</strong> n_estimators controls the number of boosting stages, learning_rate shrinks the contribution of each tree.</em>
"""
iris = load_iris()
X = iris.data
y = iris.target

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.4,
    random_state=42
)

model = GradientBoostingClassifier(random_state=42)

grid = {
    "n_estimators" : [50,100,150],
    "learning_rate" : [0.01, 0.05, 0.1]
}

grid_search = GridSearchCV(model,param_grid=grid,cv=5,scoring="accuracy")
grid_search.fit(X_train,y_train)

pre = grid_search.predict(X_test)
print("Predicted : ",pre)

acc = accuracy_score(y_test,pre)
print("Accuracy : ",acc)

print("Best Parameters:", grid_search.best_params_)
print("Best CV Accuracy:", grid_search.best_score_)
"""

# Q5. Find a real-world use case of boosting in a popular Indian app (such as fraud detection in Paytm or spam filter in WhatsApp). Write 3-4 lines describing how boosting could improve the app's performance.
"""
Paytm can use boosting algorithms like **AdaBoost or Gradient Boosting** to detect suspicious transactions and prevent online payment fraud.

1. Boosting combines multiple weak machine learning models to create a strong model.
2. It can analyse transaction amount, payment frequency, location, and unusual spending patterns.
3. It can identify suspicious transactions more accurately and help reduce fraud.
4. This improves payment security and builds customer trust.

**Conclusion:** Boosting can help Paytm detect fraudulent transactions quickly and improve the safety of digital payments.
"""