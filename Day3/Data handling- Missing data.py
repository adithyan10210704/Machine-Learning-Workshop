import pandas as pd
data={
    'Name':['Alice','Bob',None,'David'],
    'Age':[25,None,35,40],
    'City':['New York','Los Angeles','Chicago',None]
}
df=pd.DataFrame(data)
print(df)
df_dropped=df.dropna()
print(df_dropped)
df_filled=df.fillna('Unknown')
print(df_filled)