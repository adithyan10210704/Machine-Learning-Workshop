import pandas as pd
data={
    'A':[1,2,3,4],
    'B':[2,3,4,5]
}
df = pd.DataFrame(data)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df_normalized=pd.DataFrame(scaler.fit_transform(df),columns=df.columns)
print("\n After normalisation:\n",df_normalized)