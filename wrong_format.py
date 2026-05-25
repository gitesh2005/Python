import pandas as pd

df = pd.read_csv('data.csv')

# print(df)


df['Date'] = pd.to_datetime(df['Date'] , format = 'mixed')

# print(df)


df.dropna(subset=['Date'], inplace= True)

print(df)