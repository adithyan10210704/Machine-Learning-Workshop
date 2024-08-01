import pandas as pd
from sklearn.model_selection import train_test_split
data={
    'Feature1':[1,2,3,4,5,6,7,8,9,10],
    'Feature2':[11,12,13,14,15,16,17,18,19,20],
    'Target':[0,1,0,1,0,1,0,1,0,1]
}
df=pd.DataFrame(data)
X=df[['Feature1','Feature2']]
y=df['Target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Training features:\n",X_train)
print("Test features:\n",X_test)
print("Training targets:\n",y_train)
print("Test targets:\n",y_test)
