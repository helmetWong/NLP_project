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
#df = olympics_df.filter(['text', 'user_location', 'user_followers', 'user_friends'], axis = 1)
df = olympics_df.filter(['text'], axis = 1)
print (df)   #312_825
row = 190000 
df = df[0:row]



'''
https://www.analyticsvidhya.com/blog/2021/06/text-preprocessing-in-nlp-with-python-codes/
'''

import string

def remove_punctuation (text):
    '''
    remove_punctuation () -> remove all punctuation that listed in the library of string.punctuation
    parameters:
        text (string)
    return: 
        list of string without any punctuation
    '''
    punctuationFree="".join([i for i in text if i not in string.punctuation])
    return punctuationFree

# should remove http first -> not yet move


no_pun_text = df['text'].apply(lambda x: remove_punctuation(x))
colStart = 1
df.insert (loc = colStart +0, column = "modified", value = no_pun_text)


####################### please try to print before del 'text' column ##################################
#print (df[:50])

del df['text']

lower_text = df['modified'].apply(lambda x: x.lower())
colStart = 1
df.insert (loc = colStart +0, column = 'lower_text', value = lower_text)


from nltk.tokenize import sent_tokenize, word_tokenize

def tokenization(text):
    tokens =word_tokenize(text)
    return tokens

token_list = df['lower_text'].apply (lambda x: tokenization(x))
df.insert (loc = colStart +1, column = 'token', value = token_list)
df.drop(['modified', 'lower_text'], inplace=True, axis=1)

from nltk.corpus import stopwords

stop_words = set (stopwords.words("english"))

def remove_stopwords(text):
    output= [i for i in text if i not in stop_words]
    return output


no_stopwords = df['token'].apply(lambda x:remove_stopwords(x))

colStart = 1
df.insert (loc = colStart +0, column = 'no_stopwords', value = no_stopwords)

from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
def lemmatizer(text):
    lemm_text = [wordnet_lemmatizer.lemmatize(word) for word in text]
    return lemm_text

lem = df['no_stopwords'].apply(lambda x:lemmatizer(x))
colStart = 1
df.insert (loc = colStart +1, column = 'lem_words', value = lem)
del df['token']


#print (df[:50])
print (df)
