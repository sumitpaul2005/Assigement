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
from sklearn.ensemble import RandomForestClassifier 


# Q1. Load the Iris dataset using scikit-learn, split it into train and test sets, and train a RandomForestClassifier with default parameters. Print the accuracy on the test set.
"""
i = load_iris()
X = i.data
y = i.target

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.4,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=4,
    random_state=42,
    min_samples_split=2,
    criterion="gini"
)

model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Preducted : ",pre)

acc = accuracy_score(y_test,pre)
print("Accuracy : ",acc)
"""

# Q2. Simulate a Flipkart-style product category classifier: create a small DataFrame with 20 products, each with features like price, rating, and brand, and a category label. Use RandomForestClassifier to predict the product category and print the feature importance values.
"""
df = pd.DataFrame(
    {
    'Price': [
        15000, 25000, 12000, 800, 1200,
        500, 700, 30000, 45000, 35000,
        1000, 1500, 900, 2000, 1800,
        22000, 28000, 40000, 600, 1100
    ],
    'Rating': [
        4.5, 4.3, 4.1, 4.2, 4.0,
        3.8, 4.1, 4.6, 4.7, 4.4,
        4.3, 4.2, 3.9, 4.5, 4.1,
        4.2, 4.6, 4.8, 3.7, 4.0
    ],
    'Brand': [
        'Samsung', 'Apple', 'Redmi', 'Nike', 'Puma',
        'Adidas', 'Nike', 'Apple', 'Samsung', 'Apple',
        'Puma', 'Nike', 'Adidas', 'Puma', 'Nike',
        'Redmi', 'Samsung', 'Apple', 'Adidas', 'Puma'
    ],
    'Category': [
        'Electronics', 'Electronics', 'Electronics',
        'Fashion', 'Fashion', 'Fashion', 'Fashion',
        'Electronics', 'Electronics', 'Electronics',
        'Fashion', 'Fashion', 'Fashion', 'Fashion',
        'Fashion', 'Electronics', 'Electronics',
        'Electronics', 'Fashion', 'Fashion'
    ]
}
)

print(df)

le = LabelEncoder()
df["Brand"] = le.fit_transform(df["Brand"])

X = df[['Price',"Rating","Brand"]]
y = df["Category"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=50,
    max_depth=4,
    random_state=42,
    min_samples_split=2,
    criterion="gini"
)

model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Preducted : ",pre)

acc = accuracy_score(y_test,pre)
print("Accuracy : ",acc)

print("Importance : ",model.feature_importances_)
"""

# Q3. Tune the n_estimators and max_depth parameters of RandomForestClassifier on the Iris dataset by trying at least 3 different values for each, and report which combination gives the best test accuracy.<br><br><em><strong>Hint:</strong> Use a simple for loop to try combinations and print results.</em>
"""
i = load_iris()
X = i.data
y = i.target

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.4,
    random_state=42
)

best_acc = 0
best_model = None
for n in range(50,200,50):
    for d in range(2,8,2):
        model = RandomForestClassifier(
            n_estimators=n,
            max_depth=d,
            random_state=42
        )

        model.fit(X_train, y_train)

        pre = model.predict(X_test)

        acc = accuracy_score(y_test, pre)

        print("n_estimators:", n,
              "max_depth:", d,
              "Accuracy:", acc)

        if acc > best_acc:
            best_acc = acc
            best_model = (n, d)

print("\nBest Parameters:", best_model)
print("Best Accuracy:", best_acc)
"""

# Q4. Explain with code how bagging in Random Forest helps avoid overfitting compared to a single decision tree. Show the difference in test accuracy between DecisionTreeClassifier and RandomForestClassifier on the same dataset.
"""
i = load_iris()
X = i.data
y = i.target

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=50,
    max_depth=4,
    random_state=42,
    min_samples_split=2,
    criterion="gini"
)

model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Preducted : ",pre)

acc = accuracy_score(y_test,pre)
print("Random Forest Accuracy : ",acc)

Dmodel = DecisionTreeClassifier(criterion="gini",max_depth=4,min_samples_split=2)
Dmodel.fit(X_train,y_train)

D_pre = Dmodel.predict(X_test)
print("Decision Tree : ",D_pre)

D_acc = accuracy_score(y_test,D_pre)
print("Decision Tree Accuracy : ",D_acc)
"""

# Q5. Use ChatGPT to generate Python code that loads a CSV file of Spotify song data and builds a RandomForestClassifier to predict if a song will be a hit based on features like tempo, danceability, and energy. Run the code, fix any errors, and describe one thing you learned from the AI-generated solution.<br><br><em><strong>Hint:</strong> You can use a sample CSV from Kaggle or create your own small dataset.</em>


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load CSV file
df = pd.read_csv("spotify_hits.csv")

print(df.head())

# Select features and target
X = df[['Tempo', 'Danceability', 'Energy']]
y = df['Hit']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100, random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

# Check accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Actual Values:", list(y_test))
print("Predicted Values:", list(y_pred))
print("Accuracy:", accuracy)

# Confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Predict a new song
new_song = pd.DataFrame({
    'Tempo': [120],
    'Danceability': [85],
    'Energy': [90]
})

prediction = model.predict(new_song)

if prediction[0] == 1:
    print("Song Prediction: Hit")
else:
    print("Song Prediction: Not Hit")


# 4. What I learned from AI-generated code I learned that Random Forest uses multiple decision trees to make predictions. 
# It combines their results to improve prediction accuracy. I also learned how to load a CSV file, split data into training and testing sets, train a model, and calculate accuracy using accuracy_score().

# 5. Final conclusion
# The Random Forest Classifier successfully predicted whether a Spotify song is a Hit or Not Hit using Tempo, Danceability, and Energy.
