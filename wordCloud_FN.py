import pandas as pd
import numpy as np
import os
import re
import string
import matplotlib.pyplot as plt
import time
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud, STOPWORDS
from sklearn.feature_extraction.text import CountVectorizer  

https = 'https://t.co/'
wordnet_lemmatizer = WordNetLemmatizer()

def remove_http (text):
    '''
    remove_http (text):
        This function remove 'https://t.co' + 10 following characters in
        a string
    parameter:
        text (string)
    return:
        text (string)
    '''
    try: 
        id =  text.find(https,0)

        if id > -1:
            return text[:id] + text[id+23:]
        else: 
            return text
    except:
        print ("error:" + str(text))
        return ""

def df_remove_http(dataframe, inputName, newColName):
    '''
    df_remove_http (dataframe, inputName, newColName):
    parameter:
        dataframe(dataframe)
        inputName (string)
        newColName (string)
    return:
        dataframe (dataframe)

    '''
    newCol = dataframe[inputName].apply (lambda x:remove_http(x))
    dataframe.insert(loc = 1, column = newColName, value = newCol)
    del dataframe[inputName]
    return dataframe

def remove_punctuation (text):
    '''
    remove_punctuation ( ) -> remove all punctuation that listed in the library of string.punctuation
    parameters:
        text (string)
    return: 
        list of string without any punctuation
    '''
    punctuationFree="".join([i for i in text if i not in string.punctuation])
    return punctuationFree

def df_remove_punctuation (dataframe, inputName, newColName):
    '''
    remove_punctuation ( , , )-> remove all punctuations in a column of dataframe 
    parameters:
        dataframe (dataframe)
        inputName (string)
        newColName (string)
    return: 
        single column dataframe
    '''
    newCol = dataframe[inputName].apply(lambda x:remove_punctuation(x))
    dataframe.insert(loc = 1, column = newColName, value = newCol)
    del dataframe[inputName]
    return dataframe

def df_lowerCase(dataframe, inputName, newColName):
    '''
    lowerCase ( , , )-> change all the capital letter to lower case  
    parameters:
        dataframe (dataframe)
        inputName (string)
        newColName (string)
    return: 
        single column dataframe
    '''
    newCol = dataframe[inputName].apply (lambda x: x.lower())
    dataframe.insert(loc = 1, column = newColName, value = newCol)
    del dataframe[inputName]
    return dataframe

def tokenization(text):
    '''
    tokenization ( ) -> change a line of string into token in a list
    parameters:
        text (string)
    return: 
        list of string 
    '''
    tokens =word_tokenize(text)    
    return tokens

def df_tokenization(dataframe, inputName, newColName):
    '''
    df_tokenization ( , , )-> tokenize each row of string into a list for each row  
    parameters:
        dataframe (dataframe)
        inputName (string)
        newColName (string)
    return: 
        single column dataframe
    '''
    newCol = dataframe[inputName].apply(lambda x:tokenization(x))
    dataframe.insert(loc = 1, column = newColName, value = newCol)
    del dataframe[inputName]
    return dataframe

def remove_stopwords(text):
    '''
    remove_stopwords ( ) -> input a list of string and remove all English stopwords
    parameters:
        text (list)
    return: 
        output (list) 
    '''
    output= [i for i in text if i not in stop_words]
    return output

def df_remove_stopwords(dataframe, inputName, newColName):
    '''
    df_remove_stopwords ( , , )-> remove stopwords in rows in dataframe  
    parameters:
        dataframe (dataframe)
        inputName (string)
        newColName (string)
    return: 
        single column dataframe
    '''
#    stop_words = set (stopwords.words("english"))
    newCol = dataframe[inputName].apply(lambda x:remove_stopwords(x))
    dataframe.insert(loc = 1, column = newColName, value = newCol)
    del dataframe[inputName]
    return dataframe

def lemmatizer(text):
    '''
    lemmatizer ( ) -> lemmatize the words in the list
    parameters:
        text (list)
    return: 
        output (list) 
    '''     
    lemm_text = [wordnet_lemmatizer.lemmatize(word) for word in text]
    return lemm_text

def df_lemmatizer(dataframe, inputName, newColName):
    '''
    df_lemmatizer ( , , )-> lemmatize the words in a row in dataframe 
    parameters:
        dataframe (dataframe)
        inputName (string)
        newColName (string)
    return: 
        single column dataframe
    '''
    newCol = dataframe[inputName].apply(lambda x:lemmatizer (x))
    dataframe.insert(loc = 1, column = newColName, value = newCol)
    del dataframe[inputName]
    return dataframe

# Function to remove emoji.
def remove_emoji(string):
    '''
    remove_emoji ( ) -> remove the emoji in the string
    parameters:
        string (string)
    return: 
        output (string) 
    '''    
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               #u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

