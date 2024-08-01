import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, \
    roc_curve
import matplotlib.pyplot as plt

data = {
    'hours_studied': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'previous_score': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    'passed': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}
df = pd.DataFrame(data)
x = df[['hours_studied', 'previous_score']]
y = df['passed']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
y_pred_prob = model.predict_proba(x_test)[:, 1]

conf_matrix = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_prob)  # to enhance the image quality and to identify the issue

print(f"Confusion matrix:\n{conf_matrix}")
print(f"Accuracy:{acc}")
print(f"Precision:{prec}")
print(f"Recall:{rec}")
print(f"F1 score:{f1}")
print(f"ROc AUC:{roc_auc}")
# plot Roc curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

plt.plot(fpr, tpr, label=f'AUC ={roc_auc:2f}')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel("False Positive")
plt.ylabel("True Positive")
plt.title("Roc curve")
plt.legend()
plt.show()

