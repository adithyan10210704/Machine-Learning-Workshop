import pandas as pd
from sklearn.preprocessing import StandardScaler
data={
    'A': [1,2,3,4],
    'B':[2,3,4,5]
}
df=pd.DataFrame(data)
scaler=StandardScaler()
df_standardized=pd.DataFrame(scaler.fit_transform(df),columns=df.columns)
print("\n After standardisation:\n", df_standardized)