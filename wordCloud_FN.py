import pandas as pd
import numpy as np
import os
import string
import matplotlib.pyplot as plt
import time
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud, STOPWORDS
from sklearn.feature_extraction.text import CountVectorizer  

https = 'https://t.co/'
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
    newCol = dataframe[inputName].apply (lambda x: x.lower())
    dataframe.insert(loc = 1, column = newColName, value = newCol)
    del dataframe[inputName]
    return dataframe

def tokenization(text):
    tokens =word_tokenize(text)
    return tokens

def df_tokenization(dataframe, inputName, newColName):

    newCol = dataframe[inputName].apply(lambda x:tokenization(x))
    dataframe.insert(loc = 1, column = newColName, value = newCol)
    del dataframe[inputName]
    return dataframe

def remove_stopwords(text):
    output= [i for i in text if i not in stop_words]
    return output

def df_remove_stopwords(dataframe, inputName, newColName):
#    stop_words = set (stopwords.words("english"))
    newCol = dataframe[inputName].apply(lambda x:remove_stopwords(x))
    dataframe.insert(loc = 1, column = newColName, value = newCol)
    del dataframe[inputName]
    return dataframe

def lemmatizer(text):
    wordnet_lemmatizer = WordNetLemmatizer()
    lemm_text = [wordnet_lemmatizer.lemmatize(word) for word in text]
    return lemm_text

def df_lemmatizer(dataframe, inputName, newColName):

    newCol = dataframe[inputName].apply(lambda x:lemmatizer (x))
    dataframe.insert(loc = 1, column = newColName, value = newCol)
    del dataframe[inputName]
    return dataframe