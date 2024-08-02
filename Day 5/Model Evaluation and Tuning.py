import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, train_test_split,KFold
from sklearn.ensemble import RandomForestClassifier
data=load_iris()
X=data.data
y=data.target
clf=RandomForestClassifier(random_state=42)
kf=KFold(n_splits=10,shuffle= True,random_state=42)
scores=cross_val_score(clf,X,y,cv=kf)
print(f'Cross-Validation Scores: {scores}')
print(f'Mean Accuracy Score: {scores.mean()}:.2f')