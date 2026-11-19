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


# Q1. Implement a K-Nearest Neighbors (KNN) classifier in Python to predict whether a Flipkart product review is 'positive' or 'negative' using a small dataset of review texts and their labels.<br><br><em><strong>Hint:</strong> Use scikit-learn's KNeighborsClassifier and convert the text data into numerical features using CountVectorizer.</em>
"""
df = pd.read_csv("flipkart_reviews.csv")
print(df)

vect = CountVectorizer()
X = vect.fit_transform(df['Sentiment'])
y = df['Review']

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

model = KNeighborsClassifier(n_neighbors=2, weights='distance')
model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Predicted : ",pre)

print("Acutal : ",y_test)
print("Predicted : ",pre)

acc = accuracy_score(y_test,pre)
print("Accuracy : ",acc)
"""

# Q2. Compare the accuracy of KNN using Euclidean distance vs. Manhattan distance on a dataset of Spotify song features (e.g., tempo, danceability, energy) to classify songs as 'workout' or 'chill' playlists.<br><br><em><strong>Hint:</strong> Use the 'metric' parameter in KNeighborsClassifier to switch between 'euclidean' and 'manhattan'.</em>
"""
df = pd.read_csv("spotifycls.csv")
print(df)

X = df[["Tempo","Danceability","Energy"]]
y = df["Playlist"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=2,metric="euclidean")
model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Actual : ",y_test)
print("Predicted : ",pre)

acc1 = accuracy_score(y_test,pre)
print("Accuracy : ",acc1)

model = KNeighborsClassifier(n_neighbors=2,metric="manhattan")
model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Actual : ",y_test)
print("Predicted : ",pre)

acc2 = accuracy_score(y_test,pre)
print("Accuracy : ",acc2)

if acc1 > acc2:
    print("Euclidean gives better accuracy")
elif acc2 > acc1:
    print("Manhattan gives better accuracy")
else:
    print("Both models give equal accuracy")
"""

# Q3. Use Gaussian Naive Bayes to classify whether an IRCTC train booking is likely to be 'confirmed' or 'waitlisted' based on features like booking time, train popularity, and travel day (use a small mock dataset).
"""
df = pd.read_csv("irctc_booking.csv")
print(df)
# df['Booking_Status'] = df['Booking_Status'].map({'confirmed' : 1, 'waitlisted' : 0})

X = df[['Booking_Time','Train_Popularity']]
y = df['Booking_Status']

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

model = GaussianNB()
model.fit(X_train,y_train)

pre = model.predict(X_test)
print(pre)

acc = accuracy_score(y_test,pre)
print("Accuracy : ",acc)
"""

# Q4. Build a Multinomial Naive Bayes classifier to categorize WhatsApp chat messages as 'personal', 'group', or 'spam' using example message texts and labels.<br><br><em><strong>Constraint:</strong> Use scikit-learn's MultinomialNB and show the confusion matrix for your results.</em>
"""
df = pd.read_csv("whatsapp_messages.csv")
print(df)

X = df['Message']
cv = CountVectorizer()
X = cv.fit_transform(X)
y = df['Label']

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

model = MultinomialNB()
model.fit(X_train,y_train)

pre = model.predict(X_test)
print("Preducted : ",pre)

acc = accuracy_score(y_test,pre)
print("Accuracy : ",acc)

conf = confusion_matrix(y_test,pre,labels=['personal','group','spam'])
print("Confusion Matrix \n",conf)
"""

# Q5. Use ChatGPT or Copilot to generate Python code for a KNN-based image classifier that distinguishes between images of cricket bats and footballs (use any small sample image dataset or random pixel arrays), then run and test the code, noting any changes you made to get it working.<br><br><em><strong>Hint:</strong> Paste the AI-generated code, describe any errors, and how you fixed them.</em>

np.random.seed(42)

X = []
y = []

# Cricket Bat Images
for i in range(50):
    img = np.random.randint(0, 40, (8, 8))
    img[:, 3:5] += 180
    img = np.clip(img, 0, 255)
    X.append(img.flatten())
    y.append("Cricket Bat")

# Football Images
for i in range(50):
    img = np.random.randint(0, 40, (8, 8))
    img[2:6, 2:6] += 180
    img = np.clip(img, 0, 255)
    X.append(img.flatten())
    y.append("Football")

# Convert into NumPy arrays
X = np.array(X)
y = np.array(y)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Create KNN model
model = KNeighborsClassifier(n_neighbors=3)

# Train model
model.fit(X_train, y_train)

# Prediction
pre = model.predict(X_test)
print("Predicted:", pre)

# Accuracy
acc = accuracy_score(y_test, pre)
print("Accuracy:", acc)

# Confusion Matrix
conf = confusion_matrix(
    y_test, pre,
    labels=["Cricket Bat", "Football"]
)
print("Confusion Matrix:")
print(conf)

# Classification Report
print(classification_report(y_test, pre))

# Test a new cricket bat image
new_img = np.random.randint(0, 40, (8, 8))
new_img[:, 3:5] += 180
new_img = np.clip(new_img, 0, 255)

new_img = new_img.flatten().reshape(1, -1)

prediction = model.predict(new_img)
print("New Image Prediction:", prediction[0])

# Errors and Fixes
# 1. KNN requires numerical data, so NumPy arrays were used.
# 2. Converted 2D images into 1D using flatten().
# 3. Used train_test_split() to divide training and testing data.
# Conclusion
# KNN successfully classified cricket bat and football sample images with 100% accuracy on the generated test dataset.