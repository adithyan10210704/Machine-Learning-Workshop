import pandas as pd
df=pd.read_csv('ML.csv')
print(df)
df=pd.read_excel('ML excel.xlsx',sheet_name='Sheet1')
print(df)
df=pd.read_json('ML.json')
print(df)
import sqlite3
conn=sqlite3.connect('ML-SQL.sql')
df=pd.read_sql_query('SELECT * FROM ML -SQL',conn)
print(df)