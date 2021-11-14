import pandas as pd
import os


path = ""
filename = "Olympics_Tokyo_tweets.csv"

df = pd.read_csv(os.path.join(path, filename))

simone = ['simone bile', 'simone', 'bile', 'simone_bile', 'simon','simonebile', 'simone biles', 'biles'] #7343

jade = ['jade carey', 'jade', 'carey' ,'jadecarey', 'jade_carey'] #255

PV = ['pv sindhu', 'pvsindhu', 'sindhu', 'pv'] #6208

naomi = ['naomi osaka', 'naomi', 'osaka', 'naomiosaka', 'osaka naomi',
         'naomi_osaka'] #1984

tom = ['tom', 'tom daley', 'tomdaley', 'tom_daley'] #6334

mirabai = ['mirabai', 'chanu', 'mirabai_chanu', 'mirabai chanu'] #1291

swim = ['swimming', 'swim'] #6461

triathlon = ['triathlon'] #2623

volleyball = ['volleyball'] #2683

ateez  = ['ateez', 'ateezofficial', 'ateezofficial ateez', 'olympicslovesateez ateez', 'olympicslovesateez ateezofficial',\
            'answer olympicslovesateez', 'olympicslovesateez dreamer', 'olympicslovesateez', 'win olympicslovesateez',\
            'olympicslovesateez', 'slovesateez dreamer', 'slovesateez'] #16,117

usa = ["usa", 'america', 'us', 'united states'] #71513

china = ['china'] #3344

india = ['india'] #14527

australia = ['australia'] #2881

jamaica = ['jamaica'] #1727

pattern = "|".join(jamaica)

mask = df[df['text'].str.contains(pattern, case = False, na=False)]

print (mask.shape)
mask.to_csv("intermediate_jamaica.csv", encoding = 'utf-8')