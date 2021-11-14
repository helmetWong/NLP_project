from wordCloud_FN import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import concurrent.futures
from collections import Counter
import matplotlib.pyplot as plt
#import pandas as pd

def processFunction (rows, nrows):
    '''     
     processFunction (rows, nrows):  
      is a functions to execute steps
        to perform the data preparation for wordcloud.
      parameter:
        rows (int)      -> number of rows in a csv file for NOT from 1 to "rows"
        nrows (int)     -> number of rows to load in a dataframe
      return 
        text (string)   -> to input in a wordcloud function. 

      The data preparation is applied in following steps: 
       Step 1: Remove all 'remove all 'https://t.co/' + 10 
       Step 2: Remove all emoji
       Step 3: lower case on text
       Step 4: remove all tailor stopwords (defined above)
       Step 5: remove all the punctuation
       Step 6: tokenization
       Step 7: remove English stopwords
       Step 8: lemmatization       

       return: df (dataframe)
    '''

    ####    Tailor stopwords    ######################################################
    #
    #  Make a list of tailor topwords to
    #  remove these words to retrieve better information from wordcloud
    #
    ##################################################################################
    tailor_stopwords = []
    #tailor_stopwords = ['im', 'u', 's', 'g', 'w','b','c','oh'
    #    'olympic', 'sport', 'olympics', 'tokyo olympic','olympi'
    #    'olymics olympic','tokyo2020 olympic',
    #                    'olympics tokyo2020', 'olympics olympic', 'tokyo', 'olympicgame'
    #                    'ateezofficial', 'ateez', 'official', 'lovesateez',
    #                    'get','got', 'got answer', 'today', 'love', 'like', 'hope', 'also', 'win love', 'wa', 'one', 'tching', 'tch'
    #                    'gon', 'gon na', 'na', 'win', 'answer', 'watching', 'watch','game', 'would'] 

    replaced_to = ""

    #####    Reading partial csv file     ############################################
    #
    #  Instead of load the entire csv file in a single dataframe, 
    #  we load a range of rows in the csv file in a smaller datafraeme.
    #  Parallel programming and iteration will be discussed below.
    #  This function slip "rows" from the first (1) row and 
    #  read "nrows".
    #  Only read the columns 'text' and 'data'  
    #
    ##################################################################################

    path = ""
#    filename = "intermediate_jamaica.csv"
    filename = "Olympics_Tokyo_tweets.csv"
    df = pd.read_csv(os.path.join(path, filename), header = 0, 
                              skiprows =range (1, rows), 
                              nrows = nrows, 
                              usecols=['text', 'date'])

    ####    MASK THE DATE    #########################################################
    #
    #  Mask certin rows in relation to the "date" column
    #  Retrieve the rows within the mask
    #
    ##################################################################################

    df['date'] = pd.to_datetime(df['date'], errors = 'coerce').dt.normalize()
    start_date = '2021-07-22' 
    end_date = '2021-08-10'
    mask = (df['date'] > start_date) & (df['date'] <= end_date)
    df = df.loc[mask]

    ####    Step for data preparation    #############################################
    #
    #   Plase refer documentation above.
    #
    ##################################################################################

    df = df_remove_http (df, 'text', 'no_http')                     ## step 1: remove all 'https://t.co/' + 10 

    df['no_http'] = df['no_http'].apply(remove_emoji)               ## step 2: remove emoji

    df = df_lowerCase (df, 'no_http', 'lower_text')                 ## step 3: lower case on text

    df['lower_text'] = df['lower_text'].\
        replace(dict (zip (tailor_stopwords,\
        [replaced_to] *len(tailor_stopwords))),\
        regex = True)                                               ## step 4: remove first set of tailor stopwords
    
    df = df_remove_punctuation (df, 'lower_text', 'no_pun_text')    ## step 5: remove the punctuation 


    df= df_tokenization(df, 'no_pun_text', 'tok_words')             ## step 6: tokenization

    df= df_remove_stopwords(df, 'tok_words','no_stopwords' )        ## step 7: remove English stopwords 

    df = df_lemmatizer (df, 'no_stopwords', 'results')              ## step 8: lemmatization

    df['results'] = df['results'].\
        apply(remove_another_stopwords)                             ## step 9: remove second set of tailor stopwords
  
    return df

def main():
    print (processFunction.__doc__)
    filename = "Olympics_Tokyo_tweets.csv"
#    filename = "intermediate_jamaica.csv"
    stop_words = set (stopwords.words("english"))
    t1 = time.perf_counter()
    print ("start....")

    ####    Divide the datesets for parallel programming     #########################
    #
    #   The dataset of "Olympics_Tokyo_tweets.csv" have around 320,000 rows.
    #   The processFunction will load "skip" numbers of rows x "range_words" times.
    #   We will use parallel programming to run the processFunction 
    #   The develop of this program has a i7-8700 intel CPU (6 cores CPU).    
    #   Optimization for entire dataset: 
    #       54,000 (slip) x 6 (range_words) = 324,000 < 320,000 rows.
    #   We can fine tune slip and range_words if we use mask "date" functions.
    #
    ##################################################################################

    skip = 54000
    range_words = 6
    rows = list()
    nrows = list()
    wholeText = ""
    totalWords = 0
    for n in range (range_words):
        rows.append((skip * n)+ 1 )
        nrows.append(skip)

    print (f"Preform parallel running on {range_words} times.")
    print (f"Read the datafile \"{filename}\" of {nrows[0]} rows and start each run in rows as follows: \n{rows}")


    #####    parallel run function      ##############################################
    #   
    #   parameter:
    #       processFunction ( , )
    #          parameters of the processFunction 
    #           rows (int)      -> number of rows in a csv file for NOT from 1 to "rows"
    #           nrows (int)     -> number of rows to load in a dataframe
    #   return:
    #       results (list)      -> a list of string after data preparation
    #
    ##################################################################################

#    with concurrent.futures.ProcessPoolExecutor() as executor:
    with concurrent.futures.ProcessPoolExecutor(max_workers = 6) as executor:
    #with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(processFunction, rows, nrows)
    
    df = pd.DataFrame(columns = ['results', 'date'])
    for result in results:
        df = pd.concat([df, result], ignore_index=True)

    df.to_csv('result_overall.csv', encoding = 'utf-8')   
    print (df) 

    t2 = time.perf_counter()
    print(f'Finished in {t2-t1} seconds')    
    

if __name__ == '__main__':
    main()


