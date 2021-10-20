import pandas as pd
import os
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

https = 'https://t.co/'
def remove_http (text):
    id =  text.find(https,0)
    if id > -1:
        return text[:id] + text[id+23:]
    else: 
        return text

def df_remove_http(dataframe, inputName, newColName):
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

    newCol = dataframe[inputName].apply(lambda x:remove_stopwords(x))
    dataframe.insert(loc = 1, column = newColName, value = newCol)
    del dataframe[inputName]
    return dataframe

def lemmatizer(text):
    lemm_text = [wordnet_lemmatizer.lemmatize(word) for word in text]
    return lemm_text

def df_lemmatizer(dataframe, inputName, newColName):

    newCol = dataframe[inputName].apply(lambda x:lemmatizer (x))
    dataframe.insert(loc = 1, column = newColName, value = newCol)
    del dataframe[inputName]
    return dataframe


if __name__ == "__main__":

    path = ""
    filename = "Olympics_Tokyo_tweets.csv"
    olympics_df = pd.read_csv(os.path.join(path, filename))
    
    df = olympics_df.filter(['text'], axis = 1)                 ## step 1: retrive the column 'text' only 
    #print (df)   #312_825
    #row = 190000 
    row = 2000
    df = df[0:row]

    #print (df[96:99])
    df = df_remove_http(df,'text', 'no_http')                    ## step 2: remove all 'https://t.co/' + 10 characters

    #print (df[96:99])
    df = df_lowerCase (df, 'no_http', 'lower_text')              ## step 3: lower case on text
    #print (df)

    df = df_remove_punctuation (df, 'lower_text', 'no_pun_text') ## step 4: remove the punctuation 
    #print (df)   
    
    df= df_tokenization(df, 'no_pun_text', 'tok_words')          ## step 5: tokenization
    #print (df)

    stop_words = set (stopwords.words("english"))
    df = df_remove_stopwords (df, 'tok_words', 'no_stopwords')   ## step 6: remove stopwords
    #print (df)

    wordnet_lemmatizer = WordNetLemmatizer()
    df = df_lemmatizer (df, 'no_stopwords', 'lem_words')         ## step 7: lemmate 
    print (df)




















