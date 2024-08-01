import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
data=datasets.load_iris()
X=data.data
y=data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
clf=SVC(kernel='linear',random_state=42)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
print(f'Accuracy: {accuracy:.2f}')
print("Classification Report")
print(classification_report(y_test,y_pred,target_names=data.target_names))
print("Confusion Matrix")
print(confusion_matrix(y_test,y_pred))
def plot_decision_boundaries(X,y,model,title):
    h=.02
    x_min,x_max=X[:,0].min()-1,X[:,0].max()+1
    y_min,y_max=X[:,1].min()-1,X[:,1].max()+1
    xx,yy=np.meshgrid(np.arange(x_min, x_max, h),np.arange(y_min, y_max, h))
    Z=model.predict(np.c_[xx.ravel(),yy.ravel()])
    Z=Z.reshape(xx.shape)
    plt.contourf(xx,yy,Z,cmap=plt.cm.coolwarm,alpha=0.8)
    plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.coolwarm,edgecolors='k')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title(title)
    plt.show()

X_reduced=X[:,:2]
X_train_reduced,X_test_reduced,y_train_reduced,y_test_reduced=train_test_split(X_reduced,y,test_size=0.3,random_state=42)
clf_reduced=SVC(kernel='linear',random_state=42)
clf_reduced.fit(X_train_reduced,y_train_reduced)
plot_decision_boundaries(X_test_reduced,y_test_reduced,clf_reduced,'SVM Decision Boundaries(2D Features)')