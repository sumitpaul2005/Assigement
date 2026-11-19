# Q1. Given the following confusion matrix from a spam filter (Actual: Spam=70, Not Spam=130; Predicted: Spam=60, Not Spam=140; TP=50, TN=120, FP=10, FN=20), manually calculate the values of accuracy, precision, recall, and F1 score on paper or in a Jupyter notebook.
"""
TP = 50
TN = 120
FP = 10
FN = 20

acc = (TP + TN) / (TP + TN + FP + FN)

prec = TP / (TP + FP)

recall = TP / (TP + FN)

f1_score = 2 * (prec * recall) / (prec + recall)

print("Accuracy : ",acc)
print("Precision : ",prec)
print("Recall : ",recall)
print("F1 Score : ",f1_score)
"""

# Q2. Write a Python function called print_confusion_matrix(tp, tn, fp, fn) that prints the confusion matrix in a readable table format for any given values of true positives, true negatives, false positives, and false negatives.
"""
def confusion(TP,TN,FP,FN):
    print("Confusion Matrix")
    print("--------------------------------------------")
    print("                                Predicted")
    print("                          Spam          Not Spam")
    print("Actual Spam :            ",TP,"           ",FN)
    print("Actual Not Spam :        ",FP,"           ",TN)
    
confusion(50,120,10,20)
"""

# Q3. Imagine you are evaluating a fake news detection model for a social media app. The model flagged 80 posts as fake, of which 60 were actually fake (TP), and missed 30 fake posts (FN). There were 120 posts correctly identified as not fake (TN), and 10 real posts wrongly flagged as fake (FP). Calculate and print the precision and recall for this model.<br><br><em><strong>Hint:</strong> Precision = TP / (TP + FP), Recall = TP / (TP + FN)</em>
"""
TP = 60
FN = 30
TN = 120
FP = 10

precision = TP / (TP + FP)
Recall = TP / (TP + FN)

print("Precision : ",precision)
print("Recall : ",Recall)
"""

# Q4. Given a confusion matrix for a food delivery fraud detection system (TP=40, TN=150, FP=20, FN=10), write Python code to compute the F1 score and explain in one line what the F1 score tells you about the model's performance.<br><br><em><strong>Hint:</strong> F1 = 2 * (precision * recall) / (precision + recall)</em>

TP = 40
TN=150 
FP=20
FN=10

prec = TP / (TP + FP)

recall = TP / (TP + FN)

f1_score = 2 * (prec * recall) / (prec + recall)

print("Precision : ",prec)
print("Recall : ",recall)
print("F1 Score : ",f1_score)

# F1 Score: It tells us how well the model balances precision and recall while detecting fraudulent transactions.
