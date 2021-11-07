import matplotlib.pyplot as plt
import os
import csv
import pandas as pd
# Pie chart, where the slices will be ordered and plotted counter-clockwise:

path = ""
filename = "predict_simone.csv"

df = pd.read_csv(os.path.join(path, filename))

freq = df.groupby(df['Prediction']).count().unstack()
print (freq)
explode = [0, 0, 0.1]

plt.pie(freq, labels = freq.index, explode = explode,
        autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'})
plt.show()



