import pandas as pd
df=pd.read_csv("malayalam_actors_actress\\malayalam_actors_actress.csv")
print(df.shape)
print(df.columns)
print(df.head())
print(df.tail())
print(df.info())
print(df.isnull().sum())
print("=====================")
