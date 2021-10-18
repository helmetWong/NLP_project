import pandas as pd
import os

'''
https://www.youtube.com/watch?v=xvqsFTUsOmc
'''
path = ""
filename = "Olympics_Tokyo_tweets.csv"

olympics_df = pd.read_csv(os.path.join(path, filename))
#pd.set_option('max_columns', None)

#del df['id','user_screen_name','favorited', 'user_created_at', 'language']
#df.drop(['id','user_screen_name','favorited', 'user_created_at', 'language'], inplace=True, axis=1)
df = olympics_df.filter(['text', 'user_location', 'user_followers', 'user_friends'], axis = 1)

print(df)
