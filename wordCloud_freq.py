import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import re
import string
from collections import Counter


with open ('results.txt', 'r', encoding='utf-8') as f:
    results = f.read()

split_words = results.split()
Counter = Counter(split_words)
most_occur = Counter.most_common(52)
mostCommon = pd.DataFrame(most_occur, 
                          columns=['Word', 'Frequency'])
mostCommon = mostCommon.iloc[1:, :]

# create subplot of the different data frames
dim = (8, 12)
fig, ax = plt.subplots (figsize = dim)
sns.barplot( x = 'Frequency', y = 'Word', data=mostCommon)

plt.show()