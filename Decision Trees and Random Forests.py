import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
import numpy as np
from sklearn.datasets import load_iris
data=load_iris()
X=data.data
y=data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
clf=DecisionTreeClassifier(random_state=42)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
accuracy=np.mean(y_pred==y_test)
print(f'Accuracy:{accuracy:.2f}')
plt.figure(figsize=(20,10))
plot_tree(clf,feature_names=data.feature_names,class_names=data.target_names,filled=True,rounded=True,fontsize=12)
plt.show()