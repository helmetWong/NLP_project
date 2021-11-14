import matplotlib.pyplot as plt
import matplotlib
from numpy import *
from sklearn import *
from scipy import stats
import csv
import time
random.seed(100)


def read_text_data(fname):
    txtdata = []
    classes = []
    topics  = []
    with open(fname, 'r', encoding='UTF-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            # get the text
            txtdata.append(row[0])
            # get the class (convert to integer)
            if len(row)>1:
                classes.append(row[1])
                topics.append(row[2])
    
    if (len(classes)>0) and (len(txtdata) != len(classes)):        
        raise Exception("mismatched length!")
    
    return (txtdata, classes, topics)

def read_csv_data(fname):
    txtdata = []
    classes = []
    topics  = []
    with open(fname, 'r', encoding='UTF-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            # get the text
            txtdata.append(row[1])
            # get the class (convert to integer)
#             if len(row)>1:
#                 classes.append(row[1])
#                 topics.append(row[2])
    
#     if (len(classes)>0) and (len(txtdata) != len(classes)):        
#         raise Exception("mismatched length!")
    
    return (txtdata, classes, topics)

def write_csv_kaggle_sub(fname, Y):
    # fname = file name
    # Y is a list/array with class entries
    
    # header
    tmp = [['Id', 'Prediction']]
    
    # add ID numbers for each Y
    for (i,y) in enumerate(Y):
        tmp2 = [(i+1), y]
        tmp.append(tmp2)
        
    # write CSV file
    with open(fname, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(tmp)

# load the data
(traintxt, trainY, _) = read_text_data("sanders_tweets_train.txt")
(testtxt, _, _)       = read_csv_data("result_overall.csv")
t1 = time.perf_counter()
print ("start....")
print(len(traintxt))
print(len(testtxt))

# Bag-of-Words representation

cntvect = feature_extraction.text.CountVectorizer(stop_words='english', max_features=4500)

# create the vocabulary
cntvect.fit(traintxt)

# calculate the vectors for the training data
trainXbow = cntvect.transform(traintxt)

# calculate vectors for the test data
testXbow = cntvect.transform(testtxt)

## print the vocabulary
#print(cntvect.vocabulary_)

# SVM with RBF kernel
paramgrid = {'C': logspace(-2,3,20), 'gamma': logspace(-4,3,20) }
print(paramgrid)

svmrbf = model_selection.GridSearchCV(svm.SVC(kernel='rbf'), paramgrid, cv=6, n_jobs=10, verbose=True)


svmrbf.fit(trainXbow, trainY);
print("best params:", svmrbf.best_params_)

# predict the testset: SVM with RBF kernel
predY = svmrbf.best_estimator_.predict(testXbow)

t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')  

write_csv_kaggle_sub("predict_overall.csv", predY)