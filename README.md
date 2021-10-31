# NLP_project

worldCloudFn.py includes certain functions to do data preparation in text mining.
printDoc.py     uses to print the docstring of worldCloud.py and save in help.txt
wordCloud_parallel.py will use worldCloudFn.py to do data preperation (currently 8 steps, see below).
                      This will create a word cloud for data sciences to select words for futher analysis. 


dataset:
https://www.kaggle.com/amritpal333/tokyo-olympics-2021-tweets
Olympics_Tokyo_tweets.csv(98.54 MB)

Functions for data preparation:

Step 1: Remove all 'remove all 'https://t.co/' + 10 
Step 2: Remove all emoji
Step 3: lower case on text
Step 4: remove all tailor stopwords (defined above)
Step 5: remove all the punctuation
Step 6: tokenization
Step 7: lemmatization       
Step 8: join all the words together seperated by " " within a row
