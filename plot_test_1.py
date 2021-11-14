import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt

path = ""
filename = "Olympics_Tokyo_tweets.csv"
df = pd.read_csv(os.path.join(path, filename), usecols= ['date'])

df['date'] = pd.to_datetime(df['date'], errors = 'coerce').dt.normalize()
#df['date'] = pd.to_datetime(df['date'], errors = 'coerce').dt.normalize()

plt.figure (figsize = [14,8])
plt.hist(df, cumulative =True, bins = 10) 
#plt.hist(df, cumulative =True, density = True, bins = 100)

plt.xticks( rotation = 45)

plt.show()