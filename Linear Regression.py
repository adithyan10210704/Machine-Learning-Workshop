import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
np.random.seed(0)
X=2*np.random.rand(100,1)
y=4+3*X+np.random.randn(100,1)
model=LinearRegression()
model.fit(X,y)
y_pred=model.predict(X)
plt.scatter(X,y,color='blue')
plt.plot(X,y_pred,color='red')
plt.xlabel('Independent variable')
plt.ylabel('Dependent variable')
plt.title('Simple Linear Regression')
plt.show()