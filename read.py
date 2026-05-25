import pandas as pd

pd.options.display.max_rows = 999

df = pd.read_csv('data.csv');

# print(df.to_string())    # use to print whole data frame


# print(df) 


print(df.info())

