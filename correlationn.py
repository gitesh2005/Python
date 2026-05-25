import pandas as pd

df = pd.read_csv('data1.csv')

print(df.to_string())


print(df.corr())