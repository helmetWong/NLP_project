from wordCloud_FN import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import concurrent.futures

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
       Step 4: remove first set of tailor 
       Step 5: remove the punctuation
       Step 6: tokenization
       Step 8: remove English stopwrods
       Step 7: lemmatization  
       Step 8: remove second set of tailor stopwords 
       Step 9: join all the words together seperated by " " within a row
       Step 10: join all rows into a string 
       (These functions are written in wordCloud_FN.py
        please read the docstring "printDoc.py" for details).
    '''

    ####    Tailor stopwords    ######################################################
    #
    #  Make a list of tailor topwords to
    #  remove these words to retrieve better information from wordcloud
    #
    ##################################################################################
    tailor_stopwords = []
    tailor_stopwords = ['olympic', 'tokyoolympic', 'olympicgame','answer','tokyo2020',\
                        'answer slovesateez','slovesateez','slovesateez', 'solvesateez',\
                        'slovesateez dreamer']

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
        regex = True)                                               ## step 4: remove first set tailor stopwords
    
    df = df_remove_punctuation (df, 'lower_text', 'no_pun_text')    ## step 5: remove the punctuation 

    df= df_tokenization(df, 'no_pun_text', 'tok_words')             ## step 6: tokenization

    df= df_remove_stopwords(df, 'tok_words','no_stopwords' )        ## step 7: remove English stopwords   
    
    df = df_lemmatizer (df, 'no_stopwords', 'lem_words')            ## step 8: lemmatization

    df['lem_words'] = df['lem_words'].\
        apply(remove_another_stopwords)                             ## step 9: remove second set of tailor stopwords

    df['lem_words'] = df['lem_words'].\
        apply(lambda x: ' '.join([word for word in x]))             ## step 10: join words in every rows
    
    text = " ".join(review for review in df.lem_words)              ## step 11: join all words in a single text
    return text

def main():
    print (processFunction.__doc__)
    filename = "Olympics_Tokyo_tweets.csv"
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

    with concurrent.futures.ProcessPoolExecutor() as executor:
    #with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(processFunction, rows, nrows)

    #####   creating the Word Cloud    ###############################################
    #
    #   join all the text from the list of results together
    #   apply the stop_words here
    #   create the wordcloud
    #
    ##################################################################################

    for result in results: 
        wholeText = wholeText + " " + result
        totalWords += len(wholeText)

    print ("There are {} words in the combination of all review.".format(totalWords))
    final_wordcloud = WordCloud(width = 968, height = 968, 
                    background_color ='black', 
                    stopwords = stop_words, 
                    min_font_size = 10).generate(wholeText)

    # Displaying the WordCloud                    
    plt.figure(figsize = (10, 10), facecolor = None) 
    plt.imshow(final_wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 

    with open ('results.txt', 'w', encoding='utf-8') as f:
        f.write(wholeText)
    
    t2 = time.perf_counter()
    print(f'Finished in {t2-t1} seconds')
    plt.show()

if __name__ == '__main__':
    main()