import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler,LabelEncoder,MinMaxScaler,PolynomialFeatures
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression,Ridge,Lasso,ElasticNet
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error,root_mean_squared_error
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Q1. Create a Python function sigmoid(x) that takes a numeric input and returns the sigmoid value using the formula 1 / (1 + exp(-x)). Test your function with x = -2, 0, and 3.
"""
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

n = int(input("Enter the number : "))
print(sigmoid(n))
"""

# Q2. Given a dataset of 10 Instagram posts with features 'likes' and 'has_caption' (1 if caption present, 0 if not), and a label 'viral' (1 if post went viral, 0 otherwise), write code to fit a logistic regression model to predict 'viral' using scikit-learn. Print the model coefficients.
"""
data = {
    'likes': [120, 4500, 45, 9200, 210, 80, 1600, 6800, 310, 5100],
    'has_caption': [1, 1, 0, 1, 0, 0, 1, 1, 0, 1],
    'viral': [0, 1, 0, 1, 0, 0, 0, 1, 0, 1]  # 1 = viral, 0 = not viral
}

df = pd.DataFrame(data)

X = df[['likes', 'has_caption']]
y = df['viral']

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

model = LogisticRegression(random_state=42)
model.fit(X, y)

pre = model.predict(X_test)
print(pre)

print("Coefficient : ",model.coef_)
"""

# Q3. Plot the sigmoid function for x values from -10 to 10 using matplotlib, and visually indicate the threshold at 0.5 on the plot.<br><br><em><strong>Hint:</strong> Use plt.axhline() to draw the threshold line.</em>

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.linspace(-10, 10, 400)
y = sigmoid(x)

plt.plot(x, y, label='Sigmoid Function $\sigma(x)$', color='blue', linewidth=2)
plt.axhline(y=0.5, color='red', linestyle='--', label='Threshold = 0.5')
plt.axvline(x=0, color='gray', linestyle=':', alpha=0.7)
plt.title('Sigmoid Activation Function', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('$\sigma(x)$', fontsize=12)
plt.ylim(-0.1, 1.1)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='best')
plt.show()


# Q4. Given a probability output from your logistic regression model, write a function that classifies the result as 'Viral' or 'Not Viral' based on a threshold value that you can set (default 0.5). Test your function with probabilities 0.2, 0.6, and 0.8 and thresholds 0.5 and 0.7.

def classify_viral(probability, threshold=0.5):
    return 'Viral' if probability >= threshold else 'Not Viral'

probabilities = [0.2, 0.6, 0.8]
thresholds = [0.5, 0.7]

for thresh in thresholds:
    print(f"=== Testing with Threshold: {thresh} ===")
    for prob in probabilities:
        prediction = classify_viral(prob, threshold=thresh)
        print(f"  Probability {prob} -> {prediction}")
    print()