import pandas as pd
data={
    'Name': ['Alice', 'Bob', None, 'David'],
    'Age': [25, None, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', None]
}
df=pd.DataFrame(data)
print(df)
def double_age(age):
    return age*2
df['Double age']=df['Age'].apply(double_age)
print(df)
df['Age Plus Ten']=df['Age'].apply(lambda x:x+10)
print(df)