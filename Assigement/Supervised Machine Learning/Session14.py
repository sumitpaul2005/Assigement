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
from sklearn.svm import SVC

# Q1. Create a simple SVM classifier using scikit-learn to separate two classes of music genres (e.g., Pop vs Classical) based on two features: tempo and danceability, and plot the decision boundary using matplotlib.
"""
df = pd.DataFrame(
    {
    'Tempo': [120, 125, 130, 115, 110, 60, 65, 70, 75, 80],
    'Danceability': [80, 85, 75, 90, 82, 20, 25, 30, 35, 28],
    'Genre': ['Pop', 'Pop', 'Pop', 'Pop', 'Pop',
              'Classical', 'Classical', 'Classical',
              'Classical', 'Classical']
}
)

print(df)
X = df[['Tempo','Danceability']]
y = df['Genre']

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = SVC(kernel="linear")
model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Predicted : ",pre)

acc = accuracy_score(y_test,pre)
print("Accuracy : ",acc)

plt.scatter(X['Tempo'], X['Danceability'], c=(y == 'Pop'), cmap='coolwarm')

# Decision boundary
w = model.coef_[0]
b = model.intercept_[0]

x = np.linspace(X['Tempo'].min(), X['Tempo'].max(), 100)
y_line = -(w[0] * x + b) / w[1]

plt.plot(x, y_line, color='green', label='Decision Boundary')

plt.xlabel('Tempo')
plt.ylabel('Danceability')
plt.title('SVM Music Genre Classification')
plt.legend()
plt.show()
"""

# Q2. Given a dataset of Flipkart product reviews labeled as positive or negative, use an SVM with a linear kernel to classify the reviews and print the accuracy score.
"""
df = pd.read_csv("flipkart_reviews.csv")
print(df)

cvect = CountVectorizer()
X = cvect.fit_transform(df["Sentiment"])
y = df["Review"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.6,
    random_state=42
)

model = SVC(
    kernel="linear",
    random_state=42
)
model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Predicted : ",pre)

acc = accuracy_score(y_test,pre)
print("Accuracy : ",acc)
"""

# Q3. Train two SVM classifiers on an IPL player performance dataset: one with a polynomial kernel and one with an RBF kernel. Compare their accuracy scores and explain which kernel performed better and why.<br><br><em><strong>Hint:</strong> Use scikit-learn's SVC class and the 'kernel' parameter.</em>
"""
df = pd.read_csv("ipl_performance.csv")
print(df)

X = df[['Runs','Balls_Faced','Strike_Rate','Fours','Sixes']]
y = df['Performance']

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.3,
    random_state=42
)

model = SVC(
    kernel="poly",
    random_state=42
)
model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Predicted : ",pre)

acc = accuracy_score(y_test,pre)
print("Accuracy : ",acc)

model = SVC(
    kernel="rbf",
    random_state=42
)
model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Predicted : ",pre)

acc = accuracy_score(y_test,pre)
print("Accuracy : ",acc)

# The kernel with the higher accuracy performs better on the test dataset.
# - Polynomial kernel: Identifies polynomial relationships between player performance features.
# - RBF kernel: Can identify more complex non-linear patterns.
"""

# Q4. Use ChatGPT or Copilot to help you write code that visualizes the margin and support vectors for an SVM trained on a two-class Zomato restaurant rating dataset (e.g., 'Good' vs 'Bad' ratings). Paste your code and a screenshot of the plot.

df = pd.DataFrame({
    "Votes": [35,50,65,80,95,110,125,140,155,170,
              45,75,105,135,165,190,210,230,250,270,
              55,90,120,150,180,205,225,245,265,285],
    "Average_Cost_for_two": [180,220,250,280,300,320,350,380,400,420,
                             200,240,270,310,340,360,390,410,440,460,
                             230,260,290,330,350,380,400,430,450,480],
    "Rating": ["Bad"]*15 + ["Good"]*15
})

X = df[["Votes", "Average_Cost_for_two"]]
y = df["Rating"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Train SVM
model = SVC(kernel="linear", C=1)
model.fit(X_train, y_train)

pre = model.predict(X_test)

print("Accuracy :", accuracy_score(y_test, pre))
print("Support Vectors :", len(model.support_vectors_))

# Create decision boundary and margins
xx, yy = np.meshgrid(
    np.linspace(X_train[:,0].min()-0.8, X_train[:,0].max()+0.8, 400),
    np.linspace(X_train[:,1].min()-0.8, X_train[:,1].max()+0.8, 400)
)

Z = model.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot
plt.figure(figsize=(9,6))

for label, marker in [("Bad","o"),("Good","^")]:
    mask = y_train.to_numpy() == label
    plt.scatter(X_train[mask,0], X_train[mask,1],
                marker=marker, s=65, label=label)

plt.contour(xx, yy, Z, levels=[-1,0,1],
            linestyles=["--","-","--"])

plt.scatter(
    model.support_vectors_[:,0],
    model.support_vectors_[:,1],
    s=180,
    facecolors="none",
    edgecolors="black",
    linewidths=1.5,
    label="Support Vectors"
)

plt.xlabel("Votes (standardized)")
plt.ylabel("Average Cost for Two (standardized)")
plt.title("SVM Decision Boundary and Margins")
plt.legend()
plt.grid(True)
plt.show()

# Decision Boundary: The solid line separates Good and Bad ratings.
# Margins: The two dashed lines show the margins around the decision boundary.
# Support Vectors: The black circles identify the data points closest to the decision boundary.
# Accuracy: The model achieved approximately 88.89% accuracy on this illustrative dataset.