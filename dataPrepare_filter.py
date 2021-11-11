import pandas as pd
import os


path = ""
filename = "Olympics_Tokyo_tweets.csv"

df = pd.read_csv(os.path.join(path, filename))

simone_bile = ['simone bile', 'simone', 'bile', 'simone_bile', 'simon','simonebile']

jade = ['jade carey', 'jade', 'carey' ,'jadecarey', 'jade_carey']

ateez   = ['ateez', 'ateezofficial', 'ateezofficial ateez', 'olympicslovesateez ateez', 'olympicslovesateez ateezofficial',\
            'answer olympicslovesateez', 'olympicslovesateez dreamer', 'olympicslovesateez', 'win olympicslovesateez',\
            'olympicslovesateez', 'slovesateez dreamer', 'slovesateez']


pattern = "|".join(ateez)

mask = df[df['text'].str.contains(pattern, case = False, na=False)]

print (mask.shape)
mask.to_csv("intermediate_ateez.csv", encoding = 'utf-8')