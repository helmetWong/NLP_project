from wordCloud_FN import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import concurrent.futures

t1 = time.perf_counter()
print ("start....")
path = ""
filename = "Olympics_Tokyo_tweets.csv"

skip = 50000
stop_words = stopwords.words("english")


tailor_stopwords = ['olympic', 'sport', 'olympics', 'tokyo olympic','olymics olympic','tokyo2020 olympic',
                    'olympics tokyo2020', 'olympics olympic', 'tokyo', 'olympicgame'
                    'ateezofficial', 'ateez', 'official', 'lovesateez',
                    'get','got', 'got answer', 'today', 'love', 'like', 'hope', 'also', 'win love',
                    'gon', 'gon na', 'na', 'win', 'answer', 'watching', 'watch','game', 'would'] #+ stop_words

replaced_to = ""

#rows = [1, (skip * 1) + 1, (skip * 2) + 1, (skip * 3) + 1, (skip * 4) + 1, (skip * 5) + 1, (skip * 6) + 1 ]
#nrows = [50000, 50000, 50000, 50000, 50000, 50000, 50000]
wordnet_lemmatizer = WordNetLemmatizer()
rows = list()
nrows = list()
wholeText = ""
totalWords = 0
for n in range (4):
    rows.append((skip * n)+ 1 )
    nrows.append(skip)


def download_csv (rows, nrows):
    df = pd.read_csv(os.path.join(path, filename), header = 0, 
                              skiprows =range (1, rows), 
                              nrows = nrows, usecols=[1])
    df = df_remove_http (df, 'text', 'no_http')                     ## step 2: remove all 'https://t.co/' + 10 
    df = df_lowerCase (df, 'no_http', 'lower_text')                 ## step 3: lower case on text
    df = df_remove_punctuation (df, 'lower_text', 'no_pun_text')    ## step 4: remove the punctuation 

 
    df['no_pun_text'] = df['no_pun_text'].replace(dict (zip (tailor_stopwords, 
                                                             [replaced_to] *len(tailor_stopwords))),
                                                 regex = True)                         

    #df= df_tokenization(df, 'no_pun_text', 'tok_words')          ## step 5: tokenization
    #df = df_remove_stopwords (df, 'tok_words', 'no_stopwords')   ## step 6: remove 
    #df = df_lemmatizer (df, 'tok_words', 'lem_words') 
    #df['tok_words'] = df['tok_words'].apply(lambda x: ' '.join([word for word in x]))
    text = " ".join(review for review in df.no_pun_text)
    return text

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(download_csv, rows, nrows)

for result in results: 
    wholeText = wholeText + " " + result
    totalWords += len(wholeText)

print ("There are {} words in the combination of all review.".format(totalWords))

    # Creating the Word Cloud
final_wordcloud = WordCloud(width = 968, height = 968, 
                background_color ='black', 
                stopwords = stop_words, 
                min_font_size = 10).generate(wholeText)

# Displaying the WordCloud                    
plt.figure(figsize = (10, 10), facecolor = None) 
plt.imshow(final_wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')
plt.show()