import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    roc_curve,
    roc_auc_score,
    confusion_matrix
)

data = load_breast_cancer()
X = data.data
y = data.target


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_scores = model.predict_proba(X_test)[:, 1]

fpr, tpr, thresholds = roc_curve(y_test, y_scores)

final_auc = roc_auc_score(y_test, y_scores)
print("Final AUC:", final_auc)

print("\nThreshold-wise values:")
print("Threshold\tFPR\t\tTPR\t\tAUC")

for i in range(len(thresholds)):
    if i > 0:
        auc_i = roc_auc_score(y_test, y_scores >= thresholds[i])
    else:
        auc_i = 0.0
    print(f"{thresholds[i]:.4f}\t\t{fpr[i]:.4f}\t\t{tpr[i]:.4f}\t\t{auc_i:.4f}")

y_pred = (y_scores >= 0.5).astype(int)
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix (Threshold = 0.5):")
print(cm)

TN, FP, FN, TP = cm.ravel()
print(f"TP: {TP}, FP: {FP}, FN: {FN}, TN: {TN}")

plt.figure()
plt.plot(fpr, tpr, label="ROC Curve (AUC = %.2f)" % final_auc)
plt.plot([0, 1], [0, 1], linestyle="--", label="Random Classifier")

plt.xlabel("False Positive Rate (FPR)")
plt.ylabel("True Positive Rate (TPR)")
plt.title("ROC Curve - Logistic Regression")
plt.legend()
plt.grid()

plt.show()
