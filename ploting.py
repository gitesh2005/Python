import pandas as pd

import matplotlib.pyplot as plt


df = pd.read_csv('data.csv')

df.plot()
plt.show()   # line plot



#scatter plot -->

df.plot(kind = 'scatter' , x = 'Duration' , y = 'Calories')

df.plot(kind = 'scatter' , x = 'Duration' , y = 'Maxpulse')

plt.show()



# histogram

df["Duration"].plot(kind = 'hist')

plt.show()


# 