import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
data={
    'square_footage':[1500,1600,1700,1800,1900,2000],
    'num_bedrooms':[3,3,3,4,4,4],
    'prices':[300000,320000,340000,360000,380000,40000]
}
df=pd.DataFrame(data)
X=df[['square_footage','num_bedrooms']]
y=df['prices']
model=LinearRegression()
model.fit(X,y)
predicted_prices=model.predict(X)
print(f"Intercept:{model.intercept_}")
print(f"Coefficients:{model.coef_}")
