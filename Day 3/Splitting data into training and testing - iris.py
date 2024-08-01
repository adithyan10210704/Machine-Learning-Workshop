from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
print("Training features shape:",X_train.shape)
print("Test features shape:",X_test.shape)
print("Training labels shape:",y_train.shape)
print("Test labels shape:",y_test.shape)
