import numpy as np
import csv
from mySVM import mySVM as mys
from myKernel import spectrumKernel as sK

# Method to load the csv data
def readData(filename):
    data=list()
    with open(filename,'r') as csvfile:
        reader=csv.reader(csvfile) # create a csv reader object
        for row in reader:
            data.append(row[1]) # loop through the reader and add new fields to  the data
    data = data[1:]
    return data

def trainTestSplit(X, Y, splitFraction):
    idx = round(splitFraction * len(Y))
    trainX = X[:idx]
    trainY = Y[:idx]
    testX = X[idx:]
    testY = Y[idx:]
    return trainX, trainY, testX, testY


Xtr0 = readData('..\\Xtr0.csv')
Ytr0 = readData('..\\Ytr0.csv')

trainX, trainY, testX, testY = trainTestSplit(Xtr0, Ytr0, 0.80)
temp = sK(order=3, missmatch=0)
svmClassifier = mys(lmd=1, kernel=temp)

svmClassifier.fit(trainX, trainY)
pred = svmClassifier.predict(testX)
score = svmClassifier.score(pred, testY)
print(Xtr0)
'''
hypothesis methods:

# SVM with sequential kernel

# RNN

# LSTM

'''


