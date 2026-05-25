import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string())

mean = df["Calories"].mean()

median = df["Duration"].median()

mode = df["Pulse"].mode()[0]

print(df.fillna({"Calories" : mean , "Duration" : median , "Pulse" : mode}).to_string())

