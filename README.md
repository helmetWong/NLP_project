# NLP_project

(Micheal Wong 18.11.2021, a group project of Big Data in CityU in semester A 2021/22)
--------------------------

Dataset:

https://www.kaggle.com/amritpal333/tokyo-olympics-2021-tweets

Olympics_Tokyo_tweets.csv(98.54 MB)

---------------------------

Data preprocessing stage: 

worldCloudFn.py includes certain functions to do data preparation in text mining.

printDoc.py     uses to print the docString of worldCloud.py and save in help.txt

wordCloud_parallel.py will use worldCloudFn.py to do data preperation (currently 8 steps, see below).
                      This will create a word cloud for data sciences to select words for further analysis.
                      The program uses parallel programming technique.
                      output a "result_{name}.csv file
                      
dataPrepare_filter.py use to filter the interesting words from the dataset and re-input into word_Cloudparallel.py or worldCloud_parallel.py 

---------------------------

Model training and prediction stage:

tweets_sentiment_analysis_train.py  uses to train a model by using train.csv or sanders_tweets_train.txt
                                    the model and vectors saved in classification.model and vectorizer.pickle respectively. 
                                    apply 10 folds cross validation and max faetures = 148,000

tweets_sentiment_predict_and_plot_pie.py    input "result_{name}.csv file
                                            output a predict2_{name}.csv file and a pie chart. 
                                            
---------------------------
 
Visualization programs:

plot_test1.py   plot the number of rows in respect of frequency of date in bar chart
plot_freq.py    plot the frequency of words in a dataset (input = result_{name}.csv) in horizontal bar chart

---------------------------

Functions for data preparation:

Step 1: Remove all 'remove all 'https://t.co/' + 10 

Step 2: Remove all emoji

Step 3: lower case on text

Step 4: remove first set of tailor stopwords 

Step 5: remove all the punctuation

Step 6: tokenization

Step 7: remove English stopwords

Step 8: lemmatization      

Step 9: remove second set of tailor stopwords

Step 10: join all the words together seperated by " " within a row

Step 11: join all words in a single text

![Overall_after pre-processing](https://user-images.githubusercontent.com/63725876/142440549-c677a383-9e0f-4965-ba56-29f994c96251.png)

