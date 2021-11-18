import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from sklearn import *
from scipy import stats
import csv
import time
import pickle
np.random.seed(100)

def read_training_data(fname):
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
    
    if (len(classes)>0) and (len(txtdata) != len(classes)):        
        raise Exception("mismatched length!")
    
    return (txtdata, classes)


(traintxt, trainY) = read_training_data("train.csv")
t1 = time.perf_counter()
print ("start....")
print(len(traintxt))

# Bag-of-Words representation

cntvect = feature_extraction.text.CountVectorizer(stop_words='english', max_features=148000)

# create the vocabulary
count_vect = cntvect.fit(traintxt)

# calculate the vectors for the training data
trainXbow = cntvect.transform(traintxt)

# SVM with RBF kernel
paramgrid = {'C': np.logspace(-2,3,20), 'gamma': np.logspace(-4,3,20) }
print(paramgrid)

svmrbf = model_selection.GridSearchCV(svm.SVC(kernel='rbf'), paramgrid, cv=6, n_jobs=8, verbose=True)

model = svmrbf.fit(trainXbow, trainY);

# Save the vectorizer
vec_file = 'vectorizer.pickle'
pickle.dump(count_vect, open(vec_file, 'wb'))

# Save the model
mod_file = 'classification.model'
pickle.dump(model, open(mod_file, 'wb'))

t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')  

