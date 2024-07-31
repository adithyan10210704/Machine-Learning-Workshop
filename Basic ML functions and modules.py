import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report
iris=load_iris()
X=iris.data
y=iris.target
df=pd.DataFrame(data=X,columns=iris.feature_names)
df['target']=y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Training features shape:",X_train.shape)
print("Test features shape:",X_test.shape)
print("Training labels shape:",y_train.shape)
print("Test labels shape:",y_test.shape)
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)
model=LogisticRegression(random_state=42)
model.fit(X_train_scaled,y_train)
y_pred=model.predict(X_test_scaled)
accuracy=accuracy_score(y_test,y_pred)
report=classification_report(y_test,y_pred)
print(f"Accuracy: {accuracy}")
print(f"Classification Report: {report}")


