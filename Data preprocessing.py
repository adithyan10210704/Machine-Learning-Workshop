import pandas as pd
from sklearn.impute import SimpleImputer
data={
    'A':[1,2,None,4],
    'B':[None,2,3,4],
    'C':[1,None,3,4],
}
df=pd.DataFrame(data)
df_dropped=df.dropna()
print("After dropping rows with missing values:\n",df_dropped)
df_dropped_cols=df.dropna(axis=1)
print("\nAfter dropping columns with missing values:\n",df_dropped_cols)