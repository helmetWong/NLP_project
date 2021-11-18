import matplotlib.pyplot as plt
import os
import csv
import pandas as pd
import numpy as np
from sklearn import *
from scipy import stats
import pickle

def read_csv_data(fname):
    txtdata = []
    classes = []
    with open(fname, 'r', encoding='UTF-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            # get the text
            txtdata.append(row[1])
    
    return (txtdata, classes)

def write_csv_kaggle_sub(fname, Y):

    tmp = [['Id', 'Prediction']]
    
    # add ID numbers for each Y
    for (i,y) in enumerate(Y):
        tmp2 = [(i+1), y]
        tmp.append(tmp2)
        
    # write CSV file
    with open(fname, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(tmp)

cntvect = pickle.load(open('vectorizer.pickle', 'rb'))
model = pickle.load(open('classification.model', 'rb'))

path = ""
test = "tom"
filename = "predict2_" + test + ".csv"

(testtxt, _)       = read_csv_data("result_" + test + ".csv")

testXbow = cntvect.transform(testtxt)
predY = model.best_estimator_.predict(testXbow)


write_csv_kaggle_sub(filename, predY)

df = pd.read_csv(os.path.join(path, filename))

freq = df.groupby(df['Prediction']).count().unstack()
print (freq)
label = ["neutral", "negative", "positive"]
explode = [0, 0, 0.15]

plt.pie(freq, labels = label, explode = explode,
        autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'})
plt.title(test.upper())
plt.show()



