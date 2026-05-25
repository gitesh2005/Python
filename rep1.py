import pandas as pd

df = pd.read_csv('data.csv')

# df.loc[7 , 'Duration'] = 45                 by this we change the values 1 - by - 1 manually

# for x in df.index:                            this is for reaplace the all values which are greater than the 30 using the for loop
#     if df.loc[x , 'Duration'] > 30:
#         df.loc[x ,'Duration'] = 29


# Removong the rows using the loop

for y in df.index:
    if df.loc[y , 'Duration'] > 50:
        df.drop(y , inplace=True)

print(df)