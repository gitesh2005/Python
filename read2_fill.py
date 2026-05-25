import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string())


new_df = df.fillna(110 , inplace=True);

print(new_df.to_string())
