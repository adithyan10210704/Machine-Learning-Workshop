import pandas as pd
from sklearn.preprocessing import LabelEncoder
data={'Category':['A','B','A','C']}
df=pd.DataFrame(data)
label_encoder=LabelEncoder()
df['Category_Encoded']=label_encoder.fit_transform(df['Category'])
print("\n After label encoding:\n",df)